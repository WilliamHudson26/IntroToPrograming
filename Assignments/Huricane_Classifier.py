def main():
    category = "Null"
    try:
        MPH = int(input("input the storms windspeed (MPH)\n->"))
        if MPH <=0:
            raise ValueError
        if MPH < 74:
            category = "Tropical Storm"
        elif MPH < 96:
            category = "Category 1"
        elif MPH < 111:
            category = "Category 2"
        elif MPH < 130:
            category = "Category 3"
        elif MPH < 157:
            category = "Category 4"
        elif MPH >= 157:
            category = "Category 5"

        if category == "Tropical Storm":
            print("You have recorded a tropical storm.")
        else:
            print("You have recorded a " + category + " Huricane!")
    except ValueError:
        print("Invalid")
        main()
main()