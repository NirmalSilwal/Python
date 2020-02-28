from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

# print(chrome_browser)
chrome_browser.maximize_window()

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
