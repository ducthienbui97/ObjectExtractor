# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 23:52:41 2017

@author: thienbui
"""

from face_extractor import Extractor
Extractor.extract('lena.tif',cascadeFile = Extractor.HAARCASCADE_ALT2)