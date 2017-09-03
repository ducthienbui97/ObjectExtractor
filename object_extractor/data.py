# -*- coding: utf-8 -*-
"""
Created on Sun Sep 3 18:05:00 2017

@author: thienbui
"""

import os


def _name2path(name):
    data_path = os.path.join(os.path.dirname(__file__), 'data')
    return os.path.join(data_path, name)


FRONTALFACE_ALT = _name2path('haarcascade_frontalface_alt.xml')
FRONTALFACE_ALT2 = _name2path('haarcascade_frontalface_alt2.xml')
FRONTALFACE_ALT_TREE = _name2path('haarcascade_frontalface_alt_tree.xml')
FRONTALFACE_DEFAULT = _name2path('haarcascade_frontalface_default.xml')
EYE = _name2path('haarcascade_eye.xml')
EYE_TREE_EYEGLASSES = _name2path('haarcascade_eye_tree_eyeglasses.xml')
FRONTALCATFACE = _name2path('haarcascade_frontalcatface.xml')
FRONTALCATFACE_EXTENDED = _name2path('haarcascade_frontalcatface_extended.xml')
FULLBODY = _name2path('haarcascade_fullbody.xml')
LEFTEYE_2SPLITS = _name2path('haarcascade_lefteye_2splits.xml')
LOWER_BODY = _name2path('haarcascade_lowerbody.xml')
PROFILEFACE = _name2path('haarcascade_profileface.xml')
RIGHTEYE_2SPLITS = _name2path('haarcascade_righteye_2splits.xml')
SMILE = _name2path('haarcascade_smile.xml')
UPPER_BODY = _name2path('haarcascade_upperbody.xml')
