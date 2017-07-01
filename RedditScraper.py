
# VERSION 1.1
# Improvements include: takes a list of subreddits and goes through them all
# Includes calls to gyfcatdl.py - DONE
#Copyright Simon Augustus - augustus.writer@gmail.com


from bs4 import BeautifulSoup
import praw
from urllib2 import urlopen
import urllib2
import sys
from urlparse import urljoin
import config
import imgurdl
import requests
import subprocess
from gfycat import gfycat
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cache = []
soup = BeautifulSoup

def reddit_login():
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "Test URL scraper for Reddit v0.3"
                )
    print("***********logged in successfully***********")
    return r

def get_category_links(subredditName, r):
    print("Grabbing subreddit...")
    submissions = r.subreddit(subredditName).hot(limit=50)
    print("Grabbing links")
    count = 0
    for submission in submissions:
        info = {
        #'author_name': submission.author.name,
        'created_time': submission.created_utc,
        'reddit_id': submission.id,
        'title': submission.title,
        'submitted_url': submission.url,
        'domain': submission.domain,
        'imgur': None
        }
        call1 = "python imgurdl.py -i "
        call11 = "python imgurdl.py -a "
        call2 = info['submitted_url']
        call3 = " " 
        call4 = "-o "
        call5 = "'/Volumes/portable/'"
    #parse imgur ids to catch direct links 
        if "http://i.imgur.com" in submission.url:
            this_url = submission.url[19:]
            imgur_id = this_url[:-4]
            info['imgur'] = imgur_id
            print("Downloading", info['submitted_url'])
            link = info['submitted_url'].split('/')
            print(link)
            identitiy = link[3].split('.')
            id = identitiy[0]
            print(id, " is the ID")
            exitcode = subprocess.call(call1 + id + call3 + call4 + call5, shell=True)
            count+= 1
        if "http://imgur.com/" in submission.url:
            if "/a/" in submission.url:             #Something around calling gallaries 
                imgur_id = submission.url[19:]
                info['imgur'] = imgur_id
                print("Downloading", info['submitted_url'])
                link = info['submitted_url'].split('/')
                print(link)
                identitiy = link[4].split('.')
                id = identitiy[0]
                print(id, " is the ID")
                exitcode = subprocess.call(call11 + id + call3 + call4 + call5, shell=True)
                count+= 1
            elif "/a/" in submission.url:
                imgur_id = submission.url[24:]
                print(info['submitted_url'])
                link = info['submitted_url'].split('/')
                print(link)
                identitiy = link[4].split('.')
                id = identitiy[0]
                print(id, " is the ID")
                exitcode = subprocess.call(call11 + id + call3 + call4 + call5, shell=True)
                count+= 1
            elif "http://i.imgur.com/gifv" in submission.url:
                this_url = submission.url[19:]
                imgur_id = this_url[:-4]
                info['imgur'] = imgur_id
                print("Downloading", info['submitted_url'])
                link = info['submitted_url'].split('/')
                print(link)
                identitiy = link[3].split('.')
                id = identitiy[0]
                print(id, " is the ID")
                exitcode = subprocess.call(call1 + id + call3 + call4 + call5, shell=True)
                print(identitiy, "--------------------------------------------------------------")
            else:
                imgur_id = submission.url[17:]
                info['imgur'] = imgur_id
                print("Downloading", info['submitted_url'])
                link = info['submitted_url'].split('/')
                print(link)
                identitiy = link[3].split('.')
                id = identitiy[0]
                print(id, " is the ID")
                exitcode = subprocess.call(call1 + id + call3 + call4 + call5, shell=True)
                count+= 1
        if "https://gfycat.com/" in submission.url: 
                print("Downloading ", info['submitted_url'])      
                downloadMe = gfycat().upload(info['submitted_url'])
                downloadMe.download("/Volumes/portable/")
    print("Found", count, "links")

def gfycatdl(subredditName, r):
    print("Grabbing subreddit for GFYCAT LINKS...")
    submissions = r.subreddit(subredditName).hot(limit=1000)
    print("Grabbing links")
    for submission in submissions:
        info = {
        #'author_name': submission.author.name,
        'created_time': submission.created_utc,
        'reddit_id': submission.id,
        'title': submission.title,
        'submitted_url': submission.url,
        'domain': submission.domain,
        'imgur': None
        }
        if "https://gfycat.com/" in submission.url: 
            print(info['submitted_url'])      
            downloadMe = gfycat().upload(info['submitted_url'])
            downloadMe.download("/Volumes/portable/")        

                
    
    
    
cprint(figlet_format('REDDIT IMGUR & GFYCAT SCRAPER Version 1.1', font='starwars'),
       'white', attrs=['bold'])
r = reddit_login()
get_category_links(sys.argv[1], r) 
