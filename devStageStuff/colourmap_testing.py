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


#import matplotlib
# Force matplotlib to not use any Xwindows backend.
#matplotlib.use('Agg')

import matplotlib.pyplot as plt

from PIL import Image

import subprocess

import julia_image_generator as jig


#here is an explosion calculator for a simple power julia set
class thetaExplosionCalculator(object):

    def __init__(self):
        
        self.powerLevel = 2
        self.order = 50
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
        return False, 0
    
    
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


#resolution = (1080, 1920)
resolution = (500, 840)

xlim = [-2.0, 2.0]
ylim = [-2, 2]

extent = xlim + ylim

lims = [xlim, ylim]

values = list(range(0, 181))

values[:] = [((2 * math.pi)/361) * x for x in values]


colours = ['Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']


for ci, c in enumerate(colours):
    
    #calcer.theta = v
    
    plane = jig.generate_image(resolution, lims, calcer.calc_explosion)
    
    plt.figure()
    plt.imshow(plane, extent=extent, cmap=c)
    plt.axis('off')
    
    #frameNo = pad_number(vi)
    
    save_name = os.path.join(save_folder, c + '.png')
    
    plt.savefig(save_name, bbox_inches='tight', pad_inches=0, dpi=300)
    
    plt.close('all')

'''
for vi, v in enumerate(values):

    calcer.theta = v
    
    plane = jig.generate_image(resolution, lims, calcer.calc_explosion)
    
    plt.figure()
    plt.imshow(plane, extent=extent, cmap='prism')
    plt.axis('off')
    
    frameNo = pad_number(vi)
    
    save_name = os.path.join(save_folder, frameNo + '.png')
    
    #plt.savefig(save_name, bbox_inches='tight', pad_inches=0, dpi=300)
    
    #plt.close('all')
    
    break
''' 
#subprocess.call(["ffmpeg", "-framerate", "15", "-i", "./tmp/%03d.png", "-crf", "20",  "./tmp/testing_cmaps.mp4"])
#plt.show()

'''
#iterate through a series of values for the power value
for vi, v in enumerate(values):
    
    calcer.powerLevel = v

    plane = jig.generate_image(resolution, lims, calcer.calc_explosion)
    
    plt.figure(figsize=(1080/100, 1920/100), dpi=300)
    plt.imshow(plane, extent=extent, cmap='hot')
    plt.axis('off')
    
    frameNo = pad_number(vi)
    
    save_name = os.path.join(save_folder, frameNo + '.png')
    
 '''