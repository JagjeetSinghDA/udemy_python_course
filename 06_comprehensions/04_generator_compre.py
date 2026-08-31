daily_sales = [5,10,12,7,3,8,3,6,4,5,9,11,2,1]

# Create a generator expression to calculate the square of each sale

total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)  # This will print the generator object, not the values

