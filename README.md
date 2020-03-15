# julia_sets_tools #
A series of programs designed for examining julia sets. The code is all in the scripts folder. There are 4 scripts of interest.  

## Examples ##

<div align="center"><img src='./high_res_powers.gif' height=340px></div>

<img src='./theta_p2.gif' height=340px>｜<img src='./theta_p3.gif' height=340px>

## Files ##

* `julia_image_generator.py`:- This is the tool that takes in a function to apply to each pixel and then populates that pixel appropriately.
* `julia_sets_basic.py`:- This produces the mandelbrot set but can be modified to produce other julia sets
* `moving_power_julia_set_generator.py`:- This produces a video where each frame has a different value for p in the equation z_{n+1} = z_{n}^{p} + C where C is z_{0}. By default it goes from 0 to 5 in 0.1 increment steps
* `theta_calculation.py`:- This generates videos of moving \theta for  the equation z_{n+1} = z_{n}^{p} + e^{i*\theta}. This is the code used to generate the gifs attached to this readme


Convert from mp4 to a gif 

``ffmpeg -i ./testing_theta.mp4 -r 15 -vf scale=512:-1 example.gif``