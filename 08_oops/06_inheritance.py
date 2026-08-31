class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")

class MasalaChai(BaseChai):
    def add_spies(self):
        print("Adding spices to the chai....")


class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai....")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

# masala_chai = MasalaChai("Masala")
# (masala_chai.prepare())
# masala_chai.add_spies()
shop = ChaiShop()
fancy_shop = FancyChaiShop()
shop.serve()
fancy_shop.serve()