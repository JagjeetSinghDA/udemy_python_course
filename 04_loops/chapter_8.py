staff = [("Amit", 16), ("zara", 17), ("Raj", 15)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print(f"No one is eligible to manage the  staff")

# here else is outside the if condition but inside the for loop, it will only run when loop will not break