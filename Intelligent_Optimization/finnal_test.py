from sko.GA import GA,RCGA
from sko.DE import DE
from sko.PSO import PSO
from ACO import ACO
import matplotlib.pyplot as plt
import numpy as np
from cec2019comp100digit import cec2019comp100digit as F
#十个测试函数的维度和上下限
dim = [9,16,18,10,10,10,10,10,10,10]

lb = [-8192,-16384,-4,-100,-100,-100,-100,-100,-100,-100]
ub = [8192,16384,4,100,100,100,100,100,100,100]
'''
（3）停止准则：运行完nf=20000次函数值计算次数；
（4）每个测试问题独立测试nr=30次，以避免随机扰动；
（5）用一个nf*nr*np的三维向量存储测试结果，其中np表示测试函数的个数；
'''

#pso = PSO(func=demo_func, n_dim=3, pop=40, max_iter=150, lb=[0, -1, 0.5], ub=[1, 1, 1], w=0.8, c1=0.5, c2=0.5)
"""
for i in range(2,3): #10个测试函数
    plt.figure()
    bench = F
    bench.init(i+1,dim[i])
    #func = lambda x: bench.eval(x)
    def func(x):
        print('sss')
        return bench.eval(x)
    #定义若干种算法
    ga = GA(func=func, n_dim=dim[i], size_pop=100, max_iter=250, prob_mut=0.001,lb=[lb[i] for _ in range(dim[i])], ub=[ub[i] for _ in range(dim[i])])
    de = DE(func=func, n_dim=dim[i], size_pop=100, max_iter=250, prob_mut=0.001,lb=[lb[i] for _ in range(dim[i])], ub=[ub[i] for _ in range(dim[i])])
    pso = PSO(func=func, n_dim=dim[i], pop=100, max_iter=250, lb=[lb[i] for _ in range(dim[i])], ub=[ub[i] for _ in range(dim[i])], w=0.8, c1=0.5, c2=0.5)
    aco = ACO([2500,100,[lb[i] for _ in range(dim[i])],[ub[i] for _ in range(dim[i])]],func,)
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
"""
record_ga = []
record_de = []
record_pso = []
record_aco = []
record_rcga = []
count = 0
best_y = 1e19 # 储存当前的最优解
nf = 20000
temp_record = [] #记录记录一个算法，一个测试函数的一次run结果
for i in range(10):#10个测试函数
    bench = F
    bench.init(i+1,dim[i])
    r_i = []
    #func = lambda x: bench.eval(x)
    print(f'function{i+1}')
    def func(x):
        global count,nf,best_y,temp_record
        y = bench.eval(x)
        if y<best_y:
            best_y = y
        if count<nf:
            temp_record.append(best_y) 
        count += 1
        return y

    for j in range(5): # 5个算法
            r_j = []
            for k in range(30): #每个算法测试30次
                agent = None
                #初始化智能体，懒得写reset()
                if j==0:
                    agent = GA(func=func, n_dim=dim[i], size_pop=100, max_iter=nf//100, prob_mut=0.001,lb=[lb[i] for _ in range(dim[i])], ub=[ub[i] for _ in range(dim[i])])
                elif j==1:
                    agent = DE(func=func, n_dim=dim[i], size_pop=100, max_iter=nf//100, prob_mut=0.001,lb=[lb[i] for _ in range(dim[i])], ub=[ub[i] for _ in range(dim[i])])
                elif j==2:
                    agent = PSO(func=func, n_dim=dim[i], pop=100, max_iter=nf//100, lb=[lb[i] for _ in range(dim[i])], ub=[ub[i] for _ in range(dim[i])], w=0.8, c1=0.5, c2=0.5)
                elif j==3:
                    agent = ACO([nf//100,100,[lb[i] for _ in range(dim[i])],[ub[i] for _ in range(dim[i])]],func)
                elif j==4:
                    agent = RCGA(func=func, n_dim=dim[i], size_pop=100, max_iter=nf//100, prob_mut=0.001,lb=[lb[i] for _ in range(dim[i])], ub=[ub[i] for _ in range(dim[i])])
                agent.run()
                print(f'{j}==',best_y)
                best_y = 1e19
                count = 0
                r_j.append(temp_record)
                temp_record = []
            if j==0:
                record_ga.append(r_j)
            elif j==1:
                record_de.append(r_j)
            elif j==2:
                record_pso.append(r_j)
            elif j==3:
                record_aco.append(r_j)
            else:
                record_rcga.append(r_j)
record_ga = np.array(record_ga)
record_de = np.array(record_de)
record_pso = np.array(record_pso)
record_aco=np.array(record_aco)
record_rcga=np.array(record_rcga)
print(record_pso.shape)
print(record_de.shape)
print(record_ga.shape)
print(record_aco.shape)
print(record_rcga.shape)
np.save('record_ga.npy',record_ga)
np.save('record_de.npy',record_de)
np.save('record_pso.npy',record_pso)
np.save('record_aco.npy',record_aco)
np.save('record_rcga.npy',record_rcga)
