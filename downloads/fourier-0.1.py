#! -*- encoding: utf-8 -*-

#    Visualize the vibrations of a string using Fourier series.
#    Copyright (C) <2014>  <Francesco Pasa>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import division

import sys
from math import *
from scipy.integrate import quad
from scipy.interpolate import interp1d
from matplotlib import pyplot as plt
from matplotlib import animation
import itertools
import numpy as np
import random
import time

nframes = 300
M = 3
x0 = 7
L = 10
fmax = 15
v = 1
pcl = 0
randx = np.arange(11) 
randy = np.fromiter(itertools.chain([0], (np.random.rand(L-1) - 0.5) * 2*M, [0]), int, 11)

def parabola(x):
    return -0.1*x**2 + 0.1*L*x

def pizzico(x):
    if x < x0:
        return x / x0 * M
    else:
        return (L - x) / (L - x0) * M

rand = interp1d(randx, randy, kind='cubic')

# INSERIRE FUNZIONE CHE SI VUOLE DENTRO A VECTORIZE (parabola, pizzico o rand)
f = np.vectorize(pizzico)

def rebalta(f, x):
    if x >= 0:
        return f(x)
    else:
        return -f(-x)

# fourier
bs = []
for n in range(1, fmax+1):
    k = pi/L*n
    b = quad(lambda x: rebalta(f, x)*sin(k*x), -L, L)[0] / L
    bs.append(b)


def f1(x, t):
    s = []
    
    for n in range(1, fmax+1):
        k = pi/L*n
        w = v*pi*n/L
        s.append(bs[n-1]*sin(k*x)*cos(w*t))
    
    return sum(s)

f1 = np.vectorize(f1)

xs = np.arange(0, L*1.01, L/100)
fig = plt.figure()
plt.plot(xs, f(xs))
line, = plt.plot(xs, f1(xs, 0))
plt.axes().set_ylim((-5, 5))
plt.axes().grid(True)

# animation function. This is called sequentially
def animate(i):
    global pcl
    
    sys.stdout.write("\b" * pcl + "{:.1f} %".format(float(i)/nframes*100))
    sys.stdout.flush()
    if i == 0:
        pcl = 6
    else:
        pcl = 5 + int(ceil(log10(float(i)/nframes*100)))
    
    line.set_data(xs, f1(xs, i*0.1))
    return line,

# call the animator. blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, frames=nframes, interval=20)

anim.save('fourier.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()