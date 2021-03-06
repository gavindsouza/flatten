# ref images at https://www.effigis.com/en/solutions/satellite-images/satellite-image-samples/
# my notebook ~ flatten/_refs
# colab trials ~ https://colab.research.google.com/drive/1ETj5ytlNOHSUrMc31JM6EDWdqeXLxMJg#scrollTo=Jd918I5mLtk1

from numpy.fft import fft2, ifft2
import numpy as np
import cv2


class Compress:
    def __init__(self, img):
        self.img = img
        # self.mask = np.zeros(img.shape)
        self.r, self.g, self.b = cv2.split(img)

        self.fft2d_r = fft2(self.r)
        self.fft2d_g = fft2(self.g)
        self.fft2d_b = fft2(self.b)

        self.fft2_img = np.zeros(img.shape)

        self.fft2_img[..., 0] = self.fft2d_r
        self.fft2_img[..., 1] = self.fft2d_g
        self.fft2_img[..., 2] = self.fft2d_b

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
        c_img = np.zeros(shape=self.img)
        th_r, th_g, th_b = self.__thresh__(x)

        for i in range(len(self.fft2_img)):  # row
            for j in range(len(self.fft2_img[i])):  # column
                if self.fft2_img[i][j][0] < th_r:
                    self.fft2_img[i][j][0] = 0
                if self.fft2_img[i][j][0] < th_g:
                    self.fft2_img[i][j][0] = 0
                if self.fft2_img[i][j][0] < th_b:
                    self.fft2_img[i][j][0] = 0

        r = ifft2(self.fft2_img[..., 0])
        g = ifft2(self.fft2_img[..., 1])
        b = ifft2(self.fft2_img[..., 2])

        c_img[..., 0], c_img[..., 1], c_img[..., 2] = r, g, b

        return c_img

    def compress_okay(self):
        x = 0.005
        c_img = self.img.copy()
        th_r, th_g, th_b = self.__thresh__(x)

        c_img[self.fft2_img[..., 0] < th_r] = 0
        c_img[self.fft2_img[..., 1] < th_g] = 0
        c_img[self.fft2_img[..., 2] < th_b] = 0

        for i in range(3):  # three channels
            c_img[..., i] = ifft2(c_img[..., i])

        return c_img

    def compress_hard(self):
        x = 0.01
        c_img = self.img.copy()
        th_r, th_g, th_b = self.__thresh__(x)

        c_img[self.fft2_img[..., 0] < th_r] = 0
        c_img[self.fft2_img[..., 1] < th_g] = 0
        c_img[self.fft2_img[..., 2] < th_b] = 0

        for i in range(3):  # three channels
            c_img[..., i] = ifft2(c_img[..., i])

        return c_img


"""
from my notebook reference :: added ref 

img_ = plt.imread('nystylepizza.png')
r, g, b = cv2.split(img_)
r, g, b = fft2(r), fft2(g), fft2(b)

r[r < np.average(r)] = 0
g[g < np.average(g)] = 0
b[b < np.average(b)] = 0

r, g, b = ifft2(r), ifft2(g), ifft2(b)

img_[..., 0] = r
img_[..., 1] = g
img_[..., 2] = b

plt.imshow(abs(img))

"""
