# we read about the return function in this, one value return, early return amd multiple returns and how to handle them

# def make_chai():
#     # return "Here is your masala chai."
#     print(f"Here is your masala chai.")

# return_value = make_chai()
# print(return_value)
# print()



def idle_chaiwala():
    pass

print(idle_chaiwala())


def sold_cups():
    return 120

total = sold_cups()
print(total)


def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "Chai is ready"
    print("Chai") #this is early return from a function, if a value returns from a return, then after nothing will be executed
print(chai_status(0))
print(chai_status(10))



def chai_report():
    return 100, 20, 10 # sole, remaining

sold, remaining, _ = chai_report()
print("Sold: ", sold)
print("Remaining: ", remaining)