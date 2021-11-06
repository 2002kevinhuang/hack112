import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("/Users/bradywales/hack112/chromedriver")
driver.get("https://twitter.com")

while(driver.current_url != "https://twitter.com/home"):
    print("true")
print("false")


