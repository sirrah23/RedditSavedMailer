# Introduction
Welcome to the **Reddit Saved Mailer**. This application
will allow you to email a random post that you've saved
on Reddit to a specified email address.

This is a way to rediscover things that you saved a long time ago
and haven't had a chance to revisit since.

# Setup
Create a new app in your Reddit account preferences
and obtain the client id and client secret.

Once you have cloned the repository you need to create
a `config.ini` file at the root of the project
containing the following content:

```ini
[Reddit]
username = <reddit username>
password = <reddit password>
clientid = <Reddit app id>
clientsecret = <Reddit app secret>

[Email]
destination = <email to send post to>
```

# Running the script
Install pipenv onto your system. Once you do that you can run:

```python
pipenv run python src/main.py
```
