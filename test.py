import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome("../hack112/chromedriver")
url = 'https://www.reddit.com/login'
driver.get(url)
html =  BeautifulSoup(driver.page_source, "html.parser")

print(driver.current_url)

while(driver.current_url == "https://www.reddit.com/login/"):
    print("Logging in")
print("logged in")

html =  BeautifulSoup(driver.page_source, "html.parser")
result = html.find_all("h3",{"class":"_eYtD2XCVieq6emjKBH3m"})
for item in result:
    print(item.text)

