'''
File Name: image-reader.py
Author: jrctrabuco
Date Created: Aug 30 2018
Last Modified: Aug 31 2018
Python Version 3.6.6

This modules contains the functions and objects necessary to collect image
information from a raspberry py camera. and to expoort a profile based on a
fixed position image where the prfile source will appear allways in the same
place on the screen, imposed by the desing of the device.
'''
import os
import numpy as np
from skimage import io, measure
from picamera import picamera
from time import sleep

#situation awarness and file system

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_storage = os.path.join(project_root,'data')


#reusable functions

def take_picture(savePath):
    '''
    Function to take a picture with the picamera module
    and save it on a given directory
    ! function will not return anything !

    ex:
    take_picture(c:/pitures/beatiful pictures)
    will save a pictue on that directory
    '''
    camera = PiCamera()
    camera.start_preview()
    sleep (10)
    camera.capture(savePath)
    camera.stop_preview()
    return ()

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

class Calibrant():

    def __init__( self , profileParamsm):
        self.name = str(self)
        take_picture(data_storage+self.name)
        self.image =
