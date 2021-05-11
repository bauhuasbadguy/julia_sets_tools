#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 17:16:32 2021

@author: stuart
"""

#zooming in on the mandelbrot set

import os
import time

import glob

import matplotlib.pyplot as plt

plt.close('all')

import julia_image_generator as jig

#here is an explosion calculator for a simple power julia set
class explosionCalculator(object):

    def __init__(self, order):
        
        self.powerLevel = 2
        self.order = order
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

#function for recalculating our limits for zooming in
def recalculate_limits(start_lims, target_point, zoom_rate):
    
    #work out how big our previous window was
    window_width = start_lims[1] - start_lims[0]
    
    #work out how wide the new window is
    new_window_width = window_width * zoom_rate
    
    #move the window over so that it is more focused on the target
    
    #first find how central the point is
    left = target_point - start_lims[0] 
    right = target_point - start_lims[1] 
    
    #now work out how far over we need to move
    move_over = ((abs(left) - abs(right))/2) * zoom_rate
    #move_over = ((left - right)/2) * zoom_rate
    
    #print(move_over)
    #calulate where our new leftmost point should be
    new_left = start_lims[0] + move_over
    #check we're moving closer in and not moving too far over
    if new_left < start_lims[0]:
        
        new_left = start_lims[0]
    
    #calculate where the right side of the frame will be now
    new_right = new_left + new_window_width
    
    #if we're moving too far over we need to recalculate to make sure we don't
    #move over too far
    if new_right > start_lims[1]:
        
        move_over = new_right - start_lims[1]
        
        new_left -= move_over 
        
        new_right = new_left + new_window_width
    
    return [new_left, new_right]


###################################
### End of function definitions ###
###################################

start_time = time.time()

#480p resolution
resolution = (420, 640)

#720p resolution
#resolution = (720, 1280)

#1080p resolution
#resolution = (1080, 1920)

#set the starting limits in x and y
xlims = [-2.2, 1.2]
ylims = [-1.2, 1.2]

#set the parameters for how we're going to zoom into the set
frames = 550
zoom_rate = 0.95

#set our target point, x+iy with [x, y]
target = [-0.93614662004, -0.29860200001]

#set the order for our plots. This is the step at which we give up looking for 
#an explosion. A higher order takes longer to calculate but allows for greater
#zooming in
order = 500

#set up the calculation tool so we can tune parameters being used if we so wish
calcer = explosionCalculator(order)


for frame in range(frames):
    
    #generate our image
    plane = jig.generate_image(resolution, [xlims, ylims], explosion_function=calcer.calc_explosion, stableZero = False)
    
    #set the limits of the image
    extent = xlims + ylims
    
    #generate and save the image
    plt.imsave('./tmp/zoom_test' + str(frame) + '.png', plane, cmap='jet', vmin=0, vmax=order, dpi=300)

      
    #zoom in
    xlims = recalculate_limits(xlims, target[0], zoom_rate)
    ylims = recalculate_limits(ylims, target[1], zoom_rate)

    
print("TOOK {0}s".format(time.time() - start_time))

#ffmpeg -r 10 -i ./tmp/zoom_test%01d.png -vcodec mpeg4 -y movie.mp4

#create a video
os.system("ffmpeg -r 10 -i ./tmp/zoom_test%01d.png  ./mandelbrotZoom.mp4")

#ffmpeg -r 20 -i ./tmp/zoom_test%01d.png  ./mandelbrotZoom.mp4

'''
#delete the frames
files = glob.glob("./tmp/*.png")
for file in files:
    
    os.remove(file)

'''
