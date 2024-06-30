from sko.GA import GA
from sko.DE import DE
from sko.PSO import PSO
from ACO import ACO
import matplotlib.pyplot as plt
import numpy as np
from cec2019comp100digit import cec2019comp100digit as F
dim = [9,16,18,10,10,10,10,10,10,10]

lb = [-8192,-16384,-4,-100,-100,-100,-100,-100,-100,-100]
ub = [8192,16384,4,100,100,100,100,100,100,100]






#pso = PSO(func=demo_func, n_dim=3, pop=40, max_iter=150, lb=[0, -1, 0.5], ub=[1, 1, 1], w=0.8, c1=0.5, c2=0.5)
for i in range(2,3): #10个测试函数
    plt.figure()
    bench = F
    bench.init(i+1,dim[i])
    func = lambda x: bench.eval(x)
    #定义若干种算法
    ga = GA(func=func, n_dim=dim[i], size_pop=100, max_iter=250, prob_mut=0.001,lb=[lb[i] for _ in range(dim[i])], ub=[ub[i] for _ in range(dim[i])])
    de = DE(func=func, n_dim=dim[i], size_pop=100, max_iter=250, prob_mut=0.001,lb=[lb[i] for _ in range(dim[i])], ub=[ub[i] for _ in range(dim[i])])
    pso = PSO(func=func, n_dim=dim[i], pop=100, max_iter=250, lb=[lb[i] for _ in range(dim[i])], ub=[ub[i] for _ in range(dim[i])], w=0.8, c1=0.5, c2=0.5)
    aco = ACO([2500,100,[lb[i] for _ in range(dim[i])],[ub[i] for _ in range(dim[i])]],func)
    ga_best_x,ga_best_y = ga.run()
    de_best_x,de_best_y = de.run()
    pso.run()
    print(f'=====func{i+1}=====')
    print(f'ga_best_y={ga_best_y}')
    print(f'de_best_y={de_best_y}')
    print(f'pso_best_y={pso.gbest_y}')
    bench.end()
    h_ga = ga.all_history_Y
    h_de = de.all_history_Y
    h_pso = pso.gbest_y_hist
    plt.plot(range(len(h_ga)),[i.min() for i in h_ga ],c ='red',label='ga')
    plt.plot(range(len(h_de)),[i.min() for i in h_de ],c='blue',label='de')
    plt.plot(h_pso,c='yellow',label='pso')
    plt.legend(loc='best')
    plt.show()
    aco.main()



'''
#bench.init(3, 18) # Init function 3
lb= [-4 for _ in range(18)]
ub= [4 for _ in range(18)]
ans = 0
def demo_func(x):
    global ans
    ans +=1
    return bench.eval(x)
de = DE(func=demo_func, n_dim=18, size_pop=100, max_iter=500, prob_mut=0.001,
        lb=lb, ub=ub,)
best_x, best_y = de.run()
print('best_x:', best_x, '\n', 'best_y:', best_y)
h = de.all_history_Y
bench.end()
print(ans)
plt.plot(range(len(h)),[i.min() for i in h ])

plt.show()
'''