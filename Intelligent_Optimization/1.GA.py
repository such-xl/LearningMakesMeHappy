import numpy as np
import matplotlib.pyplot as plt
# 目标函数
def objective_function(x):
    return x * np.sin(10 * np.pi * x) + 1
# 初始化
def initialize_population(size, x_min, x_max):
    return np.random.rand(size) * (x_max - x_min) + x_min # 生成[x_min,x_max]之间的浮点数

# 适应度函数
def fitness(population):
    fit = objective_function(population)
    return  fit - np.min(fit) + 0.01 #将适应度归到正数，用于轮盘赌选择

# 选择
def select(population, fitnesses, num_parents):
    # 轮盘赌选择或者可以用别的选择算法
    indexes = np.random.choice(len(population), size=num_parents, replace=True, p=fitnesses/fitnesses.sum())
    return population[indexes]


# 交叉
def crossover(parents, num_offsprings):
    offsprings = np.empty(num_offsprings)
    for k in range(num_offsprings):
        parent1_idx = np.random.randint(0, parents.shape[0])
        parent2_idx = np.random.randint(0, parents.shape[0])
        crossover_point = np.random.rand()
        offsprings[k] = crossover_point * parents[parent1_idx] + (1 - crossover_point) * parents[parent2_idx]
    return offsprings

# 变异
def mutate(offsprings, mutation_rate, x_min, x_max):
    for idx in range(len(offsprings)):
        if np.random.rand() < mutation_rate:
            random_value = offsprings[idx] + np.random.rand() * 2 - 1
            if random_value<x_min:
                random_value = x_min
            if random_value>x_max:
                random_value = x_max
            offsprings[idx] = random_value
    return offsprings

# 算法参数
population_size = 100
num_generations = 10000
x_min = -1
x_max = 2
num_parents = 50
num_offsprings = population_size - num_parents
mutation_rate = 0.01

# 初始化种群
population = initialize_population(population_size, x_min, x_max)
best_y_list = []

# 运行遗传算法
for _ in range(num_generations):
    fit = fitness(population)
    parents = select(population, fit, num_parents)
    offsprings = crossover(parents, num_offsprings)
    offsprings = mutate(offsprings, mutation_rate, x_min, x_max)
    population[:num_parents] = parents
    population[num_parents:] = offsprings
    b_i = np.argmax(fitness(population))
    b_x = population[b_i]
    best_y_list.append(objective_function(b_x))

# 结果
best_index = np.argmax(fitness(population))
best_x = population[best_index]
best_y = objective_function(best_x)
print(f"Best solution: x = {best_x}, f(x) = {best_y}")
x = np.linspace(x_min, x_max, 400)
y = objective_function(x)
plt.figure()
plt.subplot(1,2,1)
plt.title('6720230789   xiale')
plt.plot(x, y, label='f(x) = x sin(10πx) + 1')
plt.scatter(best_x,best_y,s=35,c='red',alpha=.7,label='best solution')
plt.legend(loc='best')
plt.subplot(1,2,2)
plt.plot(range(num_generations),best_y_list)
plt.xlabel('generations')
plt.ylabel('best_y')
plt.show()