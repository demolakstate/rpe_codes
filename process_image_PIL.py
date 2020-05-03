import cv2, os
import numpy as np

# list images

img_list = os.listdir('images')







from PIL import Image

im1 = Image.open('/home/demolakstate/Desktop/celebaHQ_s5_i64000_avg.jpg')
im2 = Image.open('/home/demolakstate/Desktop/celebaHQ_s5_i64000_avg.jpg')

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

get_concat_h(im1, im1).save('pillow_concat_h_2.jpg')
get_concat_v(im1, im1).save('pillow_concat_v_2.jpg')






