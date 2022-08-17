class Mammals:
    def walk(self):
        print('Walking')

class Dog(Mammals):
    pass

class Cat(Mammals):
    pass

cat = Cat()
cat.walk()