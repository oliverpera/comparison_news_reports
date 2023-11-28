import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Daten für die Balken
categories = ['Tagesschau','Bild', 'Focus', 'FAZ' , 'TAZ']
values1 = [45, 60, 52, 59, 43]  # Daten für Balken 1
values2 = [13, 50, 25, 35, 38]  # Daten für Balken 2
values3 = [21, 29, 7, 1, 33]  # Daten für Balken 2

# Erstellung des Balkendiagramms
fig = make_subplots(rows=1, cols=1)


fig.add_trace(go.Bar(x=categories, y=values1, name='Trump', text=values1), row=1, col=1 )
fig.add_trace(go.Bar(x=categories, y=values2, name='Merkel', text=values2), row=1, col=1)
fig.add_trace(go.Bar(x=categories, y=values3, name='Gorbatschow', text=values3), row=1, col=1)


# Layout-Anpassungen
fig.update_layout(title='Anzahl Einzigartiger Wörter',
                  xaxis_title='Zeitungen',
                  yaxis_title='Anzahl Einzigartiger Wörter in Prozent')
# Diagramm anzeigen
fig.show()