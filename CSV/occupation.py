import csv #7 points ; 6 points left
with open("C:\\Users\\825426\\Documents\\Intro to Programing\\IntroToPrograming\\CSV\\occupation-2018-census-csv.csv","r",encoding = "utf-8") as file:
    table = csv.DictReader(file)
    grape_grower = "null"
    oc_with_num = "null"
    oc_with_code = "null"
    common = []
    occupation = []
    oc_max = "null"
    oc_min = "null"

    for row in table:
        if row['Occupation'] == "Total" or row['Occupation'] == "Total stated" or row['Occupation'] == "Not stated" or row['Occupation'] == "Response outside scope" or row['Occupation'] == "Response unidentifiable":
            continue
        common.append(int(row['Employe']))
        occupation.append(row['Occupation'])
        if row['Occupation'] == "Grape Grower":
            grape_grower = str(row['Employe'])
        if row['Employe'] == "14298":
            oc_with_num = row['Occupation']
        if row['Code'] == "451311":
            oc_with_code = row['Occupation']
        if int(row['Employe']) == max(common):
            oc_max = row['Occupation']
        if int(row['Employe']) == min(common):
            oc_min = row['Occupation']
                
        
    print("The most common occupation is "+ oc_max +" with "+ str(max(common)) +" employees")
    print("The most common occupation is "+ oc_min +" with "+ str(min(common)) +" employees")
    print("There are " + grape_grower + " grape growers")
    print("The occupation with 14298 employees is " + oc_with_num)
    print("The occupation with the code 451311 is " + oc_with_code)