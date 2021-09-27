import tensorflow as tf
import keras as kr
import numpy as np

print("hello world")
print("我想对你说 hello world!")

#创建列表、元组、和多维数组
a = ["大三","A1952",18] # 列表
b = (1,2,3) # 元组
c = np.array([(1,2),(3,4),(5,6)]) # 多维数组
print(a)
print(b)
print(c)

#生成2个size一样的随机数组，并纵向合并和横向合并，在对合并后的数组扁平化
arr1 = np.random.randint(1,10,size=(3,3))
arr2 = np.random.randint(1,10,size=(3,3))
arr3 = np.hstack((arr1,arr2)) # arr3 = np.concatenate((arr1,arr2),axis=1)) 横向合并
arr4 = np.vstack((arr1,arr2)) # arr4 = np.concatenate((arr1,arr2),axis=0)) 纵向合并
arr5 = arr3.flatten() # arr3扁平化
arr6 = arr4.flatten() # arr4扁平化
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
print(arr6)

#随机生成1-1000，50*15大小的矩阵，并使用常用统计函数，打印结果
arr = np.random.randint(1,1000,size=(50,15))

print('创建的数组：\n', arr)
print('数组的和：',np.sum(arr))
print('数组纵轴的和',np.sum(arr,axis=0))
print('数组横轴的和',np.sum(arr,axis=1))
print('数组的均值',np.mean(arr))
print('数组横轴的均值',np.mean(arr,axis=1))
print('数组的标准差',np.std(arr))
print('数组横轴的标准差',np.std(arr,axis=1))
