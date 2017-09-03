# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 22:59:52 2017

@author: thienbui
"""

import cv2
import os


class Extractor:
    _current_dir = os.path.dirname(__file__)
    HAARCASCADE_ALT = os.path.join(
        _current_dir, 'data', 'haarcascade_frontalface_alt.xml')
    HAARCASCADE_ALT2 = os.path.join(
        _current_dir, 'data', 'haarcascade_frontalface_alt2.xml')
    HAARCASCADE_ALT_TREE = os.path.join(
        _current_dir, 'data', 'haarcascade_frontalface_alt_tree.xml')
    HAARCASCADE_DEFAULT = os.path.join(
        _current_dir, 'data', 'haarcascade_frontalface_default.xml')
    _current_cascade = HAARCASCADE_DEFAULT
    _classifier = cv2.CascadeClassifier(_current_cascade)

    @classmethod
    def load(cls, path=HAARCASCADE_DEFAULT):
        """Load cascade xml file and save to _current_cascade
        path -- the path of the file (default HAARCASCADE_DEFAULT).
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
        """ Return list of faces detected.
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
        """ Extract the faces from image and return number of faces detected
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
        faces = cls.detect(image,
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
        for (x, y, w, h) in faces:
            face_size = max(w, h)
            face = image[y:y + face_size, x:x + face_size]
            face_path = os.path.join(
                output_directory, output_prefix + '_' + str(idx) + '.jpg')
            if size:
                face = cv2.resize(face, (size, size))
            cv2.imwrite(face_path, face)
            idx += 1
        return len(faces)
