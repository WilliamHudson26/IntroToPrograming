import time

answer = input("->")

def loop():
    global answer
    if answer == "countdown":
        listr = [10,9,8,7,6,5,4,3,2,1]
        for num in listr:
            print(num)
            time.sleep(1)
        print("Bazinga!")
    elif answer == "sum":
        listr = input("input numbers (seperated by spaces)\n->")
        listr = listr.split()
        total = 0
        try:
            for num in listr:
                total += int(num)
            print(total)
        except ValueError:
            print("ValueError")
            loop()
    elif answer == "square":
        listr = [1,2,3,4,5]
        newlistr = []
        for num in listr:
            newlistr.append(num*num)
        print(newlistr)
    elif answer == "count vowels":
        text = input("input string \n->").lower()
        listr = list(text)
        total = 0
        for char in listr:
            if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
                total += 1
        print(total)
    elif answer == "table":
        print("I AM THE TABLE!")
        number = input("input number \n->")
        listr = list(range(1,100))
        for num in listr:
            mult = number * num
            print(str(number) + " x " + str(num) + " = " + str(mult))
    elif answer == "names":
        names = ["josh", "joel", "jim"]
        for nam in names:
            print("Hello, " + nam)
    else:
        print("we don't do that around here...")
        answer = input("->")
        loop()
loop()