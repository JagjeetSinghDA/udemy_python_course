# value = 13 

# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")


# value = 13 

# if (remainer := value % 5):
#     print(f"Not divisible, remainder is {remainer}")


# available_sizes = ["small", "Medium", "LARGE"]

# if (requested_size := input("Enter your cup size: ")) in available_sizes:
#     print(f"Serving {requested_size} chai")
# else:
#     print(f"Size is unavailable - {requested_size}")


flavours = ["masala", "ginger", "lemon", "mint"]

print("Available flavours: ", flavours)

while (flavour:= input("Choose your flavour: ")) not in flavours:
    print(f"Sorry, {flavour} chai is not available")
print(f"You choose {flavour} chai")