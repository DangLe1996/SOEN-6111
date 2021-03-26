from dask import dataframe as df
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv('covid.csv')
# print(data)
#print(type(data))
# print(data["County Name"])
# print(data["2021-03-23"])


df = pd.DataFrame(data, columns=['2020-03-23', '2021-03-23'])
#print(df.head(100))

'''
plt.scatter(df["County Name"], df["2021-03-23"])
plt.xlabel("County Name")
plt.ylabel("2021-03-23")
plt.show()
'''

km = KMeans(n_clusters=8, init='random', n_init=1, max_iter=300, random_state=0)
km.fit(df)
km.labels_
km.cluster_centers_




data['classification'] = km.labels_.tolist()

print(data["classification"].head())


