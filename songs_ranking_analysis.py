#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 16:22:10 2021

@author: yangyang-z
"""

import pandas as pd

city_names = []#类行为列表，存放着所有城市的名字
dataframe_list = []
city_name = pd.read_excel('/Users/yangyang-z/documents/python/apple_music/城市URL和sql语句.xlsx','Sheet10',usecols=[1],names=None,header=None)
for i in range(len(city_name)):
    city_names.append(city_name[1][i])
city_path = pd.read_excel('/Users/yangyang-z/documents/python/apple_music/城市URL和sql语句.xlsx','Sheet10',usecols=[6],names=None,header=None)
save_path = pd.read_excel('/Users/yangyang-z/documents/python/apple_music/城市URL和sql语句.xlsx','Sheet12',usecols=[2],names=None,header=None)


for i in city_path[6]:
    date = []#存放着第i个城市的数据日期,当作city_dataframe的列属性
    songs_list = []#用来存放第i个城市在107天内出现过的所有歌曲，当作city_dataframe的行属性
    #date
    long = pd.read_excel(i)
    plus = 0
    for t in range(int(len(long)/25)): 
        city_date = pd.read_excel(i)['DATE'][plus][5:10]
        date.append(city_date)
        plus = plus+25
    
    #songs_list
    for j in range(len(date)):
        day_song = pd.read_excel(i)['SONG'][j*25:(j+1)*25]
        for s in day_song:
            if s not in songs_list:
                songs_list.append(s)
                
    #dataframe
    city_dataframe = pd.DataFrame(index=songs_list)#用来存放第i个城市在统计期间内的排名情况
    
    for q in range(len(date)):
        id_list = []
        daily_song = pd.read_excel(i)['SONG'][q*25:(q+1)*25]
        daily_id = pd.read_excel(i)['ID'][q*25:(q+1)*25]
        h = daily_song.tolist()
        v = daily_id.tolist()
        for y in songs_list:
            if y in h:
                id_list.append(v[h.index(y)])
            else:
                id_list.append(0)
        print('insert ',date[q])
        city_dataframe[date[q]] = id_list
        
    dataframe_list.append(city_dataframe)
    
for i in range(len(dataframe_list)):
    dataframe_list[i].to_csv(save_path[2][i])

