# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = tcf.438
insta_password = Sevilla1+

comments = ['Nice shot! @{}',
        'I love your profile! @{tcf.438}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{tcf.428}?',
        'Love your posts @{tcf.438}',
        'Looks awesome @{tcf.438}',
        'Getting inspired by you @{tcf.438}',
        ':raised_hands: Yes!',
        'I can feel your passion @{tcf.438} :muscle:']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=tcf. 438,
                  password=Sevilla1+,
                  headless_browser=False)

with smart_run(session):
  """ Activity flow """		
  # general settings		
  session.set_dont_include(["hippo_max", "friend2", "friend3"])		
  
  # activity		
  session.like_by_tags(["natgeo"], amount=30)

  # Joining Engagement Pods
  session.set_do_comment(enabled=True, percentage=30)
  session.set_comments(comments)
  session.join_pods(topic='sports', engagement_mode='no_comments')
