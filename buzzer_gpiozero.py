#Import necessary libraries 
from time import sleep
from gpiozero import Buzzer

#Set GPIO pins
buzzer = Buzzer(27)

#Turn buzzer on
buzzer.on()
sleep(1)

#Turn buzzer off
buzzer.off()
sleep(3)

#Blink function turns buzzer on & off at 1 second intervals
buzzer.blink()
sleep(5)

buzzer.off()

exit()
