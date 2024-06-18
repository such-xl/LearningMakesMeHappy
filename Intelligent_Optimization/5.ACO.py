# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import copy
 
# 参数
'''
ALPHA:信息启发因子，值越大，则蚂蚁选择之前走过的路径可能性就越大
      ，值越小，则蚁群搜索范围就会减少，容易陷入局部最优
BETA:Beta值越大，蚁群越就容易选择局部较短路径，这时算法收敛速度会
     加快，但是随机性不高，容易得到局部的相对最优
'''
ALPHA, BETA, RHO, Q = 1.0,2.0,0.5,100.0

# 城市数，蚁群
city_num, ant_num = 50,50


distance_x = [
    178,272,176,171,650,499,267,703,408,437,491,74,532,
    416,626,42,271,359,163,508,229,576,147,560,35,714,
    757,517,64,314,675,690,391,628,87,240,705,699,258,
    428,614,36,360,482,666,597,209,201,492,294]

distance_y = [
    170,395,198,151,242,556,57,401,305,421,267,105,525,
    381,244,330,395,169,141,380,153,442,528,329,232,48,
    498,265,380,120,165,50,433,63,491,275,348,222,288,
    490,213,524,244,114,104,552,70,425,227,331]


#城市距离和信息素
distance_graph = [ [0.0 for col in range(city_num)] for raw in range(city_num)]

pheromone_graph = [ [1.0 for col in range(city_num)] for raw in range(city_num)]
 
 
 
#----------- 蚂蚁 -----------
class Ant(object):
 
    # 初始化
    def __init__(self,ID):
        
        self.ID = ID
        self.path = []               # 当前蚂蚁的路径           
        self.total_distance = 1e9    # 当前路径的总距离
        self.move_count = 0          # 移动次数
        self.current_city = -1       # 当前停留的城市
        self.open_table_city = [False for i in range(city_num)] # 探索城市的状态 T:去过，F：未去      
 
    # 初始数据
    def _clean_data(self):
        city_index = np.random.randint(0,city_num-1) # 随机初始出生点
        self.current_city = city_index
        self.path.append(city_index)
        self.open_table_city[city_index] = True
        self.move_count = 1
        self.total_distance = 0
    
    # 选择下一个城市
    def __choice_next_city(self):
        
        next_city = -1
        select_citys_prob = np.zeros((city_num),dtype=float)
 
        # 获取去下一个城市的概率
        for j in range(city_num):
            if not self.open_table_city[j]: # 如果这个城市没有去过
                # 计算概率：与信息素浓度成正比，与距离成反比
                Tij = pheromone_graph[self.current_city][j]
                nij = 1.0/distance_graph[self.current_city][j]
                select_citys_prob[j] = np.power(Tij,ALPHA) * np.power(nij,BETA)

        # 轮盘赌选择下一个城市

        select_citys_prob = np.nan_to_num(select_citys_prob)
        select_citys_prob = select_citys_prob/select_citys_prob.sum()
        next_city = np.random.choice(np.array(len(select_citys_prob)),p=select_citys_prob)

        # 返回下一个城市序号
        return next_city
    
    # 计算路径总距离
    def __cal_total_distance(self):
        
        temp_distance = 0.0
 
        for i in range(1, city_num):
            start, end = self.path[i], self.path[i-1]
            
            temp_distance += distance_graph[start][end]
 
        # 回路
        end = self.path[0]
        temp_distance += distance_graph[start][end]
        self.total_distance = temp_distance
        
    
    # 移动操作
    def __move(self, next_city):
        
        self.path.append(next_city)
        self.open_table_city[next_city] = True
        self.total_distance += distance_graph[self.current_city][next_city]
        self.move_count += 1
        # 更新信息素
        # 信息素增加
        pheromone_graph[self.current_city][next_city] += Q/distance_graph[self.current_city][next_city]
        pheromone_graph[next_city][self.current_city] += Q/distance_graph[self.current_city][next_city]
        # 信息素挥发
        for i in pheromone_graph:
            for j in i:
                j *= (1-RHO)
        self.current_city = next_city
        
    # 搜索路径
    def search_path(self):
 
        # 初始化数据
        self._clean_data()
 
        # 搜素路径，遍历完所有城市为止
        while len(self.path)<50:
            # 移动到下一个城市
            next_city =  self.__choice_next_city()
            self.__move(next_city)
 
        # 计算路径总长度
        self.__cal_total_distance()
 
#----------- TSP问题 -----------
        
class TSP(object):
 
    def __init__(self, n = city_num):

        # 计算城市之间的距离
        for i in range(city_num):
            for j in range(city_num):
                temp_distance = pow((distance_x[i] - distance_x[j]), 2) + pow((distance_y[i] - distance_y[j]), 2)
                temp_distance = pow(temp_distance, 0.5)
                distance_graph[i][j] =float(int(temp_distance + 0.5))

        # 初始信息素
        for i in range(city_num):
            for j in range(city_num):
                pheromone_graph[i][j] = 1.0
                
        self.ants = [Ant(ID) for ID in range(ant_num)]  # 初始蚁群
        for ant in self.ants:
            ant._clean_data()
        self.best_ant = Ant(-1)                         # 初始最优解
        self.iter = 100000                               # 初始化迭代次数 
        
    # 开始搜索
    def search_path(self):
        for i in range(self.iter):
            for ant in self.ants:
                ant.search_path()
                # 更新最优解
                if ant.total_distance < self.best_ant.total_distance:
                    self.best_ant = copy.deepcopy(ant)
                # 初始化每只蚂蚁
                ant._clean_data() 


tsp = TSP()

tsp.search_path()
print(tsp.best_ant.total_distance)
print(tsp.best_ant.path)
print(len(tsp.best_ant.path))
# 画图
plt.figure()
plt.scatter(distance_x,distance_y)
plt.title('')
x = np.array(distance_x)[tsp.best_ant.path]
y = np.array(distance_y)[tsp.best_ant.path]
plt.plot(x,y)
plt.title(f'best router totle distance is {tsp.best_ant.total_distance} \n6720230789 xiale')
plt.show()