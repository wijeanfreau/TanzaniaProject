from playwright.sync_api import sync_playwright
import re
import time

baselink = 'https://maktaba.tetea.org/exam-results/FTNA2015/formtwo-2015.html'
masterlist = []
year = str(2015)

with sync_playwright() as pw:
    #Open a new browser, context, and page
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #Go to the page, grab all the links
    page.goto(baselink)
    time.sleep(5)
    schoollinks = page.locator('a').all()
    schoolit = 0
    #Iterate through the links, but skip the first 12 because they're useless
    for ischool in schoollinks:
        if schoolit < 13:
            schoolit += 1
            continue
        #Grab the school name, then go to the results for that school
        school = ischool.inner_text()
        school = re.sub(r',', '', school)
        print(f'Headed to school {school} in {year}')
        ischool.click()
        time.sleep(1)
        #Grab all the table rows on the page
        rows = page.locator('tr').all()
        #Iterate through the rows
        for row in rows:
            cells = row.locator('td').all()
            #Check if the row is a row we like, by looking at the first cell and seeing if it's a CNO number
            if len(cells) == 0:
                continue
            if not re.match(r'\d{4}', cells[0].inner_text()):
                continue
            #Create our csvline, and iterate through each cell on the good rows.
            csvline = [school,year]
            for cell in cells:
                cellcontents = cell.inner_text()
                cellcontents = re.sub(r',', '', cellcontents)
                csvline.append(cellcontents)
            print(csvline)
            masterlist.append(csvline)
        page.goto(baselink)
                
                
    page.close()
    context.close()
    browser.close()
    
with open('V:/FHSS-JoePriceResearch/RA_work_folders/Winthrop_Jeanfreau/TanzaniaProject/TanzaniaCSVs/TZF2ExamResults2015Raw.csv', 'w') as work_file:
    for row in masterlist:
        row_text = ''
        for item in row:
            row_text = row_text + item + ','
        row_text = row_text + '\n'
        work_file.write(row_text)