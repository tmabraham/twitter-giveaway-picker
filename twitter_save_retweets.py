import requests
import os
token = os.environ['TOKEN']

tweet_id = '1479928224377303042'
url = 'https://api.twitter.com/2/tweets/{}/retweeted_by'.format(tweet_id)
print(url)
headers = {'Authorization': 'Bearer {}'.format(token)}
retweets_resp = requests.request("GET", url, headers=headers)
retweets = retweets_resp.json()
retweeters = [r['username'] for r in retweets['data']]

from time import time
t = int(time())
with open('results/retweeters-ids-%s-%s.txt' % (tweet_id, t), 'w') as f_out:
    for r in retweeters:
        f_out.write(r)
        f_out.write('\n')
print('done')