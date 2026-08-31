class Chai:
    size = 150 #ml

    def describe(self):
        return (f"Size of the cup is {self.size} ml")


cup1 = Chai()

print(cup1.describe()) #calling a class by object
print(Chai.describe(cup1)) #calling a class by class then need to pass the object

cup2 = Chai()
cup2.size = 250
print(cup2.describe())