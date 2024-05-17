import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(-1,1,50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x,y1,label='up')
plt.plot(x,y2,color='red',linewidth=1.0,linestyle='--',label='down')
plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am x')
plt.ylabel('I am y')
new_ticks = np.linspace(-2, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none') # spines 四边框
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data', 0)) # 将x轴移到y轴的0号位置
ax.spines['left'].set_position(('data', 0))

# Annotation标注
x0 = .25
y0 = 2*x0 + 1
plt.scatter(x0, y0, s=50, color='b')
plt.plot([x0, x0], [y0, 0], 'k--', lw=1.5)
# method 1
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
# method 2
plt.text(-2, 1, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$', fontdict={'size': 10, 'color': 'r'})

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))
#第二张图
# plt.figure()
# plt.plot(x, y2)

plt.legend(loc='best')
plt.show()