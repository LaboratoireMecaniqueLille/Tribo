Breaking tribometer
===================

This git repository is the code that drives the breaking tribometer
of the the LamCube. It relies on the open-source project "Crappy" which
can be found [here](https://github.com/LaboratoireMecaniqueLille/crappy).

It can perform a wide range of tests, which can be defined simply with simple
functions exposed to the user, like inertia simulation or constant power
for thermal studies. This code automatically starts high-frequency acquisition
from the sensors with a Spectrum PCIe card and standard acquisition with 2
Labjack T7 boards. This setup can read from more than 100 channels for
temperature and other standard frequency sensors (~ 100Hz)
and 16 high frequency sensors (100 kHz).

This project cannot be used as-is by anyone with a different setup, but
this is a great example of what can be accomplished with Crappy.