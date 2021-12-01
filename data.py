import random
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("data.csv")
df1 = df["Height(Inches)"].tolist()

fig = ff.create_distplot([df1],["height"],show_hist = True)
fig.show()