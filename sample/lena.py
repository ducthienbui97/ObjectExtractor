# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 23:52:41 2017

@author: thienbui
"""
import os
from face_extractor import Extractor
CURRENT_PATH = os.path.dirname(__file__)
Extractor.extract(os.path.join(CURRENT_PATH, 'lena.jpg'))
