# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 00:51:00 2017

@author: thienbui
"""

from face_extractor import Extractor
print (Extractor.extract('ASEAN.jpg',
                         cascadeFile = Extractor.HAARCASCADE_ALT2, # use haarcascade_frontalface_alt.xml
                         outputDirectory = 'AseanSample', # output images into AseanSample folder
                         outputPrefix = 'out', # prefix of output is out
                         startCount = 1 # images start with _1 instead of _0
                         )) # return 10 faces
