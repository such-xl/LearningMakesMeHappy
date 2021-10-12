# 1. 使用np.linspace定义x: 范围是(-1,1);个数是50, 仿真一维数据组(x,y)表示曲线y=2x+1

import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(-1,1,50)
y = 2.*x+1
print(3.)
plt.plot(x,y)
plt.show()


# 2. P.76(4) plot绘图的主要参数设置方法(简单写)
"""
    x,y: 接收array, 表示x轴和y轴对应的数据
    color:  接收特定string, 指定线条颜色, 默认为None
    linestyle:  接收特定string, 指定线条类型, 默认为"-"
    marker: 接收特定string, 表示绘制的点的类型, 默认为None
    alpha: 接收0~1的小数, 表示点的透明度, 默认为None
"""
# 3. P.76(5) sklearn提供哪些功能
"""
    (1)数据预处理   (2)模型选择      (3)分类   
    (4)回归         (5)聚类         (6)降维
"""
# 4. 使用scipy的pdist进行数据对象距离的计算 课本P96, 习题(3)
#import numpy as np
from scipy.spatial.distance import pdist

x1 = (2,4,3,6,8,2)
y1 = (1,4,2,7,5,3)
X = np.vstack([x1,y1])
print('欧式距离: ', pdist(X,'euclidean'))
print('曼哈顿距离: ', pdist(X, 'cityblock'))
print('闵可夫斯基距离: ', pdist(X, 'minkowski', p=3))
# 5. 简述标称属性、非对称二元属性、数值属性和词频向量的相似度评价方法 习题(4)
"""
    标称属性: 两个对象i和j之间的相异性根据不匹配率进行计算
                d(i,j) = (p-m)/p = 1 - m/p
             m:匹配的数目, 即对象i,j状态相同的属性数
             p:对象的属性总数
    非对称二元属性: 只关心"正匹配"的情况, 忽略负匹配数
                    d(i,j) = (r+s)/(q+r+s)
                   r：i为1, j为0的属性数
                   s: i为0, j为1的属性数
                   q: i,j都为1的属性数
    数值属性: 数值属性的对象相似度一般用数据对象间的距离度量
              如欧式距离、曼哈顿距离、切比雪夫距离、闵可夫斯基距离及汉明距离等
    词频向量: 一般采用余弦相似度
              sim(x,y) = (x.*y)/(||x||*||y||)
              x,y:文档解析出来的两个词频向量
"""
