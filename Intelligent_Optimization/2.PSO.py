import numpy as np
import matplotlib.pyplot as plt

def object_function(x):
    return 10.0 * np.sin(5.0*x) + 7.0 * np.abs(x-5) + 10


def fitness_func(x): # 求最小值，值越小适应度越大，所有以函数值的相反数做为适应度
    return -1 * object_function(x)

def velocity_update(v, x, p_best, g_best, c1, c2,w, max_v):
    '''更新每个粒子的速度向量
    输入：
    v-当前粒子群体的速度向量矩阵
    x-当前粒子群体的位置向量矩阵
    p_best-每个粒子历史最优的位置向量矩阵
    g_best-历史最优的粒子位置向量
    c1,c2-“自我认知”和“社会认知”系数
    w 惯性系数
    max_val-限制粒子的最大速度
    输出：
    更新后的粒子群体速度向量矩阵
    '''
    size = x.shape[0]   # 获取粒子个数
    r1 = np.random.random(size=size)
    r2 = np.random.random(size=size)
    v_update = w*v + c1*r1*(p_best-x) + c2*r2*(g_best-x)
    #检测并修改超出自变量取值范围的值

    v_update[v_update<-max_v] = -1*max_v
    v_update[v_update>max_v] = max_v
    return v_update

def position_update(x,v):

    '''更新粒子群体的位置矩阵'''

    return x + v

#粒子群算法主函数
def pso_solver():
    '''粒子群算法求解主函数'''
    #parameters
    wi,we = 0.9,0.4  # 初始惯性权重和最终惯性权重
    c1,c2 = 2,2     # 学习因子
    size = 2000       #种群大小
    iter_num = 10000     #算法迭代最大次数
    max_v = 0.5       #限制粒子的最大速度为0.5
    fitness_value_list = []     #记录搜索过程中全体最优适应度的变化
    X_MIN, X_MAX = -10, 10  # x的取值范围
    #PSO算法迭代过程

    x = np.random.uniform(low=X_MIN,high=X_MAX,size=size)   # 初始化种群位置

    v = np.random.uniform(low=-max_v,high=max_v,size=size) # 初始化粒子速度
    #每个粒子的历史局部最优 p_best
    p_best = x
    p_fitness = fitness_func(p_best)
    #全局历史最优 g_best 
    g_fitness = max(p_fitness)
    loc = p_fitness.argmax()
    g_best = x[loc] 
    fitness_value_list.append(g_fitness)

    #迭代
    for i in range(0,iter_num):
        w = (wi-we)*(iter_num-i-1)/iter_num + we
        v = velocity_update(v,x,p_best,g_best,c1,c2,w,max_v)
        x = position_update(x,v)
        p_fitness_current = fitness_func(x) # 当前粒子的适应度
        g_fitness_current = p_fitness_current.max() #这一代粒子的最优适应度
        g_best_current = x[p_fitness_current.argmax()] #这一代粒子的最优位置
        #更新每个粒子的历史最优位置
        p_fitness = np.maximum(p_fitness,p_fitness_current)
        #更新种群历史最优位置
        if g_fitness > g_fitness_current:
            g_fitness = g_fitness_current
            g_best = g_best_current

            # 记录最优值的改变
        fitness_value_list.append(g_fitness)
        i += 1
    #返回历史最优值变化列表和最优值对应粒子位置向量列表
    return fitness_value_list,g_best,X_MIN,X_MAX


fitness_value_list,best_x,X_MIN,X_MAX= pso_solver()
best_y = object_function(best_x)

print(f"Best solution: x = {best_x}, f(x) = {best_y}")
x = np.linspace(X_MIN,X_MAX, 400)
y = object_function(x)

plt.figure()
plt.subplot(1,2,1)
plt.title('6720230789 xiale')
plt.plot(x, y, label='f(x) = 10sin(5x) + 7|x-5|')
plt.scatter(best_x,best_y,s=35,c='red',alpha=.7,label='best solution')
plt.legend(loc='best')
plt.subplot(1,2,2)
plt.plot(range(len(fitness_value_list)),fitness_value_list)
plt.xlabel('item_num')
plt.ylabel('g_fitness')
plt.show()


 