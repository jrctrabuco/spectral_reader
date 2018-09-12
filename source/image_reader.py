'''
File Name: image-reader.py
Author: jrctrabuco
Date Created: Aug 30 2018
Last Modified: set 11 2018
Python Version 3.6.6

This modules contains the functions and objects necessary to collect image
information from a raspberry py camera. and to expoort a profile based on a
fixed position image where the prfile source will appear allways in the same
place on the screen, imposed by the desing of the device.
'''
import os
import numpy as np
from source import settings
from skimage import io, measure
#from picamera import picamera
from time import sleep
from datetime import datetime     


#situation awarness and file system

now = datetime.now().strftime("%a-%d.%m.%Y-%H:%M:%S")

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_storage = os.path.join(project_root,'data')
calibrant_storage = os.path.join(data_storage,'calibrants')
measurement_storage = os.path.join(data_storage,'measurements')


#reusable functions

def initialize_camera():
    camera = PiCamera(**settings.PiCamera)
    camera.iso = 100
    camera.shutter_speed = camera.exposure_speed
    sleep(10)
    camera.exposure_mode = 'off'
    awbgain = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = awbgain
    return(camera)

def take_picture(camera, savePath):
    '''
    Function to take a picture with the picamera module
    and save it on a given directory
    ! function will not return anything !

    ex:
    take_picture(c:/pitures/beatiful pictures)
    will save a pictue on that directory
    
    '''
    if camera.exposure_mode == 'off':
        output = np.empty((2464,3280,3), dtype= np.uint8)
        camera.capture(output,**settings.capture)

    else:
        raise ValueError ('Camera not initialized')
    return (output)

def get_profile(imageLocation, startPixel, endPixel, profileWidth):
    '''
    uses scikit-image tools to get a profile from an image converted
    to black and white given a locatio and the expected postion for the
    profile

    returns a profile as a numpy array
    '''
    image = io.imread(imageLocation, as_gray=True)
    profile = measure.profile_line(image, startPixel,
                                   endPixel, linewidth=profileWidth)
    return profile

"""
--------------------------------------------------------------------------------
MAIN CLASSES
--------------------------------------------------------------------------------
"""

class Measurement():

    def __init__(self, name, measurementType):

        self.name = name
        self.type = measurementType
        self.pictureID = ''

        if measurementType =='calibrant':
            self.saveLocation = calibrant_storage
        elif measurementType == 'zero':
            self.saveLocation = measurement_storage
        elif measurementType == 'measurement':
            self.saveLocation = measurement_storage
        else:
            raise ValueError ("invalid type of measurment: use only 'calibrant' 'zero' 'measurement' ")

    def get_image (self, camera):
        self.pictureID = self.type + now + '.tif'
        self.imgPath = (self.saveLocation+self.pictureID)
        take_picture(camera, self.imgPath)
        return self.imgPath

    def profile (self, imgPath, start, stop, width ):
        
        self.rawProfile = get_profile(imgPath, start, stop, width)
        return self.rawProfile

    def fit_profile(self, profile, xx = 0, order = 3):
        if xx == 0:
            xx = np.arange(len(profile))

        self.profileParams = np.polyfit(xx, profile, order)

        return self.profileParams
        





    

