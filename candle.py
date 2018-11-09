##################################################################
##                 RASPBERRY PI DIODE CONTROL                   ##
##################################################################

# AUTHOR: Manuel Ruiz Pérez
# DATE: 08 November 2018
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
import RPIO as GPIO
import time
import random

# Set the PWM output we're using for the LED
LED = 17

# Define the setup general status:
def setup():
    global power
    GPIO.setmode(GPIO.BCM) # Say to RPI that we're using the BCM GPIO numeration.
    GPIO.setup(LED, GPIO.OUT) # Set the LED pin as an output.
    #pwm = GPIO.PWM(LED, 200) # Coment 1: See down.
    power.start(100) # Starting at a brightness of 100%

# Defining the brightness variation cycle:
def set_brightness(new_brightness):
    power.ChangeDutyCycle(new_brightness) # Sets brightness of the LED by change duty cycle.

def flicker(): # Coment 2: See down.
    set_brightness(random.randrange(0, 100))
    time.sleep(random.randrange(1, 10) * 0.01)

# The wrapper around the flicker function makes sure the GPIO hardware
# is cleaned up when the user presses CTRL-C. Take it into account.

# Defining the main program loop, it's what are going to make the program
# to do what we want to do.
def loop():
    try:
        while True:
            flicker()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

# Set up the hardware:
setup()

# Start the flickering:
loop()
##########################################
# CODE END


####################################################################
# COMENTS:
#   1. Start PWM on the LED pin at 200Hz with a 100% duty cycle. At
#      lower frecuencies the LED would flicker even when we wanted
#      it on solidly.
#
#   2. We want a random brightness between 0% and 100%. Then we'll
#      hold it for a random time between 0.01 and 0.1 seconds to get 
#      a nice flicker effect. Play with these values to make the 
#      effect suit your liking.
####################################################################




