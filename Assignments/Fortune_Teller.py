import random

print("I am the great Osgard, Seer of Dreams\nYour fortune will be in sight after you answer these queries")
def questionA():
    try:
        return int(input("->"))
    except ValueError:
        print("Oops, that was beyond my sight, try again...")
        return questionA()
def questionB():
    try:
        return float(input("->"))
    except ValueError:
        print("Oops, that was beyond my sight, try again...")
        return questionB()

print("First: What is your Lucky Number?")
a1 = questionA()
print("Second: How far into the future do you wish to see?")
a2 = questionB()
print("Finaly: What is the magical number that multiplies this fortune?")
a3 = questionB()

fortune = ((random.randint(1,100) - a1) + a2) * a3