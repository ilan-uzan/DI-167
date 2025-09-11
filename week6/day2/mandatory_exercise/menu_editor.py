# menu_editor.py
from week6.day2.mandatory_exercise.menu_item import MenuItem
from week6.day2.mandatory_exercise.menu_manager import MenuManager

def prompt_price(msg: str) -> int:
    while True:
        val = input(msg).strip()
        try:
            return int(val)
        except ValueError:
            print("Please enter a whole number (e.g., 35).")

def add_item_to_menu():
    name = input("Item name: ").strip()
    price = prompt_price("Item price: ")
    item = MenuItem(name, price)
    if item.save():
        print("Item was added successfully.")
    else:
        print("Error: could not add item.")

def remove_item_from_menu():
    name = input("Name of item to delete: ").strip()
    item = MenuItem(name, 0)
    if item.delete():
        print("Item was deleted successfully.")
    else:
        print("Error: item not found or could not be deleted.")

def update_item_from_menu():
    current_name = input("Current item name: ").strip()
    existing = MenuManager.get_by_name(current_name)
    if not existing:
        print("Error: item not found.")
        return
    new_name = input("New item name: ").strip()
    new_price = prompt_price("New item price: ")
    if existing.update(new_name, new_price):
        print("Item was updated successfully.")
    else:
        print("Error: item could not be updated.")

def view_item():
    name = input("Item name to view: ").strip()
    it = MenuManager.get_by_name(name)
    if it:
        print(f"[#{it.id}] {it.name} — {it.price}")
    else:
        print("Item not found.")

def show_restaurant_menu():
    items = MenuManager.all()
    if not items:
        print("(menu is empty)")
        return
    print("\n=== Restaurant Menu ===")
    for it in items:
        print(f"[#{it.id}] {it.name} — {it.price}")
    print("=======================\n")

def show_user_menu():
    while True:
        print("""
(V) View an Item
(A) Add an Item
(D) Delete an Item
(U) Update an Item
(S) Show the Menu
(Q) Quit
""")
        c = input("Your choice: ").strip().lower()
        if c == 'v': view_item()
        elif c == 'a': add_item_to_menu()
        elif c == 'd': remove_item_from_menu()
        elif c == 'u': update_item_from_menu()
        elif c == 's': show_restaurant_menu()
        elif c == 'q':
            show_restaurant_menu()
            print("Goodbye!")
            break
        else:
            print("Unknown option, try again.")

if __name__ == "__main__":
    show_user_menu()