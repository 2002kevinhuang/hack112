import tkinter
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from cmu_112_graphics import *
import time


def appStarted(app):
    app.reddit = reddit()


def keyPressed(app, event):
    print(app.reddit)


def redrawAll(app, canvas):
    y, margin = 30, 0
    for line in app.reddit:
        canvas.create_text(20, y + margin, text=line, anchor=tkinter.NW, width=app.width - 50)
        margin += y
    # canvas.create_text(20, 20, text=app.reddit, anchor=tkinter.NW, width=app.width-50)


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


# print(reddit())
runApp(width=800, height=600)

# This should work
