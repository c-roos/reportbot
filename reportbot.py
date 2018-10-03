import re, praw, config

# Configuration variables, stored in config.py
usr = config.username
psw = config.password
cid = config.client_ID
scrt = config.client_secret
agnt = config.user_agent
subs = config.subreddits
target = config.target_phrase
msg = config.report_message
subjct = config.pm_subject

# This bot was built with the intention of reporting reposts on Reddit.
# This means it needs to pull a link to the original post out of the comment calling it
# to include in the report message. This regex is used to do just that.
regex = r"\[" + re.escape(target) + "\]\((.*)\)"

# I didn't put the pm template in the config file since format() is called on it.
# If the pm template is changed, the format() call probably needs to be changed as well
PM_TEMPLATE = 'I reported u/{} for you. \n\nReport text: "{}"'

def handle_comment(comment):
    
    # Use regex to see if comment contains phrase to call the bot
    matches = re.findall(regex, comment.body, re.MULTILINE)
    
    # If not, move on
    if len(matches) == 0:
        return
    
    # Otherwise, get the post the comment is on
    post = comment.submission
    
    # Make sure post isn't already deleted
    if post.author is None:
        return
    
    # The report text is built from the report message phrase in the config file and the link
    # pulled from the comment by the regex.
    # The private message is built from the PM template, the report text, and the post author's name.
    report_text = msg + matches[0]
    pm_text = PM_TEMPLATE.format(post.author.name, report_text)
    
	# Print to console because why not.
    print(pm_text)
    
    # The post is reported and a PM sent to the caller.
    post.report(report_text)
    comment.author.message(subjct, pm_text)
    
# Main function
def main():

    # Obtain a reddit instance
    reddit = praw.Reddit(client_id=cid, client_secret=scrt, user_agent=agnt, username=usr, password=psw)

    # Obtain subreddits
    subreddits = reddit.subreddit(subs)

    # Get comment stream
    comments = subreddits.stream.comments()

    # Handle each comment
    for comment in comments:
        handle_comment(comment)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stopping bot')
        exit()
    except:
        # Error messages are ugly so if something goes wrong, just mysteriously exit.
        # There is surely nothing wrong with this approach.
        print('Bot encountered an error. Shutting down')
        exit()