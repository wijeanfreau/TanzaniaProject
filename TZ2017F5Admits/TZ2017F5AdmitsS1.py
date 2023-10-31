from playwright.sync_api import sync_playwright, expect
import time
import re

baselink = 'https://web.archive.org/web/20180224235524/https://www.tamisemi.go.tz/form_five_selection_or/'
masterlist = []

with sync_playwright() as my_playwright:
    #Open a chrome browser, context, and page.
    my_chrome = my_playwright.chromium.launch(headless=False)
    context = my_chrome.new_context()
    page = context.new_page()
    page.goto(baselink)
    #See how many pages are on the site:
    totalstr = page.get_by_text('Last').get_attribute('href')
    totalmatch = re.match(r'\?page=(\d{1,3})', totalstr)
    total = int(totalmatch.group(1))
    #Iterate through those pages:
    for i in range(0,total):
        screen = i + 1
        nextscreen = screen + 1
        print(f'We\'re on page {screen}')
        #Get a list of all the rows on the page:
        try:
            rows = page.locator('tr.show').all()
            #Iterate through the row:
            for row in rows:
                csvline = []
                cells = row.locator('td').all()
                for cell in cells:
                    content = cell.inner_text()
                    csvline.append(content)
                print(csvline)
                masterlist.append(csvline)
            page.get_by_text('Next').click()
            time.sleep(2)
        except:
            print(f'Oops, had an issue on screen {screen}')
            page.goto(f'https://web.archive.org/web/20170912153547/http://www.tamisemi.go.tz/form_five_selection_or/?page={nextscreen}')
            continue
    page.close()
    context.close()
    my_chrome.close()
    
with open('V:/FHSS-JoePriceResearch/RA_work_folders/Winthrop_Jeanfreau/TanzaniaProject/TanzaniaCSVs/TZ2017F5AdmitsS1.csv', 'w') as work_file:
    for row in masterlist:
        row_text = ''
        for item in row:
            row_text = row_text + item + ','
        row_text = row_text + '\n'
        work_file.write(row_text)