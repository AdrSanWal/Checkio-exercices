import re


class Chat:
    def __init__(self):
        self.dialogue = []
    def connect_human(self, human):
        human.chat = self
    def connect_robot(self, robot):
        robot.chat = self
    def show_human_dialogue(self):
        return '\n'.join([''.join(_) for _ in self.dialogue])
    def show_robot_dialogue(self):
        vowels = re.compile('[aeiou]{1}', flags=re.I)
        others = re.compile('[^aeiou]{1}', flags=re.I)
        robot_dialogue = [(a, re.sub(vowels, '0', re.sub(others, '1', b))) for a, b in self.dialogue]
        return '\n'.join([''.join(_) for _ in robot_dialogue])

class Human:
    def __init__(self, name):
        self.name = name
    def send(self, message):
        self.chat.dialogue.append((f'{self.name} said: ', message))

class Robot:
    def __init__(self, name):
        self.name = name
    def send(self, message):
        self.chat.dialogue.append((f'{self.name} said: ', message))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""

#     print("Coding complete? Let's try tests!")

chat.show_robot_dialogue()