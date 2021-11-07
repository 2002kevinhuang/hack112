import tkinter
import copy
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from cmu_112_graphics import *
import time
from reddit import *
from twitter import *
from youtube import *


def appStarted(app):
    # app.reddit = scrapeReddit()
    app.redditColors = ['#6C7A89'] * 7
    # app.twitter = scrapeTwitter()
    app.twitterColors = ['#003171'] * 7
    app.twitterTextColors = ['black'] * 7
    # app.youtube = scrapeYoutube()
    app.youtubeColors = ['#E68364'] * 6
    app.youtubeTextColors = ['black'] * 6
    # animations
    app.r1, app.r2, app.r3, app.r4 = 1, 1, 1, 1
    app.animateColors = ['white'] * 4
    app.headerColors = ['#6C7A89', '#22A7F0', '#E68364', '#D24D57']

    # custom cursor
    # app.cursor_radius = 5
    # app.cursor_fill = '#D9B611'
    # app.cursor_x, app.cursor_y = -1, -1

    # temporary patch to make runtime faster / revert before final version
    app.reddit = [['Which film is the perfect comedy?', 'r/AskReddit', 'u/BlackmoreGrant'], ['We like thumb-wrestling with ourselves as much as anybody else, but the XP gains just hit different when you’re racking up wins across the expansive 7.6” edge-to-edge display of Galaxy Z Fold3 5G — perfectly sized for your pocket or purse so you can take your game to the next level wherever you go.', 'u/SamsungMobileUS', 'u/SamsungMobileUS'], ['DWG KIA vs. EDward Gaming / 2021 World Championship - Final / Post-Match Discussion', 'r/leagueoflegends', 'u/Soul_Sleepwhale'], ["My roommate cooks frozen pizzas without taking them off the cardboard. He says that's the proper way to cook them and I'm weird because I don't.", 'r/mildlyinfuriating', 'u/an_evil_eskimo'], ['I captured the Horsehead and Flame nebula with my home telescope.', 'r/space', 'u/chucksastro'], ['Are you vaccinated?', 'r/teenagers', 'u/pjanmaxxx'], ['[Highlight] Luka beats the Celtics at the Buzzer with a crazy three', 'r/nba', 'u/CP3_for_MvP'], ['Well?', 'r/gaming', 'u/nisebblumberg']]
    app.twitter = [['Carnegie Mellon University', '@CarnegieMellon', "New research from @ProfGS_ and @FollowStevens's Jose E. Ramirez-Marquez  suggests that monitoring social media during hurricanes could help communities better plan for and mitigate the impacts of climate change. https://cmu.is/twitter-hurricanes…"], ['Bill Gates', '@BillGates', 'As we’ve seen this past year, new variants of a disease can emerge over time. In order to develop new tools to fight the disease, we need to identify those variants quickly. Dr. Senjuti Saha is one expert working to sequence SARS-CoV-2: https://b-gat.es/3kjGgYx'], ['President Biden', '@POTUS', 'We need to build an economy that gives working people a fair shot. We need to restore fairness to our tax code. We need to make long overdue investments in our infrastructure. We need to pass the Bipartisan Infrastructure Deal and my Build Back Better Agenda.'], ['SpaceX', '@SpaceX', 'Splashdown! Welcome back to planet Earth, @Inspiration4x!'], ['CMU Provost Office', '@CMUProvost', "Behind every great performance is inspiration, and behind that inspiration is a great teacher. That's why @CarnegieMellon is proud to be the exclusive higher ed partner of @TheTonyAwards. https://cmu.is/tonys-theatre\n\nTune into the #TonyAwards Sept. 26 on @CBS and @paramountplus."], ['SpaceX', '@SpaceX', 'Dragon has entered its last orbit before reentry and splashdown → http://spacex.com/launches'], ['Carnegie Mellon University', '@CarnegieMellon', 'CareLink provides an alternative option for finding help or a job and is a way for our Tartan community to connect, support one another, and embrace our shared talent. https://cmu.is/carelink'], ['SpaceX', '@SpaceX', 'Orbital moonrise'], ['President Biden', '@POTUS', 'My plan is very clear: we will not raise taxes on anyone making under $400,000 a year.\n \nIt’s only corporations and people making over $400,000 a year who will see their taxes go up.'], ['President Biden', '@POTUS', 'Big corporations and the super wealthy have to start paying their fair share.\n \nIt is long overdue.'], ['Carnegie Mellon University', '@CarnegieMellon', "Researchers from CMU and @OregonState on Team Explorer put autonomous robots to the test, developing tech to aid first responders in environments that are unsafe for humans.\n\nThey're competing in the final leg of the @DARPA #SubTChallenge.\n\nhttps://cmu.is/scs-subtchallenge… #TartanProud"], ['Carnegie Mellon University', '@CarnegieMellon', '"If you lead your life the right way, the karma will take care of itself. The dreams will come to you.”\n\nOn this day 14 years ago, only a few weeks after learning he had just months to live, CMU professor and alumnus Randy Pausch delivered what became known as "The Last Lecture."'], ['Elon Musk', '@elonmusk', 'Moving at ~23 times speed of sound, circling Earth every ~90 minutes'], ['AirLab', '@AirLabCMU', '#TeamExplorerSubt is packed and ready to go!']]
    app.youtube = [['Squid Game - SNL', 'Saturday Night Live', 'https://i.ytimg.com/vi/vWdHPMhy270/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&amp;rs=AOn4CLBRjFFWOF4SZJsLnqyNkPmJnuo0rQ', 'https://www.youtube.com/watch?v=vWdHPMhy270'], ['Guy Pulls Out Sign on Gophers Kiss Cam', 'Minnesota Gophers', 'https://i.ytimg.com/vi/MyfYodavAj8/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&amp;rs=AOn4CLAjlco_UAvXpcWwjr-D7m0t51UShA', 'https://www.youtube.com/watch?v=MyfYodavAj8'], ['Pokemon but the World Champion controls the AI', 'SmallAnt', 'https://i.ytimg.com/vi/QTxoDSAe7yw/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&amp;rs=AOn4CLDkakXcqJfsbcSJuR3_rBTVVgpWdg', 'https://www.youtube.com/watch?v=QTxoDSAe7yw'], ['Risk', 'Telepurte', 'https://i.ytimg.com/vi/wqJAMFH1pqA/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&amp;rs=AOn4CLCz84OzpAXg2EVv4UnRhss8iDm2PQ', 'https://www.youtube.com/watch?v=wqJAMFH1pqA'], ['Liquid Venom Suit Covers My Whole Body!', 'JLaservideo', 'https://i.ytimg.com/vi/8Xfz09IJTYY/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&amp;rs=AOn4CLDeYPHOZLEFExj9NnQgOsLzHmzTgg', 'https://www.youtube.com/watch?v=8Xfz09IJTYY'], ['20 FUNNY MOMENTS WITH REPORTERS IN SPORTS', 'SportsPro', 'https://i.ytimg.com/vi/QIwA0TG5Oho/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&amp;rs=AOn4CLCa-6F6xJBLo_hyyDgiUhswSZ2GJw', 'https://www.youtube.com/watch?v=QIwA0TG5Oho'], ['What Happens After 30 Days of Cold Showers', 'Gravity Transformation - Fat Loss Experts', 'https://i.ytimg.com/vi/nOuzSOnfyv0/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&amp;rs=AOn4CLDSJ2N96Kycf79EswUBvuuZi8DStA', 'https://www.youtube.com/watch?v=nOuzSOnfyv0'], ['Teenagers Trapped Inside A Cave For 1000 Years, But They Still Never Aged', 'Scifi Recapped', 'https://i.ytimg.com/vi/26eD2jw7sSk/hqdefault.jpg?sqp=-oaymwEcCOADEI4CSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&amp;rs=AOn4CLCR1aTSS-rueiwUh7JTWOigwQVqnw', 'https://www.youtube.com/watch?v=26eD2jw7sSk'], ['Snoop Dogg Realizes He Left His Stream Live for 8 hours+', "ghecco's twitch clips", 'https://i.ytimg.com/vi/TAOM449H6Y8/hqdefault.jpg?sqp=-oaymwEcCOADEI4CSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&amp;rs=AOn4CLBmKARVe3c82tet3dfRURDJZ-uCxA', 'https://www.youtube.com/watch?v=TAOM449H6Y8'], ['Facebook Is Dead', 'penguinz0', 'https://i.ytimg.com/vi/fdMil7y4Vk4/hqdefault.jpg?sqp=-oaymwEcCOADEI4CSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&amp;rs=AOn4CLA8l2DGHNGDrWUdm6dqj2ZLP6UnTA', 'https://www.youtube.com/watch?v=fdMil7y4Vk4'], ['What Does it Actually Feel Like to be Shot', 'The Infographics Show', 'https://i.ytimg.com/vi/BmwVxj6E2KE/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&amp;rs=AOn4CLA-Z8U7oHyeQy7zGS1Nh9wv0Ov6Zg', 'https://www.youtube.com/watch?v=BmwVxj6E2KE'], ['Conservative Covid-19 survivor is now getting vaccinated but losing friends', 'CNN', 'https://i.ytimg.com/vi/X1DL53cVJd0/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&amp;rs=AOn4CLAsqm9i1DCcTiFyvee8JyI4hyhwWA', 'https://www.youtube.com/watch?v=X1DL53cVJd0'], ['Companies face religious exemption requests for COVID-19 vaccine', 'CBS News', 'https://i.ytimg.com/vi/qwY24i9Z1XE/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&amp;rs=AOn4CLA-CccOgrpo0O0pd-68lxzsSt6Ohg', 'https://www.youtube.com/watch?v=qwY24i9Z1XE'], ['Reacting to Aaron Rodgers opening up on positive COVID-19 test and vaccination status | This Just In', 'ESPN', 'https://i.ytimg.com/vi/QADmWcbEytI/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&amp;rs=AOn4CLCnaY4okf3h5yIp76nGLP22gmDciA', 'https://www.youtube.com/watch?v=QADmWcbEytI'], ['Businesses have until after the holidays to implement Biden Covid vaccine mandate', 'CNBC Television', 'https://i.ytimg.com/vi/-sd-gZz04F8/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&amp;rs=AOn4CLDkIcAGH4ww0vRygTTIw8tDzB-cWg', 'https://www.youtube.com/watch?v=-sd-gZz04F8']]

    # thumbnails need to be loaded in appStarted
    app.thumbnails = []
    for i in range(6):
        thumbnail = app.youtube[i][2]
        app.thumbnails.append(thumbnail)
    app.images_temp = [app.loadImage(thumbnail) for thumbnail in app.thumbnails]
    app.images = [app.scaleImage(image, 0.1771) for image in app.images_temp]


