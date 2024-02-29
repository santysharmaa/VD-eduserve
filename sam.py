# Given a class Item with an attributes of name and price, 
# create an Order class that has an attribute item_list that is intitialized to the empty list in the constructor.
#  Then add an add_item method that takes an item and appends it to the item_list attribute.
#  Then create a get_total method that returns the total price for all the items in item_list attribute

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.item_list = []

    def add_item(self, item):
        self.item_list.append(item)

    def get_total(self):
        total = 0
        for item in self.item_list:
            total += item.price
        return total
item1 = Item("item1", 10)
item2 = Item("item2", 20)
item3 = Item("item3", 30)

order = Order()
order.add_item(item1)
order.add_item(item2)
order.add_item(item3)

print(order.get_total()) # Output: 60