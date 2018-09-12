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
    'sensor_mode' : 3,
    'resolution' : (3280,2464),
    'framerate' : None,
    'framerate_range' : None,
}

'''# Exposure settings
Exposure = {
    'exposure_mode' : 'off',
    'iso' : 100 ,
    'shutter_speed' : 1000, 
    'awb_mode' : 'off',
    'awb_gain' : (2.0,2.0),
'''


}


# Capture Settings

capture = {
    'format' : 'yuv',
    'resize' : None,
    'bayer' : False,
}