# initially used for testing / debugging
# def keyPressed(app, event):
#     print(app.reddit)
# useless for now


# animation too slow because CMU graphics limited to 10 fps
# def timerFired(app):
#     if app.animateColors[0] != ['white']:
#         if app.r1 <= 30:
#             app.r1 += 5
#     else:
#         app.r1 = 1


def mouseMoved(app, event):
    # custom cursor
    # app.cursor_x = event.x
    # app.cursor_y = event.y

    # reddit header animation
    middle = app.width/4
    height = 30
    if middle-50 <= event.x <= middle+50 and height-20 <= event.y <= height+20:
        app.animateColors[0] = ['#BFBFBF']
        app.r1 = 27
        app.headerColors[0] = 'black'
    else:
        app.animateColors[0] = ['white']
        app.r1 = 1
        app.headerColors[0] = '#6C7A89'

    # twitter header animation
    middle2 = app.width/4 * 3
    height2 = 30
    if middle2-50 <= event.x <= middle2+50 and height2-20 <= event.y <= height2+20:
        app.animateColors[1] = ['#003171']
        app.r2 = 27
        app.headerColors[1] = 'white'
    else:
        app.animateColors[1] = ['white']
        app.r2 = 1
        app.headerColors[1] = '#22A7F0'

    # youtube header animation
    middle3 = app.width/4
    height3 = app.height/2 + 30
    if middle3-50 <= event.x <= middle3+50 and height3-20 <= event.y <= height3+20:
        app.animateColors[2] = ['#CF000F']
        app.r3 = 27
        app.headerColors[2] = 'white'
    else:
        app.animateColors[2] = ['white']
        app.r3 = 1
        app.headerColors[2] = '#E68364'

    # youtube header animation
    middle4 = app.width/4 * 3
    height4 = app.height/2 + 30
    if middle4-50 <= event.x <= middle4+50 and height4-20 <= event.y <= height4+20:
        app.animateColors[3] = ['#FBCACA']
        app.r4 = 27
        app.headerColors[3] = 'black'
    else:
        app.animateColors[3] = ['white']
        app.r4 = 1
        app.headerColors[3] = '#D24D57'

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

    # youtube colors
    if 30 <= event.x <= 256.67 and 508 <= event.y <= 685.5:  # 1
        app.youtubeColors[0] = '#CF000F'
        app.youtubeTextColors[0] = 'white'
    else:
        app.youtubeColors[0] = '#E68364'
        app.youtubeTextColors[0] = 'black'
    if 286.67 <= event.x <= 513.34 and 508 <= event.y <= 685.5:  # 2
        app.youtubeColors[1] = '#CF000F'
        app.youtubeTextColors[1] = 'white'
    else:
        app.youtubeColors[1] = '#E68364'
        app.youtubeTextColors[1] = 'black'
    if 543.34 <= event.x <= 770 and 508 <= event.y <= 685.5:  # 3
        app.youtubeColors[2] = '#CF000F'
        app.youtubeTextColors[2] = 'white'
    else:
        app.youtubeColors[2] = '#E68364'
        app.youtubeTextColors[2] = 'black'
    if 30 <= event.x <= 256.67 and 703 <= event.y <= 880.5:  # 4
        app.youtubeColors[3] = '#CF000F'
        app.youtubeTextColors[3] = 'white'
    else:
        app.youtubeColors[3] = '#E68364'
        app.youtubeTextColors[3] = 'black'
    if 286.67 <= event.x <= 513.34 and 703 <= event.y <= 880.5:  # 5
        app.youtubeColors[4] = '#CF000F'
        app.youtubeTextColors[4] = 'white'
    else:
        app.youtubeColors[4] = '#E68364'
        app.youtubeTextColors[4] = 'black'
    if 543.34 <= event.x <= 770 and 703 <= event.y <= 880.5:  # 6
        app.youtubeColors[5] = '#CF000F'
        app.youtubeTextColors[5] = 'white'
    else:
        app.youtubeColors[5] = '#E68364'
        app.youtubeTextColors[5] = 'black'


