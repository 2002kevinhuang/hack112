import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def reddit():
    driver = webdriver.Chrome("../hack112/chromedriver")
    url = 'https://www.reddit.com/'
    driver.get(url)
    print(driver.current_url)
    while (driver.current_url == "https://www.reddit.com/login/"):
        print("Logging in")
    print("success")
    time.sleep(2)
    html = BeautifulSoup(driver.page_source, "html.parser")
    result = html.find_all("h3", {"class": "_eYtD2XCVieq6emjKBH3m"})
    results = []
    for item in result:
        results.append(item.text)
    return results
