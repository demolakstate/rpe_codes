
import os
from random import sample

data = os.listdir('/data/RPE/Non_GAN_experiments/r-fcn/Object-Detection_rfcn_version_15_percent_validation_2nd_fold/images')




fold_1 = ['439', '385', '341', '363', '343', '366', '381', '495', '298', '347', '440', '427', '331', '304', '310', '296', '345']

print('data', data)

def removeFold_1(data, fold):
	for f in fold:
		data.remove(f + '.jpg')

	return


def removeFold(data, fold):
	for f in fold:
		data.remove(f)

	return


print(len(data))
removeFold_1(data, fold_1)

fold_2 = sample(data, 17)


print(len(data))
removeFold(data, fold_2)

fold_3 = sample(data, 17)


print(len(data))
removeFold(data, fold_3)	

fold_4 = sample(data, 17)


print(len(data))
removeFold(data, fold_4)


fold_5 = sample(data, 17)


print(len(data))
removeFold(data, fold_5)


fold_list_2 = list()
for f in fold_2:
	fold_list_2.append(str(f[:-4]))	



fold_list_3 = list()
for f in fold_3:
	fold_list_3.append(str(f[:-4]))



fold_list_4 = list()
for f in fold_4:
	fold_list_4.append(str(f[:-4]))



fold_list_5 = list()
for f in fold_5:
	fold_list_5.append(str(f[:-4]))



print('fold_list_1:', len(fold_1), ' ', fold_1)
print('fold_list_2:', len(fold_list_2), ' ', fold_list_2)
print('fold_list_3:', len(fold_list_3), ' ', fold_list_3)
print('fold_list_4:', len(fold_list_4), ' ', fold_list_4)
print('fold_list_5:', len(fold_list_5), ' ', fold_list_5)





