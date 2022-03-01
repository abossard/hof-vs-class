class Adder:
    def __init__(self, a):
        self.a = a

    def add(self, b):
        return self.a + b


def create_adder(a):
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
