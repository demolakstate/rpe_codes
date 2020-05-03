import cv2, os
import numpy as np

# list images

img_list = os.listdir('images')

print(img_list)

image = cv2.imread('/data/RPE/Data_preprocessing_3/images/1_4.jpg')
image_2 = cv2.imread('/data/RPE/Data_preprocessing_3/images/1_33.jpg')
# I just resized the image to a quarter of its original size
#image = cv2.resize(image, (0, 0), None, .25, .25)

#grey = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# Make the grey scale image have three channels
#grey_3_channel = cv2.cvtColor(grey, cv2.COLOR_GRAY2BGR)

numpy_vertical = np.vstack((image, image_2, image))
numpy_horizontal = np.hstack((image, image_2, image))

#numpy_vertical_concat = np.concatenate((image, image_2), axis=0)
#numpy_horizontal_concat = np.concatenate((image, image_2), axis=1)

#cv2.imshow('Main', image)
cv2.imshow('Numpy Vertical', numpy_vertical)
cv2.imshow('Numpy Horizontal', numpy_horizontal)
#cv2.imshow('Numpy Vertical Concat', numpy_vertical_concat)
#cv2.imshow('Numpy Horizontal Concat', numpy_horizontal_concat)

cv2.waitKey()
