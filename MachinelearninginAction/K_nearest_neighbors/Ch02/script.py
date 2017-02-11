import numpy as np
import operator
import kNN

groups,labels = kNN.createDataSet()

print(groups)
print(labels)

def classify0(inX,dataSet,labels,k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX,(dataSetSize,1)) - dataSet # calculating the distance using Eucledian distance formula ie (x2-x1) and (y2-y1) in the formula sqrt((x2-x1)**2 + (y2-y1)**2)
	sqDiffMat = diffMat**2 # is (x2-x1)**2 & (y2-y1)**2
	sqDistances = sqDiffMat.sum(axis = 1) # is (x2-x1)**2 + (y2-y1)**2
	distances = sqDistances**0.5 #is sqrt((x2-x1)**2 + (y2-y1)**2)
	sortedDistIndicies = distnaces.argsort() # sorting distances from lowest to highest based on their indicies
	classCount = {}
	for i in range(k):
		voteIlabel  = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	sortedClassCount = sorted(classCount.iteritems(),key = operator.itemgetter(1),reverse = True)
	return sortedClassCount [0] [0]



'''import kNN
reload(kNN)
datingDataMat,datingLabels = kNN.file2matrix('datingTestSet.txt')
import matplotlib
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
plt.show()

fig2 = plt.figure();ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1], datingDataMat[:,2],15.0*np.array(datingLabels), 15.0*np.array(datingLabels))
plt.show()
'''
import pandas as pd
import numpy as np

df = pd.DataFrame(data = np.random.rand(5,5),columns=["A","B","C","D","E"])

minVals = df.min(1)

print minVals

a = np.tile(minVals,(50,1))
print type(a)



