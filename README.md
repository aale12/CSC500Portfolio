# CSC500 – Critical Thinking Assignment 4  
## Item Purchase Calculator  

### 📌 Overview  
This program provides a simple shopping cart simulation that allows the user to enter two items, each with a name, price, and quantity. It calculates the total cost for each item and the combined total for both items.  

The solution was developed as part of **Critical Thinking Assignment 4** for **CSC500 – Principles of Programming** at Colorado State University - Global.  

---

### 🖥️ Program Features  
- Defines an `ItemToPurchase` class with the following:  
  - **Attributes**: `item_name` (string), `item_price` (float), `item_quantity` (int)  
  - **Constructor**: Initializes default values (`"none"`, `0.0`, `0`)  
  - **Methods**:  
    - `print_item_cost()` → Prints formatted cost for an item  
    - `get_total_cost()` → Returns total cost (price × quantity)  

- Prompts the user for input for **two items**  
- Creates two `ItemToPurchase` objects  
- Prints the cost of each item  
- Calculates and displays the **total cost**  

---

### 📋 Example Usage

```
Enter the name of item 1:
Chocolate Chips
Enter the price of item 1:
3
Enter the quantity of item 1:
1

Enter the name of item 2:
Bottled Water
Enter the price of item 2:
1
Enter the quantity of item 2:
10

TOTAL COST
Chocolate Chips 1 @ $3.00 = $3.00
Bottled Water 10 @ $1.00 = $10.00

Total: $13.00

---

### ▶️ How to Run  
1. Ensure you have **Python 3.x** installed  
2. Save the program as `CSC500CTA4.py`  
3. Open a terminal or command prompt in the program’s directory  
4. Run the program:  
   ```
   python CSC500CTA4.py
   ```


