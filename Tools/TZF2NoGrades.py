import csv
import re

#Check the layout of the CSV before running this!
year = '2014'
#We need to iterate through each list and remove the grades from the data
csvpath = f'V:\FHSS-JoePriceResearch\RA_work_folders\Winthrop_Jeanfreau\TanzaniaProject\TanzaniaCSVs\TZF2ExamResults{year}Raw.csv'
newcsvpath = f'V:\FHSS-JoePriceResearch\RA_work_folders\Winthrop_Jeanfreau\TanzaniaProject\TanzaniaCSVs\TZF2ExamResults{year}Clean.csv'


#Open the CSV
with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)
    rows = list(csv_reader)

#Iterate through each row
for row in rows:
    try:
        #Go find the index number of the GPA/Points
        #Change this regex to match the first item after individual grades, and nothing else.
        pattern = r'\d\.\d'
        index_match = []
        for n, entry in enumerate(row):
            if re.search(pattern, entry):
                index_match.append(n) #With that index, we know when the grades end in our list.
        

        grade_start = 6 #So that row[grade_start] will return the first grade
        grade_end = max(index_match) #So that row[grade_end] will return the GPA/Points. We don't want it to return the last grade because when we delete the slice, the end point is non-inclusive.
        #Delete the slice of grades
        del row[grade_start:grade_end]
        print(row)
    except Exception as error:
        print(f'Oops, found an error! They were probably absent, but here\'s the error anyways: ', error)
        print(row)

#Write all of our new rows to a new, clean, CSV.
with open(newcsvpath, 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(rows)

file.close()