# Reportbot
This is a short bot I made to help me report rule breaking posts on Reddit. The official Reddit app for iOS doesn't allow for custom report messages, which are necessary for some reports.
### Requirements
Reportbot is written in Python 3. It uses [PRAW](https://praw.readthedocs.io/en/latest/) to interact with reddit.com.
### Details
There are two important files that make up Reportbot: config.py and reportbot.py. 

- config.py: contains the configuration variables that need to be set by the user, including, but not limited to, Reddit username and password, what subreddits to monitor, and phrases the bot will look for and use in report messages.

- reportbot.py is the contains the actual functions and main program used by the bot.

To run the bot, you just have to make sure config.py is filled out and then run the main program in reportbot.py (and make sure you have PRAW installed).

I made this bot for reporting reposts (since doing so often requires providing a link to the original post). Because of that, the regex used by the bot checks reddit comments for markdown format links. The url in the link is assumed to be the original post and therefore included in the report message. If this bot is used for reporting anything other than reposts, the regex and method of building the report message in reportbot.py would need to be modified.
