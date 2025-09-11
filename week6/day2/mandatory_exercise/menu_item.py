# menu_item.py
from typing import Optional
from week6.day2.mandatory_exercise.db import get_conn

class MenuItem:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
        self.id: Optional[int] = None

    def save(self) -> bool:
        sql = """
            INSERT INTO menu_items (item_name, item_price)
            VALUES (%s, %s)
            RETURNING item_id;
        """
        try:
            conn = get_conn()
            cur = conn.cursor()
            cur.execute(sql, (self.name, self.price))
            self.id = cur.fetchone()[0]
            conn.commit()
            cur.close(); conn.close()
            return True
        except Exception:
            # print("Save error:", e)
            return False

    def delete(self) -> bool:
        # prefer id if we have it; else by name
        if self.id is not None:
            sql = "DELETE FROM menu_items WHERE item_id = %s;"
            params = (self.id,)
        else:
            sql = "DELETE FROM menu_items WHERE item_name = %s;"
            params = (self.name,)

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(sql, params)
        deleted = (cur.rowcount == 1)
        conn.commit()
        cur.close(); conn.close()
        return deleted

    def update(self, new_name: str, new_price: int) -> bool:
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

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(sql, params)
        ok = (cur.rowcount == 1)
        if ok:
            self.name, self.price = new_name, new_price
        conn.commit()
        cur.close(); conn.close()
        return ok

    def __repr__(self) -> str:
        return f"MenuItem(id={self.id}, name={self.name!r}, price={self.price})"