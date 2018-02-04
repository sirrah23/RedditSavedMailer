import requests

class Client:

    def __init__(self, username, password, clientid, clientsecret, appname):
        self.token = self.generateToken(username, password, clientid, clientsecret, appname)
        if not self.token:
            raise ValueError("Bad credentials, unable to retrieve token")

    def generateToken(self, username, password, clientid, clientsecret, appname):
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
