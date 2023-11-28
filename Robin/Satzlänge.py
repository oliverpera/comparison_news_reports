import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Daten für die Balken
categories = ['Tagesschau','Bild', 'Focus', 'FAZ' , 'TAZ']
values1 = [467, 975, 627, 685, 340]  # Daten für Balken 1
values2 = [307, 951, 606, 669, 668]  # Daten für Balken 2
values3 = [499, 236, 431, 389, 362]  # Daten für Balken 2

# Erstellung des Balkendiagramms
fig = make_subplots(rows=1, cols=1)


fig.add_trace(go.Bar(x=categories, y=values1, name='Trump', text=values1), row=1, col=1 )
fig.add_trace(go.Bar(x=categories, y=values2, name='Merkel', text=values2), row=1, col=1)
fig.add_trace(go.Bar(x=categories, y=values3, name='Gorbatschow', text=values3), row=1, col=1)


# Layout-Anpassungen
fig.update_layout(title='Wortanzahl der Unterschiedlichen Zeitungen',
                  xaxis_title='Zeitungen',
                  yaxis_title='Anzahl Wörter',
                  barmode='stack')
# Diagramm anzeigen
fig.show()