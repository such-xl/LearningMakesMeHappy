import numpy as np
import matplotlib.pyplot as plt
class Population:
    def __init__(self, MIN_X, MAX_X, dim, factor, rounds, size, object_func, CR=0.75):
        self.MIN_X = MIN_X
        self.MAX_X = MAX_X
        self.dimension = dim
        self.factor = factor # 缩放因子
        self.rounds = rounds
        self.size = size
        self.cur_round = 0
        self.CR = CR
        self.object_func = object_func
        # 初始化种群
        self.individuality = np.random.uniform(low=MIN_X,high=MAX_X,size=size)

        self.fitness = self.fitness_func(self.individuality)
        self.mutant = None
        self.best_x = 0.0
        self.best_y = 0.0
        self.best_fitness_record = []
    def fitness_func(self,x):
        """"由于是求最大值，所有用函数值对应适应度"""
        return self.object_func(self.individuality)
    
    def mutate(self):
        mutant = []
        for i in range(self.size):
            r  = np.array([0,0,0])
            while r.shape[0] != len(set(r)):
                r = np.random.randint(low=0,high=self.size,size=3)
            
            tmp = self.individuality[r[0]] + (self.individuality[r[1]] - self.individuality[r[2]]) * self.factor
            if tmp>self.MAX_X:
                tmp = self.MAX_X
            if tmp<self.MIN_X:
                tmp = self.MIN_X
            mutant.append(tmp)
        self.mutant = np.array(mutant)
 
    def crossover(self):
        """一元函数，简化交叉"""
        l = np.random.uniform(0,1,self.size)
        next_individuality = self.individuality * l + self.mutant*(1-l)
        return next_individuality
    def select(self,next_individuality):
        # 合并两个数组
        new_individuality = np.append(next_individuality,self.individuality)
        fitness = self.object_func(new_individuality)
        idx = np.argsort(fitness)[::-1][0:self.size]
        self.individuality = new_individuality[idx]
        self.fitness = self.fitness_func(self.individuality)


    def print_best(self):
        idx = np.argmax(self.fitness)
        self.best_x = self.individuality[idx]
        self.best_y = self.object_func(self.best_x)
        print("轮数：" + str(self.cur_round))
        print("最佳个体：" ,self.best_x)
        print("目标函数值：",self.best_y)
    def draw(self):
        x = np.linspace(self.MIN_X,self.MAX_X, 4000)
        y = self.object_func(x)
        plt.figure()
        plt.subplot(1,2,1)
        plt.plot(x, y, label='f(x) = x sin(10πx) + 1')
        
        plt.title('6720230789   xiale')
        plt.scatter(self.best_x,self.best_y,s=35,c='red',alpha=.7,label='best solution')
        plt.legend(loc='best')
        plt.subplot(1,2,2)
        plt.plot(range(self.rounds),self.best_fitness_record)
        plt.xlabel('generations')
        plt.ylabel('best_fitness')
        plt.show()      
    def evolution(self):
        while self.cur_round < self.rounds:
            self.mutate()
            next_individuality =  self.crossover()
            self.select(next_individuality)
            self.print_best()
            self.cur_round = self.cur_round + 1
            self.best_fitness_record.append(np.max(self.fitness))

def f(x):
    return x * np.sin(10 * np.pi * x) + 1


p = Population(MIN_X=-2,MAX_X=4,dim=1,factor=0.8,rounds=100,size=20,object_func=f)
p.evolution()
p.draw()