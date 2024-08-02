import numpy as np
import matplotlib.pyplot as plt
record_ga=np.load('record_ga.npy')
record_de=np.load('record_de.npy')
record_pso=np.load('record_pso.npy')
record_aco=np.load('record_aco.npy')
record_rcga=np.load('record_rcga.npy')

def remove_outliers(arr):
    masks = []
    for data in arr:
        Q1 = np.percentile(data, 25, axis=0)
        Q3 = np.percentile(data, 75, axis=0)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        # 生成一个布尔数组，标志每个位置是否为离群点
        mask = (data >= lower_bound) & (data <= upper_bound)
        masks.append(mask)
        # 只保留非离群点的数据
    cleaned_data = np.where(masks,arr,np.nan)
    return cleaned_data

record_ga = remove_outliers(record_ga)
record_de = remove_outliers(record_de)
record_pso = remove_outliers(record_pso)
record_aco = remove_outliers(record_aco)
record_rcga = remove_outliers(record_rcga)
for i in range(10):
    plt.figure(num=i+1)
    ga = np.nanmean(record_ga[i],axis=0)
    de = np.nanmean(record_de[i],axis=0)
    pso = np.nanmean(record_pso[i],axis=0)
    aco = np.nanmean(record_aco[i],axis=0)
    rcga = np.nanmean(record_rcga[i],axis=0)
    plt.plot(ga,c='#8ECFC9',label='GA')
    plt.plot(de,c='#FFBE7A',label='DE')
    plt.plot(pso,c='#FF8884',label='PSO')
    plt.plot(aco,c='#BEB8DC',label='ACO')
    plt.plot(rcga,c='#C82423',label='RCGA')
    plt.title(f'TEST FUNCTION{i+1}')
    plt.legend(loc='best')
    plt.savefig(f'imgs/fun{i+1}.png')
