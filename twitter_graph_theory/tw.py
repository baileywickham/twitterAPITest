import twitter

CONSUMER_KEY = 'tya10QXDwZgeGZ9ceLspavrgh'
CONSUMER_SECRET = 'GeIq5l1zfo1VU0e4qDKahE2BC7yWp10MbB1KuOmnKR8MNxcFzT'
ACCESS_TOKEN = '1146829205520314368-HWPswIPSYWAb8QqpGsEPJEVsH2GIrX'
ACCESS_TOKEN_SECRET = '7nMoWmIBuo3SLJxmR8GD6IOkMtcUYCcsLI79A9nteKDoz'

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)


def main():
    f = api.GetFriends(screen_name='Bencox04')
    map(pp, [f for f in f])


def pp(friend):
    print('usr: ', friend.name, friend.screen_name)


main()
users = api.GetUser(screen_name='Bencox04')
