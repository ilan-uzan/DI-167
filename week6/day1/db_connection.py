import psycopg2
import requests
import json

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

    # Create table (safe to re-run)
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
    print("🛠️ Table ensured.")

    # Run a query that DOES return a row
    cur.execute("SELECT version();")
    print("PostgreSQL version:", cur.fetchone()[0])

    # Optional sanity checks
    cur.execute("SELECT COUNT(*) FROM countries;")
    print("Rows in countries:", cur.fetchone()[0])

except Exception as e:
    print("❌ Error:", e)
finally:
    try:
        cur.close()
        conn.close()
        print("🔒 Connection closed.")
    except:
        pass