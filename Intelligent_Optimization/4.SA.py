import numpy as np
import matplotlib.pyplot as plt

# 目标函数，这里以二维空间的某个函数为例
def objective_function(x):
    return (1-x**2)**0.5

# 模拟退火算法主体函数
def simulated_annealing(objective, bounds, max_iterations, initial_temp, cooling_rate):
    current_x = np.random.uniform(bounds[0], bounds[1])
    current_eval = objective(current_x)
    best_x = current_x
    best_eval = current_eval
    temp = initial_temp

    evaluations = [current_eval]
    temperatures = [temp]
    positions = [current_x]

    for i in range(max_iterations):
        next_x = current_x + np.random.uniform(-0.1, 0.1) * (bounds[1] - bounds[0])
        next_x = max(bounds[0], min(next_x, bounds[1]))
        next_eval = objective(next_x)

        if next_eval < best_eval:
            best_x, best_eval = next_x, next_eval

        delta_eval = next_eval - current_eval
        if delta_eval < 0 or np.random.rand() < np.exp(-delta_eval / temp):
            current_x, current_eval = next_x, next_eval

        evaluations.append(current_eval)
        positions.append(current_x)
        temperatures.append(temp)
        temp *= cooling_rate

    return best_x, best_eval, evaluations, temperatures, positions

# 设置参数
max_iterations = 1000
initial_temp = 10
cooling_rate = 0.99
bounds = [-10, 10]

# 执行模拟退火算法
best_x, best_eval, evaluations, temperatures, positions = simulated_annealing(
    objective_function, bounds, max_iterations, initial_temp, cooling_rate)

# 打印结果
print('最优解: x=%.3f, f(x)=%.3f' % (best_x, best_eval))

# 绘图展示
plt.figure()
plt.subplot(311)
plt.title('Objective Function Value')
plt.plot(evaluations)

plt.subplot(312)
plt.title('Temperature')
plt.plot(temperatures)

plt.subplot(313)
plt.title('Position')
plt.plot(positions)

plt.tight_layout()
plt.show()