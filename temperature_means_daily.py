#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:27:53 2021

@author: yangyang-z
"""

import pandas as pd
import numpy as np
from collections import defaultdict
city_path = pd.read_excel('/Users/yangyang-z/documents/python/apple_music/城市URL和sql语句.xlsx','Sheet11',
                          usecols=[1],names=None,header=None)
path_list = []
for i in range(len(city_path)):
    path_list.append(city_path[1][i])
path_list[0] = '/Users/yangyang-z/documents/city_weather_data_export/20210926/tokyo.xls'
city_temperature = pd.DataFrame(
index = ['tokyo','osaka','nagoya','sapporo','fukuoka','kyoto','sendai','naha',
        'new_york_city','london','paris','seoul','accra','almaty','atlanta','auckland',
        'austin','bangkok','barcelona','beijing','bengaluru','berlin','birmingham','bogota',
        'bordeaux','brisbane','budapest','buenos_aires','busan','calgary','cape_town','chicago',
        'cologne','kobenhavn','dallas','delhi','denver','detroit','dubai','dublin',
        'durban','edmonton','frankfurt','glasgow','guadalajara','guangzhou','ciudad_de_guatemala','hamburg',
        'honolulu','houston','istanbul','jakarta','johannesburg','Kyiv','kingston','kuala_lumpur',
        'lagos','lima','liverpool','los_angeles','lyon','madrid','manchester','manila',
        'marseille','medellin','melbourne','ciudad_de_mexico','miami','milano','monterrey','montreal',
        'Moscow','mumbai','Munich','nairobi','napoli','nashville','ottawa','philadelphia',
        'phoenix','prague','quebec_city','rio_de_janeiro','riyadh','rome','san_diego',
        'san_francisco','san_jose','san_juan','santiago_de_chile','santo_domingo','Sao_Paulo','seattle','shanghai',
        'sydney','taipei','Tel_Aviv','toronto','vancouver','wien','warszawa','washington_DC','winnipeg','Zurich']
,columns = ['2021-08-16', '2021-08-17', '2021-08-18', '2021-08-19', '2021-08-20', '2021-08-21', '2021-08-22', 
            '2021-08-23', '2021-08-24', '2021-08-25', '2021-08-26', '2021-08-27', '2021-08-28', '2021-08-29', 
            '2021-08-30', '2021-08-31', '2021-09-01', '2021-09-02', '2021-09-03', '2021-09-04', '2021-09-05', 
            '2021-09-06', '2021-09-07', '2021-09-08', '2021-09-09', '2021-09-10', '2021-09-11', '2021-09-12', 
            '2021-09-13', '2021-09-14', '2021-09-15', '2021-09-16', '2021-09-17', '2021-09-18', '2021-09-19',
            '2021-09-20', '2021-09-21', '2021-09-22', '2021-09-23', '2021-09-24', '2021-09-25', '2021-09-26'])
name = ['tokyo','osaka','nagoya','sapporo','fukuoka','kyoto','sendai','naha',
        'new_york_city','london','paris','seoul','accra','almaty','atlanta','auckland',
        'austin','bangkok','barcelona','beijing','bengaluru','berlin','birmingham','bogota',
        'bordeaux','brisbane','budapest','buenos_aires','busan','calgary','cape_town','chicago',
        'cologne','kobenhavn','dallas','delhi','denver','detroit','dubai','dublin',
        'durban','edmonton','frankfurt','glasgow','guadalajara','guangzhou','ciudad_de_guatemala','hamburg',
        'honolulu','houston','istanbul','jakarta','johannesburg','Kyiv','kingston','kuala_lumpur',
        'lagos','lima','liverpool','los_angeles','lyon','madrid','manchester','manila',
        'marseille','medellin','melbourne','ciudad_de_mexico','miami','milano','monterrey','montreal',
        'Moscow','mumbai','Munich','nairobi','napoli','nashville','ottawa','philadelphia',
        'phoenix','prague','quebec_city','rio_de_janeiro','riyadh','rome','san_diego',
        'san_francisco','san_jose','san_juan','santiago_de_chile','santo_domingo','Sao_Paulo','seattle','shanghai',
        'sydney','taipei','Tel_Aviv','toronto','vancouver','wien','warszawa','washington_DC','winnipeg','Zurich']
date_list = ['2021-08-16', '2021-08-17', '2021-08-18', '2021-08-19', '2021-08-20', 
             '2021-08-21', '2021-08-22', '2021-08-23', '2021-08-24', '2021-08-25', 
             '2021-08-26', '2021-08-27', '2021-08-28', '2021-08-29', '2021-08-30', 
             '2021-08-31', '2021-09-01', '2021-09-02', '2021-09-03', '2021-09-04', 
             '2021-09-05', '2021-09-06', '2021-09-07', '2021-09-08', '2021-09-09', 
             '2021-09-10', '2021-09-11', '2021-09-12', '2021-09-13', '2021-09-14', 
             '2021-09-15', '2021-09-16', '2021-09-17', '2021-09-18', '2021-09-19', 
             '2021-09-20', '2021-09-21', '2021-09-22', '2021-09-23', '2021-09-24', 
             '2021-09-25', '2021-09-26']
for x in range(len(path_list)):
    print(name[x])
    print(path_list[x])
    city_weather = pd.read_excel(path_list[x],names = None)
    date_time = defaultdict(list)
    #date_time['2021-08-15'].append(default_temperature)
    date_means = {'0':0}
    for i in range(len(date_list)):
        temp_dict =defaultdict(list)#这个字典的键一天中各个时间点，值为各个时间点对应的温度值
        for j in range(len(city_weather)):
            if city_weather['date'][j][:10] == date_list[i]:#the roles of i+1 is to caculate means from 8/16
                temp_dict[city_weather['date'][j][11:13]].append(city_weather['humidity'][j])
            if i < len(date_list)-1:
                if city_weather['date'][j][:10] == date_list[i+1]:
                    break
        #接下来求日均温度
        #先判断是否缺这几个点中的一个或多个，如果有缺，则将缺失项摘出来放到一个列表里
        time = ['02','08','14','20']
        '''sub_time = np.array([['01','03']
                            ,['00','04']
                            ,['07','09']
                            ,['06','10']
                            ,['13','15']
                            ,['12','16']
                            ,['19','21']
                            ,['18','22']])
        '''
        temp_time = []
        lack_time = []
        for key in temp_dict.keys():
            temp_time.append(key)
        for t in time:
            if t not in temp_time:
                lack_time.append(t)
        if len(lack_time) == 0:#没有缺失时间点
            means = (temp_dict['02'][0] + temp_dict['08'][0] + temp_dict['14'][0] + temp_dict['20'][0]) / 4
            date_time[date_list[i]].append(temp_dict['02'][0])
            date_time[date_list[i]].append(temp_dict['08'][0])
            date_time[date_list[i]].append(temp_dict['14'][0])
            date_time[date_list[i]].append(temp_dict['20'][0])
            date_means[date_list[i]] = means        
        #在缺失时间点的上一到两位和下一到两位找替代值
        else:
            for p in lack_time:
                if p == '02':
                    if '01' in temp_dict:
                        temp_dict['02'].append(temp_dict['01'][0])
                    elif '03' in temp_dict:
                        temp_dict['02'].append(temp_dict['03'][0])
                    elif '00' in temp_dict:
                        temp_dict['02'].append(temp_dict['00'][0])
                    elif '04' in temp_dict:
                        temp_dict['02'].append(temp_dict['04'][0])
                    else:
                        temp_dict['02'].append(date_time[date_list[i-1]][0])
                if p == '08':
                    if '07' in temp_dict:
                        temp_dict['08'].append(temp_dict['07'][0])
                    elif '09' in temp_dict:
                        temp_dict['08'].append(temp_dict['09'][0])
                    elif '06' in temp_dict:
                        temp_dict['08'].append(temp_dict['06'][0])
                    elif '10' in temp_dict:
                        temp_dict['08'].append(temp_dict['10'][0])
                    else:
                        temp_dict['08'].append(date_time[date_list[i-1]][1])    
                if p == '14':
                    if '13' in temp_dict:
                        temp_dict['14'].append(temp_dict['13'][0])

                    elif '15' in temp_dict:
                        temp_dict['14'].append(temp_dict['15'][0])
                    elif '12' in temp_dict:
                        temp_dict['14'].append(temp_dict['12'][0])
                    elif '16' in temp_dict:
                        temp_dict['14'].append(temp_dict['16'][0])
                    else:  
                        temp_dict['14'].append(date_time[date_list[i-1]][2])            
                if p == '20':
                    if '19' in temp_dict:
                        temp_dict['20'].append(temp_dict['19'][0])
                    elif '21' in temp_dict:
                        temp_dict['20'].append(temp_dict['21'][0])
                    elif '18' in temp_dict:
                        temp_dict['20'].append(temp_dict['18'][0])
                    elif '22' in temp_dict:
                        temp_dict['20'].append(temp_dict['22'][0])
                    else:
                        temp_dict['20'].append(date_time[date_list[i-1]][3])   
            means = (temp_dict['02'][0] + temp_dict['08'][0] + temp_dict['14'][0] + temp_dict['20'][0]) / 4
            date_time[date_list[i]].append(temp_dict['02'][0])
            date_time[date_list[i]].append(temp_dict['08'][0])
            date_time[date_list[i]].append(temp_dict['14'][0])
            date_time[date_list[i]].append(temp_dict['20'][0])
            date_means[date_list[i]] = means
    #date_time

    tem_means = []
    for i in date_means.values():
        tem_means.append(i)
    tem_means.remove(0)
    city_temperature.loc[name[x]] = tem_means
print(city_temperature)
#city_temperature.to_excel('/Users/yangyang-z/documents/music_data_analysis/city_temperature_means.xlsx')