# PROGRAM PEMBUATAN CLASSIFIERS ID3 
import numpy as np
from decimal import Decimal

# pembuatan fungsi dan prosedur
def load(): # mengambil data dari file
	with open("Train.txt") as f:
		train_set = np.loadtxt(f,skiprows=1,usecols=(x for x in range(1,12)))

		# train_feat = [[round(Decimal(train_set[x][y]),3) for y in range(len(train_set[x])-1)] for x in range(len(train_set))] SALAH
		# train_class = [int(train_set[i][10]) for i in range(len(train_set))] SALAH
		train_feat = train_set[:,0:10]
		train_class = train_set[:,10]

		return train_feat, train_class
		# akhir fungsi load
def entropi(train_y):
	index = [np.where(train_y == float(i)) for i in range(2)]
	# print index[0][0]
	# print index[1][0]
	print len(index[0][0]), len(index[1][0])
	# print len(index[0][0])+len(index[1][0])
	p = [(1.0*len(index[i][0]))/len(train_y) for i in range(len(index))]
	# print p[0]
	# print p[1]
	# print p[0]+p[1]
	rumus = [p[i]*np.log2(p[i]) for i in range(len(index))]

	return -1*sum(rumus)
def gain(S,train_y):
	
	pass


# pengambilan data
train_x, train_y = load()

print train_x[0],train_y[0]
print entropi(train_y)

# learning


# testing
# testing akurasi