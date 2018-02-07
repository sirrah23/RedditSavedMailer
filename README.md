# Introduction
Welcome to the **Reddit Saved Mailer**. This application
will allow you to email a random post that you've saved
on Reddit to a specified email address.

# Setup
Create a new app in your Reddit account preferences
and obtain the client id and client secret.

Once you have cloned the repository you need to create
a `config.ini` file in the root directory of the project
with the following content:

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
Make sure you have pipenv installed on your system Then you
can do:

```python
pipenv run python main.py
```
