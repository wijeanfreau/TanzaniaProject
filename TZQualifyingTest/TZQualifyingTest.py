from playwright.sync_api import sync_playwright, expect
import time
import re
#re.findall vs re.finditer
baselink = 'https://maktaba.tetea.org/exam-results/QT2016/QT2016.html'
masterlist = []

with sync_playwright() as my_playwright:
    browser = my_playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #Go to the page
    page.goto(baselink)
    #Grab all the year links, then navigate to the right year
    lyears = page.locator('a.navbar').all()
    for lyear in lyears:
        year = lyear.inner_text()
        lyear.click()
        time.sleep(5)
        #Grab all the text on the page
        try:
            masstext = page.locator('pre').inner_text()
            print('Using pre tag')
        except:
            masstext = page.locator('xmp').inner_text()
            print('Using xmp tag')
        pattern = r'(\d{4})\s{2}([FM])\s{2}(\b[A-Z]+(?:\'[A-Z]+)?\s+[A-Z]+(?:\'[A-Z]+)?\s+\w+(?:\'[A-Z]+)?\b)\s+([A-Z]+)'
        students = re.findall(pattern, masstext)
        for student in students:
            cno, gender, name, remark = student
            csvline = [cno, gender, name, remark, year]
            print(csvline)
            masterlist.append(csvline)
    
    page.close()
    context.close()
    browser.close()
    
with open('V:/FHSS-JoePriceResearch/RA_work_folders/Winthrop_Jeanfreau/TanzaniaProject/TanzaniaCSVs/TZQualifyingTest.csv', 'w') as work_file:
    for row in masterlist:
        row_text = ''
        for item in row:
            row_text = row_text + item + ','
        row_text = row_text + '\n'
        work_file.write(row_text)