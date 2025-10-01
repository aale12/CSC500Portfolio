class ItemToPurchase:
    # Constructor to initialize item details and set attributes
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    # Method to print item cost
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(
            f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}"
        )

    # Method to calculate and return the total cost of the item
    def get_total_cost(self):
        return self.item_price * self.item_quantity


if __name__ == "__main__":
    # Prompt user to enter details for two items
    # Item 1
    item1_name = input("Enter the name of item 1:\n")
    item1_price = float(input("Enter the price of item 1:\n"))
    item1_quantity = int(input("Enter the quantity of item 1:\n"))

    # Item 2
    item2_name = input("\nEnter the name of item 2:\n")
    item2_price = float(input("Enter the price of item 2:\n"))
    item2_quantity = int(input("Enter the quantity of item 2:\n"))

    # Create objects from user input
    item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)
    item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)

    # Print Total cost of items
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    total = item1.get_total_cost() + item2.get_total_cost()
    print(f"\nTotal: ${total:.2f}")
