import csv #1 points
with open("C:\\Users\\825426\\Documents\\Intro to Programing\\IntroToPrograming\\CSV\\occupation-2018-census-csv.csv","r",encoding = "utf-8") as file:
    table = csv.DictReader(file)

    for row in table:
        if row['Occupation'] == "Grape Grower":
            grape_grower = str(row['Employed_census_usually_resident_population_count_aged_15_years_and_over'])
        print("There are " + grape_grower + " grape growers")