"""
This is an example of higher order functions and how they compare e.g. to class based structures.

Essentially it's the same concept:
- you have a constructor (e.g. __init__ or the create function)
- you have a concealed place for dependencies or state (e.g. members or closure)
- you return something that combines/uses the inside state


"""


class Adder:
    """
    This is a class based structure.
    """
    def __init__(self, a):
        """
        This is the constructor.
        :param a:
        """
        self.a = a

    def add(self, b):
        return self.a + b


def create_adder(a):
    """
    This is a function based structure. and similar to the constructor above
    :param a:
    :return:
    """
    return lambda b: a + b


def create_adder2(a):
    def adder(b):
        return a + b

    return adder


if __name__ == '__main__':
    adder1 = Adder(10)
    print(adder1.add(20))
    adder2 = create_adder(10)
    print(adder2(20))
    adder3 = create_adder2(10)
    print(adder3(20))


