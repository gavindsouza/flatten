# ref images at https://www.effigis.com/en/solutions/satellite-images/satellite-image-samples/

from numpy.fft import fft2, ifft2
import numpy as np
import cv2

import matplotlib.pyplot as plt
import shutil
import requests


class Compress:
    def __init__(self, img):
        self.r, self.g, self.b = cv2.split(img)

        self.fft2d_r = fft2(self.r)
        self.fft2d_g = fft2(self.g)
        self.fft2d_b = fft2(self.b)

        self.max_r = np.amax(self.fft2d_r)
        self.max_g = np.amax(self.fft2d_g)
        self.max_b = np.amax(self.fft2d_b)

    def __thresh__(self, x):
        th_r = abs(0.1 * self.max_r * x)
        th_g = abs(0.1 * self.max_g * x)
        th_b = abs(0.1 * self.max_b * x)

        return th_r, th_g, th_b

    def compress_soft(self):
        x = 0.001
        th_r, th_g, th_b = self.__thresh__(x)

    def compress_okay(self):
        x = 0.005
        th_r, th_g, th_b = self.__thresh__(x)

    def compress_hard(self):
        x = 0.01
        th_r, th_g, th_b = self.__thresh__(x)