def redrawAll(app, canvas):
    vertical_divide = app.width / 2
    horizontal_divide = app.height / 2
    # 4-section dividers
    canvas.create_line(vertical_divide, 0, vertical_divide, app.height, width=2)
    canvas.create_line(0, horizontal_divide, app.width, horizontal_divide, width=2)
    # animated circles
    canvas.create_oval(vertical_divide / 2 - 2 * app.r1, 30 - app.r1, vertical_divide / 2 + 2 * app.r1,
                       30 + app.r1, width=0, fill=app.animateColors[0])
    canvas.create_oval(vertical_divide / 2 * 3 - 2 * app.r2, 30 - app.r2, vertical_divide / 2 * 3 + 2 * app.r2,
                       30 + app.r2, width=0, fill=app.animateColors[1])
    extra_margin = 15
    canvas.create_oval(vertical_divide / 2 - 2 * app.r3 - extra_margin, horizontal_divide + 30 - app.r3,
                       vertical_divide / 2 + 2 * app.r3 + extra_margin, horizontal_divide + 30 + app.r3, width=0,
                       fill=app.animateColors[2])
    extra_margin2 = 27
    canvas.create_oval(vertical_divide / 2 * 3 - 2 * app.r4 - extra_margin2, horizontal_divide + 30 - app.r4,
                       vertical_divide / 2 * 3 + 2 * app.r4 + extra_margin2,
                       horizontal_divide + 30 + app.r4, width=0, fill=app.animateColors[3])
    # section headers
    canvas.create_text(vertical_divide / 2, 30, text='Reddit', font=('Bold', '30'),
                       fill=app.headerColors[0])
    canvas.create_text(vertical_divide / 2 * 3, 30, text='Twitter', font=('Bold', '30'),
                       fill=app.headerColors[1])
    canvas.create_text(vertical_divide / 2, horizontal_divide+30, text='YouTube', font=('Bold', '30'),
                       fill=app.headerColors[2])
    canvas.create_text(vertical_divide / 2 * 3, horizontal_divide+30, text='Instagram', font=('Bold', '30'),
                       fill=app.headerColors[3])
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
        # 3 twitter sections text creation
        canvas.create_text(845, reddit_text_locations[i], text=name, font='15', anchor=tkinter.W,
                           fill=app.twitterTextColors[i])
        canvas.create_text(800 + twitter_lengths[0] + 15, reddit_text_locations[i], text=handle, font='15',
                           anchor=tkinter.W, fill=app.twitterTextColors[i])
        canvas.create_text(800 + twitter_lengths[1] + 15, reddit_text_locations[i], text=tweet, font='15',
                           anchor=tkinter.W, fill=app.twitterTextColors[i])

    # youtube
    vidnames = []
    for i in range(6):
        vidname = app.youtube[i][0]
        max_vidname = 32
        if vidname.isupper():
            vidname = vidname[:max_vidname-7].rstrip() + '...'
        elif len(vidname) > max_vidname:
            vidname = vidname[:max_vidname-3].rstrip() + '...'
        vidnames.append(app.youtube[i][0])
        creator = '(' + app.youtube[i][1] + ')'
        thumbnail = app.youtube[i][2]
        link = app.youtube[i][3]

        # testing youtube box sizes
        youtube_width = 226.67
        youtube_height = 127.55
        margin = 5
        shift = 7
        temp_x = [30, 30+youtube_width+30, 30+2*(youtube_width+30)]

        i = i % 3
        # first row
        x = temp_x[i]
        canvas.create_rectangle(x, horizontal_divide+65-shift, x+youtube_width,
                                horizontal_divide+65+youtube_height-shift,
                                fill='grey', width=0)
        canvas.create_image(x, horizontal_divide+65-shift, image=ImageTk.PhotoImage(app.images[i]),
                            anchor=tkinter.NW)
        # vidname title text
        canvas.create_rectangle(x, horizontal_divide+192.5+margin-shift, x+youtube_width,
                                horizontal_divide+192.5+margin+45-shift,
                                fill=app.youtubeColors[i], width=0)  # 192.5 = 65 + 127.5
        canvas.create_text(x+10, (horizontal_divide+192.5+margin-shift)+13,
                           text=vidname, font='5', fill=app.youtubeTextColors[i], anchor=tkinter.W)
        canvas.create_text(x+10, (horizontal_divide+192.5+margin-shift)+32,
                           text=creator, font='5', fill=app.youtubeTextColors[i], anchor=tkinter.W)
        # second row
        canvas.create_rectangle(x, horizontal_divide+260-shift, x+youtube_width,
                                horizontal_divide+260+youtube_height-shift,
                                fill='grey', width=0)
        canvas.create_image(x, horizontal_divide+260-shift, image=ImageTk.PhotoImage(app.images[i+3]),
                            anchor=tkinter.NW)
        canvas.create_rectangle(x, horizontal_divide+387.5+margin-shift, x+youtube_width,
                                horizontal_divide+387.5+margin+45-shift,
                                fill=app.youtubeColors[i+3], width=0)  # 260 + 127.5 = 387.5
        canvas.create_text(x+10, (horizontal_divide+387.5+margin-shift)+13,
                           text=vidname, font='5', fill=app.youtubeTextColors[i+3], anchor=tkinter.W)
        canvas.create_text(x+10, (horizontal_divide+387.5+margin-shift)+32,
                           text=creator, font='5', fill=app.youtubeTextColors[i+3], anchor=tkinter.W)

    # custom cursor
    # canvas.create_oval(app.cursor_x-app.cursor_radius, app.cursor_y-app.cursor_radius,
    #                    app.cursor_x+app.cursor_radius, app.cursor_y+app.cursor_radius, fill=app.cursor_fill,
    #                    width=0)

runApp(width=1600, height=900)
