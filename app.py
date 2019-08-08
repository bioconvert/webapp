import base64
import dash
import dash_core_components as dcc
import dash_html_components as html
import layout
from stylesheet import *


app = dash.Dash(__name__)

# home_image = 'images/home.png'
# encoded_image = base64.b64encode(open(home_image, 'rb').read())

app.layout = layout.mainframe()

if __name__ == '__main__':
    app.run_server(debug=True)