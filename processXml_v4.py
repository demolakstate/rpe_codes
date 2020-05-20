
import os

import xml.etree.ElementTree as ET



img_list = os.listdir('/data/blackveatch/Object-Detection/validation/annotations_val/xmls')

for img in img_list:

	tree = ET.parse('/data/blackveatch/Object-Detection/validation/annotations_val/xmls/{}'.format(img))

	root = tree.getroot()

	#for child in root:
	#	print(child.tag)


	#for elem in root.iter():
	#	print(elem.tag)


	for filename in root.iter('filename'):
		print(filename.text)
		filename.text = filename.text.replace(' ', '')


	tree.write('/data/blackveatch/Object-Detection/validation/annotations_val/xmls/{}'.format(img))
