import tkinter
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from cmu_112_graphics import *
import time
from reddit import *


def appStarted(app):
    # app.reddit = scrapeReddit()
    app.test = []


# def keyPressed(app, event):
    # print(app.reddit)


def redrawAll(app, canvas):
    # reddit testing
    # y, margin = 30, 0
    # for line in app.reddit:
    #     canvas.create_text(20, y + margin, text=line, anchor=tkinter.NW, width=app.width - 50)
    #     margin += y
    # canvas.create_text(20, 20, text=app.reddit, anchor=tkinter.NW, width=app.width-50)
    vertical_divide = app.width/2
    horizontal_divide = app.height/2
    # 4-section dividers
    canvas.create_line(vertical_divide, 0, vertical_divide, app.height, width=2)
    canvas.create_line(0, horizontal_divide, app.width, horizontal_divide, width=2)
    # section headers
    canvas.create_text(vertical_divide/2, 30, text='Reddit', font=('Bold', '30'))
    canvas.create_text(vertical_divide/2 * 3, 30, text='Twitter', font=('Bold', '30'))
    # rectangles
    height, gap = 38, 15
    x, y = 30, 50
    while y + height < horizontal_divide-20:
        # canvas.create_rectangle(x, y+gap, 200, y+height+gap, width=0, fill='#D2D7D3',
        #                         activefill='#95A5A6', activewidth=10)
        # canvas.create_rectangle(230, y+gap, vertical_divide-30, y+height+gap)
        canvas.create_rectangle(x, y+gap, vertical_divide-30, y+height+gap, width=0, fill='#D2D7D3',
                                activefill='#95A5A6', activewidth=10)
        canvas.create_rectangle(200, y+gap, 230, y+height+gap, fill='white', width=0)
        canvas.create_rectangle(vertical_divide+30, y+gap, app.width-30, y+height+gap, width=0, fill='#22A7F0',
                                activefill='#003171', activewidth=10)
        canvas.create_rectangle(vertical_divide+200, y+gap, vertical_divide+230, y+height+gap, fill='white', width=0)
        canvas.create_rectangle(vertical_divide+350, y+gap, vertical_divide+380, y+height+gap, fill='white', width=0)
        y += height + gap
        # 200 to 230, 350 to 380

# print(reddit())
runApp(width=1600, height=900)

# This should work
