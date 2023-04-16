from app.database import cursor

with cursor() as cur:
    cur.execute(
        """
        CREATE TABLE todo (
            id integer PRIMARY KEY,
            description text DEFAULT '',
            completed boolen DEFAULT false
        )
        """
    )
