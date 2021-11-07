import tkinter
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from cmu_112_graphics import *
import time
from reddit import *
from twitter import *


def appStarted(app):
    app.reddit = scrapeReddit()
    app.redditColors = ['#6C7A89'] * 7
    # app.twitter = scrapeTwitter()
    app.twitter = [['President Biden', '@POTUS',
                    'Initial unemployment insurance claims are down by nearly two-thirds since when I took office. \n\nThis is real progress – and we’re not slowing down.'],
                   ['President Biden', '@POTUS',
                    'No one should have to choose between paying for lifesaving medication or putting food on the table.\n \nMy Build Back Better Framework will help lower prescription drug costs for Americans.'],
                   ['Bill Gates', '@BillGates',
                    'Getting to zero emissions will be the hardest thing people have ever done. This was a great conversation about the power of innovation and what the world can accomplish if we work together.'],
                   ['Bill Gates', '@BillGates',
                    'I was truly inspired to hear @Vinisha27738476 speak at #COP26 this week. Her optimism and passion for innovation makes me hopeful that we can avoid a climate disaster.'],
                   ['President Biden', '@POTUS',
                    'Today, the Labor Department issued its rule requiring COVID-19 vaccinations for companies with 100 or more employees and HHS released its rule to ensure that health care workers are vaccinated.\n \nTogether, they will cover about 100 million Americans and help us beat COVID-19.'],
                   ['President Biden', '@POTUS',
                    'May the light of Diwali remind us that from darkness there is knowledge, wisdom, and truth. From division, unity. From despair, hope.\n\nTo Hindus, Sikhs, Jains, and Buddhists celebrating in America and around the world — from the People’s House to yours, happy Diwali.'],
                   ['President Biden', '@POTUS',
                    'Please, get your kids vaccinated. It’s safe and effective — and the best way to put this pandemic behind us.'],
                   ['Bill Gates', '@BillGates',
                    'Thank you, @SecGranholm for your leadership. The commitment of @ENERGY and the innovate spirit of our National Labs will drive the breakthroughs we need to help the whole world get to #NetZero.'],
                   ['President Biden', '@POTUS',
                    'We have made incredible progress on COVID-19 over these past nine months.\n \nBut we have to keep going.\n \nSo please, do your part. Get vaccinated.'],
                   ['Bill Gates', '@BillGates',
                    'Public-private collaborations will be critical to reducing emissions and achieving our 2050 climate goals. Our work with @MICleanEnergyRD will help us do just that.'],
                   ['Bill Gates', '@BillGates',
                    'I’m excited about @Breakthrough Energy’s expanded work with @MICleanEnergyRD. Thank you, @JonathanWNV for your partnership.']]
    app.twitterColors = []
    app.twitterTextColors = []


def keyPressed(app, event):
    print(app.reddit)
    # useless for now


def mouseMoved(app, event):
    # reddit colors
    if 30 <= event.x <= 770 and 65 <= event.y <= 103:
        app.redditColors[0] = '#6C7A89'
    else:
        app.redditColors[0] = '#95A5A6'
    if 30 <= event.x <= 770 and 118 <= event.y <= 156:
        app.redditColors[1] = '#6C7A89'
    else:
        app.redditColors[1] = '#95A5A6'
    if 30 <= event.x <= 770 and 171 <= event.y <= 209:
        app.redditColors[2] = '#6C7A89'
    else:
        app.redditColors[2] = '#95A5A6'
    if 30 <= event.x <= 770 and 224 <= event.y <= 262:
        app.redditColors[3] = '#6C7A89'
    else:
        app.redditColors[3] = '#95A5A6'
    if 30 <= event.x <= 770 and 277 <= event.y <= 315:
        app.redditColors[4] = '#6C7A89'
    else:
        app.redditColors[4] = '#95A5A6'
    if 30 <= event.x <= 770 and 330 <= event.y <= 368:
        app.redditColors[5] = '#6C7A89'
    else:
        app.redditColors[5] = '#95A5A6'
    if 30 <= event.x <= 770 and 383 <= event.y <= 421:
        app.redditColors[6] = '#6C7A89'
    else:
        app.redditColors[6] = '#95A5A6'


def redrawAll(app, canvas):
    # reddit testing
    # y, margin = 30, 0
    # for line in app.reddit:
    #     canvas.create_text(20, y + margin, text=line, anchor=tkinter.NW, width=app.width - 50)
    #     margin += y
    # canvas.create_text(20, 20, text=app.reddit, anchor=tkinter.NW, width=app.width-50)
    vertical_divide = app.width / 2
    horizontal_divide = app.height / 2
    # 4-section dividers
    canvas.create_line(vertical_divide, 0, vertical_divide, app.height, width=2)
    canvas.create_line(0, horizontal_divide, app.width, horizontal_divide, width=2)
    # section headers
    canvas.create_text(vertical_divide / 2, 30, text='Reddit', font=('Bold', '30'),
                       fill='#6C7A89', activefill='black')
    canvas.create_text(vertical_divide / 2 * 3, 30, text='Twitter', font=('Bold', '30'),
                       fill='#22A7F0', activefill='#003171')
    # rectangles
    height, gap = 38, 15
    x, y = 30, 50
    reddit_text_locations = []
    i = 0
    twitter_lengths = [195, 320]
    while y + height < horizontal_divide - 20:
        canvas.create_rectangle(x, y + gap, vertical_divide - 30, y + height + gap, width=0, fill=app.redditColors[i])
        canvas.create_rectangle(170, y + gap, 200, y + height + gap, fill='white', width=0)  # used to be 200-230
        canvas.create_rectangle(vertical_divide + 30, y + gap, app.width - 30, y + height + gap, width=0,
                                fill='#22A7F0',
                                activefill='#003171', activewidth=10)
        canvas.create_rectangle(vertical_divide + twitter_lengths[0] - 30, y + gap,
                                vertical_divide + twitter_lengths[0], y + height + gap, fill='white', width=0)
        canvas.create_rectangle(vertical_divide + twitter_lengths[1] - 30, y + gap,
                                vertical_divide + twitter_lengths[1], y + height + gap, fill='white', width=0)
        reddit_text_locations.append((y + gap + y + height + gap) / 2)
        y += height + gap
        i += 1

    for i in range(7):
        # reddit
        sub = app.reddit[i][1]
        if len(sub) > 17:
            sub = sub[:14].rstrip() + '...'
        title = app.reddit[i][0]
        max_title = 86
        if len(title) > max_title:
            title = title[:max_title - 3].rstrip() + '...'
        canvas.create_text(45, reddit_text_locations[i], text=sub, font='15', anchor=tkinter.W)
        canvas.create_text(215, reddit_text_locations[i], text=title, font='15', anchor=tkinter.W)
        # twitter
        name = app.twitter[i][0]
        if len(name) > 16:
            name = name[:13].rstrip() + '...'
        handle = app.twitter[i][1]
        if len(handle) > 10:
            handle = handle[:7].rstrip() + '...'
        tweet = app.twitter[i][2]
        tweet_length = 67
        if len(tweet) > tweet_length:
            tweet = tweet[:tweet_length - 3].rstrip() + '...'
        canvas.create_text(845, reddit_text_locations[i], text=name, font='15', anchor=tkinter.W)
        canvas.create_text(800 + twitter_lengths[0] + 15, reddit_text_locations[i], text=handle, font='15',
                           anchor=tkinter.W)
        canvas.create_text(800 + twitter_lengths[1] + 15, reddit_text_locations[i], text=tweet, font='15',
                           anchor=tkinter.W)

runApp(width=1600, height=900)
