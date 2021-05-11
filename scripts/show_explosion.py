#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 18:10:22 2021

@author: stuart
"""

#show the explosion in recurant values

import matplotlib.pyplot as plt

plt.close('all')

def calculate_recurrance(ns, z0):
    
    powerLevel = 2

    zn = 0
    
    outX = []
    outZ = []
    for n in ns:
        
        #break if we've hit an insanely high value that causes an overflow error
        try:
            zn = zn**powerLevel + z0
        except:
            break
        
        #store these values
        outX.append(n)
        outZ.append(zn)
        
        #break if the value is exploding
        if abs(zn) > 5000:
            break
        
    #out.append(abs(zn))
    
    return outX, outZ

###################################
### End of function definitions ###
###################################

#set the values we are going to investigate
values = [complex(0.5, 0.5),
          complex(0.3, 0.7),
          complex(-0.3, 0.5),
          complex(0.3, 0.5)
          ]
        
#the points we want to investigate
xs = list(range(0, 101))

fig, ax = plt.subplots(2, 2)
yi = 0
for i, value in enumerate(values):
    
    xi = i % 2
    
    
    [N, Z] = calculate_recurrance(xs, value)

    ax[yi, xi].plot(N, Z)
    ax[yi, xi].set_xlabel('n')
    ax[yi, xi].set_ylabel(r'z$_{n}$')
    ax[yi, xi].set_title(str(value.real) + ' + ' + str(value.imag) + 'i')

    if xi == 1:
        
        yi += 1


plt.show()