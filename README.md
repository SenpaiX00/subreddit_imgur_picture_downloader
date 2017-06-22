# subreddit_imgur_picture_downloader
Package that takes a subreddit name as an argument and takes all the hot posts, finds imgur links, and downloads them to a specified folder

SET UP & INITIAL CONSIDERATIONS BEFORE RUNNING 
1. This is written for Python 2, not 3. I have not checked it in Python 3, but given backwards compatibility issues between 2 and 3, I doubt it will work in 3. I plan to test it and update the code for Python 3 in the near future.
2. you will need to to a pip install praw - currently there are some imported packages that are not required. But praw is a must, also urllib2 if you don't already have it.
3. You will need to go to line 49 of the RedditScraper.py file and changethe variable call5 to reflect your desired download location. In the next version this will not be required.
4. You will also need to set up a config file with your Reddit API access credentials. A good tutorial for this is here: https://www.youtube.com/watch?v=krTUf7BpTc0 and I have included an example config where you can fill in the blanks.

That's about it for set up. 

RUNNING
This script is intended to run off of the bash shell only and will not work in windows command prompt. I have only tested it in OSX so far, but there shoul dbe no issues running it on other unix based systems.
The basic commpand is:

  python RedditScraper.py <ENTER NAME OF SUBREDDIT>
  
for example:

  python RedditScraper.py Art
  
ACKNOWLEDGEMENTS
About half the code for this came from leonardicus' imgurdl. His command line python code for straight imgur downloads was highly significant to the creation of this code. I have added additional functionality to it.
If you are interested in using just an Imgur download command line interface, then please see leonardicus' Imgurdl script here: https://github.com/leonardicus/imgurdl/blob/master/readme.md

FUTURE ADDITIONS
1. Test this code in Python 3 and update as necessary to produce a Python 3 version
2. In version 1.2 I will remove unesed imports
3. In version 1.2 I will allow users to pass in a specific download location on the command line, for now this must be hard coded into the core package file
4. I will be producing a version compatible for Windows users
5. I will be adding in gfycat functionality in the near future so users can download gyfcat videos from subreddits too 
