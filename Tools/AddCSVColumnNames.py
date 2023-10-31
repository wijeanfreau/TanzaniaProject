import csv

column_names = ['SCHOOL','YEAR','CNO','REPEATER','NAME OF CANDIDATE','SEX','CIVICS','HISTORY','GEOGRAPHY','KISWAHILI','ENGLISH','PHYSICS','CHEMISTRY','BIOLOGY','B/MATH','GPA','CLASS']

csv_filename = 'V:/FHSS-JoePriceResearch/RA_work_folders/Winthrop_Jeanfreau/TanzaniaProject/TanzaniaCSVs/TZF2ExampResults2014.csv'

with open(csv_filename, 'r', newline='') as input_file:
    reader = csv.reader(input_file)
    
    data = [row for row in reader]
    
with open(csv_filename, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(column_names)
    writer.writerows(data)
            
print('Added column names.')