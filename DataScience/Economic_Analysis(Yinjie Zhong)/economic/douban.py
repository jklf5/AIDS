# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 19:23:22 2017

@author: cheny
"""

import pandas as pd
df1=pd.read_csv('./douban5wan.csv',encoding='gbk')
a=df1[['onyear','rate']]
data=a[(a['onyear']==2016) | (a['onyear']==2017)]
print(data)
data_count=data.count()#数量
data_mean=data.mean()#均值
data_median=data.median()#中位数
data_var=data.var()#方差
data_std=data.std()#标准差
print("数量为：\n%s\n均值为：\n%s\n中位数为：\n%s\n方差为：\n%s\n标准差为：\n%s\n"%(data_count,data_mean,data_median,data_var,data_std))
d=input()