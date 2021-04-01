from urllib.request import urlopen
import json
from sklearn.cluster import AgglomerativeClustering
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
import pandas as pd
data = pd.read_csv('data/covid_confirmed_usafacts.csv')

df = pd.DataFrame(data, columns=['2020-03-23', '2021-03-23'])
df1 = data.iloc[:, 4:]

km = AgglomerativeClustering(n_clusters=10 )
km.fit(df1)
km.labels_
data['classification'] = km.labels_.tolist()

new_df = data[['countyFIPS', 'classification']]


import plotly.graph_objects as go

fig = go.Figure(go.Choroplethmapbox(geojson=counties,  locations=new_df['countyFIPS'],
                                    z=new_df['classification'],
                                    colorscale="Viridis", zmin=0, zmax=12,
                                    marker_opacity=0.5, marker_line_width=0))
fig.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()



import plotly.express as px

fig = px.choropleth(new_df, geojson=counties, locations='countyFIPS', color='classification',
                           color_continuous_scale="Viridis",
                           range_color=(0, 10),
                           scope="usa",
                           labels={'classification':'cluster'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()