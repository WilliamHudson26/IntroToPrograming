def graphics(image):
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

graphics("title")
graphics("helmet stars")
start = "null"
print("Type 'start' to Play...")
while start != "start":
    start = input("->")
    if start == "start":
        break
    else:
        print("incorect syntax")

#Intro
print("\n" \
"You are a rookie astronaut who has been tasked to reclaim the blackbox of a deralect space station, \n" \
"The ")