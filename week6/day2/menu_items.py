# menu_item.py
from typing import Optional
from db import get_cursor
import psycopg2

class MenuItem:
    """
    Represents a row in menu_items.
    After save(), self.id is populated.
    """
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
        self.id: Optional[int] = None

    def save(self) -> bool:
        """
        Insert this item. On success set self.id and return True.
        If name is unique and already exists, return False.
        """
        sql = """
            INSERT INTO menu_items (item_name, item_price)
            VALUES (%s, %s)
            RETURNING item_id;
        """
        try:
            with get_cursor() as cur:
                cur.execute(sql, (self.name, self.price))
                self.id = cur.fetchone()[0]
            return True
        except psycopg2.Error as e:
            # Handle duplicate (if UNIQUE constraint exists), or other db errors
            # print(f"[save] DB error: {e}")
            return False

    def delete(self) -> bool:
        """
        Delete this item. Prefer delete by id if present; else by name.
        Returns True if exactly one row was deleted.
        """
        if self.id is not None:
            sql = "DELETE FROM menu_items WHERE item_id = %s;"
            params = (self.id,)
        else:
            sql = "DELETE FROM menu_items WHERE item_name = %s;"
            params = (self.name,)

        with get_cursor() as cur:
            cur.execute(sql, params)
            return cur.rowcount == 1

    def update(self, new_name: str, new_price: int) -> bool:
        """
        Update this item to (new_name, new_price). Use id if available; else by current name.
        Mutates self.name/self.price on success.
        """
        if self.id is not None:
            sql = """
                UPDATE menu_items
                   SET item_name = %s, item_price = %s
                 WHERE item_id = %s;
            """
            params = (new_name, new_price, self.id)
        else:
            sql = """
                UPDATE menu_items
                   SET item_name = %s, item_price = %s
                 WHERE item_name = %s;
            """
            params = (new_name, new_price, self.name)

        with get_cursor() as cur:
            cur.execute(sql, params)
            ok = cur.rowcount == 1
            if ok:
                self.name, self.price = new_name, new_price
            return ok

    def __repr__(self) -> str:
        return f"MenuItem(id={self.id}, name={self.name!r}, price={self.price})"