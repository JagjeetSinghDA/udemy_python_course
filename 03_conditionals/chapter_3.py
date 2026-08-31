order_size = input("which chai would you like to have: [Small, Medium & Large]: ").lower()


if order_size == 'small':
    print(f"Price is 10 rupees")
elif order_size == 'medium':
    print(f"Price is 15 rupees")
elif order_size == 'large':
    print(f"Price is 20 rupees")
else:
    print(f"Unknown Cup Size")