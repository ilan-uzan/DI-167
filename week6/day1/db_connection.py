import psycopg2
from psycopg2.extras import execute_values
import requests

API_URL = "https://restcountries.com/v3.1/all"

def normalize_country(obj):
    # Be flexible: fall back to cca3/ccn3 if cca2 missing
    name = (obj.get("name") or {}).get("common")
    cap_list = obj.get("capital") or []
    capital = cap_list[0] if cap_list else None
    code = obj.get("cca2") or obj.get("cca3") or (str(obj.get("ccn3")) if obj.get("ccn3") else None)
    region = obj.get("region")
    population = obj.get("population")

    if not name or not code:
        return None
    return (name, capital, code, region, population)

try:
    conn = psycopg2.connect(
        database="countries",
        user="postgres",
        password="VIVELAFRANCE",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS countries (
            country_id   SERIAL PRIMARY KEY,
            country_name VARCHAR(100) NOT NULL,
            capital      VARCHAR(50),
            flag_code    VARCHAR(100) UNIQUE,
            region       VARCHAR(100),
            population   BIGINT CHECK (population >= 0)
        );
    """)
    conn.commit()

    # --- fetch + debug ---
    resp = requests.get(API_URL, timeout=30, headers={"User-Agent": "countries-loader/1.0"})
    print("HTTP status:", resp.status_code)
    payload = resp.json()
    print("JSON type:", type(payload).__name__)
    if isinstance(payload, list):
        print("Items:", len(payload))
        if payload:
            print("Sample keys:", list(payload[0].keys())[:8])
    else:
        print("Payload keys:", list(payload.keys()))

    # transform
    rows = []
    if isinstance(payload, list):
        for obj in payload:
            mapped = normalize_country(obj)
            if mapped: rows.append(mapped)

    print(f"🌍 Will upsert rows: {len(rows)}")

    if rows:
        upsert_sql = """
            INSERT INTO countries (country_name, capital, flag_code, region, population)
            VALUES %s
            ON CONFLICT (flag_code) DO UPDATE
            SET country_name = EXCLUDED.country_name,
                capital      = EXCLUDED.capital,
                region       = EXCLUDED.region,
                population   = EXCLUDED.population;
        """
        execute_values(cur, upsert_sql, rows, page_size=200)
        conn.commit()
        print("✅ Upsert complete.")

    cur.execute("SELECT COUNT(*) FROM countries;")
    print("📦 Total rows in countries:", cur.fetchone()[0])

except Exception as e:
    print("❌ Error:", e)
finally:
    try:
        cur.close(); conn.close()
        print("🔒 Connection closed.")
    except:
        pass