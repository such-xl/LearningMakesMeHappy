import numpy as np
import matplotlib.pyplot as plt

# 目标函数，这里以二维空间的某个函数为例
def objective_function(x):
    return 10.0 * np.sin(5.0*x) + 7.0 * np.abs(x-5) + 10
def metrospolis(current_eval,next_eval,temp):
    #求最小值
    if next_eval<=current_eval:
        return True
    else:
        p = np.exp((current_eval-next_eval)/temp)
        if np.random.random()<=p:
            return True
        return False
# 模拟退火算法主体函数
def simulated_annealing(objective, bounds, max_iterations, initial_temp,end_temp, cooling_rate):
    """
        objective: 函数
        bounds : x的取值范围
        max_iterations: 最大迭代次数
        initial_temp: 初始温度
        cooling_rate: 冷却速率
    """
    current_x = np.random.uniform(bounds[0], bounds[1]) # 随机生成一个x

    current_eval = objective(current_x) # 计算当前函数值，即能量

    best_x = current_x   # 记录最优解x

    best_eval = current_eval    #记录最优能量值 

    temp = initial_temp # 温度变量

    evaluations = [current_eval]   # 记录能量变化 
    temperatures = [temp]          # 记录温度变化
    positions = [current_x]        # 记录x的位置变化

    while np.abs(temp-end_temp) > 1e-2:
        for i in range(max_iterations):
            # 在当前解的邻域内随机选择一个新解。邻域可以通过定义一些小的扰动来确定
            next_x = current_x + np.random.uniform(-0.1, 0.1) * (bounds[1] - bounds[0])
            # 确保生成的解在定义域内
            next_x = max(bounds[0], min(next_x, bounds[1]))
            next_eval = objective(next_x)

            if metrospolis(current_eval,next_eval,temp):
                current_x,current_eval = next_x,next_eval

            if next_eval < best_eval:
                best_x, best_eval = next_x, next_eval

        evaluations.append(current_eval)
        positions.append(current_x)
        temp *= cooling_rate
        temperatures.append(temp)
    return best_x, best_eval, evaluations, temperatures, positions

# 设置参数
max_iterations = 50
initial_temp = 10
cooling_rate = 0.8
bounds = [-5, 10]
end_temp = 0
# 执行模拟退火算法
best_x, best_eval, evaluations, temperatures, positions = simulated_annealing(
    objective_function, bounds, max_iterations, initial_temp,end_temp, cooling_rate)

# 打印结果
print('最优解: x=%.3f, f(x)=%.3f' % (best_x, best_eval))

# 绘图展示
plt.figure()
plt.subplot(311)
plt.title('temperatures')
plt.plot(temperatures)

plt.subplot(312)
plt.title('6720230789   xiale')
x = np.linspace(bounds[0],bounds[1],4000)
y = objective_function(x)
plt.scatter(best_x,best_eval,s=35,c='red',alpha=.7,label='best solution')
plt.plot(x, y, label='f(x) = 10sin(5x) + 7|x-5|')
plt.legend(loc='best')
plt.subplot(313)
plt.title('x_position')
plt.plot(positions)
plt.tight_layout()
plt.show()