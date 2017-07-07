# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 22:59:52 2017

@author: thienbui
"""

import cv2
import os

class Extractor:
    HAARCASCADE_ALT = 'data/haarcascade_frontalface_alt.xml'
    HAARCASCADE_ALT2 = 'data/haarcascade_frontalface_alt2.xml'
    HAARCASCADE_ALT_TREE = 'data/haarcascade_frontalface_alt_tree.xml'
    HAARCASCADE_DEFAULT = 'data/haarcascade_frontalface_default.xml'
    _current_cascade = HAARCASCADE_DEFAULT
    _classifier = cv2.CascadeClassifier(_current_cascade)

    @classmethod
    def load(cls,path = HAARCASCADE_DEFAULT):
        if path != cls._current_cascade:
            cls._current_cascade = path
            cls._classifier = cv2.CascadeClassifier(path)

    @classmethod
    def readImage(cls, imagePath):
        return cv2.imread(imagePath)

    @classmethod
    def colorToGray(cls, image):
        return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    @classmethod
    def detect(cls,
               image,
               minSize = (50, 50),
               scaleFactor = 1.1,
               minNeighbors = 5,
               cascadeFile = _current_cascade):

        classifier = cls._classifier
        if cascadeFile != cls._current_cascade:
#            print(cascadeFile, cls._current_cascade)
            classifier = cv2.CascadeClassifier(cascadeFile)

        grayImage = cls.colorToGray(image)
        return classifier.detectMultiScale(grayImage,
                                           scaleFactor = scaleFactor,
                                           minNeighbors = minNeighbors,
                                           minSize = minSize)

    @classmethod
    def extract(cls,
                imagePath,
                scaleFactor = 1.1,
                minNeighbors = 5,
                minSize = (50, 50),
                cascadeFile = _current_cascade):

        cls.extractToSize(imagePath,
                          size = None,
                          scaleFactor = scaleFactor,
                          minNeighbors = minNeighbors,
                          minSize = minSize,
                          cascadeFile = cascadeFile)

    @classmethod
    def extractToSize(cls,
                      imagePath,
                      size = (50,50),
                      scaleFactor = 1.1,
                      minNeighbors = 5,
                      minSize = (50, 50),
                      cascadeFile = _current_cascade):

        image = cls.readImage(imagePath)
        faces = cls.detect(image,
                           scaleFactor = scaleFactor,
                           minNeighbors = minNeighbors,
                           minSize = minSize,
                           cascadeFile = cascadeFile)

        for idx, (x, y, w, h) in enumerate(faces):

            faceSize = max(w,h)
            face = image[y:y + faceSize,x:x + faceSize]
            facePath = os.path.splitext(imagePath)[0]+'_'+str(idx)+'.jpg'

            if size:
                face = cv2.resize(face, size)
            cv2.imwrite(facePath,face)

Extractor.extract('lena.tif',cascadeFile = Extractor.HAARCASCADE_ALT2)