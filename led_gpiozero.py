# import necessary libraries
from time import sleep
from gpiozero import LED

#RPI pin configuration
led = LED(5)

#Turn led on
led.on()
sleep(2)

#Turn led off
led.off()
sleep(3)

#Blink function makes led turn on and off at 1 second intervals
led.blink()
sleep(5)
led.off()
