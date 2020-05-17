import os, shutil

file_list = os.listdir('./train/annotations_s')

s = ['174_180', '6_12', '497', '314', '198_204', '349', '302', '347', '340', '144_150', '372', '374', '341', '102_108', '319', '387', '357', '126_132', '495', '267', '312_318', '434', '36_42', '380', '435', '361']

print('files', file_list)

def search(search_list, file_list):
	for item in search_list:
		if item + '.xml' in file_list:
			# move file
			shutil.move('./train/annotations_s/' + item +  '.xml', './train/annotations')




search(s, file_list)


