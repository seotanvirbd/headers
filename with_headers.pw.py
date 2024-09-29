from playwright.sync_api import sync_playwright

x = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
with sync_playwright() as p:
    browser = p.chromium.launch()
    context= browser.new_context(user_agent= x)
    page = context.new_page() 
    response= page.goto('https://www.indeed.com/jobs?q=datascience')
    print(response.status)
    
