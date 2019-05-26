# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 20:47:35 2017

@author: cheny
"""

import pandas as pd
from collections import Counter

#import pmf1


def pd_pmf(df,title='PMF'):
    cd=df.iloc[:,0]
    c=Counter(cd)
    x1=sorted(list(c.keys()))
    total=len(df)
    if title=='':
        title='PMF'  
    ndf=pd.DataFrame(index=x1,columns=[title]) #空白df
    for i in x1:
        ndf.loc[i,title]= c[i]/total#计算频率, 为什么不直接写len(df)
    return ndf 
    
'''  
def joint_pmf(df1,df2):
    df3=df1.copy()
    for i in df2.index:        
        if i not in df3.index:
            df3.loc[i]=0
    df3=df3.sort_index()
    return df3
'''
    
df1=pd.read_csv('./douban5wan.csv',encoding='gbk')
#title 电影名称， rate电影评分，rate_nums 评论的人数，onyear 发行年份，area 发行国家 
df17=df1[df1['onyear']==2017]
df16=df1[df1['onyear']==2016]
rate16=df16[['rate']]
rate17=df17[['rate']]
pmf17=pd_pmf(rate17,'2017')
pmf16=pd_pmf(rate16,'2016')
pmf=pd.concat([pmf16,pmf17],axis=1)
ax=pmf.plot.bar(figsize=(14,7),title='对比')
print('2017:',rate17.describe(),'2016:',rate16.describe())