'''
File Name settings.py
Author jrctrabuco
Date Created Set 11 2018
Last Modified Set 11 2018
Python Version 3.6.6

Module that contains the settings to configure an individual 
device. this module allow to tweak the settings witout interfering
with the core module
'''

'''
------------------------------------------------------------------
CAMERA SETTINGS USING the pycamera module 1.13
------------------------------------------------------------------
'''

#Initialization Settings

PiCamera = {
    'sensor_mode' : 0,
    'resolution' : None,
    'framerate' : None,
    'framerate_range' : None,
}

# Capture Settings

capture = {
    'format' : None,
    'resize' : None,
    'bayer' : False,
}