#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter
from time import sleep
from sys  import exit
import json as simplejson
from random import randrange

# Api twitter para conectar
# https://apps.twitter.com/app/12816710/keys
api = twitter.api(
      consumer_key='gMgM98BADb4kiH4Y0M7AD5gw3',
      consumer_secret='YA7l1GF6iLfdd8H0ybS9iBgBKXIhsWm0Nu89mHpnMnPcqpwYnZ',
      access_token_key='528603134-F4XrgrN8v5jwzxEvxeHIKjyMxajclVEVnToGYS7x',
      access_token_secret='GALsD4zAoopfgLrpBPR4apboUsN6tc0bMo3pLTeAc7nW1'
      )

user = 'otluix'
lstname = 'Amigos'
AMIGOS = []
NOME = {}
FOLLOWERS = {}
parameters = {}
parameters['cursor'] = -1
ic = 0
while (parameters['cursor'] !=0):
      url = '%s/%s/%s/members.json' % (api.base_url, user) #, lstname)

      json = api.FetchUrl(url, parameters=parameters)
      data = simplejson.loads(json)
      for u in data['users']:
        AMIGOS.append(u)
      parameters['cursor'] = int(data['next_cursor_str'])

      if (ic == 10): break
      ic += 1

for a in AMIGOS:
    NOMES[a['screen_name']] = 1

users = api.GetFollowers()
for u in users:
    status = ""
    try:
        if (NOMES[u.screen_name] == 1):
            FOLLOWERS['@' + u.screen_name] = 1
            status = "OK"
    except:
        status = "NOT"

    print (u.screen_name, status)
    
SIZE = 140
MSG = "#FF"
i = 1
api.PostUpdates("Automated python-twitter-#FF mode=on")
for uid in FOLLOWERS.keys():
    if not (randrange(0,2)):
        print ("Nao foi:", uid)
        continue
    print (i, uid)
    if ( len(MSG + " " + uid) > SIZE):
        print (MSG)
        api.PostUpdate(MSG)
        sleep(60)
        MSG = "#FF " + uid
    else:
        MSG += " " + uid
    i += 1

sleep(60)
print (MSG)
api.PostUpdate(MSG)

api.PostUpdates("Python Twitter #rockz!!!")
api.PostUpdates("Automated python-twitter-#FF mode=off")
