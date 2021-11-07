import tkinter
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from cmu_112_graphics import *
import time
from reddit import *


def appStarted(app):
    app.reddit = scrapeReddit()
    app.test = []


def keyPressed(app, event):
    print(app.reddit)


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
    canvas.create_text(vertical_divide/2, 30, text='Reddit', font=('Bold', '30'),
                       fill='#6C7A89', activefill='black')
    canvas.create_text(vertical_divide/2 * 3, 30, text='Twitter', font=('Bold', '30'),
                       fill='#22A7F0', activefill='#003171')
    # rectangles
    height, gap = 38, 15
    x, y = 30, 50
    reddit_text_locations = []
    while y + height < horizontal_divide-20:
        # canvas.create_rectangle(x, y+gap, 200, y+height+gap, width=0, fill='#D2D7D3',
        #                         activefill='#95A5A6', activewidth=10)
        # canvas.create_rectangle(230, y+gap, vertical_divide-30, y+height+gap)
        canvas.create_rectangle(x, y+gap, vertical_divide-30, y+height+gap, width=0, fill='#D2D7D3',
                                activefill='#95A5A6', activewidth=10)
        canvas.create_rectangle(170, y+gap, 200, y+height+gap, fill='white', width=0) # used to be 200-230
        canvas.create_rectangle(vertical_divide+30, y+gap, app.width-30, y+height+gap, width=0, fill='#22A7F0',
                                activefill='#003171', activewidth=10)
        canvas.create_rectangle(vertical_divide+200, y+gap, vertical_divide+230, y+height+gap, fill='white', width=0)
        canvas.create_rectangle(vertical_divide+350, y+gap, vertical_divide+380, y+height+gap, fill='white', width=0)
        reddit_text_locations.append((y+gap+y+height+gap)/2)
        y += height + gap

    for i in range(7):
        sub = app.reddit[i][1]
        if len(sub) > 17:
            sub = sub[:14].rstrip() + '...'
        title = app.reddit[i][0]
        max_title = 85
        if len(title) > max_title:
            title = title[:max_title-3].rstrip() + '...'
        canvas.create_text(45, reddit_text_locations[i], text=sub, font='15', anchor=tkinter.W)
        canvas.create_text(215, reddit_text_locations[i], text=title, font='15', anchor=tkinter.W)


# print(reddit())
runApp(width=1600, height=900)

# This should work