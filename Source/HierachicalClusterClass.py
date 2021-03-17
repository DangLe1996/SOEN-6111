from sklearn.cluster import AgglomerativeClustering as AC
import os
import pathlib
from utils import readDataClass as RC
import numpy as np
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering


rootDir = pathlib.Path(__file__).parent.parent
dataDir = os.path.join(rootDir,'data')
datapath = os.path.join(dataDir,'covid_confirmed_usafacts.csv')

dataObj = RC(datapath)

startDate = '10/11/20'
endDate = '11/11/20'

dataInterval = dataObj.getCountyDateInterval(startDate, endDate, 10).compute().T

result = dataObj.dataDF[dataObj.dataDF.apply(dataObj.filterByCounty,axis = 1)]

stateData = dataObj.getDateInterval(dataObj.filterByState,startDate,endDate,10)
countyDate = dataObj.getDateInterval(dataObj.filterByCounty,startDate,endDate,10)

def hierachicalClustering(data):
    model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)
    model.fit(data)
    plt.title('Hierarchical Clustering Dendrogram')
    # plot the top three levels of the dendrogram
    plot_dendrogram(model, truncate_mode='level', p=3)
    plt.xlabel("Number of points in node (or index of point if no parenthesis).")
    plt.show()

def plot_dendrogram(model, **kwargs):
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack([model.children_, model.distances_,
                                      counts]).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)


model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)

model = model.fit(dataInterval)
plt.title('Hierarchical Clustering Dendrogram')
# plot the top three levels of the dendrogram
plot_dendrogram(model, truncate_mode='level', p=3)
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show()

iris = load_iris()
X = iris.data

# setting distance_threshold=0 ensures we compute the full tree.
model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)

model = model.fit(X)
plt.title('Hierarchical Clustering Dendrogram')
# plot the top three levels of the dendrogram
plot_dendrogram(model, truncate_mode='level', p=3)
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show()