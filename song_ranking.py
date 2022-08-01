#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 22:03:49 2021

@author: yangyang-z
"""

import pandas as pd
song_quantity = pd.read_csv('/Users/yangyang-z/Documents/music_data_analysis/20211111_songs_ranking/kyoto.csv')

city_names = []
city_name = pd.read_excel('/Users/yangyang-z/documents/python/apple_music/城市URL和sql语句.xlsx','Sheet10',usecols=[1],names=None,header=None)
city_names = city_name[1].tolist()

city_features = pd.DataFrame(index=city_names)

save_path = pd.read_excel('/Users/yangyang-z/documents/python/apple_music/城市URL和sql语句.xlsx','Sheet12',usecols=[2],names=None,header=None)
songs_quantity = []
for i in range(len(save_path[2])):
    city = pd.read_csv(save_path[2][i])
    length = len(city.iloc[:,0])
    songs_quantity.append(length)
city_features['songs_quantity'] = songs_quantity
city_features.to_csv('/Users/yangyang-z/Documents/music_data_analysis/20211111_songs_ranking/all_city_features.csv')

city_allday_sum = []
city_daily_sum = []
for i in range(len(save_path[2])):
    summ1 = 0
    dict_daily = {}
    c = pd.read_csv(save_path[2][i])
    columns = c.columns
    columns_list = columns.tolist()
    columns_list.remove('Unnamed: 0')
    length = len(c.iloc[:,0])
    for j in range(len(columns_list)):
        summ2 = 0
        if j < len(columns_list) - 1:
            for l in range(length):
                if c[columns_list[j]][l] != c[columns_list[j+1]][l]:
                    summ1 = summ1 + 1
                    summ2 = summ2 + 1
            
        dict_daily[columns_list[j]] = summ2#日变化次数

    city_allday_sum.append(summ1)#期间总变化次数
    city_daily_sum.append(dict_daily)
city_features['total changes'] = city_allday_sum
city_features.to_csv('/Users/yangyang-z/Documents/music_data_analysis/20211111_songs_ranking/all_city_features.csv')

date = city_daily_sum[0]
for i in date.keys():
    city_features[i] = ""
temp1 = city_features
for i in range(len(city_names)):
    for j in city_daily_sum[i].keys():
        temp1.loc[city_names[i],j] = city_daily_sum[i][j]
        
temp1.to_csv('/Users/yangyang-z/Documents/music_data_analysis/20211111_songs_ranking/all_city_features.csv')


