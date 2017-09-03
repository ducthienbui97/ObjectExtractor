# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 00:51:00 2017

@author: thienbui
"""
import os
from object_extractor import Extractor
CURRENT_PATH = os.path.dirname(__file__)
print(Extractor.extract(os.path.join(CURRENT_PATH, 'ASEAN.jpg'),
                        cascade_file=Extractor.HAARCASCADE_ALT2,  # haarcascade_frontalface_alt.xml
                        # output images into AseanSample folder
                        output_directory=os.path.join(
                            CURRENT_PATH, 'AseanSample'),
                        output_prefix='out',  # prefix of output is out
                        start_count=1))  # images start with _1 instead of _0
