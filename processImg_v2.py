
import os

img_list = os.listdir('xmls')

for img in img_list:


  with open("xmls/{}".format(img), 'r') as file_1:
    filedata = file_1.read()


  filedata = filedata.replace('KSU Cloudy', '')
  filedata = filedata.replace('KSU Sunny', '')
  filedata = filedata.replace('KSU PartlyCloudy', '')
  filedata = filedata.replace(' ', '')
  filedata = filedata.replace('(', '')
  filedata = filedata.replace(')', '')
  filedata = filedata.replace('\t', '')

  with open("xmls/{}".format(img), 'w') as file_2:
    file_2.write(filedata)
		
	




# ------
(base) demolakstate@demolakstate:/data/blackveatch/Object-Detection/images$ mmv '*)*' '#1#2'
(base) demolakstate@demolakstate:/data/blackveatch/Object-Detection/images$ mmv '   (*' '#1'
   (* -> #1 : no match.
Nothing done.
(base) demolakstate@demolakstate:/data/blackveatch/Object-Detection/images$ mmv 'KSU Cloudy*' '#1'
(base) demolakstate@demolakstate:/data/blackveatch/Object-Detection/images$ mmv 'KSU PartlyCloudy*' '#1'
(base) demolakstate@demolakstate:/data/blackveatch/Object-Detection/images$ mmv 'KSU Sunny*' '#1'
(base) demolakstate@demolakstate:/data/blackveatch/Object-Detection/images$ mmv '(*' '#1'
(* -> #1 : no match.
Nothing done.
(base) demolakstate@demolakstate:/data/blackveatch/Object-Detection/images$ mmv ' (*' '#1'
(base) demolakstate@demolakstate:/data/blackveatch/Object-Detection/images$ mmv '  (*' '#1'
(base) demolakstate@demolakstate:/data/blackveatch/Object-Detection/images$ mmv '   (*' '#1'
   (* -> #1 : no match.
Nothing done.
(base) demolakstate@demolakstate:/data/blackveatch/Object-Detection/images$ mmv '*)*' '#1#2'




