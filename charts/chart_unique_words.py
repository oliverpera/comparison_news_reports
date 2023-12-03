import plotly.graph_objs as go
from plotly.subplots import make_subplots

categories = ['Tagesschau','Bild', 'Focus', 'FAZ' , 'TAZ']
values1 = [45, 60, 52, 59, 43] 
values2 = [13, 50, 25, 35, 38] 
values3 = [21, 29, 7, 1, 33]  

fig = make_subplots(rows=1, cols=1)

fig.add_trace(go.Bar(x=categories, y=values1, name='Trump', text=values1), row=1, col=1 )
fig.add_trace(go.Bar(x=categories, y=values2, name='Merkel', text=values2), row=1, col=1)
fig.add_trace(go.Bar(x=categories, y=values3, name='Gorbatschow', text=values3), row=1, col=1)

fig.update_layout(title='Anzahl einzigartiger Wörter',
                  xaxis_title='Zeitungen',
                  yaxis_title='Anzahl einzigartiger Wörter in Prozent')

fig.show()