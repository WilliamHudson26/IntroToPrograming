import csv #5 points ; complete
with open("C:\\Users\\825426\\Documents\\Intro to Programing\\IntroToPrograming\\CSV\\deniro.csv","r",encoding = "utf-8") as file:
    table = csv.DictReader(file)
    average = 0
    rateings = []
    longest = "null"
    longness = 0
    rows = 0

    for row in table:
        average += int(row['Score'])
        rateings.append(int(row['Score']))
        if longness < len(str(row['Title'])):
            longest = str(row['Title'])
            longness = len(str(row['Title']))
        if int(row['Score']) == max(rateings):
            title_max = str(row['Title'])
            rate_max = int(row['Score'])
        if int(row['Score']) == min(rateings):
            title_min = str(row['Title'])
            rate_min = int(row['Score'])
        rows += 1

    print("The highest rated movie is" + title_max + " with a score of " + str(rate_max))
    print("The lowest rated movie is" + title_min + " with a score of " + str(rate_min))
    print("The average rateing of Rober De Niro's movies is " + str(round(average/rows)))
    print("The longest movie title is" + longest)