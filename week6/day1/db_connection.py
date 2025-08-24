import psycopg2
from psycopg2.extras import execute_values
import requests
import time

HEADERS = {"User-Agent": "countries-loader/1.0 (+https://example.com)"}

V3_URL = "https://restcountries.com/v3.1/all"
V3_PARAMS = {"fields": "name,capital,cca2,region,population"}

V2_URL = "https://restcountries.com/v2/all"  # fallback

def fetch_countries():
    # Try v3 first
    try:
        r = requests.get(V3_URL, params=V3_PARAMS, headers=HEADERS, timeout=30)
        if r.status_code == 200:
            data = r.json()
            assert isinstance(data, list)
            return "v3", data
        else:
            print("v3 request failed:", r.status_code, r.text[:200])
    except Exception as e:
        print("v3 exception:", e)

    # Fallback to v2
    try:
        time.sleep(0.5)
        r = requests.get(V2_URL, headers=HEADERS, timeout=30)
        if r.status_code == 200:
            data = r.json()
            assert isinstance(data, list)
            return "v2", data
        else:
            print("v2 request failed:", r.status_code, r.text[:200])
    except Exception as e:
        print("v2 exception:", e)

    return None, []

def normalize_v3(obj):
    name = (obj.get("name") or {}).get("common")
    capital_list = obj.get("capital") or []
    capital = capital_list[0] if capital_list else None
    code = obj.get("cca2")
    region = obj.get("region")
    population = obj.get("population")
    if not name or not code:
        return None
    return (name, capital, code, region, population)

def normalize_v2(obj):
    # v2 schema differs
    name = obj.get("name")
    capital = obj.get("capital")
    code = obj.get("alpha2Code")
    region = obj.get("region")
    population = obj.get("population")
    if not name or not code:
        return None
    return (name, capital, code, region, population)

# --- DB work ---
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

    source, payload = fetch_countries()
    print(f"Source used: {source or 'none'}; items: {len(payload)}")

    rows = []
    if source == "v3":
        for obj in payload:
            m = normalize_v3(obj)
            if m: rows.append(m)
    elif source == "v2":
        for obj in payload:
            m = normalize_v2(obj)
            if m: rows.append(m)

    print(f"🌍 Prepared rows: {len(rows)}")

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

    # sample verify
    cur.execute("SELECT country_name, capital, flag_code FROM countries ORDER BY country_name LIMIT 10;")
    for r in cur.fetchall():
        print(r)

except Exception as e:
    print("❌ Error:", e)
finally:
    try:
        cur.close(); conn.close()
        print("🔒 Connection closed.")
    except:
        pass