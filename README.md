
# Lego-Pen-Plotter
Pen plotter built entirely of lego elements including motors and controller. Programmed with PyBricks and Python.

Lego design files available on [Rebrickable](https://rebrickable.com/mocs/MOC-239758/jormono/lego-pen-plotter)

# Text Generator
I've developed a program that converts typed words into coordinates for the pen plotter, at the time of this writing, it is the only functional program I have developed for the plotter
![Plotter Sign](https://github.com/user-attachments/assets/73def290-746f-4b3f-a109-371021c321f4)

# Work Flow
* Build Pen Plotter
* Install Pybricks firmware on hub
* run Plotter_Font.py on your computer
* when prompted, type out whatever text you wish the pen plotter to write
* when prompted, supply a file name. The file will be save directly into the same directory
* open the pybricks web ui
* upload the file(s) that Plotter_Font.py generated
* Connect to your hub via bluetooth
* send the (first) file by pressing the "play" button, if you hover your cursor over the button a tooltip will pop up which reads "Run this program [F5]"
* send the next file if applicable
