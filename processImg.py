
import os

img_list = os.listdir('annotations/xmls')

for img in img_list:
   fout = open("annotations/xm/{}".format(img[11:]), "wt")
   f = open("annotations/xmls/{}".format(img), "r")


   for line in f.readlines():
     fout.write(line.replace('BloodImage_', ''))

   f.close()
   fout.close()









