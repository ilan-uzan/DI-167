# db.py
import os
from contextlib import contextmanager
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv() 

DB_NAME = os.getenv("PGDATABASE", "restaurant_menu")
DB_USER = os.getenv("PGUSER", "postgres")
DB_PASS = os.getenv("PGPASSWORD", "")
DB_HOST = os.getenv("PGHOST", "localhost")
DB_PORT = os.getenv("PGPORT", "5432")

@contextmanager
def get_cursor(dict_cursor: bool = False):
    """
    Context manager that yields a cursor and commits/rolls back automatically.
    Usage:
        with get_cursor() as cur:
            cur.execute("SELECT 1;")
            print(cur.fetchone())
    """
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT,
        )
        cur_factory = RealDictCursor if dict_cursor else None
        cur = conn.cursor(cursor_factory=cur_factory)
        yield cur
        conn.commit()
    except Exception:
        if conn:
            conn.rollback()
        raise
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()