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

# The target string is what the bot will reply to on Twitter. 
targetstring = 'MobyDickAhoy!'
"""Keywords are words the bot will look for in tweets it'll reply to, and it
will attempt to use them as seeds for the reply"""
keywords = ['whale', 'Moby Dick', 'ship', 'harpoon', 'water']
# This is added to the end of any outgoing tweet.
suffix = '#MrBottie'

# Limits the number of replies allowed by the bot. Default of 2.
maxconvdepth = 2
# Trigger autoreply
tweetbot.twitter_autoreply_start(targetstring, keywords=keywords, prefix=prefix, suffix=suffix, maxconvdepth=maxconvdepth)

# Start periodically tweeting...(forever for now)
while true:
	bottie.twitter_tweeting_start(days=0, hours=6, minutes=0, keywords=None, prefix=None, suffix='#MrBottie')

# Call to stop tweeting for later use
bottie.twitter_tweeting_stop()
