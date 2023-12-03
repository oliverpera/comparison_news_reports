import plotly.graph_objs as go
from plotly.subplots import make_subplots

categories = ['Tagesschau','Bild', 'Focus', 'FAZ' , 'TAZ']
values1 = [0, 0.02, 0, 0.12, 0.05] 
values2 = [0, 0.01, 0.15, 0.06, 0.1] 
values3 = [0.03, 0.16, 0.06, 0.07, 0] 

avg_values = [(v1 + v2 + v3) / 3 for v1, v2, v3 in zip(values1, values2, values3)]
rounded_avg_values = [round(wert, 2) for wert in avg_values]

fig = make_subplots(rows=1, cols=1)
fig.add_trace(go.Bar(x=categories, y=rounded_avg_values, name='Trump', text=rounded_avg_values), row=1, col=1)

fig.update_layout(title='Subjektivitäts-Score bei Anwendung auf vollständigen Artikeln',
                  xaxis_title='Zeitungen',
                  yaxis_title='Subjektivität')

fig.show()