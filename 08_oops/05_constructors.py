# __init__ objects


class ChaiOrder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"

order = ChaiOrder("Masala", 200)
print(order.summary())

order2 = ChaiOrder("Ginger", 100)
print(order2.summary())
