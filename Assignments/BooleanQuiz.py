print("- - - - - Boolean Quiz - - - - -")
print("Question 1 - - - - - - - - - - -")
answer1 = int(input("An intiger that fits within the limitations of 8-bit hardware\n->"))
print(answer1 < 256)
print("Question 2 - - - - - - - - - - -")
answer2 = input("The color that dominates the screen to indicate a system crash\n->")
print(answer2 == "blue")
print("Question 3 - - - - - - - - - - -")
answer3 = int(input("The number in the name of Xbox's second commecrcialy sold gameing console\n->"))
print(answer3 == 360)
print("Question 4 - - - - - - - - - - -")
answer4 = int(input("The exact amount of pie im sending to your doorstep (in lbs)\n->"))
print(answer4 == 0)
print("Question 5 - - - - - - - - - - -")
answer5 = int(input("A speed above sound (in m/s)\n->"))
print(answer5 > 343)
grade = 0
if (answer1 < 256):
    grade =+ 1
if (answer2 == "blue"):
    grade =+ 1
if (answer3 == 360):
    grade =+ 1
if (answer4 == 0):
    grade =+ 1
if (answer5 > 343):
    grade =+ 1
print("Your grade is " + str(grade))