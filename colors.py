import twitter
api = twitter.Api(conuser_key='KCpd1MjS4AKTh2vS0poWq9Plp',
        consumer_secret='EJYRMJRg1tGDvemYJsf1ou9jgcvEP8zRVnL66VJisRn0yBldf3',
        access_token_key='2751102888-8HKrPfo6zfBc4vwhD0qGRzl0O1XnE8HhkL2cWuM',
        access_token_secrret='F7Vw2Qf40DUpmfUqlbc5Wtrv5ZQJtNBB7mRcDnkmpJv9C')


def readTweet():
    st = api.GetUserTimeline(screen_name=user)

def parseTweet():
    for s in s.text.split('\n'):
        color = s.split(' ').remove(0)
        if color not in colorDict:
            colorDict.append(color : [s.favorite_count])
        else:
            colorDict[color].append(s.favorite_count)

