#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:22:07 2021
@author: yangyang-z
"""
'''
1.将tokyo的Excel表中的数据读出来
2.将数据按照每25个分为一天，总共44天
3.将每一天的数据按照ID升序排列
4.从第一天开始统计出现的每一首歌在这44天内的出现频率
5.统计在这44天内出现在榜单内的歌的排行的变化的程度
可以将4和5中的结果画图
'''
import pandas as pd
from  collections import defaultdict
import requests

city_means = pd.DataFrame(index = ['tokyo','osaka','nagoya','sapporo','fukuoka','kyoto','sendai','naha',
'new_york_city','london','paris','seoul','accra','almaty','atlanta','auckland','austin','bangkok',
'barcelona','北京','bengaluru','berlin','birmingham','bogota','bordeaux','brisbane','budapest',
'buenos_aires','busan','calgary','cape_town','chicago','koln','kobenhavn','dallas','delhi','denver',
'detroit','dubai','dublin','durban','edmonton','frankfurt','glasgow','guadalajara','广州','ciudad_de_guatemala',
'hamburg','honolulu','houston','istanbul','jakarta','johannesburg','knib','kingston','kuala_lumpur',
'lagos','lima','liverpool','los_angeles','lyon','madrid','manchester','manila','marseille','medellin',
'melbourne','ciudad_de_mexico','miami','milano','monterrey','montreal','mockba','mumbai','munchen',
'nairobi','napoli','nashville','ottawa','philadelphia','phoenix','prague','quebec_city','rio_de_janeiro',
'riyadh','roma','cahkt','san_diego','san_francisco','san_jose','san_juan','santiago_de_chile','santo_domingo',
'sao_paulo','seattle','上海','sydney','台北','テルアビブ','toronto','vancouver','wien','warszawa',
'washington_DC','winnipeg','zurich_zurich_zurigo'],
columns=['danceability','energy','key','loundiness','mode','speechiness',
'acousticness','instrumentalness','liveness','valence','tempo'])

#get token
url_gettoken = 'https://accounts.spotify.com/api/token'
headers_gettoken = {
    'Authorization': 'Basic ZWUzNTNjMjcyYzBmNGIxYjkwOGJmNzNmNmI5ZTNkMjk6MmUzMjQ4YzRlNDk0NGRmNmIxMjM1YTA4YmI5ZTIyMmE=',
}
data = {
  'grant_type': 'client_credentials'
}
response = requests.post(url_gettoken, headers=headers_gettoken, data=data)
access_token = response.json()['access_token']
a = ['Bearer ']
a[0] = a[0] + access_token
#get token end
#curl of getting songs' id
url_search = 'https://api.spotify.com/v1/search'
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

#curl of getting songs' id end
city_path = pd.read_excel('/Users/yangyang-z/documents/python/apple_music/城市URL和sql语句.xlsx','Sheet10',
                          usecols=[2],names=None,header=None)
city_name = pd.read_excel('/Users/yangyang-z/documents/python/apple_music/城市URL和sql语句.xlsx','Sheet10',
                          usecols=[1],names=None,header=None)

temp1 = city_path.values.tolist()
temp2 = city_name.values.tolist()
city_path_list = []
city_name_list = []
for i in temp1:
    city_path_list.append(i[0])
for i in temp2:
    city_name_list.append(i[0])
for flag in range(len(city_path_list)):
    print("for city",city_name_list[flag],"\n")
    y = city_path_list[flag]
    xlsx = pd.ExcelFile(y)
    city = pd.read_excel(xlsx)
    #2.将数据按照每25个分为一天，总共44天
    #3.将每一天的数据按照ID升序排列
    #4.从第一天开始统计出现的每一首歌在这44天内的出现频率
    day_num = int(len(city)/25)
    fre = {}#创建一个可以统计歌曲出现频度的字典
    song_rank = defaultdict(list)
    print(day_num)
    for i in range(day_num):
        temp = city[i*25:(i+1)*25]#按照顺序，每25个歌曲分为一天
        data = temp.sort_values(by = "ID",ascending = True)#按指定列排序 dataframe sort_values
        data.index = range(len(data))#pandas.DataFrame的index重新排列（从0开始）
        #print(data.SONG[0])
        for j in range(len(data)):
            if data.SONG[j] in fre:     #如何字典中有这首歌的话，频度加1
                fre[data.SONG[j]] = fre[data.SONG[j]] + 1
            else:
                fre[data.SONG[j]] = 1   #如何字典中没有这首歌的话就将歌名作为键，频度初始化作为1，添加到字典中 
        #到这里为止fre里存放了所统计天数中出现过的歌曲
    song = []
    for key in fre.keys():
        song.append(key)
    
    for i in range(day_num):
        temp = city[i*25:(i+1)*25]#按照顺序，每25个歌曲分为一天
        data = temp.sort_values(by = "ID",ascending = True)#按指定列排序 dataframe sort_values
        data.index = range(len(data))#pandas.DataFrame的index重新排列（从0开始）
        #5.统计在这44天内出现在榜单内的歌的排行的变化的程度
        # （1）统计这44天内出现的全部歌曲的排名变换情况，可以再建一个字典，键是歌名，值是列表，里面是每天的排名
        # （2）统计哪些歌曲在第几天挤进了前25，被挤掉的歌是哪个     
        for k in range(len(data)):#data是每天的25首歌
             song_rank[data.SONG[k]].append(k+1)#将每天的25首歌的排名记录下来，放到song_rank字典中
        for n in range(len(song)):#经过第一天赋值后，将还没有在song_rank字典中的歌曲放入字典中，并将值初始化为0，因为第一天没有排进前25
             if song[n] not in song_rank.keys():
                 song_rank[song[n]].append(0)
        #到这里，在这44天内出现过在榜单上的所有歌曲都已经作为song_rank字典中的键存在于字典中了，接下里就要将每天没有排进前25的歌曲也赋值为0
        for m in range(len(song)):
             if len(song_rank[song[m]]) != (i+1):
                 song_rank[song[m]].append(0)

    change_sum = 0
    for i in range(day_num):
        change = 0
        for j in range(len(song_rank)):
            if i < (day_num-1):
                if song_rank[song[j]][i] != song_rank[song[j]][i+1]:
                    change = change + 1
        #print("the",i+1,"day changed",change,"times")
        change_sum = change_sum + change
    # print("the sum of changes:",change_sum,"times")
    # print(len(song))
    
    
    #to get songs' id
    null_id = []
    songs_id = {}
    for i in range(len(song)):
        params['q'] = song[i]
        #print(params)
        response = requests.get(url_search, headers=headers, params=params)
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
    # print(songs_id)    
    # print(null_id)
    #to get songs' id end
    
    #to get songs' audio features
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
    city_means.loc[city_name_list[flag]] = [danceability_sum/44,energy_sum/44,key_sum/44,loudness_sum/44,
                                         mode_sum/44,speechiness_sum/44,acousticness_sum/44,instrumentalness_sum/44,
                                         liveness_sum/44,valence_sum/44,tempo_sum/44]
    print(city_means)

city_means.to_excel('/Users/yangyang-z/documents/music_data_analysis/city_means_0922.xlsx')
    
    
    
    
    
    
    
    
    