import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# Returns list of tweets with format ['Name','@handle','Tweet']
def scrapeTwitter():
    driver = webdriver.Chrome("../hack112/chromedriver")
    url = 'https://www.twitter.com/'
    driver.get(url)
    while (driver.current_url != "https://twitter.com/home"):
        print("Logging in")
    print("Success")
    time.sleep(1.5)
    lenOfPage = driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    time.sleep(4.5)
    html = BeautifulSoup(driver.page_source, "html.parser")
    result = html.find_all("div", {"class": "css-1dbjc4n r-1igl3o0 r-qklmqi r-1adg3ll r-1ny4l3l"})
    results = []
    for item in result:
        tweet = item.find("div",
                          {
                              "class": "css-901oao r-1fmj7o5 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"})
        name = item.find("span", {"class": "css-901oao css-16my406 css-bfa6kz r-poiln3 r-bcqeeo r-qvutc0"})
        handle = item.find("div", {
            "class": "css-901oao css-bfa6kz r-9ilb82 r-18u37iz r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-qvutc0"})
        if type(tweet) is None:
            continue
        results.append([name.text, handle.text, tweet.text])
    return results
