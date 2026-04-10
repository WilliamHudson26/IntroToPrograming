a1 = True
a2 = True
a3 = True
a4 = True
a5 = True
def tally_score():
    if (answer1 == 12):
        a1 = False
    if (answer2 >= 10 and answer2 < 100):
        a2 = False
    if (answer3 == 65 or answer3 == 66):
        a3 = False
    if (answer4 >= 0 and answer4 <= 255):
        a4 = False
    if (answer5 == 21 or answer5 == 67 or answer5 == 69):
        a2 = False
    return int(100/(int(a1)+int(a2)+int(a3)+int(a4)+int(a5)))

answer1 = int(input("how many inches are there in a foot?\n->"))
answer2 = int(input("type a two digit number\n->"))
answer3 = int(input("when did the dinosaurs die?\n->"))
answer4 = int(input("type a 8-bit integer\n->"))
answer5 = int(input("what is the funny number?\n->"))

print("Your score is " + str(tally_score()) + "%")