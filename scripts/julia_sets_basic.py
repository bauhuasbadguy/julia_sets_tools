#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:28:09 2020

@author: stuart
"""

#julia sets code testing


import numpy as np


import matplotlib.pyplot as plt

def calc_explosion(C, rad, order=10):
    
    z0 = 0
    
    for i in range(order):
        
        z0 = z0**2 + C
        
        if abs(z0) > rad:
            return True, abs(z0)
        
    return False, 0

###################################
### End of function definitions ###
###################################


'''
#compute z
z0 = complex(-1,-0.5)
C = 0

xs = []
zs = []
z = copy.deepcopy(z0)
for i in range(5):
    
    z = z**2 + C
    
    xs.append(i)
    zs.append(abs(z))
    
plt.figure()
plt.plot(xs, zs)
plt.xlabel('i')
plt.ylabel('z')
plt.show()
'''

r = 2

resolution = (200, 300)

xlims = [-2.5, 1.5]
ylims = [-1.5, 1.5]

plane = np.zeros(resolution)

#plane should go from -2->1 in the x axis and -1->1 in the y axis

#z = xi + y
C = 0


xstep = (xlims[1] - xlims[0])/resolution[1]
ystep = (ylims[1] - ylims[0])/resolution[0]

#xpoints = [x/100 for x in range(-200, 101)]
#ypoints = [y/100 for y in range(-100, 101)]
xpoints = [(xi * xstep) + xlims[0] for xi in range(resolution[1]+1)]
ypoints = [(yi * ystep) + ylims[0] for yi in range(resolution[0]+1)]

print(len(xpoints))
print(len(ypoints))

for yi, ys in enumerate(plane):
    
    #print(len(xs))
    
    for xi, xs in enumerate(ys):
        
        #print(xi, yi)
        
        x = xpoints[xi]
        
        y = ypoints[yi]
        
        #print(x, y)
        
        c = complex(x, y)
        
        #print(z0)
        
        result = calc_explosion(c, r, order=50)
        
        if result[0]:
            
            plane[yi, xi] = result[1]


extent = [xpoints[0], xpoints[-1], ypoints[0], ypoints[-1]]
plt.figure()
plt.imshow(plane, extent=extent, cmap='hot')
plt.imshow(plane, cmap='hot')
           #cmap='copper')
plt.show()
        



