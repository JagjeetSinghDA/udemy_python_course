# def serve_chai():
#     chai_type = "Masala" # local scope
#     print(f"Inside function: {chai_type}")

# chai_type = "Lemon"
# serve_chai()
# print(f"Outside function: {chai_type}")



def chai_counter():
    chai_order = "Lemon" # enclosing scope
    def print_order():
        chai_order = "Ginger" # inner scope
        print(f"inner: {chai_order}")
    print_order()
    print(f"outer: {chai_order}")

chai_order = "Tulsi" # global scope
chai_counter()
print(f"Global: {chai_order}")