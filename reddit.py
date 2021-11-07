import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time


# Returns list of posts with format ['Title', 'subreddit', 'op']
def scrapeReddit():
    driver = webdriver.Chrome("../hack112/chromedriver")
    url = 'https://www.reddit.com/login'
    driver.get(url)
    while (driver.current_url == "https://www.reddit.com/login/"):
        print("Logging in")
    print("Success")

    # time.sleep(5)
    html = BeautifulSoup(driver.page_source, "html.parser")
    result = html.find_all("div", {"class": "_1oQyIsiPHYt6nx7VOmd1sz"})
    results = []
    for item in result:
        title = item.find("h3", {"class": "_eYtD2XCVieq6emjKBH3m"})
        # upvotesClass = item.find("div",{"class": "_23h0-EcaBUorIHC-JZyh6J"})
        # numUpvotes = upvotesClass.find("span",{"class":"D6SuXeSnAAagG8dKAb4O4"})
        sub = item.find("div", {"class": "_2mHuuvyV9doV3zwbZPtIPG"})
        op = item.find("a", {"class": "_2tbHP6ZydRpjI44J3syuqC"})
        if (title is None or sub is None or op is None):
            break
        if [title.text, sub.text, op.text] not in results:
            results.append([title.text, sub.text, op.text])
    return results
