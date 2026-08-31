# built-in functions

def chai_flavor(flavor = "Masala"):
    """return the flavor of chai."""
    chai = "ginger"
    return flavor

print(chai_flavor.__doc__)
print(chai_flavor.__name__)


# learn about built in functions from documents


def generate_bill(chai=0, samosa=0):
    """
    Docstring for generate_bill

    calculate the total bill for chai & samosa

    :param chai: number of chai (10 rs each)
    :param samosa: number of samosa (15 rs each)
    """
    total = chai*10 + samosa*15
    return total, "Thank you for visiting chaicode.com"

print(generate_bill(5,5))