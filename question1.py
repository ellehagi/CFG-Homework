class CashRegister:

    def __init__(self, discount=0):

        self.total_items = dict()  # {'item': 'price'}
        self.total_price = 0
        self.discount = discount

    def update_discount(self, new_discount):
        self.discount = new_discount

    # this method adds the item to the dictionary
    def add_item(self, item, price):
        self.total_items[item] = price
# this method removes the item from the dictionary
    def remove_item(self, item):
        self.total_items.pop(item)
# this method applies the discount
    def apply_discount(self, price):
        if self.discount > 0:
            price = self.total_price - self.total_price * (self.discount / 100)
        else:
            self.total_price = price

    def get_total(self):
        if self.total_items > 0:
            self.total_price = sum(self.total_items.values())
            self.apply_discount()
        else:
            print("no items in the basket")
# this method shows all of the items in the dictionary
    def show_items(self):
        print("Items in the register:")
        for item in self.total_items.keys():
            print(item)
# this method resets the register
    def reset_register(self):
        self.total_items.clear()
        pass