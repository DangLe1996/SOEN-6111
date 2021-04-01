import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# Importing the mall dataset with pandas

dataset = pd.read_csv('covid.csv')

df = pd.DataFrame(dataset, columns=['2020-03-23', '2021-03-23'])

# Using the elbow method to find the optimal number of clusters
'''
from sklearn.cluster import KMeans
wcss =[]
for i in range (1,50):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter =300, n_init = 10, random_state = 0)
    kmeans.fit(df)
    wcss.append(kmeans.inertia_)

# Plot the graph to visualize the Elbow Method to find the optimal number of cluster
plt.plot(range(1,50),wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

'''
distortions = []
max_k = 10
for i in range(1, max_k + 1):
    km = KMeans(n_clusters = i, init = 'k-means++', max_iter =300, n_init = 10, random_state = 0)
    km.fit(df)
    distortions.append(km.inertia_)

plt.plot(range(1, max_k + 1), distortions, marker='o')
plt.xlabel('Cluster count (k)')
plt.ylabel('Distortion')
plt.show()
