Content
-------

* [Main page](help.html)
* [Hardware description](hardware.html)
* [Auto mode interface](interface.html)
* [Auto mode code description](auto.html)
* Tools description (this page)

manual_gui.py
=============
Probably the most important of these scripts: it can drive the actuators of
the tribometer manually. It is useful in many situations: for testing
and setting of the the bench, preparing a test, manually measure data etc...
It shows a very intuitive interface. The upper field is the position of
the pad, or the force if selected. The graph shows the measured
force in N (blue), the speed in rpm (green) and on the right scale the torque
(red). The lower field is to type the target speed. You can finally push
the hydraulic in or out with the two buttons. It is not a "real" Crappy
program, but it uses the Labjack class for simplicity. Note that no data
will be saved when running this program.

hdftocsv.py
===========
As its name suggests, it can turn HDF files from the Spectrum to csv. Obviously
the size of the csv would be humongus if each datum was written, so it takes
a RESAMPLE parameter, setting one out of how many points will be taken.
Please have a look at the code for more information.

read_displacement.py
====================
A really short and simple program that reads and save the data on two channels
of the spectrum. It is meant to read the disc discplacement from the capacitec
sensor. You should rotate the disc (using manual_gui.py for example). The
resulting hdf file can be used with plot_displacement.py
Please have a look at the code for more information.

plot_displacement.py
====================
This program takes the hdf5 file generated by read_dispalcement and plots
the displacement in µm function of the angle (in deg). To do so it detects
the tops from the sensor. Make sure to set the correct number of tops
per revolution in the file, and the correct gains.
Please have a look at the code for more information.

temp.py
=======
This little script can read the thermocouples in the pad and in the disc
and print them on a map, just like during a test. This can be useful to
monitor the temperature when cooling between tests.

spectrum_single_chan.py
=======================
This file can read data from a single channel of the Spectrum and plot it.
It can be useful for settings. Here the example reads the pad real position
from the second capacitive sensor, but the gain and channel can be adjusted
to your needs.

spectrum.py
===========
Just like spectrum_single_chan.py, but it can read multiple channels at once.
In this example, it reads all the channels in Volts (gain=1) on the
-/+10V range.
