#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 13:58:31 2021

@author: yangyang-z
"""

import pandas as pd
import requests
import songs_analysis

url_gettoken = 'https://accounts.spotify.com/api/token'
headers_gettoken = {
    'Authorization': 'Basic ZWUzNTNjMjcyYzBmNGIxYjkwOGJmNzNmNmI5ZTNkMjk6MmUzMjQ4YzRlNDk0NGRmNmIxMjM1YTA4YmI5ZTIyMmE=',
}
data = {
  'grant_type': 'client_credentials'
}
response = requests.post(url_gettoken, headers=headers_gettoken, data=data)
access_token = response.json()['access_token']
print(access_token)
a = ['Bearer ']
a[0] = a[0] + access_token

url = 'https://api.spotify.com/v1/search'
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}
headers['Authorization'] = a[0]
params = {
    'q':'stay',
    'type':'track',
    'limit':'1',
}
null_id = []
songs_id = {}
song = songs_analysis.song
for i in range(len(song)):
    params['q'] = song[i]
    #print(params)
    response = requests.get(url, headers=headers, params=params)
    track = response.json()
    #print(track)
    tracks = track['tracks']
    items_list = tracks['items']
    if len(items_list) != 0:
        items_dict = items_list[0]
        id = items_dict['id']
        songs_id[song[i]] = id
    else:
        null_id.append(song[i])
        
print(songs_id)    
print(null_id)