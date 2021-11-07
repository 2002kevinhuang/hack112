import tkinter
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from cmu_112_graphics import *
import time
from reddit import *


def appStarted(app):
    app.reddit = scrapeReddit()


def keyPressed(app, event):
    print(app.reddit)


def redrawAll(app, canvas):
    y, margin = 30, 0
    for line in app.reddit:
        canvas.create_text(20, y + margin, text=line, anchor=tkinter.NW, width=app.width - 50)
        margin += y
    # canvas.create_text(20, 20, text=app.reddit, anchor=tkinter.NW, width=app.width-50)


# print(reddit())
runApp(width=800, height=600)

# This should work
