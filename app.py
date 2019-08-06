import dash
import dash_core_components as dcc
import dash_html_components as html
from stylesheet import *

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(
        children=[
            
            html.Div('Home', style = home()),
            html.Div('salut',style = header()),
        ],
    ),
    html.Div(
        children=html.Div([
            html.H1('Bioconvert', style = title()),
        ])
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)