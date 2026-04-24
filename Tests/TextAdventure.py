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
        "     ╔═════╗╔═════╗           \n" \
        "     ║ Lif ║║ Eng ║           \n" \
        "     ╚═════╝╚═════╝           \n" \
        "        ║╔════╗║       ╔═════╗\n" \
        "        ╠║Lnd ║║  ╔══╗╔║ Gre ║\n" \
        "        ║╚════╝║  ╚══╝╣╚═════╝\n" \
        "╔════╗  ║    ╔═══╗    ║   \n" \
        "║Gar ║══╬════║Elv║══╦═╝   \n" \
        "╚════╝  ║╔══╗╚═══╝ ╔══╗   \n" \
        "        ║╚══╝  ║   ╚══╝   \n" \
        "        ╚══╩═══╣ ╔══════╗ \n" \
        "           ╔══╗║ ║Hanger║ \n" \
        "           ╚══╝╩═║      ║ \n" \
        "                 ╚══════╝ \n")

    if image == "mortis":
        print("" \
        "/\ __/\  \n" \
        "* _ _ *  \n" \
        "\/   \/  \n" \
        "|     |  \n" \
        "^-   -^  \n" \
        "         \n" \
        "         \n")


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
        print("Incoherent Syntax...")

#initialize global variables
Y_pos = 0
X_pos = 0
Health = 100
Inventory = "empty"
Effect = "null"
Flashlight = "on"
Deck = "null"

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
def choose_dock():
    global outcome
    global Deck
    global X_pos
    global Y_pos
    answer = input("->")
    if answer.lower().strip() == "deck-1" or answer.lower().strip() == "deck1" or answer.lower().strip() == "1":
        print("You dock your shuttle into the bottom hanger on Deck-1.")
        outcome = "deck1"
        Deck = 1
        X_pos = 5
        Y_pos = 6
        graphics("deck1")
    elif answer.lower().strip() == "deck-2" or answer.lower().strip() == "deck2" or answer.lower().strip() == "2":
        print("You dock your shuttle into the hanger on Deck-2.")
        outcome = "deck2"
        Deck = 2
        X_pos = 6
        Y_pos = 4
    else:
        print("Not an available option")
        choose_dock()
choose_dock()
print("You then disembark from your shuttle and enter into a grey mechanical chamber.\n" \
"The airlock doors creek as they close behind you before locking in place with a loud CLANK.\n" \
"Finaly, you go to open the door to the interior of the station, but it will not budge.\n" \
"You put all your weight into pushing open the door before you hear something snap, and the door swings open.\n" \
"You enter into a cold dark hallway, barely able to be lit by your flashlight.\n" \
"You can see the hall turn a corner to the right, and near that corner is a room infront of you.\n" \
"You have the insentive to go on forward, but some part of you feels a need to find out "
"whats happening with the door you just opened.\n" \
"[Type 'inspect' to inspect any specified object]\n" \
"[Type 'north', 'south', 'east', or 'west' to move, currently you are faceing west]")
def inspect(answer):
    global Deck
    global X_pos
    global Y_pos
    answer = answer.lower().replace("inspect","")
    if answer.strip() == "door":
        if (Deck == 1 and X_pos == 5 and Y_pos == 6) or (Deck == 2 and X_pos == 6 and Y_pos == 4):
            print("The inside of the door is hardend with a thick layer of frost.\n" \
            "When you scan it, it shows to be nitrogen ice derived from dust accumulated over years of stagnation.")
            input_loop()
        else:
            print("witch door?")
    else:
        print("An object must be listed")
        print(answer)

def move(answer):
    global Deck
    global X_pos
    global Y_pos
    answer = answer.lower()
    if answer.strip() == "east":
        if Deck == 1 and X_pos == 5 and Y_pos == 6:
            X_pos -= 1
            print("You walk to the corner of the hallway.\n" \
            "You are within reach of the room of you and can allso see the hall extend north.\n" \
            "At the end of the north hallway, you can see a room with an elevator at the center of it.")

def input_loop():
    answer = input("->")
    if answer.startswith("inspect") == True:
        inspect(answer)
    if answer.lower().strip() == "east":
        move(answer)
    else:
        print("Incoherent Syntax...")
        input_loop()

input_loop()