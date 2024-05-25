import matplotlib.pyplot as plt
import matplotlib.dates as mdates
class Drawer():
    def __init__(self,tasks,start_dates,end_dates,colors):
        self.tasks = tasks
        self.start_dates = start_dates
        self.end_dates = end_dates
        self.colors = colors
        self.fig, self.ax = plt.subplots(figsize=(10, 5))
        self.bars = []
    def darw(self):
        for i, task in enumerate(self.tasks):
            start = self.start_dates[i]
            end = self.end_dates[i]
            # 使用bars来表示任务的时间范围
            bar = self.ax.barh(task, end-start, left=start, color=self.colors[i])
            self.bars.append(bar)
        # 设置轴标签，标题和网格线
        self.ax.set_xlabel('time_step')
        self.ax.set_ylabel('任务')
        self.ax.set_title('甘特图示例')
        self.ax.grid(True)
        # 显示图表
        for bar in self.bars:
            print(bar.__str__())
        plt.tight_layout()
        plt.show()
    def update(self,task,start_date,end_date):
        self.bars[0][0].set_x(start_date)
        plt.draw()
        plt.show()

# 定义任务名称
tasks = ['任务1', '任务2', '任务3']

# 定义开始日期和结束日期
start_dates =   [0,3,7] 

end_dates = [4,5,9]
colors = ['tab:blue', 'tab:orange', 'tab:green']

d = Drawer(tasks, start_dates, end_dates, colors)
d.darw()
d.update(0, 2, 5)
plt.show()
