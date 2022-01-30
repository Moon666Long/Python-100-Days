# 人生苦短，我学Python
# 2021年10月14日
'''import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import bytespdate2num
fig=plt.figure()
#ax=fig.add_subplot(1,1,1)
#def plotdemo1():
#ax.plot([1,2,3,4],[2,3,4,5])
#ax.set_xlabel("time/s")
dates,close = np.loadtxt('日期.csv',delimiter=',', unpack= True, converters={0:mdates.bytespdate2num('%Y-%m-%d')})
ax1=fig.add_subplot(1,1,1)
ax1.plot(dates,close)
plt.show()'''
import matplotlib.pyplot as plt

import numpy as np

import matplotlib.dates as mdates

from matplotlib.dates import bytespdate2num

import pandas as pd


def PlotDemo1():
    fig = plt.figure()

    fig.suptitle('figure title demo', fontsize=14, fontweight='bold')

    ax = fig.add_subplot(1, 1, 1)

    ax.set_title("axes title")

    ax.set_xlabel("x label")

    ax.set_ylabel("y label")

    dates, close = np.loadtxt('日期.csv', delimiter=",", usecols=(0, 1), unpack=True)

    ax.xaxis.set_major_locator(mdates.DayLocator(bymonthday=range(1, 32), interval=3))

    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

    plt.xticks(pd.date_range('2021-12-3', '2021-12-11', freq='3D'), rotation=45)

    ax.plot(dates, close)

    plt.show()


def getData():


    dates, close = np.loadtxt('日期.csv', delimiter=",", usecols=(0, 1), unpack=True)

    # dates = (2,3,4,55,66)

    print(dates)
    return dates,close
if __name__ == '__main__':

    PlotDemo1()