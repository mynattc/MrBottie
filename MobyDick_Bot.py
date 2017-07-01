#import required libraries
import os, markovchain

#initialize Bottie
bottie= markovchain()

# Get the current directory's path
dirname = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the book
book = os.path.join(dirname, 'mobydick.txt')

# Make your bot read the book!
bottie.read(book)

#----------------------------------------------

# Consumer Key (API Key)
cons_key = ''

# Consumer Secret (API Secret)
cons_secret = ''

# Access Token
access_token = ''

# Access Token Secret
access_token_secret = ''

# Log in to Twitter
tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

#----------------------------------------------
"""
# See if Bottie is outputting text
my_first_text = bottie.generate_text(25, seedword=['whale', 'ship'])
print("MrBottie says:")
print(my_first_text)
"""

# Start periodically tweeting...(forever for now)
while true:
	bottie.twitter_tweeting_start(days=0, hours=6, minutes=0, keywords=None, prefix=None, suffix='#MrBottie')

# Call to stop tweeting for later use
bottie.twitter_tweeting_stop()
