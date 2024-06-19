import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
env = gym.make('CliffWalking-v0')

'''
class Sarsa:
    def __init__(self,ncol,nrow,epsilon,alpha,gamma,n_action=4) -> None:
        self.Q_table = np.zeros((nrow*ncol,n_action)) # 上右下左
        self.epsilon = epsilon
        self.alpha = alpha 
        self.gamma = gamma
        self.n_action = n_action
    def take_action(self,state):
        if np.random.random() < self.epsilon:
            action = np.random.randint(self.n_action)
        else:
            action = np.argmax(self.Q_table[state])
        return action
    def update(self,s0,a0,r,s1,a1):
        td_error = r + self.gamma * self.Q_table[s1][a1] - self.Q_table[s0,a0]
        self.Q_table[s0][a0] += td_error * self.alpha    

ncol,nrow,epsilon,alpha,gamma,num_episodes,eposide = 12,4,0.1,.1,.1,500,0
np.random.seed(0)
agent = Sarsa(ncol,nrow,epsilon,alpha,gamma)
return_list = []  #记录每一条序列的回报
while eposide < num_episodes:
    done = False
    epsilon_return = 0
    s = env.reset()[0]
    a = agent.take_action(s)
    while not done:
        s1,r,done,truncated,_ = env.step(a)
        a1 = agent.take_action(s1)
        agent.update(s,a,r,s1,a1)
        s = s1
        a = a1
        epsilon_return+=r
        if done:
            print(f'{eposide}:{epsilon_return}')
        #env.render()
    return_list.append(epsilon_return)
    eposide+=1

#打印Q表格
direct = {
    0:'^',
    1:'>',
    2:'v',
    3:'<'
}
for i in range(nrow):
    for j in range(ncol):
        index = np.argmax(agent.Q_table[ncol*i+j])
        print(direct[index],end=' ')
    print()

#绘图
plt.plot(range(0,eposide),return_list)
plt.show()
np.save(f'Q_table_{num_episodes}',agent.Q_table)


'''

import gymnasium as gym
import numpy as np

# 使用训练好的策略游戏
env1 = gym.make('CliffWalking-v0',render_mode="human")
s = env1.reset()[0]
done = False
q_table = np.load("Q_table_5000.npy")
print(q_table)
while not done:
    a = np.argmax(q_table[s])
    s1,r,done,truncated,info = env1.step(a)
    s = s1
    env1.render()
