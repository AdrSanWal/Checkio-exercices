class Soldier():
    def __init__(self, **kwargs):
        self.soldier = kwargs['soldier']
        self.u_name = kwargs['u_name']
        self.name = kwargs['name']
        self.army = kwargs['army']

    def introduce(self):
        return f"{self.u_name} {self.name}, {self.army} {self.soldier}"


class Swordsman(Soldier):
    def __init__(self, **kwargs):
        super().__init__(soldier='swordsman', **kwargs)


class Lancer(Soldier):
    def __init__(self, **kwargs):
        super().__init__(soldier='lancer', **kwargs)


class Archer(Soldier):
    def __init__(self, **kwargs):
        super().__init__(soldier='archer', **kwargs)


class Army():
    def __init__(self, army, **kwargs):
        self.army = army
        self.u_names = kwargs['u_names']

    def train_swordsman(self, name):
        return Swordsman(u_name=self.u_names['swordsman'], name=name, army=self.army)
    def train_lancer(self, name):
        return Lancer(u_name=self.u_names['lancer'], name=name, army=self.army)
    def train_archer(self, name):
        return Archer(u_name=self.u_names['archer'], name=name, army=self.army)


class AsianArmy(Army):
    u_names = {'swordsman': 'Samurai',
               'lancer': 'Ronin',
               'archer': 'Shinobi'}

    def __init__(self):
        super().__init__(army='Asian', u_names=self.u_names)


class EuropeanArmy(Army):
    u_names = {'swordsman': 'Knight',
               'lancer': 'Raubritter',
               'archer': 'Ranger'}

    def __init__(self):
        super().__init__(army='European', u_names=self.u_names)


my_army = EuropeanArmy()
enemy_army = AsianArmy()


soldier_1 = my_army.train_swordsman("Jaks")
soldier_2 = my_army.train_lancer("Harold")
soldier_3 = my_army.train_archer("Robin")

soldier_4 = enemy_army.train_swordsman("Kishimoto")
soldier_5 = enemy_army.train_lancer("Ayabusa")
soldier_6 = enemy_army.train_archer("Kirigae")

assert soldier_1.introduce() == "Knight Jaks, European swordsman"
assert soldier_2.introduce() == "Raubritter Harold, European lancer"
assert soldier_3.introduce() == "Ranger Robin, European archer"
    
assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"
