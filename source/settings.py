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
    'sensor_mode' : 2,
    'resolution' : (3280,2464),
    'framerate' : None,
    'framerate_range' : None,
}

Initialization ={
    'shutterSpeed' : 5000000,
    'warmTime' : 30
}

FOV = {
    'x0' : 0,
    'xn' : 0,
    'y0' : 0,
    'yn' : 0,
}

profile = {
    'mode' : average,
    
}