from playwright.sync_api import sync_playwright, expect
import time
import re

baselink = 'https://necta.go.tz/gatce_results'
masterlist = []

with sync_playwright() as my_playwright:
    #Open a browser, context, and page.
    my_chrome = my_playwright.chromium.launch(headless=False)
    context = my_chrome.new_context()
    page = context.new_page()
    #Go to the baselink
    page.goto(baselink)
    v20thru23 = page.get_by_text('Link 1: Click here to view').all()
    #Navigate to a specific year
    for lyear in v20thru23:
        lyear.click()
        time.sleep(5)
        baseyear = page.url
        #Grab a list of all the colleges
        colleges = page.get_by_text('COLLEGE').all()
        #Iterate through each college
        for lcollege in colleges:
            #Grab the name of the college, then go the page
            college = lcollege.inner_text()
            lcollege.click()
            time.sleep(1)
            #Grab the year
            yearstr = page.get_by_text('EXAMINATION RESULTS').inner_text()
            yearmatch = re.match(r'.+(\d{4}).+RESULTS', yearstr)
            year = yearmatch.group(1)
            print(f'Found {college} in {year}!')
            #Iterate through the table of grades
            it = 0
            trows = page.locator('tr').all()
            for trow in trows:
                #Skip the first row
                if it < 1:
                    it += 1
                    continue
                #Grab the cells in each row
                cells = trow.locator('td').all()
                csvline = [college,year]
                for cell in cells:
                    content = cell.inner_text()
                    csvline.append(content)
                masterlist.append(csvline)
            
            page.goto(baseyear)
        page.goto(baselink)
        
with open('V:/FHSS-JoePriceResearch/RA_work_folders/Winthrop_Jeanfreau/TanzaniaProject/TanzaniaCSVs/TeacherTrainingExamp20-23.csv', 'w') as work_file:
    for row in masterlist:
        row_text = ''
        for item in row:
            row_text = row_text + item + ','
        row_text = row_text + '\n'
        work_file.write(row_text)