# PROGRAM PEMBUATAN CLASSIFIERS knn
import numpy as np
import operator

# pembuatan konstanta
nTetangga = 83

# pembuatan fungsi dan prosedur
def loadData(split=0.6): # mengambil data dari file
	with open("Train.txt") as f:
		data_set = np.loadtxt(f,skiprows=1,usecols=(x for x in range(1,12)))

		data_train = data_set[:int(len(data_set)*split)]
		data_test =  data_set[int(len(data_set)*split):]

		# train_feat = train_set[:,0:10]
		# train_class = train_set[:,10]

		return data_train, data_test#,train_feat, train_class
	# akhir fungsi load

def euclideandistance(p1, p2): # mencari eucledian distance antara 2 buah data p1  dan p2
	p1 = p1[0:10]
	p2 = p2[0:10]
	return np.linalg.norm(np.array(p1)-np.array(p2))
	# akhir fungsi eucledeandistance

def kumpulanTetangga(datatrain, onedatatest, k):
	distances = []
	for x in xrange(len(datatrain)):
		dist = euclideandistance(onedatatest, datatrain[x])
		distances.append((datatrain[x], dist))
		distances.sort(key=operator.itemgetter(1))
	# copy = datatrain[:]
	tetangga=[]
	for x in xrange(k):
		# index = distances.index(min(distances))
		# distances.pop(distances.index(min(distances)))
		# tetangga.append(copy.tolist().pop(index))
		tetangga.append(distances[x][0])

	return tetangga
	# akhir fungsi kumpulanTetangga

def tentukanclass(tetangga):
	jumlahClass = [0 for x in xrange(2)]
	for x in xrange(len(tetangga)):
		if 1.0 == tetangga[x][-1]:
			jumlahClass[1] += 1
		else:
			jumlahClass[0] += 1
	return jumlahClass.index(max(jumlahClass))
	# akhir tentukanclass

def knn(datatrain, datates, k):
	tetangga = kumpulanTetangga(datatrain, datates, k)
	return tentukanclass(tetangga)
	# akhir 


# data1 = [2, 2, 2]
# data2 = [4, 4, 4]
# distance = euclideandistance(data1, data2)
# print 'Distance: ' + repr(distance)



# pengambilan data
data_train, data_test = loadData()
print "jumlah data train:", len(data_train)
print "jumlah data test:", len(data_test)
# inisialisasi
k = nTetangga
# memulai k-nearest neighbor
akurasi = 0

for x in range(len(data_test)):
	hasil = knn(data_train, data_test[x], k)
	print  "hasil :",hasil,", target nyata :",data_test[x][-1]
	if  hasil == data_test[x][-1]:
		akurasi +=1
	print "jumlah benar :",akurasi,"dari",x+1,"data"

print 1.*akurasi/len(data_test)
