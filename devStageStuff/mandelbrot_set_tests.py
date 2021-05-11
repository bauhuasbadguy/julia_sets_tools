#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:28:09 2020

@author: stuart
"""

#julia sets code testing

import time
import math
import numpy as np

import matplotlib.pyplot as plt

plt.close('all')

import julia_image_generator as jig

#here is an explosion calculator for a simple power julia set
class explosionCalculator(object):

    def __init__(self):
        
        self.powerLevel = 2
        self.order = 200
        self.rad = 3
    
    #the function for calculating the explosion needs to take in a complex number
    #as its input
    def calc_explosion(self, C):
        
        z0 = 0
        
        for i in range(self.order):
            
            z0 = z0**self.powerLevel + C
            
            if abs(z0) > self.rad:
                #need to return a status and a value
                return True, i
        
        #need to return a status and a value
        return False, self.order

###################################
### End of function definitions ###
###################################

start_time = time.time()

#1080p resolution
resolution = (1080, 1920)

#increase to check plotting isnt fucking up
resolution = tuple([i*2 for i in resolution])

#set the limits in x and y
xlims = [-2.2, 1.2]
ylims = [-1.2, 1.2]

#set up the class so we can tune parameters being used if we so wish
calcer = explosionCalculator()

#generate our image
plane = jig.generate_image(resolution, [xlims, ylims], explosion_function=calcer.calc_explosion, stableZero = True)

#set the limits of the image
extent = xlims + ylims

#generate the image
plt.figure(figsize=(16, 14))
plt.imshow(plane, extent=extent, cmap='hot', interpolation='spline16')
plt.axis('off')
#plt.colorbar()

#plt.savefig('./mandelbrot_hot_noAxis_spline16__res.png', bbox_inches='tight')

plt.imsave('mandelbrot_bone_noAxis_high_res_test.png', plane, cmap='viridis')

#hot is the red colourmap
#viridis is the blue colourmap
#Greens_r is the green colourmap
#bone is the nice black and white colourmap

plt.show()

print("TOOK {0}s".format(time.time() - start_time)
      