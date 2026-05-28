import csv #6 points
with open("C:\\Users\\825426\\Documents\\Intro to Programing\\IntroToPrograming\\CSV\\faithful.csv", "r") as file:
    table = csv.DictReader(file)
    wait_time = []
    eruption_time = []
    total_wait = 0
    total_length = 0
    long_wait_eruption = 0
    rows = 0
    for row in table:
        eruption_time.append(row['Length'])
        total_length += float(row['Length'])
        wait_time.append(row['Wait'])
        total_wait += int(row['Wait'])
        rows += 1
    for row in table:
        print(row['Wait'])
        if " " + row['Wait'] == min(wait_time):
            long_wait_eruption.append(row['Length'])
            print("yes")
        continue
    print(min(wait_time))
    print("The average length was " + str(round(total_length/rows)) + " minutes!")
    print("The longest eruption time was " + str(max(eruption_time)) + " minutes!")
    print("The shortest eruption time was " + str(min(eruption_time)) + " minutes!")
    print("The average wait time was " + str(round(total_wait/rows)) + " minutes!")
    print("The longest wait time was " + str(max(wait_time)) + " minutes!")
    print("The shortest wait time was " +str(min(wait_time)) + " minutes!")
    print("The eruption time of the eruption with the longest wait was " + str(long_wait_eruption) + " minutes!")