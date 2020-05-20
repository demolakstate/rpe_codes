from xml.dom import minidom

mydoc = minidom.parse('/data/blackveatch/Object-Detection/validation/annotations_val/xmls/616.xml')

items = mydoc.getElements()


for item in items:
	print(item)
