with open("C:\\Users\\825426\\Documents\\Intro to Programing\\IntroToPrograming\\Assignments\\names.txt", "r") as file:
    lines = file.readlines()
    waldo = False
    for line in lines:
        if line == 'Waldo\n':
            waldo = True
    if waldo == True:
        print("Found Waldo!")
    else:
        print("waldo not found...")