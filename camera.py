from time import sleep          # To easily use sleep function
from picamera import PiCamera

camera = PiCamera()

for i in range(5):
    print("Say cheese!",i) 
    camera.capture('/home/pi/Desktop/Pics/image%s.jpg' % str(i))
    sleep(0.5)

camera.start_recording('/home/pi/Desktop/Pics/video.mjpeg')
print("Recording started")
sleep(3)
camera.stop_recording()
print("Recording stopped")
