class Capital():
    __instance = None
    __name = ''

    def __new__(cls, name):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            cls.__name = name
        return cls.__instance

    def name(self):
        return self.__name


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    ukraine_capital_1 = Capital("Kyiv")
    print(ukraine_capital_1.name())
    ukraine_capital_2 = Capital("London")
    print(ukraine_capital_2.name())
    ukraine_capital_3 = Capital("Marocco")

    assert ukraine_capital_2.name() == "Kyiv"
    assert ukraine_capital_3.name() == "Kyiv"

    assert ukraine_capital_2 is ukraine_capital_1
    assert ukraine_capital_3 is ukraine_capital_1

    print("Coding complete? Let's try tests!")
