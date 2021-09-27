# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 23:30:19 2021

@author: hasee
"""
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
data = load_iris()
#把data里面的数据重新赋值，因为data里有多个数据
feature=data.data
#写一个长度为150的DataFrame数据，把target里面的数值数据变成target_name里的变量数据
a=np.zeros(len(data.target))
a= pd.DataFrame(a)
# for i in range(len(data.target)):
#     if data.target[i]==0:
#         a[i:i+1]=str(data.target_names[0])
#     if data.target[i]==1:     
#         a[i:i+1]=str(data.target_names[1])
#     if data.target[i]==2:     
#         a[i:i+1]=str(data.target_names[2])
for i in range(len(data.target)):
    if data.target[i]==0:
        a.iloc[i]=str(data.target_names[0])
    if data.target[i]==1:     
        a.iloc[i]=str(data.target_names[1])
    if data.target[i]==2:     
        a.iloc[i]=str(data.target_names[2])
#把feature里加列索引
df1=pd.DataFrame(feature,columns=['花萼长度','花萼宽度','花瓣长度','花瓣宽度'])
#添加df1添加列
df1['class']=a
df1.to_csv('I:/213/Irisdata.csv')#存储到CSV中
df1.to_excel('I:/213/Irisdata.xlsx')#存储到Excel中
#读取csv和xlsx文件
irisdata=pd.read_csv('I:/213/Irisdata.csv')
irisdata=pd.read_excel('I:/213/Irisdata.xlsx')
print(irisdata.columns)

df1=pd.DataFrame(irisdata,columns=['索引','花萼长度','花萼宽度','花瓣长度','花瓣宽度','class'])
#删除多余索引
df1.drop('索引',axis=1,inplace=True)
#把数据分成二个数据集，发现索引不是从0开始的
a1=df1[0:100]
a2=df1[100:150]
#合并横向二个数据集，发现索引问题
b=a1.append(a2)
#重建索引合并数组
b=a1.append(a2,ignore_index=True)
#重建索引如果与原数据没有交集就会是全空值
a2.reindex(range(50))
#使用reset更换索引
a2.reset_index(inplace=True,drop=True)
b=a1.append(a2)
#因为有变量值不能直接转换成array
#b1=np.array(b)
# for i in range(len(data.target)):
#     if b.iloc[i:i+1,4:5].values==data.target_names[0]:
#         b.iloc[i:i+1,4:5]=0
#     if b.iloc[i:i+1,4:5].values==data.target_names[1]:   
#         b.iloc[i:i+1,4:5]=1
#     if b.iloc[i:i+1,4:5].values==data.target_names[2]:     
#         b.iloc[i:i+1,4:5]=2
# for i in range(len(data.target)):
#     if b.iloc[i:i+1,4].values==data.target_names[0]:
#         b.iloc[i:i+1,4]=0
#     if b.iloc[i:i+1,4].values==data.target_names[1]:   
#         b.iloc[i:i+1,4]=1
#     if b.iloc[i:i+1,4].values==data.target_names[2]:     
#         b.iloc[i:i+1,4]=2
        
for i in range(len(data.target)):
    if b.iloc[i,4]==data.target_names[0]:
        b.iloc[i,4]=0
    if b.iloc[i,4]==data.target_names[1]:   
        b.iloc[i,4]=1
    if b.iloc[i,4]==data.target_names[2]:     
        b.iloc[i,4]=2
        
b1=np.array(b)
print(df1.describe())
import matplotlib.pyplot as plt


plt.rcParams['font.family'] = ['SimHei']  
df1.hist() 
plt.suptitle('%s and %s'%('直方图','柱状图'))
#数据直方图histograms 用来分析单个属性在各个区间的变化分布
plt.savefig('I:/213/直方图.jpg')
plt.show() 
#KDE图，也被称作密度图(Kernel Density Estimate,核密度估计)
df1.plot(kind='kde')
plt.savefig('I:/213/密度图.jpg')
plt.show()
#fig1=plt.figure(figsize=(9,7),dpi=90) 
#ax1=fig1.add_subplot(1,2,1)
#plt.title     

#显示箱图 表示数据的离散程度和异常值
#kind='box'绘制箱图,包含子图且子图的行列布局layout为2*2，子图共用x轴、y轴刻度，标签为False
df1.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.savefig('I:/213/箱线图.jpg')
plt.show() 

df1.plot(x='花萼长度', y='花萼宽度', kind='scatter') #散点图，x轴表示花萼长度，y轴表示花萼宽度
plt.savefig('I:/213/单散点图.jpg')
plt.show() 
from pandas.plotting import scatter_matrix   
#alpha点透明度
scatter_matrix(df1, alpha=0.6, figsize=(6, 6), diagonal='kde') 
plt.savefig('I:/213//散点图.jpg')
plt.show()
df2=df1.copy()
df2.drop('class',axis=1)
import seaborn as sns
sns.pairplot(df1)
#保存图片, 由于在jupyter notebook中太大, 不能一次截图
plt.savefig('I:/213/pairplot.png')
plt.show()
