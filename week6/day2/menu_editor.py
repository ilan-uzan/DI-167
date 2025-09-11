# menu_editor.py
from menu_item import MenuItem
from menu_manager import MenuManager

def prompt_price(msg: str) -> int:
    while True:
        raw = input(msg).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid integer price (e.g., 35).")

def add_item_to_menu():
    name = input("Item name: ").strip()
    price = prompt_price("Item price: ")
    item = MenuItem(name, price)
    if item.save():
        print("Item was added successfully.")
    else:
        print("Error: could not add item (maybe duplicate name?).")

def remove_item_from_menu():
    name = input("Name of item to delete: ").strip()
    # We can delete by name without saving first
    item = MenuItem(name, 0)
    if item.delete():
        print("Item was deleted successfully.")
    else:
        print("Error: item not found or could not be deleted.")

def update_item_from_menu():
    current_name = input("Current item name: ").strip()
    # optional: get current price (not strictly needed to locate row)
    # current_price = prompt_price("Current item price (for reference): ")
    new_name = input("New item name: ").strip()
    new_price = prompt_price("New item price: ")

    # Try to load existing to get its id; this makes update unambiguous.
    existing = MenuManager.get_by_name(current_name)
    if not existing:
        print("Error: existing item not found.")
        return

    if existing.update(new_name, new_price):
        print("Item was updated successfully.")
    else:
        print("Error: item could not be updated (possible name conflict).")

def view_single_item():
    name = input("Item name to view: ").strip()
    item = MenuManager.get_by_name(name)
    if item:
        print(f"[#{item.id}] {item.name} — {item.price}")
    else:
        print("Item not found.")

def show_restaurant_menu():
    items = MenuManager.all_items()
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
        choice = input("Your choice: ").strip().lower()
        if choice == 'a':
            add_item_to_menu()
        elif choice == 'd':
            remove_item_from_menu()
        elif choice == 'u':
            update_item_from_menu()
        elif choice == 'v':
            view_single_item()
        elif choice == 's':
            show_restaurant_menu()
        elif choice == 'q':
            # show menu then exit
            show_restaurant_menu()
            print("Goodbye!")
            break
        else:
            print("Unknown option, try again.")

if __name__ == "__main__":
    show_user_menu()