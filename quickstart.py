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

like_tag_list = ['massagegun', 'sport', 'athele', 'fitness']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4600,
                                    min_followers=50,
                                    min_following=50)

    session.set_user_interact(amount=2, randomize=True, percentage=60)
    # activity
    # like les post dans les hastage sont contenu dans le tableau
    session.like_by_tags(like_tag_list, amount=10)

    # Joining Engagement Pods
    session.set_do_comment(enabled=True, percentage=35)
    session.set_comments(comments, media='Photo')
    session.join_pods(topic='sports', engagement_mode='normal')
