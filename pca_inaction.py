import numpy as np

#load dummy dataset
X = np.random.randint(10,50,100).reshape(20,5)
#center the data 
X_meaned = X - np.mean(X, axis = 0)

print(X)
#print (X_meaned)
#calculate covariance matrix
conv_mat = np.cov(X_meaned, rowvar = False)

#eigen values & eigen vectors
eigen_values, eigen_vectors = np.linalg.eigh(conv_mat)
sorted_index = np.argsort(eigen_values)[::-1]

sorted_eigenvalue = eigen_values[sorted_index]
sorted_eignvectors = eigen_vectors[sorted_index]

#select rearranged subset
n_components = 2
eigenvec_subset = sorted_eignvectors[:,0:n_components]

#transform the data to graphs
X_reduced = np.dot(eigenvec_subset.transpose(), X_meaned.transpose()).transpose()
print(X_reduced)