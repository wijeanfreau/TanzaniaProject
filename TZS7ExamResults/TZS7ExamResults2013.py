from playwright.sync_api import sync_playwright
import re
import time

baselink = 'https://maktaba.tetea.org/exam-results/PSLE2013/psle.htm'
masterlist = []
year = str(2013)

with sync_playwright() as pw:
    #Open a new browser, context, and page
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #Go to the page, grab all the links
    page.goto(baselink)
    time.sleep(5)
    schoollinks = page.locator('a').all()
    del schoollinks[:14]
    for school in schoollinks:
        print(school.inner_text())