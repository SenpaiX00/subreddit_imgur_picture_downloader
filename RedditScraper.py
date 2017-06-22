# Copyright (C) Simon Augustus - All Rights Reserved
 # Unauthorized copying of this file, via any medium is strictly prohibited
 # Proprietary and confidential
 # Written by Simon Augustus <augustus.writer@gmail.com>, July 2017
 
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
	submissions = r.subreddit(subredditName).hot(limit=1000)
	print("Grabbing comments...")
	count = 0

	#comments = subred.comments(limit = 200)
	for submission in submissions:
		#htmlSource = requests.get(submission.url).text
        #print (htmlSource)
		info = {
		#'author_name': submission.author.name,
		'created_time': submission.created_utc,
		'reddit_id': submission.id,
		'title': submission.title,
		'submitted_url': submission.url,
		'domain': submission.domain,
		'imgur': None
		}
		call1 = "python imgurdl.py -i="
		call11 = "python imgurdl.py -a="
		call2 = info['submitted_url']
		call3 = " " 
		call4 = "-o "
		call5 = "'DIRECTORY GOES HERE'" #Should reald like /Volumes/ExternalHDD/
	#parse imgur ids to catch direct links 
		if "http://i.imgur.com" in submission.url:
			this_url = submission.url[19:]
			imgur_id = this_url[:-4]
			info['imgur'] = imgur_id
			print(info['submitted_url'])
			print("downloading now")
			

			exitcode = subprocess.call(call1 + call2 + call3 + call4 + call5, shell=True)
			count+= 1
		if "http://imgur.com/" in submission.url:
			if "/a/" in submission.url:
				imgur_id = submission.url[19:]
				info['imgur'] = imgur_id
				print(info['submitted_url'])
				print("downloading now")
				exitcode = subprocess.call(call1 + call2 + call3 + call4 + call5, shell=True)
				count+= 1
			elif "/gallery/" in submission.url:
				imgur_id = submission.url[24:]
				print(info['submitted_url'])
				count+= 1
			elif "http://i.imgur.com/gifv" in submission.url:
				this_url = submission.url[19:]
				imgur_id = this_url[:-4]
				info['imgur'] = imgur_id
				print(info['submitted_url'])
				print("downloading now")
			else:
				imgur_id = submission.url[17:]
				info['imgur'] = imgur_id
				print(info['submitted_url'])
				print("downloading now")
				exitcode = subprocess.call(call1 + call2 + call3 + call4 + call5, shell=True)
				count+= 1
		
			

				exitcode = subprocess.call(call1 + call2 + call3 + call4 + call5, shell=True)
				count+= 1
	print("Found", count, "links")
	
	

r = reddit_login()
get_category_links(sys.argv[1], r) 

