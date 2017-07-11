# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 22:59:52 2017

@author: thienbui
"""

import cv2
import os


class Extractor:
    HAARCASCADE_ALT = os.path.join(os.path.dirname(__file__),'data','haarcascade_frontalface_alt.xml')
    HAARCASCADE_ALT2 = os.path.join(os.path.dirname(__file__),'data','haarcascade_frontalface_alt2.xml')
    HAARCASCADE_ALT_TREE = os.path.join(os.path.dirname(__file__),'data','haarcascade_frontalface_alt_tree.xml')
    HAARCASCADE_DEFAULT = os.path.join(os.path.dirname(__file__),'data','haarcascade_frontalface_default.xml')
    _current_cascade = HAARCASCADE_DEFAULT
    _classifier = cv2.CascadeClassifier(_current_cascade)

    @classmethod
    def load(cls,path = HAARCASCADE_DEFAULT):

        """Load cascade xml file and save to _current_cascade
        path -- the path of the file (default HAARCASCADE_DEFAULT).
        """

        if path != cls._current_cascade:
            cls._current_cascade = path
            cls._classifier = cv2.CascadeClassifier(path)

    @classmethod
    def readImage(cls, imagePath):

        """ Read image from path BGR
        imagePath -- The path of the image.
        """

        return cv2.imread(imagePath)

    @classmethod
    def bgrToRGB(cls, image):
        """ Conver BGR image to RGB
        image -- The image (numpy matrix) read by readImage function.
        """
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    @classmethod
    def bgrToGray(cls, image):

        """ Conver BGR image to gray
        image -- The image (numpy matrix) read by readImage function.
        """

        return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    @classmethod
    def detect(cls,
               image,
               minSize = (50, 50),
               scaleFactor = 1.1,
               minNeighbors = 5,
               cascadeFile = _current_cascade):

        """ Return list of faces detected.
        image -- The image (numpy matrix) read by readImage function.
        minSize -- Minimum possible object size. Objects smaller than that are ignored (default (50,50)).
        scaleFactor -- Specifying how much the image size is reduced at each image scale (default 1.1).
        minNeighbors -- Specifying how many neighbors each candidate rectangle should have to retain it (default 5).
        cascadeFile  -- The path of cascade xml file use for detection (default current value)
        """

        classifier = cls._classifier
        if cascadeFile != cls._current_cascade:
            classifier = cv2.CascadeClassifier(cascadeFile)

        grayImage = cls.bgrToGray(image)
        return classifier.detectMultiScale(grayImage,
                                           scaleFactor = scaleFactor,
                                           minNeighbors = minNeighbors,
                                           minSize = minSize)

    @classmethod
    def extract(cls,
                imagePath,
                size = None,
                scaleFactor = 1.1,
                minNeighbors = 5,
                minSize = (50, 50),
                cascadeFile = _current_cascade,
                outputDirectory = None,
                outputPrefix = None,
                startCount = 0):

        """ Extract the faces from image and return list of faces detected
        imagePath -- The path of the image.
        size -- Size of face images (default None - no rescale at all)
        image -- The image (numpy matrix) read by readImage function.
        minSize -- Minimum possible object size. Objects smaller than that are ignored (default (50,50)).
        scaleFactor -- Specifying how much the image size is reduced at each image scale (default 1.1).
        minNeighbors -- Specifying how many neighbors each candidate rectangle should have to retain it (default 5).
        cascadeFile  -- The path of cascade xml file use for detection (default current value)
        outputDirectory -- Directory where to save output (default None - same as input image)
        outputPrefix -- Prefix of output (default None - the name of input image)
        startCout -- Specifying the starting of the number put into output names (default 0)
        """

        image = cls.readImage(imagePath)
        faces = cls.detect(image,
                           scaleFactor = scaleFactor,
                           minNeighbors = minNeighbors,
                           minSize = minSize,
                           cascadeFile = cascadeFile)
        idx = startCount
        if not outputPrefix:
            outputPrefix = os.path.splitext(os.path.split(imagePath)[1])[0]
        if not outputDirectory:
            outputDirectory = os.path.split(imagePath)[0]
        if not os.path.exists(outputDirectory):
            os.makedirs(outputDirectory)
        for (x, y, w, h) in faces:
            faceSize = max(w,h)
            face = image[y:y + faceSize,x:x + faceSize]
            facePath = os.path.join(outputDirectory,outputPrefix + '_'+str(idx)+'.jpg')
            if size:
                face = cv2.resize(face, (size,size))
            cv2.imwrite(facePath,face)
            idx += 1
        return faces