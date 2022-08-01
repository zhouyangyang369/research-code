#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:32:25 2021

@author: yangyang-z
"""

#import song_spotify_id
import requests
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


'''
print(access_token)
a = ['Bearer ']
a[0] = a[0] + access_token

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}
headers['Authorization'] = a[0]
songs_id = song_spotify_id.songs_id
songs_audio_features = {}
for key in songs_id.keys():
    song_id = songs_id[key]
    url = ['https://api.spotify.com/v1/audio-features/']
    url[0] = url[0] + song_id
    response = requests.get(url[0], headers=headers)
    songs_audio_features[key] = response.json()
#print(songs_audio_features)

danceability_sum = 0
energy_sum = 0
key_sum = 0
loudness_sum = 0
mode_sum = 0
speechiness_sum = 0
acousticness_sum = 0
instrumentalness_sum = 0
liveness_sum = 0
valence_sum = 0
tempo_sum = 0

# danceability_means = 0
# energy_means = 0
# key_means = 0
# loudness_means = 0
# mode_means = 0
# speechiness_means = 0
# acousticness_means = 0
# instrumentalness_means = 0
# liveness_means = 0
# valence_means = 0
# tempo_means = 0
for key in songs_audio_features.keys():
    features = songs_audio_features[key]
    danceability = features['danceability']
    energy = features['energy']
    key = features['key']
    loudness = features['loudness']
    mode = features['mode']
    speechiness = features['speechiness']
    acousticness = features['acousticness']
    instrumentalness = features['instrumentalness']
    liveness = features['liveness']
    valence = features['valence']
    tempo = features['tempo']
    danceability_sum = danceability_sum + danceability
    energy_sum  = energy_sum + energy
    key_sum = key_sum + key
    loudness_sum = loudness_sum + loudness
    mode_sum = mode_sum + mode
    speechiness_sum = speechiness_sum + speechiness
    acousticness_sum = acousticness_sum + acousticness
    instrumentalness_sum = instrumentalness_sum + instrumentalness
    liveness_sum = liveness_sum + liveness
    valence_sum = valence_sum + valence
    tempo_sum = tempo_sum + tempo
print(danceability_sum/44)
print(energy_sum/44)
print(key_sum/44)
print(loudness_sum/44)
print(mode_sum/44)
print(speechiness_sum/44)
print(acousticness_sum/44)
print(instrumentalness_sum/44)
print(liveness_sum/44)
print(valence_sum/44)
print(tempo_sum/44)
'''

    


