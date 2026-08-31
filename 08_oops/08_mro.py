class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Herbal blend"


class D(A,C,B):
    pass


cup = D()
print(cup.label)