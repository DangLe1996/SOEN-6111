

import pandas as pd

liveData = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv",  dtype={"fips": str})
import json
from urllib.request import urlopen
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
#%%

from sklearn.cluster import AgglomerativeClustering
km = AgglomerativeClustering(n_clusters=10 )
test = liveData[['county','cases']]
#%%
km.fit(liveData[['cases']])
liveData['classification'] = km.labels_
#%%

import plotly.graph_objects as go
fig = go.Figure(go.Choroplethmapbox(geojson=counties, locations=liveData.fips, z=liveData.classification,
                                    colorscale="Viridis", zmin=0, zmax=10,
                                    marker_opacity=0.5, marker_line_width=0))
fig.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show(renderer="browser")
#%%



