# 人生苦短，我学Python
# 2021年10月14日
# -*- coding:utf-8 -*-
# coding:unicode_escape
# 编程练习
# 码字员：爱里斑的半角宽
# 开发时间： 2021/12/4 15:53

import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.pylab import mpl
import time

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
mpl.rcParams['axes.unicode_minus'] = False  # 负号显示

time_start = time.time()
# 设置初始值
k0 = 100.0   # 频率因子
E = 1e5      # 活化能
R = 8.314    # 气体常数
C = 1.0      # 可燃混合物中反应物浓度，这个值待会儿要改为C(tao)
n = 1.0      # 反应级数
V = 1.0      # 容器体积
Q = 2e7      # 可燃混合物的燃烧热
tao = np.arange(0, 1000, 0.01)  # 时间定义域
T = np.zeros(len(tao))  # 容器壁温度值域
T[0] = 1100   # 容器壁初始温度
eta = 5.0    # 散热系数
S = 6.0      # 容器壁散热面积
rho = 1.0    # 密度（话说为什么等于1啊）
cv = 1000    # 定容比热容


# 绘图框准备好
fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

# 开始求解常微分方程
# 只改变初始温度
for T[0]  in [300, 500, 800, 820, 840, 860, 880, 900, 1000, 1100]:
    T1 = np.zeros(len(tao))
    T1[0] = T[0]
    i = 0
    while (i + 1 < len(tao) and T1[i] <= 3000):
        T1[i + 1] = T1[i] + (tao[i + 1] - tao[i]) * (
                    k0 * math.exp(-E / (R * T1[i])) * C ** n * V * Q - eta * S * (T1[i] - T1[0])) / (V * rho * cv)
        i += 1
    tao1 = tao[0:i+1]
    T1 = T1[0:i+1]
    ax1.plot(tao1, T1)

# 只改变eta
for eta  in [1, 5, 9, 4.2, 4.4, 4.6, 4.8]:
    T2 = np.zeros(len(tao))
    T2[0] = T[0]
    i = 0
    while (i + 1 < len(tao) and T2[i] <= 3000):
        T2[i + 1] = T2[i] + (tao[i + 1] - tao[i]) * (
                    k0 * math.exp(-E / (R * T2[i])) * C ** n * V * Q - eta * S * (T2[i] - T2[0])) / (V * rho * cv)
        i += 1
    tao2 = tao[0:i+1]
    T2 = T2[0:i + 1]
    ax2.plot(tao2, T2)


# 添加图例等装饰
ax1.legend(['300', '500', '800', '820', '840', '860', '880', '900', '1000', '1100'],
           loc='upper right', facecolor='white', frameon=True, shadow=False, framealpha=0.5, prop={'size': 8})
ax2.legend(['1', '5', '9', '4.2', '4.4', '4.6', '10'],
           loc='upper left', facecolor='white', frameon=True, shadow=False, framealpha=0.5, prop={'size': 8})
ax1.grid()
ax2.grid()

time_end = time.time()
print('计算结束，用时：%f' % (time_end - time_start))

plt.show()