# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 00:51:00 2017

@author: thienbui
"""

from face_extractor import Extractor
print (Extractor.extract('ASEAN.jpg',cascadeFile = Extractor.HAARCASCADE_ALT2)) # return 10 faces