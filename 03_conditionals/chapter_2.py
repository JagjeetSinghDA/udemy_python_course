snack_order = (input("What would you like to have? ")).lower()

if snack_order in ['samosa', 'cookies']:
    print(f"Order Confirmed for {snack_order}! Your order will get ready in some time, Please wait.")
else:
    print(f"Item is not available.")
