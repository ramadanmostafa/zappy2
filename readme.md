Task Overview
FictionFone is a multinational telecommunication company, with head quarters in Egypt. It predominates the middle east region with a customer base of 250 million subscribers.
Recently, FictionFone corporation purchased a social media analytics tool that performs sentiment analysis on the posts and tweets of subscribers from Twitter and Facebook account. The analytics tool is great, but requires the tweets/posts to be fed manually, which is frustrating to the marketing team.
The technical team has taken the ownership to develop a tool to solve this problem. Keeping in mind, the marketing team are non-technical users, and they use Slack heavily for internal communication, they came up with the following plan.
Zappy Zappy is the name of the tool that you’re required to develop. Zappy integrates with a Slack channel and listens on specific messages. For simplicity, we the tool will listen on all messages containing the word “go”. As soon as any member of the marketing team, places a messages on a channel containing the message “go”, the tool fetches twitter feeds from the FictionFone account and saves in a mongo collection. Lastly, for our demo purpose, you will create a view that fetches tweets from mongoDB and shows in a table. Diagram below visualizes the process.


to make the projects available for slack api (slack is configured to send the messages to http://zappy.serveo.net/slack/messages/)
ssh -R zappy:80:localhost:8000 serveo.net

to run celery
celery --app=zappy.celery:app worker --loglevel=INFO --pool=eventlet

to run all the test cases:
python manage.py test --settings=zappy.test_settings

to run the project you will need to install all packages listed in the requirements.txt
-pip install -r requirements.txt

have the server up and running:
-python manage.py runserver 8000

have redis and celery running


don't forget to update zappy.settings.py, zappy.test_settings.py file with the attached slack and twitter keys
