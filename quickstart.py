# imports
import os
from os.path import join, dirname
from dotenv import load_dotenv
from instapy import InstaPy
from instapy import smart_run

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


# env

user = os.environ.get("INSTA_USERNAME")
mdp = os.environ.get("INSTA_PASSWORD")
print(mdp)
# login credentials
insta_username = user
insta_password = mdp

comments = ['Nice shot! @{}',
            'I love your profile! @{}',
            'Your feed is an inspiration :thumbsup:',
            'Just incredible :open_mouth:',
            'Love your posts @{}',
            'Looks awesome @{}',
            'Getting inspired by you @{}',
            ':raised_hands: Yes!',
            'I can feel your passion @{} :muscle:']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    Activity flow
    # general settings
    session.set_dont_include(["friend1", "friend2", "friend3"])

    # activity
    session.like_by_tags(["natgeo"], amount=10)

    # Joining Engagement Pods
    session.set_do_comment(enabled=True, percentage=35)
    session.set_comments(comments)
    session.join_pods(topic='sports', engagement_mode='no_comments')
