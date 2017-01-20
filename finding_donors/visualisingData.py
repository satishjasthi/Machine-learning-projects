#importing modules
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.manifold import TSNE
#to visuialize important characteristics of dataset
import matplotlib.pyplot as plt

#read the data
data = pd.read_csv("census.csv")
num_rows = data.shape[0]
columns = data.columns
columns

#get features and scale them & convert features into a numpy array
x = data.ix[:,:-1]
numerical = ['age','capital-loss','capital-gain','education-num','hours-per-week']
standard_scaler = StandardScaler()
x_std = standard_scaler.fit_transform(x[numerical].values)
#x_std contains only numerical features

#convert y into a dummy variable
y = data.ix[:,-1]
class_labels = np.unique(y)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

#split data into training and testing data
test_percentage = 0.2
x_train,x_test,y_train,y_test = train_test_split(x_std,y,test_size = test_percentage,random_state = 0)

#t-distributed Stochastic Neigbhor Embedding (t-SNE) visualisation
tsne = TSNE(n_components = 2,random_state = 0)
x_test_2d = tsne.fit_transform(x_test)
%qtconsole

markers = ('s','d','o','^','v')
color_map = {0:"red",1:"blue",2:"lightgreen",3:"purple",4:"cyan"}
plt.figure()
for idx,cl in enumerate(np.unique(y_test)):
    plt.scatter(x=x_test_2d[y_test==cl,0], y=x_test_2d[y_test==cl,1], c=color_map[idx], marker=markers[idx], label=cl)
plt.xlabel('X in t-SNE')
plt.ylabel('Y in t-SNE')
plt.legend(loc = "upper left")
plt.title('t-SNE visualization of test data')
plt.show()

m = x_test_2d[y_test=='A',0];
