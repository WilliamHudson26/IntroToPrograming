import time

#print("MANKIND IS DEAD")
#time.sleep(2)
#print("BLOOD IS FUEL")
#time.sleep(2)
#print("HELL IS FULL")
#time.sleep(3)
#print( "\n"
#"00  00 00   000000 0000   0000  00 00 00 00     00     \n" \
#"00  00 00     00   00  0 00  00 000      00     00     \n" \
#"00  00 00     00   0000  000000 0000  00 00     00     \n" \
#" 0000  000000 00   00 00 00  00 00 00 00 000000 000000 \n")

def act():
    return input("->")
def hallway(action):
    if action.lower().strip() == "forward":
        print("You continue forward through the hallway.")
    elif action.lower().strip() == "right":
        print("You turn the right corner and see a table on the far side with a candle ontop.")
    else:
        print("Not a valid direction")

print("The hall extends streight forward, however there is also an intersecting hallway to the right half-way down.\n" \
"which path do you chose to take?")
action = act()
hallway(action)