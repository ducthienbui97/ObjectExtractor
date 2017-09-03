# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 22:59:52 2017

@author: thienbui
"""

import cv2
import os
from .data import *


class Extractor:
    _current_cascade = FRONTALFACE_DEFAULT
    _classifier = cv2.CascadeClassifier(_current_cascade)

    @classmethod
    def load(cls, path=FRONTALFACE_DEFAULT):
        """Load cascade xml file and save to _current_cascade
        path -- the path of the file (default FRONTALFACE_DEFAULT).
        """

        if path != cls._current_cascade:
            cls._current_cascade = path
            cls._classifier = cv2.CascadeClassifier(path)

    @classmethod
    def read_image(cls, image_path):
        """ Read image from path BGR
        image_path -- The path of the image.
        """

        return cv2.imread(image_path)

    @classmethod
    def bgr_to_rgb(cls, image):
        """ Conver BGR image to RGB
        image -- The image (numpy matrix) read by readImage function.
        """

        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    @classmethod
    def bgr_to_gray(cls, image):
        """ Conver BGR image to gray
        image -- The image (numpy matrix) read by readImage function.
        """

        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    @classmethod
    def detect(cls,
               image,
               min_size=(50, 50),
               scale_factor=1.1,
               min_neighbors=5,
               cascade_file=_current_cascade):
        """ Return list of objects detected.
        image -- The image (numpy matrix) read by readImage function.
        min_size -- Minimum possible object size. Objects smaller than that are ignored (default (50,50)).
        scale_factor -- Specifying how much the image size is reduced at each image scale (default 1.1).
        min_neighbors -- Specifying how many neighbors each candidate rectangle should have to retain it (default 5).
        cascade_file  -- The path of cascade xml file use for detection (default current value)
        """

        classifier = cls._classifier
        if cascade_file != cls._current_cascade:
            classifier = cv2.CascadeClassifier(cascade_file)

        gray_image = cls.bgr_to_gray(image)
        return classifier.detectMultiScale(gray_image,
                                           scaleFactor=scale_factor,
                                           minNeighbors=min_neighbors,
                                           minSize=min_size)

    @classmethod
    def extract(cls,
                image_path,
                size=None,
                scale_factor=1.1,
                min_neighbors=5,
                min_size=(50, 50),
                cascade_file=_current_cascade,
                output_directory=None,
                output_prefix=None,
                start_count=0):
        """ Extract the objects from image and return number of objects detected
        image_path -- The path of the image.
        size -- Size of face images (default None - no rescale at all)
        image -- The image (numpy matrix) read by readImage function.
        min_size -- Minimum possible object size. Objects smaller than that are ignored (default (50,50)).
        scale_factor -- Specifying how much the image size is reduced at each image scale (default 1.1).
        min_neighbors -- Specifying how many neighbors each candidate rectangle should have to retain it (default 5).
        cascade_file  -- The path of cascade xml file use for detection (default current value)
        output_directory -- Directory where to save output (default None - same as input image)
        output_prefix -- Prefix of output (default None - the name of input image)
        startCout -- Specifying the starting of the number put into output names (default 0)
        """

        image = cls.read_image(image_path)
        objects = cls.detect(image,
                             scale_factor=scale_factor,
                             min_neighbors=min_neighbors,
                             min_size=min_size,
                             cascade_file=cascade_file)
        idx = start_count
        if not output_prefix:
            output_prefix = os.path.splitext(os.path.split(image_path)[1])[0]
        if not output_directory:
            output_directory = os.path.split(image_path)[0]
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        for (x, y, w, h) in objects:
            obj = image[y:y + h, x:x + w]
            obj_path = os.path.join(
                output_directory, output_prefix + '_' + str(idx) + '.jpg')
            if size:
                obj = cv2.resize(obj, size)
            cv2.imwrite(obj_path, obj)
            idx += 1
        return len(objects)
