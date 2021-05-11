#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 23:46:12 2020

@author: stuart
"""

#julia sets generator

import numpy as np

import itertools

import multiprocessing
from multiprocessing import Process

def generate_image(resolution, lims, explosion_function, stableZero=True):
    
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
            if result[0] or not stableZero:
                
                plane[yi, xi] = result[1]
    
    return plane


def generate_image_multiprocessing(resolution, lims, explosion_function, stableZero=True):
    
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
            if result[0] or not stableZero:
                
                plane[yi, xi] = result[1]
    
    return plane