import sys
import random

def graphics(image):
#this function draws ASCII graphics when called. This is for title screens, cutscenes, and encounters.

    if image == "title":
        print("" \
        " ████  ████  ██       ███   █ ███   ██████ ██       ███   █ ███  ██████ \n" \
        "██    ██  ██ ██      █   █  ██   █  ██     ██      █   █  ██   █ ██     \n" \
        " ███  ██  ██ ██     ███████ █████   █████  ██     ███████ █████  █████  \n" \
        "   ██ ██  ██ ██     ██   ██ ██ █    ██     ██     ██   ██ ██ █   ██     \n" \
        "████   ████  ██████ ██   ██ ██  ██  ██     ██████ ██   ██ ██  ██ ██████ \n")

    if image == "helmet stars":
        print("" \
        "      ____________      *                       +                       \n" \
        "    _/    |  |    \_               *                      *             \n" \
        "   /      |  |      \                                             +     \n" \
        " 00==================00              +                                  \n" \
        "0##0▒▒▒▓▓▓▓▓▓▓▓▓▓███0##0                          +                     \n" \
        "0##0░░▒▒▒▓▓▓▓▓▓▓▓▓▓▓0##0    +                                     *     \n" \
        " 00==================00                                   +             \n" \
        "  \     \ |||| /     /                +          *                      \n" \
        "   \_____\||||/_____/   *                                  *      *     \n" \
        "   ]‖‖‖‖‖‖‖[]‖‖‖‖‖‖‖[          *            *           +               \n")

    if image == "deck1":
        print("" \
        "     ╔═════╗╔═════╗\n" \
        "     ║ Lif ║║ Eng ║\n" \
        "     ╚═════╝╚═════╝\n" \
        "        ║╔════╗║   \n" \
        "        ╠║    ║║   \n" \
        "        ║╚════╝║   \n" \
        "╔════╗  ║    ╔═══╗ \n" \
        "║    ║══╬════║Elv║ \n" \
        "╚════╝  ║╔══╗╚═══╝ \n" \
        "        ║╚══╝  ║   \n" \
        "        ╚══╩═══╣   \n" \
        "           ╔══╗║   \n" \
        "           ╚══╝╚═  \n")

def help(type):
    if type == "title":
        print("Quit: Terminates the program\n" \
        "Difficulty: Sets the game difficulty (1 = normal; 2 = hard)\n" \
        "Seed: Sets the game seed (syntax: seed 12486432)")
def difficulty(answer):
    if answer.replace("difficulty","").strip() == "1":
        print("set difficulty to normal")
        return 1
    elif answer.replace("difficulty","").strip() == "2":
        print("set difficulty to hard")
        return 2
    else:
        print("must assign difficulty value between 1 and 2")
def seed_set(answer):
    answer = answer.replace("seed","").strip()
    if len(answer) == 8:
        print("seed set to: " + answer)
        return answer
    else:
        print("seed must contain an 8 digit numerical code")

graphics("title")
graphics("helmet stars")
answer = "null"
outcome = "null"
diff = 1
seed = 0
print("Type 'start' to Play\nOr, type 'help' to find other options...")
while answer != "start":
    answer = input("->")
    if answer == "start":
        break
    elif answer == "help":
        help("title")
    elif answer == "quit":
        sys.exit("Goodby!")
    elif answer.startswith("difficulty") == True:
        diff = difficulty(answer)
    elif answer.startswith("seed") == True:
        seed = seed_set(answer)
    else:
        print("incorrect syntax")

#initialize global variables
Y_pos = 0
X_pos = 0
Health = 100
Inventory = "empty"
Effect = "null"
Flashlight = "off"

#initialize seed
if seed == 0:
    #generates a random seed
    seed = [random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8)]
else:
    #converts seed into list
    seed = [int(d) for d in str(seed)]

#Intro
print("\n" \
"You are a rookie astronaut tasked with recovering the black box of\n" \
"a derelict space station, the Solar Flare.\n" \
"The blackbox is located in the stations bridge,\n" \
"however the station can only be accesed via the hanger bays on the east side.\n" \
"As you fly in on your shuttle, you see the station creep ever closer.\n" \
"There is a hanger bay on the middle deck (Deck-2), and another on the bottom deck (Deck-1).\n" \
"Which one will you dock into?")

#first choise
while answer.lower().strip() != "deck1" or answer.lower().strip() != "deck2":
    answer = input("->")
    if answer.lower().strip() == "deck-1" or answer.lower().strip() == "deck1" or answer.lower().strip() == "1":
        print("You dock your shuttle into the bottom hanger on Deck-1.")
        outcome = "deck1"
        X_pos = 5
        Y_pos = 6
        graphics("deck1")
    elif answer.lower().strip() == "deck-2" or answer.lower().strip() == "deck2" or answer.lower().strip() == "2":
        print("You dock your shuttle into the hanger on Deck-2.")
        outcome = "deck2"
        X_pos = 6
        Y_pos = 4
    else:
        print("Not an available option")