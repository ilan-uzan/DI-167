import requests
import psycopg2
import random

# Update these with your pgAdmin login details
DB_NAME = "countries"
DB_USER = "postgres"
DB_PASS = "your_password"   # replace with your actual password
DB_HOST = "localhost"
DB_PORT = "5432"

def get_conn():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT,
    )

def fetch_countries():
    url = "https://restcountries.com/v3.1/all"
    params = {
        "fields": "name,capital,flag,subregion,population,flags"  # slim response
    }
    headers = {
        "User-Agent": "country-seeder/1.0 (+github.com/ilan-uzan)"  # any non-empty UA
    }
    r = requests.get(url, params=params, headers=headers, timeout=30)
    if r.status_code != 200:
        # show server message to help debugging
        raise RuntimeError(f"REST Countries error {r.status_code}: {r.text[:300]}")
    return r.json()

def normalize(c):
    name = (c.get("name") or {}).get("common")
    caps = c.get("capital") or []
    capital = caps[0] if caps else None

    # prefer emoji, fall back to an image URL
    emoji = c.get("flag")
    fl = c.get("flags") or {}
    flag_url = fl.get("png") or fl.get("svg")
    flag = emoji or flag_url

    subregion = c.get("subregion")
    population = c.get("population")
    return (name, capital, flag, subregion, population)

def insert_rows(rows):
    sql = """
        INSERT INTO countries (name, capital, flag, subregion, population)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING;
    """
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.executemany(sql, rows)
        conn.commit()

def main():
    data = fetch_countries()
    sample = random.sample(data, 10)
    rows = [normalize(c) for c in sample if (c.get("name") or {}).get("common")]
    insert_rows(rows)
    print("10 random countries inserted!")

if __name__ == "__main__":
    main()