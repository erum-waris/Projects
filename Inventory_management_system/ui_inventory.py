import streamlit as st #type: ignore

class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id, name, quantity, price):
        if item_id in self.inventory:
            st.error(f"Error: Item with ID '{item_id}' already exists.")
            return False
        else:
            self.inventory[item_id] = {'name': name, 'quantity': quantity, 'price': price}
            st.success(f"Item '{name}' added to inventory.")
            return True

    def view_inventory(self):
        if not self.inventory:
            st.info("Inventory is empty.")
            return None
        else:
            data = []
            for item_id, details in self.inventory.items():
                data.append({'ID': item_id, 'Name': details['name'], 'Quantity': details['quantity'], 'Price': f"${details['price']:.2f}"})
            return data

    def update_quantity(self, item_id, new_quantity):
        if item_id in self.inventory:
            self.inventory[item_id]['quantity'] = new_quantity
            st.success(f"Quantity for item ID '{item_id}' updated to {new_quantity}.")
            return True
        else:
            st.error(f"Error: Item with ID '{item_id}' not found.")
            return False

    def update_price(self, item_id, new_price):
        if item_id in self.inventory:
            self.inventory[item_id]['price'] = new_price
            st.success(f"Price for item ID '{item_id}' updated to ${new_price:.2f}.")
            return True
        else:
            st.error(f"Error: Item with ID '{item_id}' not found.")
            return False

    def delete_item(self, item_id):
        if item_id in self.inventory:
            del self.inventory[item_id]
            st.success(f"Item with ID '{item_id}' deleted from inventory.")
            return True
        else:
            st.error(f"Error: Item with ID '{item_id}' not found.")
            return False

# Initialize inventory in Streamlit's session state
if 'inventory_system' not in st.session_state:
    st.session_state['inventory_system'] = Inventory()

inventory_system = st.session_state['inventory_system']

st.title("Inventory Management System")

menu = st.sidebar.selectbox("Select Action", ["Add Item", "View Inventory", "Update Item", "Delete Item"])

if menu == "Add Item":
    st.subheader("Add New Item")
    item_id = st.text_input("Item ID:")
    name = st.text_input("Item Name:")
    quantity = st.number_input("Quantity:", min_value=0, step=1)
    price = st.number_input("Price:", min_value=0.0, step=0.01)
    if st.button("Add"):
        if item_id and name:
            inventory_system.add_item(item_id, name, int(quantity), float(price))
        else:
            st.warning("Item ID and Name are required.")

elif menu == "View Inventory":
    st.subheader("Current Inventory")
    inventory_data = inventory_system.view_inventory()
    if inventory_data:
        st.table(inventory_data)

elif menu == "Update Item":
    st.subheader("Update Item Details")
    update_type = st.selectbox("Select Update Type", ["Update Quantity", "Update Price"])
    item_id_update = st.text_input("Enter Item ID to update:")
    if item_id_update:
        if update_type == "Update Quantity":
            new_quantity = st.number_input("Enter new quantity:", min_value=0, step=1)
            if st.button("Update Quantity"):
                inventory_system.update_quantity(item_id_update, int(new_quantity))
        elif update_type == "Update Price":
            new_price = st.number_input("Enter new price:", min_value=0.0, step=0.01)
            if st.button("Update Price"):
                inventory_system.update_price(item_id_update, float(new_price))

elif menu == "Delete Item":
    st.subheader("Delete Item")
    item_id_delete = st.text_input("Enter Item ID to delete:")
    if st.button("Delete"):
        inventory_system.delete_item(item_id_delete)