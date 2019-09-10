import random

KREWES = {
    'orpheus': ['Emily', 'Kevin', 'Vishwaa', 'Eric', 'Ray', 'Jesse', 'Tiffany', 'Amanda',],
    'rex': ['William', 'Joseph', 'Calvin', 'Ethan', 'Moody', 'Mo', 'Big Mo', 'Peihua', 'Saad',],
    'endymion': ['Grace', 'Nahi', 'Derek', 'Jun Tao', 'Connor', 'Jason', 'Tammy', 'Albert',]}

kes = random.choice(list(KREWES.keys()))


# print kes
print KREWES[kes][random.randint(0, len(KREWES[kes]) - 1)]
