# db.py
import psycopg2

DB_NAME = "restaurant_menu"   # change if your db name differs
DB_USER = "postgres"          # your postgres user
DB_PASS = "your_password"     # your password
DB_HOST = "localhost"
DB_PORT = "5432"

def get_conn():
    return psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
    )