##################################################################
##                 RASPBERRY PI DIODE CONTROL                   ##
##################################################################

# AUTHOR: Manuel Ruiz Pérez
# DATE: 11 November 2018
# CITY: Madrid, Spain.

##################################################################
## NOTES: To use the RPIO library the user need to call to python
#  whith the next comand:
#           sudo python candle.py
#
#  For problems with the RPi.GPIO library is needed to sustitute
#  if the user want to use the Rpi GPIOS.
#
#  For more information about the problem and how to solve, see:
#  https://github.com/metachris/RPIO/issues/86#issuecomment-292955309
#
#  Also is you can do this to solve if the problem starts:
#
#   sudo apt-get install python-dev
#   sudo apt-get install python3-dev
#   
#   On terminal, go to pi user and tipe this comands:
#
#   git clone https://github.com/metachris/RPIO.git --branch v2 --single-branch
#   cd RPIO
#   sudo python setup.py install
#   
#   If you do all correctly it must work.
##################################################################


## STARTING THE PROGRAM:

## Import the needed libraries:
from time import sleep\
\
led = LED(17)\
\
while True:\
    led.on()\
    sleep(1)\
    led.off()\
    sleep(1)}

##########################################
# CODE END