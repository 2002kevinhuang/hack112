import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome("../hack112/chromedriver")
url = 'https://www.twitter.com/login'
driver.get(url)

print(driver.current_url)

while(driver.current_url != "https://twitter.com/home"):
    print("Logging in")
print("logged in")

time.sleep(5)
html =  BeautifulSoup(driver.page_source, "html.parser")
result = html.find_all("div",{"class":"css-1dbjc4n r-1igl3o0 r-qklmqi r-1adg3ll r-1ny4l3l"})
print(result)
for item in result:
    print(item)
    content = item.find({"class":"css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"})
    print(item.text)

#HI