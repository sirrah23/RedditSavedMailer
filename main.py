import os, configparser
from client import Client

# Read the configuration file containing credentials
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "config.ini"))
redditConfig = config["Reddit"]

# Unpack the credentials
username = redditConfig["username"]
password = redditConfig["password"]
clientid = redditConfig["clientid"]
clientsecret = redditConfig["clientsecret"]
appname = redditConfig["appname"]

# Create a Reddit oauth client that can access the API
client = Client(username, password, clientid, clientsecret, appname)
print(client.getSavedPosts())
