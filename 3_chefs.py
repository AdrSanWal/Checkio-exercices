class AbstractCook():
    def __init__(self, **kwargs):
        self.food = kwargs['food']
        self.drink = kwargs['drink']
        self.price_food = 0
        self.price_drink = 0

    def add_food(self, food_amount, food_price):
        self.price_food += food_amount * food_price

    def add_drink(self, drink_amount, drink_price):
        self.price_drink += drink_amount * drink_price

    def total(self):
        return f'{self.food}: {self.price_food}, {self.drink}: {self.price_drink}, Total: {self.price_food + self.price_drink}'


class JapaneseCook(AbstractCook):
    def __init__(self):
        super().__init__(food='Sushi', drink='Tea')


class RussianCook(AbstractCook):
    def __init__(self):
        super().__init__(food='Dumplings', drink='Compote')

class ItalianCook(AbstractCook):
    def __init__(self):
        super().__init__(food='Pizza', drink='Juice')


client_1 = JapaneseCook()
client_1.add_food(2, 20)
client_1.add_drink(5, 4)
assert client_1.total() == "Sushi: 40, Tea: 20, Total: 60"

client_2 = RussianCook()
client_2.add_food(1, 40)
client_2.add_drink(5, 20)
assert client_2.total() == "Dumplings: 40, Compote: 100, Total: 140"

client_3 = ItalianCook()
client_3.add_food(2, 20)
client_3.add_drink(2, 10)
assert client_3.total() == "Pizza: 40, Juice: 20, Total: 60"