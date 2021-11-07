import tkinter
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from cmu_112_graphics import *
import time
from reddit import *
from twitter import *


def appStarted(app):
    # app.reddit = scrapeReddit()
    app.redditColors = ['#6C7A89'] * 7
    # app.twitter = scrapeTwitter()
    app.twitterColors = ['#003171'] * 7
    app.twitterTextColors = ['black'] * 7

    # temporary patch to make runtime faster / revert before final version
    app.reddit = [['Which film is the perfect comedy?', 'r/AskReddit', 'u/BlackmoreGrant'], ['We like thumb-wrestling with ourselves as much as anybody else, but the XP gains just hit different when you’re racking up wins across the expansive 7.6” edge-to-edge display of Galaxy Z Fold3 5G — perfectly sized for your pocket or purse so you can take your game to the next level wherever you go.', 'u/SamsungMobileUS', 'u/SamsungMobileUS'], ['DWG KIA vs. EDward Gaming / 2021 World Championship - Final / Post-Match Discussion', 'r/leagueoflegends', 'u/Soul_Sleepwhale'], ["My roommate cooks frozen pizzas without taking them off the cardboard. He says that's the proper way to cook them and I'm weird because I don't.", 'r/mildlyinfuriating', 'u/an_evil_eskimo'], ['I captured the Horsehead and Flame nebula with my home telescope.', 'r/space', 'u/chucksastro'], ['Are you vaccinated?', 'r/teenagers', 'u/pjanmaxxx'], ['[Highlight] Luka beats the Celtics at the Buzzer with a crazy three', 'r/nba', 'u/CP3_for_MvP'], ['Well?', 'r/gaming', 'u/nisebblumberg']]
    app.twitter = [['Carnegie Mellon University', '@CarnegieMellon', "New research from @ProfGS_ and @FollowStevens's Jose E. Ramirez-Marquez  suggests that monitoring social media during hurricanes could help communities better plan for and mitigate the impacts of climate change. https://cmu.is/twitter-hurricanes…"], ['Bill Gates', '@BillGates', 'As we’ve seen this past year, new variants of a disease can emerge over time. In order to develop new tools to fight the disease, we need to identify those variants quickly. Dr. Senjuti Saha is one expert working to sequence SARS-CoV-2: https://b-gat.es/3kjGgYx'], ['President Biden', '@POTUS', 'We need to build an economy that gives working people a fair shot. We need to restore fairness to our tax code. We need to make long overdue investments in our infrastructure. We need to pass the Bipartisan Infrastructure Deal and my Build Back Better Agenda.'], ['SpaceX', '@SpaceX', 'Splashdown! Welcome back to planet Earth, @Inspiration4x!'], ['CMU Provost Office', '@CMUProvost', "Behind every great performance is inspiration, and behind that inspiration is a great teacher. That's why @CarnegieMellon is proud to be the exclusive higher ed partner of @TheTonyAwards. https://cmu.is/tonys-theatre\n\nTune into the #TonyAwards Sept. 26 on @CBS and @paramountplus."], ['SpaceX', '@SpaceX', 'Dragon has entered its last orbit before reentry and splashdown → http://spacex.com/launches'], ['Carnegie Mellon University', '@CarnegieMellon', 'CareLink provides an alternative option for finding help or a job and is a way for our Tartan community to connect, support one another, and embrace our shared talent. https://cmu.is/carelink'], ['SpaceX', '@SpaceX', 'Orbital moonrise'], ['President Biden', '@POTUS', 'My plan is very clear: we will not raise taxes on anyone making under $400,000 a year.\n \nIt’s only corporations and people making over $400,000 a year who will see their taxes go up.'], ['President Biden', '@POTUS', 'Big corporations and the super wealthy have to start paying their fair share.\n \nIt is long overdue.'], ['Carnegie Mellon University', '@CarnegieMellon', "Researchers from CMU and @OregonState on Team Explorer put autonomous robots to the test, developing tech to aid first responders in environments that are unsafe for humans.\n\nThey're competing in the final leg of the @DARPA #SubTChallenge.\n\nhttps://cmu.is/scs-subtchallenge… #TartanProud"], ['Carnegie Mellon University', '@CarnegieMellon', '"If you lead your life the right way, the karma will take care of itself. The dreams will come to you.”\n\nOn this day 14 years ago, only a few weeks after learning he had just months to live, CMU professor and alumnus Randy Pausch delivered what became known as "The Last Lecture."'], ['Elon Musk', '@elonmusk', 'Moving at ~23 times speed of sound, circling Earth every ~90 minutes'], ['AirLab', '@AirLabCMU', '#TeamExplorerSubt is packed and ready to go!']]


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

    # twitter colors
    if 830 <= event.x <= 1570 and 65 <= event.y <= 103:
        app.twitterColors[0] = '#003171'
        app.twitterTextColors[0] = 'white'
    else:
        app.twitterColors[0] = '#22A7F0'
        app.twitterTextColors[0] = 'black'
    if 830 <= event.x <= 1570 and 118 <= event.y <= 156:
        app.twitterColors[1] = '#003171'
        app.twitterTextColors[1] = 'white'
    else:
        app.twitterColors[1] = '#22A7F0'
        app.twitterTextColors[1] = 'black'
    if 830 <= event.x <= 1570 and 171 <= event.y <= 209:
        app.twitterColors[2] = '#003171'
        app.twitterTextColors[2] = 'white'
    else:
        app.twitterColors[2] = '#22A7F0'
        app.twitterTextColors[2] = 'black'
    if 830 <= event.x <= 1570 and 224 <= event.y <= 262:
        app.twitterColors[3] = '#003171'
        app.twitterTextColors[3] = 'white'
    else:
        app.twitterColors[3] = '#22A7F0'
        app.twitterTextColors[3] = 'black'
    if 830 <= event.x <= 1570 and 277 <= event.y <= 315:
        app.twitterColors[4] = '#003171'
        app.twitterTextColors[4] = 'white'
    else:
        app.twitterColors[4] = '#22A7F0'
        app.twitterTextColors[4] = 'black'
    if 830 <= event.x <= 1570 and 330 <= event.y <= 368:
        app.twitterColors[5] = '#003171'
        app.twitterTextColors[5] = 'white'
    else:
        app.twitterColors[5] = '#22A7F0'
        app.twitterTextColors[5] = 'black'
    if 830 <= event.x <= 1570 and 383 <= event.y <= 421:
        app.twitterColors[6] = '#003171'
        app.twitterTextColors[6] = 'white'
    else:
        app.twitterColors[6] = '#22A7F0'
        app.twitterTextColors[6] = 'black'


def redrawAll(app, canvas):
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
                                fill=app.twitterColors[i])
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
        tweet_length = 64
        if len(tweet) > tweet_length:
            tweet = tweet[:tweet_length - 3].rstrip() + '...'
        canvas.create_text(845, reddit_text_locations[i], text=name, font='15', anchor=tkinter.W,
                           fill=app.twitterTextColors[i])
        canvas.create_text(800 + twitter_lengths[0] + 15, reddit_text_locations[i], text=handle, font='15',
                           anchor=tkinter.W, fill=app.twitterTextColors[i])
        canvas.create_text(800 + twitter_lengths[1] + 15, reddit_text_locations[i], text=tweet, font='15',
                           anchor=tkinter.W, fill=app.twitterTextColors[i])

runApp(width=1600, height=900)
