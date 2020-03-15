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

import julia_image_generator as jig

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

###################################
### End of function definitions ###
###################################
start_time = time.time()

#1080p resolution
resolution = (1080, 1920)

#set the limits in x and y
xlims = [-2.2, 1.2]
ylims = [-1.2, 1.2]

#set up the class so we can tune parameters being used if we so wish
calcer = explosionCalculator()

#generate our image
plane = jig.generate_image(resolution, [xlims, ylims], explosion_function=calcer.calc_explosion)

#set the limits of the image
extent = xlims + ylims

#generate the image
plt.figure()
plt.imshow(plane, extent=extent, cmap='hot')

plt.show()

print("TOOK {0}s".format(time.time() - start_time))
        



