with open("C:\\Users\\825426\\Documents\\Intro to Programing\\IntroToPrograming\\Assignments\\names.txt", "r") as file:
    lines = file.readlines()
    waldo = False
    line_count = 0
    for i in lines:
        if i.strip().lower() == 'Waldo\n':
            line_count += 1
            waldo = True
            break
    if waldo == True:
        print("Found Waldo!" + str(line_count) + "!")
    else:
        print("waldo not found...")