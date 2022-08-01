#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 17:13:01 2021

@author: yangyang-z
"""
'''
还没有分析：
1.将106个城市按照国家分类
2.分析各个国家的城市音乐ranking的特点
（1）各个城市之间的歌曲相似度
（2）各个城市之间歌曲排名变化程度的比较
3.分析各个国家的各个城市更倾向于本国的歌曲还是外国的歌曲，其中外国的歌曲又可以根据艺人的国籍细分为具体的国家

分析过：
1.求取每个城市在各个音声特征上的平均值
2.求取每个国家在各个音声特征上的平均值

接下来想分析：
1.通过聚类算法分析106个城市，根据音声特征将106个特征进行聚类分析，分析这些城市的相同点
2.将天气因素也加入分析，看看各个城市的各个音声特征随天气变化而变化的程度
3.将日出日落时间也加入分析（有待考虑）
'''
import matplotlib.pyplot as plt
import pandas as pd
city_means = pd.read_excel('/Users/yangyang-z/documents/music_data_analysis/city_means的副本.xlsx',header=None)
# europe_country = ['switzerland','poland','austria','czech','russia','italy','ukraine','turkey','scotland','ireland'
#           ,'denmark','hungary','spain','new_zealand','france','england','german']
country_means = pd.DataFrame(index = ['japan','american','china','german','england','france','korea','india','australia','canadian','mexico','italy']
,columns=['danceability','energy','key','loundiness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo'])
city_over3_country = ['japan','american','china','german','england','france','korea','india','australia','canadian','mexico','italy']
for i in range(len(city_over3_country)):
    country = city_means[city_means[12] == city_over3_country[i]]

    danceability = 0
    energy = 0
    key = 0
    loudness = 0
    mode = 0
    speechiness = 0
    acousticness = 0
    instrumentalness = 0
    liveness = 0
    valence = 0
    tempo = 0
    # for i in range(11): 
    #     for j in range(len(country)):
    describe = country.describe()
    means = country.mean()
    #print(means)
    features = []
    for j in range(len(means)):
        features.append(means[j + 1])
    country_means.loc[city_over3_country[i]] = features
    print(country_means)
country_means.to_excel('/Users/yangyang-z/documents/music_data_analysis/country_means_0922.xlsx')
visua_1 = pd.DataFrame(country_means,columns=['danceability'])
visua_2 = pd.DataFrame(country_means,columns=['energy'])
visua_3 = pd.DataFrame(country_means,columns=['key'])
visua_4 = pd.DataFrame(country_means,columns=['loundiness'])
visua_5 = pd.DataFrame(country_means,columns=['mode'])
visua_6 = pd.DataFrame(country_means,columns=['speechiness'])
visua_7 = pd.DataFrame(country_means,columns=['acousticness'])
visua_8 = pd.DataFrame(country_means,columns=['instrumentalness'])
visua_9 = pd.DataFrame(country_means,columns=['liveness'])
visua_10 = pd.DataFrame(country_means,columns=['valence'])
visua_11 = pd.DataFrame(country_means,columns=['tempo'])
visua_1.T.plot.bar()
visua_2.T.plot.bar()
visua_3.T.plot.bar()  
visua_4.T.plot.bar()
visua_5.T.plot.bar()
visua_6.T.plot.bar() 
visua_7.T.plot.bar()
visua_8.T.plot.bar()
visua_9.T.plot.bar()  
visua_10.T.plot.bar()
visua_11.T.plot.bar()
            