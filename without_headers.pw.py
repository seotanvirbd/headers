from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    response= page.goto('https://www.indeed.com/jobs?q=datascience')
    print(response.status)  
    browser.close()
