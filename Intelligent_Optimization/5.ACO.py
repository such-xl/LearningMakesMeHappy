import random
class Ant():
    def __init__(self,Q,R,num_city) -> None:
        self.Q = Q #信息素常量
        self.R = R #信息素挥发率
        self.router = [random.randint[0,num_city-1]]
    # 采样一个动作
    def sample(): 
       pass
    def is_done(self,num_city):
        return len(self.router) == num_city
