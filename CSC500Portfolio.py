# Anthony Le
# CSC500 - Principles of Programming
# Critical Thinking Assignment 4,6

# This program simulates a simple shopping cart where the user can input two items with their name, price, and quantity.
# It then calculates and displays the total cost for each item and the overall total.

class ItemToPurchase:
    """Class to represent an item to be purchased in a shopping cart."""
    # Constructor to initialize item details and set attributes
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        """Initialize the item with name, price, quantity, and description."""
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # Method to print item cost
    def print_item_cost(self):
        """Print the cost of the item based on its price and quantity."""
        total_cost = self.item_price * self.item_quantity
        print(
            f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}"
        )

    # Method to calculate and return the total cost of the item
    def get_total_cost(self):
        """Calculate and return the total cost of the item."""
        return self.item_price * self.item_quantity

# Shopping Cart class
class ShoppingCart:
    """Class to represent a shopping cart."""
    # Parameterized constructor which takes in customer name and date
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        """Initialize the shopping cart with customer name and current date."""
        self.customer_name = customer_name
        self.current_date = current_date
        # list of ItemToPurchase objects
        self.cart_items = []

    # Add Item Method
    def add_item(self, item):
        """Add an item to the shopping cart."""
        self.cart_items.append(item)

    # Remove Item Method
    def remove_item(self, item_name):
        """Remove an item from the shopping cart by name."""
        for item in self.cart_items:
            if item.item_name.lower() == item_name.lower():
                self.cart_items.remove(item)
                print(f"Removed {item_name} from cart.")
                return
        print("Item not found in cart. Nothing removed.")

    # Modify Item Method
    def modify_item(self, item):
        """Modify an existing item in the shopping cart."""
        for cart_item in self.cart_items:
            if cart_item.item_name.lower() == item.item_name.lower():
                # Only modify attributes that are not default values
                if hasattr(item, 'item_description') and item.item_description != "none":
                    cart_item.item_description = item.item_description
                if hasattr(item, 'item_price') and item.item_price != 0.0:
                    cart_item.item_price = item.item_price
                if hasattr(item, 'item_quantity') and item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                print(f"Modified {item.item_name} in cart.")
                return
        print("Item not found in cart. Nothing modified.")

    # Get Number Of Items Method
    def get_num_items_in_cart(self):
        """Get the total number of items in the shopping cart."""
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity
    
    # Get Cost Of Cart Method
    def get_cost_of_cart(self):
        """Calculate and return the total cost of all items in the shopping cart."""
        total_cost = sum(item.get_total_cost() for item in self.cart_items)
        return total_cost
    
    # Print Total Method
    def print_total(self):
        """Print the total cost of the shopping cart."""
        print("OUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
        total_cost = self.get_cost_of_cart()
        print(f"\nTotal: ${total_cost:.2f}")

    # Print Descriptions Method
    def print_descriptions(self):
        """Print the descriptions of all items in the shopping cart."""
        print("OUTPUT ITEM DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")



def print_menu(cart: ShoppingCart):
    """Display the menu and process user choices."""
    # Set of valid menu choices
    valid_choices = {"a", "r", "c", "i", "o", "q"}
    # Loop until user chooses to quit
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity/description/price")
        print("i - Output item descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("\nChoose an option: ").strip().lower()
        if choice not in valid_choices:
            print("Invalid choice. Please enter one of: a, r, c, i, o, q")
            continue

        if choice == "q":
            # Quit immediately
            print("Exiting menu.")
            break

        if choice == "a":
            # Ask for item details
            print("ADD ITEM TO CART")
            name = input("Enter the item name: ").strip()
            description = input("Enter the item description: ").strip()
            # Ask for item price and quantity with validation
            while True:
                try:
                    price = float(input("Enter the item price: "))
                    if price < 0:
                        print("Please enter a non-negative price.")
                        continue
                    break
                except ValueError:
                    print("Invalid price. Enter a number.")
            while True:
                try:
                    quantity = int(input("Enter the item quantity: "))
                    if quantity < 0:
                        print("Please enter a non-negative quantity.")
                        continue
                    break
                except ValueError:
                    print("Invalid quantity. Enter an integer.")
            # Create the item and add to cart
            item = ItemToPurchase(name, price, quantity, description if description else "none")
            cart.add_item(item)
            print(f"Added {name} to cart.")

        elif choice == "r":
            # Ask for name of item to remove
            print("REMOVE ITEM FROM CART")
            name = input("Enter the name of the item to remove: ").strip()
            cart.remove_item(name)

        elif choice == "c":
            # Ask for name of item to modify
            print("CHANGE ITEM DESCRIPTION/PRICE/QUANTITY")
            name = input("Enter the name of the item to modify: ").strip()
            # Ask for new values; empty input means do not change
            desc = input("Enter new description (leave blank to keep current): ").strip()
            price_input = input("Enter new price (leave blank to keep current): ").strip()
            qty_input = input("Enter new quantity (leave blank to keep current): ").strip()
            # Convert inputs, using defaults when blank
            new_desc = desc if desc != "" else "none"
            try:
                new_price = float(price_input) if price_input != "" else 0.0
            except ValueError:
                print("Invalid price entered; treating as no change.")
                new_price = 0.0
            try:
                new_qty = int(qty_input) if qty_input != "" else 0
            except ValueError:
                print("Invalid quantity entered; treating as no change.")
                new_qty = 0
            modified = ItemToPurchase(name, new_price, new_qty, new_desc)
            cart.modify_item(modified)

        elif choice == "i":
            cart.print_descriptions()

        elif choice == "o":
            cart.print_total()


if __name__ == "__main__":
    # Create a shopping cart for the customer with defaults
    customer_name = input("Enter customer name: ").strip()
    if not customer_name:
        customer_name = "none"
    current_date = input("Enter today's date (e.g. January 1, 2020): ").strip()
    if not current_date:
        current_date = "January 1, 2020"

    cart = ShoppingCart(customer_name, current_date)
    # Launch the interactive menu; it will loop until the user quits
    print_menu(cart)
