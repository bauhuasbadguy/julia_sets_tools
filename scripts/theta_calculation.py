#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 23:32:30 2020

@author: stuart
"""

#the theta thing

#this script is for doing theta stuff

import os
import time
import math
import cmath

import numpy as np

import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

import matplotlib.pyplot as plt

plt.close('all')

from PIL import Image

import subprocess

import julia_image_generator as jig


#here is an explosion calculator for a simple power julia set
class thetaExplosionCalculator(object):

    def __init__(self):
        
        self.powerLevel = 2
        self.order = 25
        self.rad = 3
        self.theta = 0
    
    #the function for calculating the explosion needs to take in a complex number
    #as its input
    def calc_explosion(self, C):
        
        z0 = C
        
        for i in range(self.order):
            
            z0 = z0**self.powerLevel + cmath.exp((complex(0, -1) * self.theta))
            
            if abs(z0) > self.rad:
                #need to return a status and a value
                return True, i
        
        #need to return a status and a value
        return False, 50
    
    
def pad_number(number, pad_len=3):
    
    number = str(number)
    
    numberLen = len(number)
    
    if numberLen > pad_len:
        raise Exception('Number is bigger than the pad length')
        
    padsNo = pad_len - numberLen
    
    for p in range(padsNo):
        
        number = '0' + number
        
    return number


###################################
### End of function definitions ###
###################################
    

save_folder = './tmp'
calcer = thetaExplosionCalculator()

start_time = time.time()


resolution = (1080, 1920)
#resolution = (500, 840)

xlim = [-2.0, 2.0]
ylim = [-2, 2]

extent = xlim + ylim

lims = [xlim, ylim]

values = list(range(0, 361))

values[:] = [((2 * math.pi)/361) * x for x in values]

#values = [math.pi]

calcer.powerLevel=3

for vi, v in enumerate(values):

    calcer.theta = v
    
    plane = jig.generate_image(resolution, lims, calcer.calc_explosion, stableZero=False)
    
    plt.figure()
    plt.imshow(plane, extent=extent, cmap='seismic')
    plt.axis('off')
    
    frameNo = pad_number(vi)
    
    save_name = os.path.join(save_folder, frameNo + '.png')
    
    plt.savefig(save_name, bbox_inches='tight', pad_inches=0, dpi=300)
    
    plt.close('all')



subprocess.call(["ffmpeg", "-framerate", "15", "-i", "./tmp/%03d.png", "-crf", "20",  "./output/testing_theta.mp4"])

os.remove('./tmp/*')
#plt.show()

