# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

#normal stand
def normal():
    pwm.set_pwm(0, 0, 320)
    time.sleep(0.01)
    pwm.set_pwm(1, 0, 400)
    time.sleep(0.01)
    pwm.set_pwm(2, 0, 500)
    time.sleep(0.01)
    pwm.set_pwm(3, 0, 440)
    time.sleep(0.01)

    pwm.set_pwm(4, 0, 120)
    time.sleep(0.01)
    pwm.set_pwm(5, 0, 240)
    time.sleep(0.01)
    pwm.set_pwm(6, 0, 200)
    time.sleep(0.01)
    pwm.set_pwm(7, 0, 280)
    time.sleep(0.01)


#move forward
def moveforward():
    #left feet
    pwm.set_pwm(0, 0, 320)
    time.sleep(0.01)
    pwm.set_pwm(1, 0, 400)
    time.sleep(0.01)
    pwm.set_pwm(2, 0, 500)
    time.sleep(0.01)
    pwm.set_pwm(3, 0, 400)
    time.sleep(0.01)

    pwm.set_pwm(4, 0, 120)
    time.sleep(0.01)
    pwm.set_pwm(5, 0, 240)
    time.sleep(0.01)
    pwm.set_pwm(6, 0, 200)
    time.sleep(0.01)
    pwm.set_pwm(7, 0, 250)
    time.sleep(0.01)

    time.sleep(1)

    pwm.set_pwm(0, 0, 280)
    time.sleep(0.01)
    pwm.set_pwm(1, 0, 400)
    time.sleep(0.01)
    pwm.set_pwm(2, 0, 500)
    time.sleep(0.01)
    pwm.set_pwm(3, 0, 400)
    time.sleep(0.01)

    pwm.set_pwm(4, 0, 100)
    time.sleep(0.01)
    pwm.set_pwm(5, 0, 280)
    time.sleep(0.01)
    pwm.set_pwm(6, 0, 300)
    time.sleep(0.01)
    pwm.set_pwm(7, 0, 250)
    time.sleep(0.01)

    time.sleep(1)

    #right feet
    pwm.set_pwm(0, 0, 320)
    time.sleep(0.01)
    pwm.set_pwm(1, 0, 400)
    time.sleep(0.01)
    pwm.set_pwm(2, 0, 500)
    time.sleep(0.01)
    pwm.set_pwm(3, 0, 400)
    time.sleep(0.01)

    pwm.set_pwm(4, 0, 220)
    time.sleep(0.01)
    pwm.set_pwm(5, 0, 350)
    time.sleep(0.01)
    pwm.set_pwm(6, 0, 200)
    time.sleep(0.01)
    pwm.set_pwm(7, 0, 250)
    time.sleep(0.01)

    time.sleep(1)

    pwm.set_pwm(0, 0, 280)
    time.sleep(0.01)
    pwm.set_pwm(1, 0, 400)
    time.sleep(0.01)
    pwm.set_pwm(2, 0, 500)
    time.sleep(0.01)
    pwm.set_pwm(3, 0, 400)
    time.sleep(0.01)

    pwm.set_pwm(4, 0, 100)
    time.sleep(0.01)
    pwm.set_pwm(5, 0, 280)
    time.sleep(0.01)
    pwm.set_pwm(6, 0, 300)
    time.sleep(0.01)
    pwm.set_pwm(7, 0, 250)
    time.sleep(0.01)

    time.sleep(1)

    pwm.set_pwm(0, 0, 280)
    time.sleep(0.01)
    pwm.set_pwm(1, 0, 400)
    time.sleep(0.01)
    pwm.set_pwm(2, 0, 500)
    time.sleep(0.01)
    pwm.set_pwm(3, 0, 400)
    time.sleep(0.01)

    pwm.set_pwm(4, 0, 100)
    time.sleep(0.01)
    pwm.set_pwm(5, 0, 280)
    time.sleep(0.01)
    pwm.set_pwm(6, 0, 300)
    time.sleep(0.01)
    pwm.set_pwm(7, 0, 250)
    time.sleep(0.01)

    time.sleep(1)


#kick the ball

def kick():
    pwm.set_pwm(0, 0, 320)
    time.sleep(0.01)
    pwm.set_pwm(1, 0, 400)
    time.sleep(0.01)
    pwm.set_pwm(2, 0, 500)
    time.sleep(0.01)
    pwm.set_pwm(3, 0, 440)
    time.sleep(0.01)

    pwm.set_pwm(4, 0, 120)
    time.sleep(0.01)
    pwm.set_pwm(5, 0, 240)
    time.sleep(0.01)
    pwm.set_pwm(6, 0, 200)
    time.sleep(0.01)
    pwm.set_pwm(7, 0, 280)
    time.sleep(0.01)

    pwm.set_pwm(0, 0, 320)
    time.sleep(0.01)
    pwm.set_pwm(1, 0, 400)
    time.sleep(0.01)
    pwm.set_pwm(2, 0, 500)
    time.sleep(0.01)
    pwm.set_pwm(3, 0, 440)
    time.sleep(0.01)

    pwm.set_pwm(4, 0, 120)
    time.sleep(0.01)
    pwm.set_pwm(5, 0, 240)
    time.sleep(0.01)
    pwm.set_pwm(6, 0, 200)
    time.sleep(0.01)
    pwm.set_pwm(7, 0, 280)
    time.sleep(0.01)

    


print('press Ctrl-C to quit...')
while True:
    
    #normal()
    #moveforward()
    #test()
    kick()
    #break
