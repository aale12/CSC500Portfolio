# CSC500 – Portfolio
## Shopping Cart App

### 📌 Overview
This repository contains a small interactive shopping cart application implemented for **CSC500 – Principles of Programming - Portfolio**. The program defines two main types:

- `ItemToPurchase` — represents a purchasable item with name, price, quantity, and description.
- `ShoppingCart` — represents a customer's cart and provides methods to add, remove, modify items, and print summaries.

The program runs as a console application and produces a simple single-letter menu to manipulate the shopping cart.

---

### 🧾 Data model & behavior

ItemToPurchase
- Attributes:
  - `item_name` (string)
  - `item_price` (float)
  - `item_quantity` (int)
  - `item_description` (string)
  - Defaults: name="none", price=0.0, quantity=0, description="none".
- Methods:
  - `print_item_cost()` — prints the formatted cost for the item.
  - `get_total_cost()` — returns price × quantity.

ShoppingCart
- Constructor accepts `customer_name` and `current_date` (defaults: "none" and "January 1, 2020").
- Attributes:
  - `customer_name` (string)
  - `current_date` (string)
  - `cart_items` (list of `ItemToPurchase`)
- Key methods:
  - `add_item(item: ItemToPurchase)` — add item to cart.
  - `remove_item(item_name: str)` — remove first matching item by name; prints "Item not found in cart. Nothing removed." if not found.
  - `modify_item(item: ItemToPurchase)` — modify an existing item by name; only non-default fields from the parameter are applied; prints "Item not found in cart. Nothing modified." if not found.
  - `get_num_items_in_cart()` — returns total quantity of items in the cart.
  - `get_cost_of_cart()` — returns total cost of all items.
  - `print_total()` — prints cart header, number of items, each item's cost, and total; prints "SHOPPING CART IS EMPTY" when cart has no items.
  - `print_descriptions()` — prints each item's name and description.

---

### ▶️ Interactive menu
When you run the script it asks for a customer name and date, then shows a menu. Each option is a single character:

- `a` — Add item to cart (prompts for name, description, price, quantity)
- `r` — Remove item from cart (prompts for item name)
- `c` — Change (modify) an item — prompts for name and optional new description, price, quantity (blank inputs mean "no change")
- `i` — Output item descriptions
- `o` — Output shopping cart (prints item costs and total)
- `q` — Quit the program

The menu re-prompts on invalid input and continues until you enter `q`.

---

### 📋 Example session

```
Enter customer name: Alice
Enter today's date (e.g. January 1, 2020): October 26, 2025

MENU
 a - Add item to cart
 r - Remove item from cart
 c - Change item quantity/description/price
 i - Output item descriptions
 o - Output shopping cart
 q - Quit

Choose an option: a
Enter the item name: The Hobbit
Enter the item description: Fantasy novel
Enter the item price: 10.99
Enter the item quantity: 1
Added The Hobbit to cart.

Choose an option: o
Alice's Shopping Cart - October 26, 2025
Number of Items: 1

The Hobbit 1 @ $10.99 = $10.99

Total: $10.99

Choose an option: q
Exiting menu.
```

---

### ▶️ How to run
Make sure you have Python 3 installed, then from the project folder run:

```powershell
python CSC500Portfolio.py
```

---


Author: Anthony Le


