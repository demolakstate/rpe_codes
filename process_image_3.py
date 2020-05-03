import cv2, os
import numpy as np

# list images

img_list = os.listdir('images')

img_tuple = ()
img_tuple_2 = ()
img_tuple_3 = ()
img_tuple_4 = ()
img_tuple_5 = ()
img_tuple_6 = ()
img_tuple_7 = ()

print(img_list)

for i, img in enumerate(img_list):
	image = cv2.imread(f'/data/RPE/Data_preprocessing_3/images/{img}')
	if i < 50:
		img_tuple = list(img_tuple)
		img_tuple.append(image)
		img_tuple = tuple(img_tuple)
	elif i < 100:
		img_tuple_2 = list(img_tuple_2)
		img_tuple_2.append(image)
		img_tuple_2 = tuple(img_tuple_2)
	elif i < 150:
		img_tuple_3 = list(img_tuple_3)
		img_tuple_3.append(image)
		img_tuple_3 = tuple(img_tuple_3)
	elif i < 200:
		img_tuple_4 = list(img_tuple_4)
		img_tuple_4.append(image)
		img_tuple_4 = tuple(img_tuple_4)
	elif i < 250:
		img_tuple_5 = list(img_tuple_5)
		img_tuple_5.append(image)
		img_tuple_5 = tuple(img_tuple_5)
	elif i < 300:
		img_tuple_6 = list(img_tuple_6)
		img_tuple_6.append(image)
		img_tuple_6 = tuple(img_tuple_6)
	else:
		img_tuple_7 = list(img_tuple_7)
		img_tuple_7.append(image)
		img_tuple_7 = tuple(img_tuple_7)
		


#image_2 = cv2.imread(f'/data/RPE/Data_preprocessing_3/images/1_33.jpg')
# I just resized the image to a quarter of its original size
#image = cv2.resize(image, (0, 0), None, .25, .25)

#grey = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# Make the grey scale image have three channels
#grey_3_channel = cv2.cvtColor(grey, cv2.COLOR_GRAY2BGR)

#numpy_vertical = np.vstack((img_tuple))
numpy_horizontal = np.hstack((img_tuple))
numpy_horizontal_2 = np.hstack((img_tuple_2))
numpy_horizontal_3 = np.hstack((img_tuple_3))
numpy_horizontal_4 = np.hstack((img_tuple_4))
numpy_horizontal_5 = np.hstack((img_tuple_5))
numpy_horizontal_6 = np.hstack((img_tuple_6))
numpy_horizontal_7 = np.hstack((img_tuple_7))

#numpy_vertical_concat = np.concatenate((image, image_2), axis=0)
#numpy_horizontal_concat = np.concatenate((image, image_2), axis=1)

#cv2.imshow('Main', image)
#cv2.imshow('Numpy Vertical', numpy_vertical)
#cv2.imshow('Numpy Horizontal', numpy_horizontal)
cv2.imwrite('./0.jpg', numpy_horizontal)
cv2.imwrite('./1.jpg', numpy_horizontal_2)
cv2.imwrite('./2.jpg', numpy_horizontal_3)
cv2.imwrite('./3.jpg', numpy_horizontal_4)
cv2.imwrite('./4.jpg', numpy_horizontal_5)
cv2.imwrite('./5.jpg', numpy_horizontal_6)
cv2.imwrite('./6.jpg', numpy_horizontal_7)




#cv2.imshow('Numpy Vertical Concat', numpy_vertical_concat)
#cv2.imshow('Numpy Horizontal Concat', numpy_horizontal_concat)

#cv2.waitKey()
