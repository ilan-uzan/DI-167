import psycopg2
from psycopg2.extras import execute_values
import requests
import json

API_URL = "https://restcountries.com/v3.1/all?fields=name,flags`"

def normalize_country(obj):
    """
    Map REST Countries v3 fields to our schema.
    - country_name: name.common
    - capital: first element of capital[] if present
    - flag_code: cca2 (alpha-2 code)
    - region: region
    - population: population
    """
    name = obj.get("name", {}).get("common")
    # capital is a list; take first if exists
    cap_list = obj.get("capital") or []
    capital = cap_list[0] if cap_list else None
    flag_code = obj.get("cca2")  # e.g., "IL", "FR"
    region = obj.get("region")
    population = obj.get("population")

    # Basic guard: require at least a name + flag_code
    if not name or not flag_code:
        return None

    return (name, capital, flag_code, region, population)

try:
    conn = psycopg2.connect(
        database="countries",
        user="postgres",
        password="VIVELAFRANCE",
        host="localhost",
        port="5432"
    )
    print("✅ Successfully connected to PostgreSQL")
    cur = conn.cursor()

    # 1) Ensure table exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS countries (
            country_id   SERIAL PRIMARY KEY,
            country_name VARCHAR(100) NOT NULL,
            capital      VARCHAR(50),
            flag_code    VARCHAR(100),
            region       VARCHAR(100),
            population   INTEGER NOT NULL CHECK (population >= 0)
        );
    """)
    conn.commit()

    # 2) Ensure a UNIQUE constraint for upsert logic (on flag_code)
    cur.execute("""
        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1
                FROM   pg_indexes
                WHERE  tablename = 'countries'
                AND    indexname = 'uq_countries_flag_code'
            ) THEN
                CREATE UNIQUE INDEX uq_countries_flag_code
                ON countries (flag_code);
            END IF;
        END$$;
    """)
    conn.commit()

    # 3) Fetch countries from API
    resp = requests.get(API_URL, timeout=30)
    resp.raise_for_status()
    payload = resp.json()

    # 4) Transform data
    rows = []
    for obj in payload:
        mapped = normalize_country(obj)
        if mapped:
            rows.append(mapped)

    print(f"🌍 Fetched {len(rows)} countries to upsert.")

    # 5) Upsert (insert or update on conflict of flag_code)
    # Using execute_values for efficient batch insert
    upsert_sql = """
        INSERT INTO countries (country_name, capital, flag_code, region, population)
        VALUES %s
        ON CONFLICT (flag_code) DO UPDATE
        SET
            country_name = EXCLUDED.country_name,
            capital      = EXCLUDED.capital,
            region       = EXCLUDED.region,
            population   = EXCLUDED.population;
    """

    if rows:
        execute_values(cur, upsert_sql, rows, page_size=200)
        conn.commit()
        print("✅ Upsert complete.")

    # 6) Sanity check
    cur.execute("SELECT COUNT(*) FROM countries;")
    print("📦 Total rows in countries:", cur.fetchone()[0])

except Exception as e:
    print("❌ Error:", e)
finally:
    try:
        cur.close()
        conn.close()
        print("🔒 Connection closed.")
    except:
        pass