#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:23:20 2021

@author: yangyang-z
"""

'''
1.柱状图：横坐标为歌曲名，纵坐标为频度，一张图
具体：可将fre字典转换为series，然后将series的索引用作x轴刻度，画垂直的柱状图
注：似乎显示频度并没有什么分析的意义，那就先放置
2.折线图：横坐标为天，纵坐标为排名，可以将35首歌的排名变化绘制到一张图中
具体：可将song_rank字典转换为dataframe，然后用dataframe的plot在一张折线图中画出35首歌在这44天内，排名的变化，横坐标为天数，纵坐标为排名
3.折线图：横坐标为天，纵坐标为当天歌曲相较于前一天的排名变化程度，一张图
具体：统计每一天中的所有歌曲发生变化的次数，当作当天排名变化程度
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import songs_analysis
import matplotlib as mpl

# data = np.arange(10)
# plt.plot(data)

# fig = plt.figure()
# ax1 = fig.add_subplot(2,2,1)
# ax2 = fig.add_subplot(2,2,2)
# ax3 = fig.add_subplot(2,2,3)

# name_list = ['monday','tuesday','friday','sunday']
# num_list = [1.5,0.6,7.8,6]
# plt.bar(range(len(num_list)),num_list,fc='b')
# plt.show()

# s = pd.Series(np.random.randn(10).cumsum(),index = np.arange(0,100,10))
# s.plot()

# df = pd.DataFrame(np.random.randn(10,7).cumsum(0),columns=['a','b','c','d','e','f','d'],index = np.arange(0,100,10))
# df.plot()
frequency = songs_analysis.fre
fre_series = pd.Series(frequency)
print(fre_series)
fre_series.plot.barh()