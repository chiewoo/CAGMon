#/usr/bin/python

import numpy as np
import math
from sklearn.decomposition import PCA
import pylab as pl
import matplotlib as plt

# Data Preprocessing

# Load Aux data sets

aux_data=np.loadtxt('rmvd_null.txt')
aux_class=np.loadtxt('rmvd_null_class.txt')


# PCA Analysis

X=aux_data
y=aux_class
target_names = ['class 1','class 2']

pca=PCA(n_components=2)
X_r=pca.fit(X).transform(X)

# Percentage of variance explained for each components                                                                    
print('explained variance ratio (first two components): %s'
      % str(pca.explained_variance_ratio_))


# Plotting

plt.pyplot.figure()
for c, i, target_name in zip("brg", [0, 1, 2], target_names):
    plt.pyplot.scatter(X_r[y == i, 0], X_r[y == i, 1], c=c, label=target_name)
plt.pyplot.legend()
plt.pyplot.title('PCA of AuxData')

plt.pyplot.savefig("pca_aux.png")
plt.pyplot.show()
