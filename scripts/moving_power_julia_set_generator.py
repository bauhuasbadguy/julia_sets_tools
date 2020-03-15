#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 00:00:10 2020

@author: stuart
"""

#moving julia set generator
import os
import time


import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

import matplotlib.pyplot as plt

from PIL import Image

import subprocess

import julia_image_generator as jig


#here is an explosion calculator for a simple power julia set
class powerExplosionCalculator(object):

    def __init__(self):
        
        self.powerLevel = 2
        self.order = 25
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
    
#when you build the video the files are ordered alphabetically so I use this function
#to make sure the filenames are in alphabetical order
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


save_folder = './tmp/'

if not os.path.exists(save_folder):

    os.mkdir(save_folder)
    
calcer = powerExplosionCalculator()

start_time = time.time()

#a high res video. You might want to set this lower to make sure it gets done quick
resolution = (1080, 1920)
#resolution = (500, 840)

xlim = [-2.0, 2.0]
ylim = [-1.2, 1.2]

extent = xlim + ylim

lims = [xlim, ylim]

values = list(range(0, 601))

values[:] = [x/100 for x in values]

#iterate through a series of values for the power value
for vi, v in enumerate(values):
    
    #change the value of the power we are using. This is why we use a class
    calcer.powerLevel = v
    
    #generate the data for the image
    plane = jig.generate_image(resolution, lims, calcer.calc_explosion)
    
    #generate the image notice I lock in the colour range
    plt.figure(figsize=(1080/100, 1920/100), dpi=300)
    plt.imshow(plane, extent=extent, cmap='hot', vmin=0, vmax=25)
    plt.axis('off')
    
    #generate the filename
    frameNo = pad_number(vi)
    save_name = os.path.join(save_folder, frameNo + '.png')
    
    plt.savefig(save_name, bbox_inches='tight', pad_inches=0, dpi=300)
    #plt.imshow(plane, cmap='hot')
               #cmap='copper')
    plt.close('all')
    #plt.show()

#generate the video
subprocess.call(["ffmpeg", "-framerate", "15", "-i", "./tmp/%03d.png", "-crf", "20",  "./output/high_res_powers.mp4"])

#remove the raw frames of the video
files = os.listdir('./tmp/')

for file in files:
    fname = os.path.join('./tmp', file)
    os.remove(fname)

print("TOOK {0}s".format(time.time() - start_time))
        