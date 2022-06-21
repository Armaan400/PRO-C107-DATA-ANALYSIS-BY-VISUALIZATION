import pandas as py
import csv
import plotly.graph_objects as go


df =py.read_csv("analysis.csv")
student_df=df.loc[df['student_id']=="TRL_abc"]
print(student_df.groupby("level")["attempt"].mean())

fig=go.Figure(go.Bar(x=student_df.groupby("level")["attempt"].mean(),
y=['level1','level2','level3','level4'],orientation='h')
)

fig.show()