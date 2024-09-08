# General Store Inventory Management System
# Coded by Smarty, ig: thenameisanshux 
class GeneralStore:
    def __init__(self):
        # Initialize with an empty inventory
        self.inventory = {}
    
    def add_item(self, item_name, price, quantity):
        # Add a new item or update an existing one in the inventory
        if item_name in self.inventory:
            print(f"Updating {item_name} with additional quantity.")
            self.inventory[item_name]['quantity'] += quantity
        else:
            self.inventory[item_name] = {'price': price, 'quantity': quantity}
            print(f"{item_name} added to the inventory.")
    
    def update_price(self, item_name, new_price):
        # Update the price of an existing item
        if item_name in self.inventory:
            self.inventory[item_name]['price'] = new_price
            print(f"Price of {item_name} updated to {new_price}.")
        else:
            print(f"{item_name} not found in the inventory.")
    
    def sell_item(self, item_name, quantity_sold):
        # Sell an item and update the inventory quantity
        if item_name in self.inventory:
            if self.inventory[item_name]['quantity'] >= quantity_sold:
                self.inventory[item_name]['quantity'] -= quantity_sold
                total_cost = quantity_sold * self.inventory[item_name]['price']
                print(f"{quantity_sold} {item_name}(s) sold for {total_cost}.")
            else:
                print(f"Insufficient stock of {item_name}.")
        else:
            print(f"{item_name} not found in the inventory.")
    
    def check_inventory(self):
        # Display the current inventory status
        if self.inventory:
            print("\nCurrent Inventory:")
            for item, details in self.inventory.items():
                print(f"Item: {item}, Price: {details['price']}, Quantity: {details['quantity']}")
        else:
            print("Inventory is empty.")
    
    def search_item(self, item_name):
        # Search for an item by name and display its details
        if item_name in self.inventory:
            print(f"Item: {item_name}, Price: {self.inventory[item_name]['price']}, Quantity: {self.inventory[item_name]['quantity']}")
        else:
            print(f"{item_name} not found in the inventory.")

# Main function to interact with the General Store
def main():
    store = GeneralStore()
    
    while True:
        print("\nOptions:")
        print("1. Add or Update Item")
        print("2. Update Item Price")
        print("3. Sell Item")
        print("4. Check Inventory")
        print("5. Search Item")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ")

        if choice == '1':
            item_name = input("Enter item name: ")
            price = float(input(f"Enter price of {item_name}: "))
            quantity = int(input(f"Enter quantity of {item_name}: "))
            store.add_item(item_name, price, quantity)
        
        elif choice == '2':
            item_name = input("Enter item name: ")
            new_price = float(input(f"Enter new price of {item_name}: "))
            store.update_price(item_name, new_price)
        
        elif choice == '3':
            item_name = input("Enter item name: ")
            quantity_sold = int(input(f"Enter quantity of {item_name} sold: "))
            store.sell_item(item_name, quantity_sold)
        
        elif choice == '4':
            store.check_inventory()
        
        elif choice == '5':
            item_name = input("Enter item name to search: ")
            store.search_item(item_name)
        
        elif choice == '6':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
