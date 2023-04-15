import sqlite3
from contextlib import contextmanager


@contextmanager
def connection():
    conn = sqlite3.connect("todo.db")
    try:
        yield conn
    except Exception:
        conn.rollback()
        raise
    else:
        conn.commit()
    finally:
        conn.close()


@contextmanager
def cursor():
    with connection() as conn:
        cur = conn.cursor()
        try:
            yield cur
        finally:
            cur.close()
