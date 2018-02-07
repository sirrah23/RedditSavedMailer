"""
Contains a Client object that interfaces with Reddit
via a set of user & app credentials.
"""
import requests

class Client:

    def __init__(self, username, password, clientid, clientsecret, appname):
        self.username = username
        self.appname = appname
        self.token = self.generateToken(username, password, clientid, clientsecret, appname)
        if not self.token:
            raise ValueError("Bad credentials, unable to retrieve token")

    def generateToken(self, username, password, clientid, clientsecret, appname):
        """
        Obtain an authorization token from Reddit given a set of credentials
        for a user and their app.
        """
        client_auth = requests.auth.HTTPBasicAuth(clientid, clientsecret)
        post_data = {"grant_type": "password", "username": username, "password": password}
        headers = {"User-Agent": "{} by {}".format(appname, username)}
        response = requests.post("https://www.reddit.com/api/v1/access_token",
                                 auth=client_auth,
                                 data=post_data,
                                 headers=headers)
        if "access_token" not in response.json():
            return None
        else:
            return response.json()["access_token"]

    def getSavedPosts(self):
        """
        Get a list of 100 saved posts using the token that
        was obtained from Reddit.
        """
        headers = {"Authorization": "bearer {}".format(self.token),
                   "User-Agent": "{} by {}".format(self.appname, self.username)}
        response = requests.get("https://oauth.reddit.com/user/{}/saved?limit=100".format(self.username),
                                headers=headers)
        def extractJSONData(j):
            """
            Inner function to extract data from each saved-posts JSON blob. We want
            to extract only the data that we care about for each item:
            - Links
            - Titles
            - Subreddits
            """
            j = j["data"]
            title_field = "title" if "title" in j else "link_title"
            permalink_field = "permalink"
            subreddit_field = "subreddit"
            return {"title": j[title_field],
                    "link": "www.reddit.com{}".format(j[permalink_field]),
                    "subreddit": j[subreddit_field]}

        return list(map(extractJSONData, response.json()["data"]["children"]))
