import random

# def roll():
#     tup = '(' + str(random.randint(1,6)) + ',' + str(random.randint(1,6)) + ')'
#     print(tup)

# roll()
# roll()

# def roll():
#     my_list = []
#     tup = ()
#     for i in range(2):
#         num = random.randint(1,6)
#         my_list.append(num)
#         tup = tuple(my_list)
#     return tup

# print(roll())

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)

        return first,second

dice = Dice()
print(dice.roll())