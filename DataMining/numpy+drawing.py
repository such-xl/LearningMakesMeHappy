# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 11:13:28 2021

@author: Administrator
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['SimHei']    #用于画图时显示中文
from sklearn.datasets import load_iris #导入数据集iris  
iris = load_iris() #载入数据集
print(iris.data)  #打印输出显示
df1=pd.DataFrame(iris.data,columns=['花萼-length', '花萼-width', '花瓣-length', '花瓣-width'])
a=np.zeros(len(iris.target))
a= pd.DataFrame(a)
#共150条记录，分别代表50条山鸢尾 (Iris-setosa)、变色鸢尾(Iris-versicolor)、维吉尼亚鸢尾(Iris-virginica)
print(iris.target) 
for i in range(len(iris.target)):
    if iris.target[i]==0:
        a[i:i+1]=iris.target_names[0]
    elif iris.target[i]==1:
        a[i:i+1]=iris.target_names[1]
    if iris.target[i]==2:
        a[i:i+1]=iris.target_names[2]
df1['class']=a

iris.data.shape  # iris数据集150行4列的二维数组
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"  
names = ['花萼-length', '花萼-width', '花瓣-length', '花瓣-width', 'class']  
dataset = pd.read_csv(url, names=names)
print(dataset['class'])
for i in range(len(iris.target)):
    if dataset.iloc[i:i+1,4].values=='Iris-setosa':
        dataset.iloc[i:i+1,4]=0
    elif dataset.iloc[i:i+1,4].values=='Iris-versicolor':
        dataset.iloc[i:i+1,4]=1
    if dataset.iloc[i:i+1,4].values=='Iris-virginica':
        dataset.iloc[i:i+1,4]=2
b=np.array(dataset)
b1=b[0:100,:]
b2=b[100:150,:]
c=np.vstack((b1,b2))
c1=np.concatenate((b1,b2),axis=0)
b3=b[:,0:4]
b4=b[:,4]
b4=b4.reshape(150,1)
c3=np.hstack((b3,b4))
c4=np.concatenate((b3,b4),axis=1)
mean=np.mean(b,axis=1)
print(np.mean(b,axis=0))
print(np.min(b,axis=0))
print(np.max(b,axis=0))
b3 = b3.astype(np.float)
print(np.std(b3,axis=0))
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['SimHei'] 
fig1= plt.figure(figsize=(9,7),dpi=90)
plt.title('iris折线图',fontsize=16)
plt.xlabel('花瓣长度',fontsize=16)
plt.ylabel('长度',fontsize=16)
plt.plot(b3[:,0])
plt.legend('花瓣长度',fontsize=16)
fig5=plt.figure(figsize=(9,7),dpi=90)
plt.title('散点图',fontsize=16)
plt.xlabel('花萼长度',fontsize=16)
plt.ylabel('花瓣长度',fontsize=16)
plt.scatter(b3[:,2],b3[:,0])
fig2=plt.figure(figsize=(9,7),dpi=90)
ax1=fig2.add_subplot(2,2,1)
plt.xlabel('class',fontsize=16)
plt.ylabel('花瓣长度',fontsize=16)
plt.scatter(b4,b3[:,0])
ax2=fig2.add_subplot(2,2,2)
plt.xlabel('class',fontsize=16)
plt.ylabel('花瓣宽度',fontsize=16)
plt.scatter(b4,b3[:,1])
ax3=fig2.add_subplot(2,2,3)
plt.xlabel('class',fontsize=16)
plt.ylabel('花萼长度',fontsize=16)
plt.scatter(b4,b3[:,2])
ax4=fig2.add_subplot(2,2,4)
plt.xlabel('class',fontsize=16)
plt.ylabel('花萼宽度',fontsize=16)
plt.scatter(b4,b3[:,3]) 
fig2.suptitle('散点矩阵图',fontsize=20)
fig3=plt.figure(figsize=(9,7),dpi=90)
ax1=fig3.add_subplot(2,2,1)
plt.title('花瓣长度直方图',fontsize=16)
plt.ylabel('花瓣长度',fontsize=16)
ax1.hist(b3[:,0])
ax2=fig3.add_subplot(2,2,2)
plt.title('花瓣宽度直方图',fontsize=16)
plt.ylabel('花瓣宽度',fontsize=16)
plt.hist(b3[:,1])
ax3=fig3.add_subplot(2,2,3)
plt.title('花萼长度直方图',fontsize=16)
plt.ylabel('花萼长度',fontsize=16)
plt.hist(b3[:,2])
ax4=fig3.add_subplot(2,2,4)
plt.title('花萼宽度直方图',fontsize=16)
plt.ylabel('花萼宽度',fontsize=16)
plt.hist(b3[:,3]) 
fig4=plt.figure(figsize=(9,7),dpi=90)
plt.boxplot(b3)
plt.xticks([1,2,3,4],['花瓣长度','花瓣宽度','花萼长度','花萼宽度']) 
