
# Lego-Pen-Plotter
Pen plotter built entirely of lego elements including motors and controller. Programmed with PyBricks and Python.
Some inspiration taken from [nWestie's NXT-Drawbot project](https://github.com/nWestie/NXT-Drawbot)

Lego design files available on [Rebrickable](https://rebrickable.com/mocs/MOC-239758/jormono/lego-pen-plotter)

# Text Generator
I've developed a program that converts typed words into coordinates for the pen plotter, at the time of this writing, it is the only functional program I have developed for the plotter
![Plotter Sign](https://github.com/user-attachments/assets/73def290-746f-4b3f-a109-371021c321f4)

## Project goals:
* make a functional pen plotter which can draw single line images
* display and run my pen plotter at events with my local LUG (Lego User Group)
    * This requires a degree of mobility and reliability
 
## TODO:
* get it to succesfully draw angled lines
* generate studio files for plotter build
* modify Plotter_Pybricks_Generator.py to automatically generate multiple output files to avoid hub memory issues
* possible build revision
    * specifically looking to color coordinate the axis (so I can explain the project to members of the public, ie the x-axis is made with red bricks and the y-axis is made with blue bricks)
    * also some general tidying up of the design that might include ordering pieces I didn't happen to have on hand when I built the original
* possible pipeline change away from fusion 360 to [vpype](https://github.com/abey79/vpype) and [vpype-gcode](https://github.com/plottertools/vpype-gcode)
* possible change from writing the data statically into the pybricks script to a more fluid script where data is streamed via bluetooth to the hub
    * the hub is very limited in memory and medium-high level of detail images will require multiple consecuitve pybricks files to be executed for a cohesive image to be drawn

## Current project workflow
* have or generate an svg line art image
* import the svg file into a CAM worflow on fusion 360 using the custom post processor found in [nWestie's NXT-Drawbot project](https://github.com/nWestie/NXT-Drawbot)
* export a plain text gcode file describing the image
* run the Plotter_Pybricks_Generator.py file with the gcode saved in the listed file path
    * when prompted by the script select the desired gcode file from the list
* possibly edit Plotter_Pybricks_Generator.py to generate a second, third etc file by changing the if statement on line 109 to write out different parts of the gcode file
    * this is a clunky temporary state that I'll worry about resolving when the project is functional
* load a pen and paper into the machine, make certain it is homed first (to be extra special safe) then run the file via the [pybricks web browser tool](https://code.pybricks.com/)
