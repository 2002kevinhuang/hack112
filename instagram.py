import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Returns list of tweets with format ['Author','Caption','ImageURl','Link to Image']
def scrapeInsta():
    driver = webdriver.Chrome("../hack112/chromedriver")
    url = 'https://www.instagram.com/accounts/login/'
    driver.get(url)
    while (driver.current_url != "https://www.instagram.com/"):
        print("Logging in")
    print("Success")
    time.sleep(1)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    time.sleep(3)

    html = BeautifulSoup(driver.page_source, "html.parser")
    result = html.find_all("div", {"class":"qF0y9 Igw0E IwRSH YBx95 _4EzTm"})
    results = []
    print(len(result))
    for item in result:
        if str(item) == "None":
            continue
        caption = item.find("span",
                        {"class": "_8Pl3R"})
        author = item.find("div", {"class": "e1e1d"})
        image = item.find("div",{"class":"KL4Bh"})
        if str(image) == "None":
            continue
        srcIndex = str(image).find("src=")
        endOfLink = str(image).find("\"", srcIndex+6)
        image = str(image)[srcIndex+5:endOfLink]
        image = image.replace("amp;", "")

        if str(caption) == "None":
            continue
        results.append([author.text,caption.text,image])
    return results
print(scrapeInsta())
