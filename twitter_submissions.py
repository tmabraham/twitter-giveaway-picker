
import requests
import os
from glob import *
from random import shuffle
token = os.environ['TOKEN']

url = 'https://api.twitter.com/2/users/by/username/iScienceLuvr'
headers = {'Authorization': 'Bearer {}'.format(token)}
user_id_resp = requests.request("GET", url, headers=headers)
user_id_resp = user_id_resp.json()
my_user_id = user_id_resp['data']['id']

retweeter_files = sorted(glob('results/retweeters-ids-*.txt'))
all_retweeters = set()
for f in retweeter_files:
    with open(f, 'r') as f_in:
        retweeters = [line.strip() for line in f_in]
        all_retweeters.update(retweeters)

likers_files = sorted(glob('results/likers-ids-*.txt'))
all_likers = set()
for f in likers_files:
    with open(f, 'r') as f_in:
        likers = [line.strip() for line in f_in]
        all_likers.update(likers)

all_submissions = all_retweeters.intersection(all_likers)
print(len(all_submissions))


all_submissions = list(all_submissions)
shuffle(all_submissions)
winners = []
for submission in all_submissions:
    # get user id for each submission
    url = 'https://api.twitter.com/2/users/by/username/{}'.format(submission)
    user_id_resp = requests.request("GET", url, headers=headers)
    user_id_resp = user_id_resp.json()
    user_id = user_id_resp['data']['id']
    # check if user follows me
    url = 'https://api.twitter.com/2/users/{}/following/'.format(user_id)
    following_resp = requests.request("GET", url, headers=headers)
    following = following_resp.json()
    following_ids = [f['id'] for f in following['data']]
    if my_user_id in following_ids:
        winners.append(submission)
    if len(winners) == 3:
        break

print('The winners are:')
print(*winners, sep='\n')
