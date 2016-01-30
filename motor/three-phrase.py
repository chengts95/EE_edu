# -*- coding: UTF-8 -*-
'''
用于绘制三相电机磁动势合成图
@author: cts
'''


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


def zhubo(t, x):
    return np.sin(t) * np.sin(x)


# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))


def centerAx(ax):
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

centerAx(ax)
line, = ax.plot([], [], lw=2, color='red')
line2, = ax.plot([], [], lw=2, color='g')
line3, = ax.plot([], [], lw=2, color='y')
line4, = ax.plot([], [], lw=2, color='b')
x = np.linspace(0, 2, 1000)


# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    line4.set_data([], [])
    return [line, line2, line3, line4]

# animation function.  This is called sequentially
# note: i is framenumber


def threePhareMag(i):
    t = 2 * np.pi * x
    u = 0.1 * i
    f1 = zhubo(t, u)
    f2 = zhubo(t - (2 / 3) * np.pi, u - (2 / 3) * np.pi)
    f3 = zhubo(t + (2 / 3) * np.pi, u + (2 / 3) * np.pi)
    line.set_data(x, f1)
    line2.set_data(x, f2)
    line3.set_data(x, f3)
    line4.set_data(x, f1 + f2 + f3)
    return [line, line2, line3, line4]


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, threePhareMag, init_func=init,
                               frames=200, interval=50, blit=True)

#anim.save('my.gif',fps=15, writer='imagemagick')

plt.show()
