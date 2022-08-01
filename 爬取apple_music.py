#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 11:48:55 2021

@author: yangyang-z
"""

import requests
import sys
from bs4 import BeautifulSoup
import pymysql

db = pymysql.connect(host = 'localhost',port = 3306,user = 'root',passwd = 'zhouyang123/',db = 'apple_music')
cursor = db.cursor()

url1 = 'https://music.apple.com/jp/playlist/%E3%83%88%E3%83%83%E3%83%9725-%E6%9D%B1%E4%BA%AC/pl.b00965bf8c6c4be8b4721e9293e8ceab'
url2 = 'https://music.apple.com/jp/playlist/トップ25-広州/pl.5b45c8decd4c4c40b40239136fe5b9ff'
url3 = 'https://music.apple.com/jp/playlist/%E3%83%88%E3%83%83%E3%83%9725-%E5%A4%A7%E9%98%AA/pl.3f22ec9c90ce447d87c61762c9876726'
r = requests.get(url1) #requests请求
print(r.status_code)
#print(r.text)
soup = BeautifulSoup(r.text,'html.parser')

songs2 = soup.find_all('div',"songs-list-row__song-name")
title = soup.find('title')


print(title.get_text())
for i in songs2: 
    print(i.get_text())
    '''
    data = (i.get_text())
    sql = "INSERT INTO osaka (song) VALUES ('%s')"
    cursor.execute(sql % data)
    db.commit()


#db.execute("drop table 广州")
'''