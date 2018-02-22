import constants
import oauth2
import urllib.parse as urlparse
import json
from user import User
from database import Database

consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)

Database.initialise(user='postgres', password='**********', host='localhost', database='learning')

user_email = input("Enter email address ")

user = User.load_from_db_by_email(user_email)

if not user:


# create a consumer, which uses consumer_key and consumer_secret to identify the app
    client = oauth2.Client(consumer)

# use the client to perform a request for the request token
    response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
    if response.status != 200:
     print("an error occurred getting the request token from Twitter")

# get request token parsing the query string returned
    request_token = dict(urlparse.parse_qsl(content.decode('utf-8')))

# ask the user to authorize out app and give us the pin code
    print("Go to the following site in your browser:")
    print("{}?oauth_token={}".format(constants.AUTHORIZATION_URL, request_token['oauth_token']))

    oauth_verifier = input("What is the PIN? ")

# create a token object which contains the request token, and the verifier
    token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
    token.set_verifier(oauth_verifier)

# create a client with consumer and the newly created (and verified) token
    client = oauth2.Client(consumer, token)

# ask twitter for an access token,
# twitter knows it should give us it because we've verified the request token
    response, content = client.request(constants.ACCESS_TOKEN_UTL, 'POST')
    access_token = dict(urlparse.parse_qsl(content.decode('utf-8')))

    print(access_token)

    # email = input("Enter your email: ")
    first_name = input("Enter your first name ")
    last_name = input("Enter your last name ")
    user = User(user_email, first_name, last_name, access_token['oauth_token'], access_token['oauth_token_secret'], None)
    user.save_to_db()



# create and 'authentised_token'
# token object and use that to perform twitter API calls on behalf of the user
authorized_token = oauth2.Token(user.oauth_token, user.oauth_token_secret)
authorized_client = oauth2.Client(consumer, authorized_token)

# make Twitter API call
response, content = authorized_client.request('https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images', 'GET')
if response.status != 200:
    print("Error while searching")

tweets = json.loads(content.decode('utf-8'))

for tweet in tweets['statuses']:
    print(tweet['text'])