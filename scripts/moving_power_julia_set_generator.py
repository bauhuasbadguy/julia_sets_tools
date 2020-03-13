#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 00:00:10 2020

@author: stuart
"""

#moving julia set generator
import time
import matplotlib.pyplot as plt

from PIL import Image

import julia_image_generator as jig


#here is an explosion calculator for a simple power julia set
class powerExplosionCalculator(object):

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


    
calcer = powerExplosionCalculator()

start_time = time.time()


resolution = (1080, 1920)

xlim = [-2.0, 2.0]
ylim = [-1.2, 1.2]

extent = xlim + ylim

lims = [xlim, ylim]

plane = jig.generate_image(resolution, lims, calcer.calc_explosion)


plt.figure(figsize=(1080/100, 1920/100), dpi=100)
plt.imshow(plane, extent=extent, cmap='hot')
plt.axis('off')

frameNo = '0'

plt.savefig('{0}.png'.format(frameNo), bbox_inches='tight', pad_inches=0)
#plt.imshow(plane, cmap='hot')
           #cmap='copper')
plt.close('all')
#plt.show()

print("TOOK {0}s".format(time.time() - start_time))
        