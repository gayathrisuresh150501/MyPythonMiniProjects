class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'{self.name} is talking')

person1 = Person('Hayley')
person1.talk()