#Write a program to maintain the stationary items and make the following operations.
#1. You should be able to add the item to the stationary
#2. Check whether the item is present in stationary, if not print the appropriate message.
#3. Update the items stock count and price, if the item id is provided.

class Stationary:
    def __init__(self):
        self.inventory = {}

    def add_item_to_stationary(self, item_id, item_name, stock_count, price):
        self.inventory[item_id] = {"item_name": item_name, "stock_count": stock_count, "price": price}

    def update_item(self, item_id, stock_count, price):
        if item_id in self.inventory:
            self.inventory[item_id]["stock_count"] = stock_count
            self.inventory[item_id]["price"] = price
        else:
            print("Item not found in inventory.")

    def check_item(self, item_id):
        if item_id in self.inventory:
            item = self.inventory[item_id]
            return f"Product Name: {item['item_name']}, Stock Count: {item['stock_count']}, Price: {item['price']}"
        else:
            return "Item not found in inventory."


stationary = Stationary()

stationary.add_item_to_stationary("I001", "Books", 100, 100.00)
stationary.add_item_to_stationary("I002", "Pens", 110, 50.00)
stationary.add_item_to_stationary("I003", "Pencils", 120, 40.00)
stationary.add_item_to_stationary("I004", "Markers", 90, 80.00)
print("Item Details:")
print(stationary.check_item("I001"))
print(stationary.check_item("I002"))
print(stationary.check_item("I003"))
print(stationary.check_item("I004"))
print("\nUpdate the price of item code - 'I001':")
stationary.update_item("I001", 100, 105.00)
print(stationary.check_item("I001"))
print("\nUpdate the stock of item code - 'I003':")
stationary.update_item("I003", 115, 40.00)
print(stationary.check_item("I003"))