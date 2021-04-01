

#%%
import pandas as pd
total_live_data = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
total_recent = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties-recent.csv"
live_data = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv'
#%%

liveData = pd.read_csv(total_live_data,  dtype={"fips": str})

#%%

covidData = liveData[['date','fips','cases']]

#%%

groupData = covidData.set_index('date').groupby('fips')
fips = list(groupData.fips.groups.keys())
resultgroupBy = groupData['cases'].apply(list).reset_index(name = 'new')
#%%
testData = resultgroupBy['new'].apply(lambda r: r[-100:]).to_list()
import numpy as np
result = np.array(testData)

#%%

from sklearn.cluster import KMeans

km = KMeans(n_clusters=10, init='random', n_init=1, max_iter=300, random_state=0)
km.fit(result)
#%%

finalDF = pd.DataFrame(data = fips)
finalDF = finalDF.rename(columns = {0:'fips'})
finalDF['classification'] = km.labels_

#%%
import json
from urllib.request import urlopen
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

#%%
print('Begin plotting')
import plotly.graph_objects as go
fig = go.Figure(go.Choroplethmapbox(geojson=counties, locations=finalDF['fips'], z=finalDF['classification'],
                                    colorscale="Viridis", zmin=0, zmax=10,
                                    marker_opacity=0.5, marker_line_width=0))
fig.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
























