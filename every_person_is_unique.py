
from datetime import date


# Current date is specified as 2018,1,1
current_date = date(2018, 1, 1)


class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = date(*map(int, birth_date.split('.')[::-1]))
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return f'{self.first_name} {self.last_name}'

    def age(self):
        return int((current_date - self.birth_date).days/365.25) #

    def work(self):
        _gender = {'male': 'He is', 'female': 'She is', 'unknown': 'Is'}
        return f'{_gender[self.gender]} a {self.job}'

    def money(self):
        return f'{self.working_years * self.salary * 12:_d}'.replace('_', ' ')

    def home(self):
        return f'Lives in {self.city}, {self.country}'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"
    print("Coding complete? Let's try tests!")