#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 14:26:24 2021

@author: yangyang-z
"""

from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
city_name = pd.read_excel('/Users/yangyang-z/documents/python/apple_music/城市URL和sql语句.xlsx','Sheet10',
                          usecols=[1],names=None,header=None)
city_means = pd.read_excel('/Users/yangyang-z/documents/music_data_analysis/city_means_0922.xlsx')
y = city_means.values
print(y[:,1:])
kmeans_3 = KMeans(n_clusters=3).fit(y[:,1:])
cluster_label3 = kmeans_3.labels_
cluster_center3 = kmeans_3.cluster_centers_
print(cluster_label3)
#print(cluster_center)
c1 = []
c2 = []
c3 = []
for  city in range(len(city_name)):
    if cluster_label3[city] == 0:
        c1.append(city_name[1][city])
    if cluster_label3[city] == 1:
        c2.append(city_name[1][city])
    if cluster_label3[city] == 2:
        c3.append(city_name[1][city])
print(c1)
print(c2)
print(c3,'\n')

kmeans_4 = KMeans(n_clusters=4).fit(y[:,1:])
cluster_label4 = kmeans_4.labels_
cluster_center4 = kmeans_4.cluster_centers_
print(cluster_label4)
#print(cluster_center)
cluster_1 = []
cluster_2 = []
cluster_3 = []
cluster_4 = []
cluster_5 = []
for  city in range(len(city_name)):
    if cluster_label4[city] == 0:
        cluster_1.append(city_name[1][city])
    if cluster_label4[city] == 1:
        cluster_2.append(city_name[1][city])
    if cluster_label4[city] == 2:
        cluster_3.append(city_name[1][city])
    if cluster_label4[city] == 3:
        cluster_4.append(city_name[1][city])
print(cluster_1)
print(cluster_2)
print(cluster_3)
print(cluster_4,'\n')

kmeans_5 = KMeans(n_clusters=5).fit(y[:,1:])
cluster_label5 = kmeans_5.labels_
cluster_center5 = kmeans_5.cluster_centers_
print(cluster_label5)
cluster1 = []
cluster2 = []
cluster3 = []
cluster4 = []
cluster5 = []
for  city in range(len(city_name)):
    if cluster_label5[city] == 0:
        cluster1.append(city_name[1][city])
    if cluster_label5[city] == 1:
        cluster2.append(city_name[1][city])
    if cluster_label5[city] == 2:
        cluster3.append(city_name[1][city])
    if cluster_label5[city] == 3:
        cluster4.append(city_name[1][city])
    if cluster_label5[city] == 4:
        cluster5.append(city_name[1][city])
print(cluster1)
print(cluster2)
print(cluster3)
print(cluster4)
print(cluster5,'\n')

kmeans_6 = KMeans(n_clusters=6).fit(y[:,1:])
cluster_label6 = kmeans_6.labels_
cluster_center6 = kmeans_6.cluster_centers_
print(cluster_label6)
cl1 = []
cl2 = []
cl3 = []
cl4 = []
cl5 = []
cl6 = []
for  city in range(len(city_name)):
    if cluster_label6[city] == 0:
        cl1.append(city_name[1][city])
    if cluster_label6[city] == 1:
        cl2.append(city_name[1][city])
    if cluster_label6[city] == 2:
        cl3.append(city_name[1][city])
    if cluster_label6[city] == 3:
        cl4.append(city_name[1][city])
    if cluster_label6[city] == 4:
        cl5.append(city_name[1][city])
    if cluster_label6[city] == 5:
        cl6.append(city_name[1][city])
print(cl1)
print(cl2)
print(cl3)
print(cl4)
print(cl5)
print(cl6)




