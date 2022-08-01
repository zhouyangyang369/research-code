#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 11:55:18 2021

@author: yangyang-z
"""
from sklearn import datasets
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
'''
皮尔逊相关系数的值域等级定义：
0.8以上高度相关； 
0.5-0.8 中度相关； 
0.3-0.5 低度相关； 
小于0.3 极弱，可视为不相关。
'''
feature_corr = pd.DataFrame(index = ['danceability','energy','key','loundiness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo']
,columns=['danceability','energy','key','loundiness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo'])
features = ['danceability','energy','key','loundiness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo']
city_means = pd.read_excel('/Users/yangyang-z/documents/music_data_analysis/city_means_0922.xlsx')
for feature in range(len(features)):
    for i in range(11):
        if city_means.corr()[features[feature]][i] > 0.80:
            feature_corr[features[feature]][i] = '高度相関'
        if 0.5 < city_means.corr()[features[feature]][i] < 0.8:
            feature_corr[features[feature]][i] = '中度相関'
        if 0.3 < city_means.corr()[features[feature]][i] < 0.5:
            feature_corr[features[feature]][i] = '低度相関'
        if city_means.corr()[features[feature]][i] < 0.3:
            feature_corr[features[feature]][i] = '無相関'
print(feature_corr)
print(sns.heatmap(city_means.corr()))
city_means_features_corr = city_means.corr()
city_means_features_corr.to_excel('/Users/yangyang-z/documents/music_data_analysis/features_correlation.xlsx')
feature_corr.to_excel('/Users/yangyang-z/documents/music_data_analysis/features_correlation_judge.xlsx')





