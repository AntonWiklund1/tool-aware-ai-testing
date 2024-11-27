import psycopg2
from typing import Tuple

def get_connection() -> Tuple[psycopg2.extensions.connection, psycopg2.extensions.cursor]:
    """Create and return a database connection and cursor."""
    conn = psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="postgres",
        port=5432,
    )
    cursor = conn.cursor()
    return conn, cursor

def close_connection(conn: psycopg2.extensions.connection, cursor: psycopg2.extensions.cursor) -> None:
    """Close database connection and cursor."""
    cursor.close()
    conn.close()