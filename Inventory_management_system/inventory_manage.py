class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id, name, quantity, price):
        if item_id in self.inventory:
            print(f"Error: Item with ID '{item_id}' already exists.")
        else:
            self.inventory[item_id] = {'name': name, 'quantity': quantity, 'price': price}
            print(f"Item '{name}' added to inventory.")

    def view_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
            return
        print("\n--- Inventory ---")
        print("ID\tName\t\tQuantity\tPrice")
        for item_id, details in self.inventory.items():
            print(f"{item_id}\t{details['name']}\t\t{details['quantity']}\t\t${details['price']:.2f}")
        print("-------------------\n")

    def update_quantity(self, item_id, new_quantity):
        if self.Inventory == {}:
            print("Inventory is empty.")
            return
        if item_id in self.inventory:
            self.inventory[item_id]['quantity'] = new_quantity
            print(f"Quantity for item ID '{item_id}' updated to {new_quantity}.")
        else:
            print(f"Error: Item with ID '{item_id}' not found.")

    def update_price(self, item_id, new_price):
        if item_id in self.inventory:
            self.inventory[item_id]['price'] = new_price
            print(f"Price for item ID '{item_id}' updated to ${new_price:.2f}.")
        else:
            print(f"Error: Item with ID '{item_id}' not found.")

    def delete_item(self, item_id):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print(f"Item with ID '{item_id}' deleted from inventory.")
        else:
            print(f"Error: Item with ID '{item_id}' not found.")

def main():
    inventory_system = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Quantity")
        print("4. Update Price")
        print("5. Delete Item")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_id = input("Enter Item ID: ")
            name = input("Enter Item Name: ")
            try:
                quantity = int(input("Enter Quantity: "))
                price = float(input("Enter Price: "))
                inventory_system.add_item(item_id, name, quantity, price)
            except ValueError:
                print("Invalid input for quantity or price. Please enter numbers.")
        elif choice == '2':
            inventory_system.view_inventory()
        elif choice == '3':
            item_id = input("Enter Item ID to update quantity: ")
            try:
                new_quantity = int(input("Enter new quantity: "))
                inventory_system.update_quantity(item_id, new_quantity)
            except ValueError:
                print("Invalid input for quantity. Please enter a number.")
        elif choice == '4':
            item_id = input("Enter Item ID to update price: ")
            try:
                new_price = float(input("Enter new price: "))
                inventory_system.update_price(item_id, new_price)
            except ValueError:
                print("Invalid input for price. Please enter a number.")
        elif choice == '5':
            item_id = input("Enter Item ID to delete: ")
            inventory_system.delete_item(item_id)
        elif choice == '6':
            print("Exiting Inventory Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()