import random

number = random.randint(1,100)
answer = "null"
print("Guess The Number!")

while answer != number:
    try:
        answer = int(input("->"))
        if answer == number:
            print("Thats It!")
        elif answer > 100 or answer < 1:
            print("Your not within range")
        elif answer == (number+1):
            print("your just above it!")
        elif answer == (number-1):
            print("your just bellow it!")
        elif answer < (number+10) and answer > (number):
            print("A bit lower!")
        elif answer > (number-10) and answer < (number):
            print("A bit higher!")
        elif answer < (number+30) and answer > (number):
            print("Lower, but you are getting close!")
        elif answer > (number-30) and answer < (number):
            print("Higher, but you are getting close!")
        elif answer < (number+100) and answer > (number):
            print("Lower...")
        elif answer > (number-100) and answer < (number):
            print("Higher...")
    except ValueError:
        print("that is not a number!")