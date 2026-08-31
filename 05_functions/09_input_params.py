# chai = "Ginger chai"

# def prepare_chai(order):
#     print("preparing ", order)

# prepare_chai(chai)
# print(chai)



# chai = [1,2,3]

# def edit_chai(cup):
#     cup[1] = 42

# edit_chai(chai)
# print(chai)



# there are two types of parameters: args and kwargs [*args & **kwargs]

# def make_chai(tea, milk, sugar):
#     print(tea, milk, sugar)

# make_chai("Darjeeling", "Yes", "Low")
# make_chai(sugar = "No", tea = "Green", milk = "Medium")


# def special_chai(*ingredients, **extras):
#     print("Ingredients", ingredients)
#     print("Extras", extras)


# special_chai("Cinnamon", "Cardamon", sweetner = "Honey", foam = "Yes")


# def chai_orders(order=[]):
#     order.append("Masala")
#     print(order)

# chai_orders()
# chai_orders()




def chai_orders(order=None):
    # order.append("Masala")
    if order is None:
        order = []
    print(order)

chai_orders()
chai_orders()

