order_amount = int(input("What's the order amount? "))
delivery_fee = 0 

if order_amount > 300:
    delivery_fee = 0
else:
    delivery_fee = 30


delivery_fee = 0 if order_amount > 300 else 30
print(f"delivery fee is {delivery_fee}")