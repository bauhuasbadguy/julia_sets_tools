# julia_sets_tools #
A series of programs designed for examining julia sets. The code is all in the scripts folder. There are 4 scripts of interest.  

## Examples ##

<div align="center"><img src='./high_res_powers.gif' height=340px></div>

<div align="center">
<img src='./theta_p2.gif' width=30%> <img src='./theta_p3.gif' width=30%> <img src='./theta_p15.gif' width=30%>
</div>

## Files ##

* `julia_image_generator.py`:- This is the tool that takes in a function to apply to each pixel and then populates that pixel appropriately.
* `julia_sets_basic.py`:- This produces the mandelbrot set but can be modified to produce other julia sets
* `moving_power_julia_set_generator.py`:- This produces a video where each frame has a different value for p in the equation z_{n+1} = z_{n}^{p} + C where C is z_{0}. By default it goes from 0 to 5 in 0.1 increment steps. This is the code used to generate the first example gif in this readme.
* `theta_calculation.py`:- This generates videos of moving \theta for  the equation z_{n+1} = z_{n}^{p} + e^{i*\theta}. This is the code used to generate the second set of gifs attached to this readme.

## Explanation ##

A full explanation can be found on [wikipedia](https://en.wikipedia.org/wiki/Julia_set). Each point in the cartesian plane is converted into a point on the complex plane so (x,y) becomes z=x + iy. These points are then fed to a recursive function, for example z_{n+1}=z_{n} + C for the mandelbrot set. If the point explodes to infinity then the iteration at which it explodes is noted and set to the value of the pixel at the points co-ordinates in the outputted image. Certain points will never explode and these are set to the maximum number of iterations that the function could possibly have gone to if it were not set to stop after a certain number. If you found this explanation horribly unclear (I mean if you understood this garbled nonsence well done) you can see a short video that explains it much better [here](https://www.youtube.com/watch?v=NGMRB4O922I) made by numberfile.

## Setup ##

You'll need python3 with:-

* numpy
* matplotlib

and you'll need ffmpeg to make the videos. I did everything using ubuntu so it was very easy but if you're using windows you might have significant trouble getting a series of images to turn into a video. I would recommend imageJ but I've not used it in a few years so that might also be a nightmare to use at this point. It was ok in 2015 from what I remember.

## How to use the code ##

The code has been set up so that there is a function for building the images when fed the desired resolution, x and y limits and the recursive function you are going to use. The resolution should be a two intiger tupple, the limits should be a list of two lists [xlimits, ylimits] and the explosion function should take in a complex number and return a status (for in the set or out of it) and the value to be shown on the image. To make this clear see the examples included in this repo (`julia_sets_basic.py`, `moving_power_julia_set_generator.py`, `theta_calculation.py`). 

## Useful tools ##

Convert from mp4 to a gif 

``ffmpeg -i ./testing_theta.mp4 -r 15 -vf scale=512:-1 example.gif``