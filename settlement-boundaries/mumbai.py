from pathlib import Path

import contextily as cx
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# sns.set()

data = Path.home()/"Documents/workspace/research/slum-mapping/"

def clean(show = True, ax = None):
    ax = ax if ax else plt.gca()
    ax.set_xticks([])
    ax.set_yticks([])
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1)
    if show: plt.show()

# map changes over time
nm = gpd.read_file(data/"mumbai-pollution-sources/navi_mumbai_industrial.geojson")

changes = gpd.read_file(data/"DLR/Endergebnis/Mumbai_Change_Detection_1973_1990_2001_2010.shp")\
    .assign(year = lambda df: df["class"].astype(int))\
    .to_crs(nm.crs)

changes_sample = changes[changes.year != 1].sample(len(changes) // 10, random_state = 0)
ax = changes_sample.plot(column = "year", linewidth = 0, categorical = True, legend = True)
nm.plot(color = "k", label = "Navi Mumbai industrial sites", ax = ax)
ax.set_xticks([])
ax.set_yticks([])
cx.add_basemap(ax, crs = changes_sample.crs.to_string(), source = cx.providers.CartoDB.Positron, zoom = 12)
plt.show()



cx.Place("Mumbai, Maharashtra, India", zoom = 8, source = cx.providers.NASAGIBS.ViirsEarthAtNight2012).plot()
