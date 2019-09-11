import random

KREWES = {
    'orpheus': ['Emily', 'Kevin', 'Vishwaa', 'Eric', 'Ray', 'Jesse', 'Tiffany', 'Amanda',],
    'rex': ['William', 'Joseph', 'Calvin', 'Ethan', 'Moody', 'Mo', 'Big Mo', 'Peihua', 'Saad',],
    'endymion': ['Grace', 'Nahi', 'Derek', 'Jun Tao', 'Connor', 'Jason', 'Tammy', 'Albert',]}

# Retrieve a random team name
# kes = random.choice(list(KREWES.keys()))

# Retrieve a random name from the random team given by kes
# print KREWES[kes][random.randint(0, len(KREWES[kes]) - 1)]

# Given team name, retrieve a random name from that team
def getName(team):
    print KREWES[team][random.randint(0, len(KREWES[team]) - 1)]

getName('orpheus')
getName('rex')
getName('endymion')
