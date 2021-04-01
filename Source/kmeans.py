from urllib.request import urlopen
import json
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
data = pd.read_csv('covid_confirmed_usafacts.csv')



#df = pd.DataFrame(data, columns=['2020-03-23', '2021-03-23'])
df1 = data.iloc[:, 4:]




km = KMeans(n_clusters=10, init='random', n_init=1, max_iter=300, random_state=0)
km.fit(df1)
km.labels_
km.cluster_centers_




data['classification'] = km.labels_.tolist()



new_df = data[['countyFIPS', 'classification']]


silihouette_score = silhouette_score(df1, km.labels_, metric='euclidean')

print("silihouette_score"+str(silihouette_score))

davies_bouldin_score = davies_bouldin_score(df1, km.labels_)
print("davies_bouldin_score"+str(davies_bouldin_score))


import plotly.express as px

fig = px.choropleth(new_df, geojson=counties, locations='countyFIPS', color='classification',
                           color_continuous_scale="Viridis",
                           range_color=(0, 10),
                           scope="usa",
                           labels={'classification':'cluster'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()