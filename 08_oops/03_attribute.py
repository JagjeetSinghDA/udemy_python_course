class Chai:
    temp = "hot"
    strength = "Strong"


cutting = Chai()
print(cutting.temp)

cutting.temp = "Mild"
cutting.cup = "small"
print("After changing", cutting.temp)
print("cup size is", cutting.cup)
print("Direct look into the class", Chai.temp)


del cutting.temp
del cutting.cup
print("After deleting temp", cutting.temp)
print("After deleting cup", cutting.cup)