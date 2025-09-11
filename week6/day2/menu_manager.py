# menu_manager.py
from typing import List, Optional
from db import get_conn
from menu_item import MenuItem

class MenuManager:
    @classmethod
    def get_by_name(cls, name: str) -> Optional[MenuItem]:
        sql = """
            SELECT item_id, item_name, item_price
              FROM menu_items
             WHERE item_name = %s
             LIMIT 1;
        """
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(sql, (name,))
        row = cur.fetchone()
        cur.close(); conn.close()

        if not row:
            return None

        mi = MenuItem(row[1], row[2])
        mi.id = row[0]
        return mi

    @classmethod
    def all(cls) -> List[MenuItem]:
        sql = "SELECT item_id, item_name, item_price FROM menu_items ORDER BY item_id;"
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close(); conn.close()

        items: List[MenuItem] = []
        for row in rows:
            mi = MenuItem(row[1], row[2])
            mi.id = row[0]
            items.append(mi)
        return items