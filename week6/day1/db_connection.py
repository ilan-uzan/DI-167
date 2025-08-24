import psycopg2
from psycopg2.extras import execute_values
import json
import os

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
    # open the saved JSON file
    with open("countries.json", "r", encoding="utf-8") as f:
        payload = json.load(f)

    print(f"📂 Loaded {len(payload)} countries from countries.json")

    # connect using env vars or defaults
    conn = psycopg2.connect(
        database=os.getenv("PGDATABASE", "countries"),
        user=os.getenv("PGUSER", "postgres"),
        password=os.getenv("PGPASSWORD", "VIVELAFRANCE"),
        host=os.getenv("PGHOST", "localhost"),
        port=os.getenv("PGPORT", "5432")
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

    # detect format (v3 vs v2) by checking fields
    rows = []
    if payload and isinstance(payload, list):
        if "cca2" in payload[0]:  # v3 format
            for obj in payload:
                m = normalize_v3(obj)
                if m: rows.append(m)
        else:  # assume v2 format
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

    # sample preview
    cur.execute("SELECT country_name, capital, flag_code FROM countries ORDER BY country_name LIMIT 10;")
    for r in cur.fetchall():
        print(r)

except Exception as e:
    print("❌ Error:", e)
finally:
    try:
        cur.close()
        conn.close()
        print("🔒 Connection closed.")
    except:
        pass