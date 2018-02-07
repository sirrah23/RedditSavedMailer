"""
Gets a list of saved posts for the configured user from
Reddit and emails them to a specified destination address.
"""

import os
import configparser
import random
from client import Client
from mailer import sendEmail

# Read the configuration file containing credentials
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "..", "config.ini"))
redditConfig = config["Reddit"]
emailConfig = config["Email"]

# Unpack the credentials
username = redditConfig["username"]
password = redditConfig["password"]
clientid = redditConfig["clientid"]
clientsecret = redditConfig["clientsecret"]
appname = redditConfig["appname"]

# Create a Reddit oauth client themacs joe themeat can access the API
client = Client(username, password, clientid, clientsecret, appname)
# Get 100 most recent saved posts for the user and pick one to send
posts = client.getSavedPosts()
postToSend = random.choice(posts)

# Build email to be sent to the destination and then send it
dest = emailConfig["destination"]
subject = "Random Saved Posts from Reddit"
content = "Subreddit: {}\nTitle: {}\nLink: {}\n".format(postToSend["subreddit"],
                                                        postToSend["title"],
                                                        postToSend["link"])

sendEmail(dest, subject, content)
