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
import PIL
from source import settings
import picamera
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
    '''
    initialize the camera
    '''
    camera = PiCamera(**settings.PiCamera)
    camera.iso = 100
    camera.shutter_speed = settings.Initialization[shutterSpeed]
    sleep(settings.initialization[warmTime])
    camera.exposure_mode = 'off'
    awbgain = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = awbgain
    camera.hflip = True
    return camera

def take_picture_luminance(camera, **settings.FOV, savePath=None):

    '''
    take an return a picture of the Y channel of a YUV campture 
    '''

    if camera.exposure_mode == 'off':
        imageYUV= picamera.array.PiYUVArray(camera)
        camera.capture(imageYUV,format='yuv')
        data = imageYUV.array[x0:xn, y0:yn, 0]

    else:
        raise ValueError ('Camera not initialized')
    
    return data


def get_profile(image, mode='maximum'):
    '''
    get a profile from the image using either max or average 
    from the y scanningof an image
    '''
    maximum = np.max(image, axis=1)
    mean = np.mean(image, axis=1)
    median = np.median(image, axis=1)

    if mode == 'maximum':
        return maximum

    elif mode == 'mean':
        return mean

    elif mode == 'median':
        return median

    else:
        raise ValueError("""Invalid Mode mode for profile can only 
                         be maximum, mean or median""")




"""
--------------------------------------------------------------------------------
MAIN CLASSES
--------------------------------------------------------------------------------
"""


class Measurement():

    def __init__(self, measurementType):

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


    def take_image (self, camera, save=False):

        self.pictureID = self.type + now + '.tif'
        self.imgPath =self.saveLocation + self.pictureID

        self.picture = take_picture_luminance(camera)

        if save == True:
            data = PIL.Image.fromarray(self.picture)
            data.save(self.imgPath)

        return self.picture


    def profile(self, image=None,path=None, **settings.profile):

        if path == None:
            self.Profile = get_profile(image, mode=mode)

        else:
            image = PIL.Image.open(path, mode='rw')
            self.Profile get_profile() 

        return self.Profile


    def fit_profile(self, profile, xx = 0, order = 3):
        if xx == 0:
            xx = np.arange(len(profile))

        self.profileParams = np.polyfit(xx, profile, order)

        return self.profileParams

class Reader():
    def __init__(status=None ):
        self.status = status

    def calibrate(calibrator=None, peaks):
        self.peaks = peaks
        if calibrator.type == Measurement:
            self.calibrator = calibrator
        
        else:
            self.calibrator = Measurement('calibrant')
            





    

