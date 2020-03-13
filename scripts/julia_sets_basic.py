#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:28:09 2020

@author: stuart
"""

#julia sets code testing

import time
import numpy as np

import matplotlib.pyplot as plt

plt.close('all')

#here is an explosion calculator for a simple power julia set
class explosionCalculator(object):

    def __init__(self):
        
        self.powerLevel = 2
        self.order = 15
        self.rad = 2
    
    #the function for calculating the explosion needs to take in a complex number
    #as its input
    def calc_explosion(self, C):
        
        z0 = 0
        
        for i in range(self.order):
            
            z0 = z0**self.powerLevel + C
            
            if abs(z0) > self.rad:
                #need to return a status and a value
                return True, abs(z0)
        
        #need to return a status and a value
        return False, 0

#this is the function for generating the images
def generate_image(resolution, lims, explosion_function):
    
    [xlims, ylims] = lims
    
    plane = np.zeros(resolution)
    
    xstep = (xlims[1] - xlims[0])/resolution[1]
    ystep = (ylims[1] - ylims[0])/resolution[0]
    
    #find the values of all the points
    xpoints = [(xi * xstep) + xlims[0] for xi in range(resolution[1]+1)]
    ypoints = [(yi * ystep) + ylims[0] for yi in range(resolution[0]+1)]
    
    for yi, ys in enumerate(plane):
        
        #print(len(xs))
        
        for xi, xs in enumerate(ys):
            
            #find x and y
            x = xpoints[xi]
            y = ypoints[yi]
        
            #convert x and y to a point in the complex plane
            c = complex(x, y)
            
            #calculate the rate of explosion this function can be swapped out if you want
            result = explosion_function(c)
            
            #check if its exploded, if not leave it as zero
            if result[0]:
                
                plane[yi, xi] = result[1]
    
    return plane

    

###################################
### End of function definitions ###
###################################
start_time = time.time()

r = 2

#1080p resolution
resolution = (1080, 1920)

xlims = [-2.2, 1.2]
ylims = [-1.2, 1.2]

calcer = explosionCalculator()

plane = generate_image(resolution, [xlims, ylims], explosion_function=calcer.calc_explosion)

extent = xlims + ylims
plt.figure()
plt.imshow(plane, extent=extent, cmap='hot')
#plt.imshow(plane, cmap='hot')
           #cmap='copper')
plt.show()

print("TOOK {0}s".format(time.time() - start_time))
        



