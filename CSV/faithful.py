import csv
with open("C:\\Users\\825426\\Documents\\Intro to Programing\\IntroToPrograming\\CSV\\faithful.csv", "r") as file:
    table = csv.DictReader(file)
    total_wait = 0
    wait_time = []
    rows = 0
    for row in table:
        wait_time.append(row["Wait"])
        total_wait += int(row["Wait"])
        rows += 1
    print("The longest wait time was " + str(max(wait_time)) + " minutes")
    print("The average waot timee was " + str(total_wait/rows) + " minutes!")