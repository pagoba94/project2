import pandas as pd
import re
import seaborn as sns
import os
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.offline as opy
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

import src.downloading as dl
import src.cleaning as cl
import src.visualization as vis


df= dl.downloading_csv('data/happiness-2015.csv')
print("Downloading happiness-2015")
df2017= dl.downloading_csv('data/happiness-2017.csv')
print("Downloading happiness-2017")
df2019= dl.downloading_csv('data/happiness-2019.csv')
print("Downloading happiness-2019")
df2021= dl.downloading_csv('data/happiness-2021.csv')
print("Downloading happiness-2021")
df2=dl.downloading_html('https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature')
print("Downloading html-average_yearly_temperature")

df = cl.cleaning_df2015(df, df2)
print("cleaning_df2015")
df2017=cl.cleaning_df2017(df2017)
print("cleaning_df2017")
df2019=cl.cleaning_df2019(df2019)
print("cleaning_df2019")
df2021=cl.cleaning_df2021(df2021)
print("cleaning_df2021")
df=cl.merging_df(df,df2017,df2019,df2021)
print("merging dfs")
df= cl.mean_columns(df)
print("creating mean_columns")
df=cl.population_df(df)
print("adding population column")

vis.happiness_temperature_scatter(df)
vis.happiness_temperature(df)
vis.happiness_worldmap(df)
vis.happiness_GDP(df)