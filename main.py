import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from cmu_112_graphics import *
import time

def reddit():
    driver = webdriver.Chrome("../hack112/chromedriver")
    url = 'https://www.reddit.com/'
    driver.get(url)
    print(driver.current_url)
    while(driver.current_url == "https://www.reddit.com/login/"):
        print("Logging in")
    print("logged in")
    html =  BeautifulSoup(driver.page_source, "html.parser")
    result = html.find_all("h3",{"class":"_eYtD2XCVieq6emjKBH3m"})
    results = []
    for item in result:
        results.append(item.text)
    return(results)

    

print(repr(reddit()))
# This should work