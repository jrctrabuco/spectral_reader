from picamera import PiCamera    
from time import sleep    
from datetime import datetime     
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import profile_line
import scipy

from skimage import io

from PIL import Image
camera = PiCamera()
camera.resolution = (480,320)     

camera.framerate=5
#camera.sensor_mode=3
#camera.shutter_speed = 6000000
#camera.iso = 100
#camera.shutter_speed = camera.exposure_speed
#camera.exposure_mode = 'off'
#g = camera.awb_gains
#camera.awb_mode = 'off'
#camera.awb_gains = g
camera.start_preview()    

#framerate=15

   #framerate=Fraction(1,6),











datedate = datetime.now().strftime("%a-%d.%m.%Y-%H:%M:%S")     
filename = '/home/pi/Pictures/IMG-' + datedate + '.jpg'     
#sleep(1)    
camera.stop_preview()
#camera.resolution = (2592,1944)     








camera.capture(filename)    
sleep(1) 

#img = Image.open(filename).convert('LA')
#img.save('/home/pi/Desktop/greyscale.png')
#spec = io.imread(filename, mode='L')
spec= scipy.misc.imread(filename,flatten=True,mode='I')
x0=150
x1=300
y=135
#spec = misc.spec(gray=True)  # retrieve a grayscale image
arraypic=(profile_line(spec, (y, x0), (y, x1),linewidth=25))
#print (arraypic)
fig, axes = plt.subplots(nrows=2)
#plt.plot(arraypic)

axes[0].plot(arraypic)

axes[1].imshow(spec)
plt.show()
