import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Daten für die Balken
categories = ['Tagesschau','Bild', 'Focus', 'FAZ' , 'TAZ']
values1 = [17, 19, 20, 22, 18]  # Daten für Balken 1

# Erstellung des Balkendiagramms
fig = make_subplots(rows=1, cols=1)

fig.add_trace(go.Bar(y=categories, x=values1, name='Trump',orientation='h', marker_color='#b40202'), row=1, col=1)



# Layout-Anpassungen
fig.update_layout(title='Durchschnittliche Satzlänge',
                  xaxis_title='Satzlänge',
                  yaxis_title='Zeitung',
                  barmode='stack',
                  uniformtext_minsize=8,)

# Diagramm anzeigen
fig.show()