
# Lego-Pen-Plotter
Pen plotter built entirely of lego elements including motors and controller. Programmed with PyBricks and Python.

Lego design files available on [Rebrickable](https://rebrickable.com/mocs/MOC-239758/jormono/lego-pen-plotter)

## Text Generator
I've developed a program that converts typed words into coordinates for the pen plotter, at the time of this writing, it is the only functional program I have developed for the plotter
![Plotter Sign](https://github.com/user-attachments/assets/73def290-746f-4b3f-a109-371021c321f4)

### Work Flow
* Build Pen Plotter
* Install Pybricks firmware on hub
* run Plotter_Font.py on your computer (NOTE: ensure the Seed A and Seed B files are in the same directory as Plotter_Font.py)
* when prompted, type out whatever text you wish the pen plotter to write
* when prompted, supply a file name. The file will be save directly into the same directory
* open the pybricks web ui
* upload the file(s) that Plotter_Font.py generated
* Connect to your hub via bluetooth
* Remove the Technic brick with the two 8 tooth gears attached, place an index card to be written on, and replace the technic brick to hold the index card securely in place
* send the (first) file by pressing the "play" button, if you hover your cursor over the button a tooltip will pop up which reads "Run this program [F5]"
* send the next file if applicable

## Etch A Sketch Mode
In Etch A Sketch mode we forgo precompiled instructions in favor of manually controlling the plotter by use of an xbox controller. See [this graphic](https://www.padcrafter.com/?col=%23242424%2C%23606A6E%2C%23FFFFFF&outline=0&templates=Pen+Plotter+Controls+%28Default%29%7CPen+Plotter+Controls+%28Alt%29&plat=01248673510&timestamp=1781654804706&rightBumper=Speed+Up%7CSpeed+Up&leftBumper=Speed+Down%7CSpeed+Down&leftStick=Movement+Control%7CUp%2FDown+controls+Y+Motor&xButton=Toggle+Alt+Control+Mode%7CToggle+Alt+Control+Mode&bButton=Move+Gantry+to+change+Paper%7CMove+Gantry+to+change+Paper&aButton=Engage%2FDisengage+Pen%7CEngage%2FDisengage+Pen&leftBumper%23rightBumper=Reset+Speed%7CReset+Speed&startButton=Initiate+Homing+Sequence%7CInitiate+Homing+Sequence&rightStick=%7CLeft%2FRight+controls+X+motor) for the control scheme (Be patient, it takes a long time to load). You'll probably need to be a better artist than I am! This program includes safeguards that stop the user from "crashing" the plotter by driving it out of bounds. It will simply ignore inputs from the xbox controller that tell it to move beyond pre-defined boundaries. Simply load the script to the hub, this will disconnect the hub from your computer automatically and allow you to connect an xbox controller see the [pybricks documentation](https://docs.pybricks.com/en/latest/iodevices/xboxcontroller.html) for a guide on pairing an xbox controller to the hub.

<img width="4096" height="3072" alt="IMG20260428153418" src="https://github.com/user-attachments/assets/f3401ab6-77b0-4d72-af70-eb42fb4cd450" />
