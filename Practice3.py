class Shoppingcart:
    def __init__(self):
        self.bag = []

    def add_stuff(self):
        num_items = int(input("Enter number of items?\n"))
        for _ in range(num_items):
            item_name = input("Enter item name?\n")
            item_price = float(input("Enter price of item?\n"))
            self.bag.append((item_name,item_price))

    def total_amount(self):
        total_price = sum(item[1] for item in self.bag)
        print("Total price of items in the bag: $", total_price)

cart = Shoppingcart()
cart.add_stuff()
cart.total_amount()







