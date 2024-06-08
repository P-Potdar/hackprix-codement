import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd
import glob2
import os, fnmatch
from pathlib import Path


from mtcnn.mtcnn import MTCNN
def extract_multiple_videos(intput_filenames, image_path_infile):

i = 1  
    cap = cv2.VideoCapture('your_video_file_path.avi' or intput_filenames)
if (cap.isOpened()== False):
        print("Error opening file")

while True:
        ret, frame = cap.read() 
            
        if ret:
            cv2.imwrite(os.path.join(image_path_infile , str(i) + '.jpg'), frame)

            cv2.imshow('frame', frame)  
        i += 1
        else:

            break

cv2.waitKey(50) #Wait 50msec
cap.release()
from skimage import measure
def mse(imageA, imageB):

    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    return err
def compare_images(imageA, imageB, title):
    m = mse(imageA, imageB)
    s = measure.compare_ssim(imageA, imageB)
    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA, cmap = plt.cm.gray)
    plt.axis("off")
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap = plt.cm.gray)
    plt.axis("off")
    plt.show()