import sklearn
import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris
iris = load_iris()

print iris.feature_names
print iris.target_names

print iris.data[0]
print iris.target[0]

test_idx = [0,50,100]

#training data
training_target = np.delete(iris.target,test_idx)
training_data = np.delete(iris.data,test_idx,axis = 0)

#testing data 
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(training_data,training_target)

print test_target
print clf.predict(test_data)
