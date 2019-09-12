import random

KREWES = {
    'orpheus':['Emily', 'Kevin', 'Vishwaa', 'Eric', 'ray', 'Jesse', 'Tiffany', 'Amanda', 'Junhee', 'Jackie', 'Tyler', 'Emory', 'Ivan', 'Elizabeth', 'Pratham', 'Shaw', 'Eric', 'Yaru', 'Kelvin', 'Hong Wei', 'Michael', 'Kiran', 'Amanda', 'Joseph', 'Tanzim', 'David', 'Yevgeniy'],
    'rex':['William', 'Joseph', 'Calvin', 'Ethan', 'Moody', 'Mo', 'Big Mo', 'Peihua', 'Saad', 'Benjamin', 'Justin', 'Alice', 'Hilary', 'Ayham', 'Michael', 'Matthew', 'Jionghao', 'Devin', 'David', 'Jacob', 'Will', 'Hannah', 'Alex'],
    'endymion':['Grace', 'Nahi', 'Derek', 'Jun Tao', 'Connor', 'Jason', 'Tammy', 'Albert', 'Kazi', 'Derek', 'Brandon', 'Kenneth', 'Lauren', 'Biraj', 'Jeff', 'Jackson', 'Taejoon', 'Kevin', 'Jude', 'Sophie', 'Henry', 'Coby', 'Manfred', 'Leia', 'Ahmed', 'Winston']}


#Retrieve a random name given the team as a parameter
def getName(team):
    print(KREWES[team][random.randint(0, len(KREWES[team] - 1))])

#Retrieve a random team and a random name from that team
def randomName():
    teams = list(KREWES.keys()) #dictionary converted into a list
    period = random.choice(teams) #chooses a random index (team) from the list
    print random.choice(KREWES[period]) #prints out a random index (name) from the chosen team

#Test Runs
#for i in range(0, 10):
#    randomName()
