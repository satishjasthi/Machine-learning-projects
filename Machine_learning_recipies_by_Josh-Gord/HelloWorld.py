#Simple Machine learning program to distinguish between apples and oranges
import sklearn
from sklearn import tree
features = [[140,1],[130,1],[150,0],[170,0]] #[a,b],here a is weight of fruit and 1 is for  apple and 0 is for orange
labels = [0 ,0,1,1]

#defining a Decision tree classifier

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

print clf.predict([160,0])
