"""
1.数据挖掘主要过程和有哪些主要算法
    过程:(1)确立挖掘目的 (2)数据准备 (3)数学建模 (4) 模型评估 (5)模型应用
    主要算法:(1)连接分析 (2)关联分析 (3) 分类 (4)聚类
2.举个数据挖掘的例子
    通过分析网购用户的网购时间段,商品类型、价格,退换货情况等网购行为,建立模型。利用模型向该用户推荐商品,推送广告并通过
反馈不断完善模型。
3.2-23_24_25_26改变数组维度,数据散开和数据合并。
    见程序主体
4.a="python",a[2]=? a[4]=?
    a[2]='t' a[4]='o'
5.numpy中常用的统计函数
    (1)sum:计算数组中的和
    (2)mean:计算数组中的均值
    (3)var:计算数组中的方差
    (4)std:计算数组中的标准差
    (5)max:计算数组中的最大值
    (6)min:计算数组中的最小值
    (7)argmax:返回数组中最大元素的索引
    (8)argmin:返回数组中最小元素的索引
    (9)cumsum:计算数组中所有元素的累计和
    (10)cumprod:计算数组中所有元素的累计积
"""
import numpy as np

#2-23 改变数组维度
arr1 = np.arange(12)
print('arr1:\n',arr1)
arr2 = arr1.reshape(3,4)
print('arr2:\n',arr2)
arr3  = arr1.reshape(2,-1)
print('arr3:\n',arr3)

#2-24 数据散开与扁平化
arr1 = np.arange(12).reshape(3,4)
print('arr1:\n',arr1)
arr2 = arr1.ravel()
print('arr2\n',arr2)
arr3 = arr1.flatten()
print('arr6\n',arr3)

#2-25 两个数组合并
arr1 = np.arange(6).reshape(3,2)
arr2=arr1*2
arr3=np.hstack((arr1,arr2))
print('横向合并:\n',arr3)
arr4 = np.vstack((arr1,arr2))
print('纵向合并\n',arr4)

#2-26 利用concatenate()函数合并数组
arr1 = np.arange(6).reshape(3,2)
arr2 = arr1*2
print('横向合并为:\n',np.concatenate((arr1,arr2),axis = 1))
print('纵向合并为:\n',np.concatenate((arr1,arr2),axis = 0))

