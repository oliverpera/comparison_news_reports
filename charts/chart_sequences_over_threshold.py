import plotly.graph_objs as go
from plotly.subplots import make_subplots

categories = ['Tagesschau','Bild', 'Focus', 'FAZ' , 'TAZ']
values1 = [1, 6, 12, 8, 5] 

fig = make_subplots(rows=1, cols=1)
fig.add_trace(go.Bar(x=categories, y=values1, name='Trump', text=values1), row=1, col=1)

fig.update_layout(title='Anzahl Sequenzen > 0.16 (Threshold Subjektivitäts-Score)',
                  xaxis_title='Zeitungen',
                  yaxis_title='Anzahl')

fig.show()