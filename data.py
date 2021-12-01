import random
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("data.csv")
df1 = df["Avg Rating"].tolist()

fig = ff.create_distplot([df1],["Avg Rating"],show_hist = True)
fig.show()
