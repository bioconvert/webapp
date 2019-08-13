import base64
import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_html_components as html
from flask import Flask, send_from_directory
import io
import layout
import os
import subprocess
from subprocess import Popen, PIPE, STDOUT
from stylesheet import *
from urllib.parse import quote as urlquote




UPLOAD_DIRECTORY = "./project/app_uploaded_files"

server = Flask(__name__)
app = dash.Dash(__name__)

# home_image = 'images/home.png'
# encoded_image = base64.b64encode(open(home_image, 'rb').read())

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app.layout = layout.mainframe()

@server.route("/download/<path:path>")
def download(path):
    """Serve a file from the upload directory."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)

@app.callback(
    Output('input_file', 'data'),
    [Input('upload_file','filename'),
     Input('upload_file', 'contents')])

def collect_file(filename, contents):
    if contents:
        data = contents.encode("utf8").split(b";base64,")[1]
        with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
            fp.write(base64.decodebytes(data))
        print('File {} loaded Successfully readed !'.format(fp))


@app.callback(
    Output('converter', 'children'),
    [Input('input-dropdown', 'value'),
    Input('output-dropdown', 'value')])
def update_output(value_input,value_output):
    if value_input and value_output :
        return 'You have selected "{}" as input format and "{}" as output format'.format(value_input,value_output)


def bash_command(cmd):
    subprocess.Popen(cmd)

@app.callback(
    Output('convertion', 'children'),
    [Input('upload_file','filename'),
     Input('input-dropdown', 'value'),
     Input('output-dropdown', 'value'),
     Input('submit_button','n_clicks')])
def convert(filename,input_value, output_value, button):
    if button:
        converter = input_value+"2"+output_value
        converter = converter.lower()
        print(converter)
        p = bash_command(["singularity", "run", "bioconvert.img", converter, filename, "--force", "-v", "INFO"])
        print(p)
        return 'Your file "{}" will be convert into "{}" format Using bioconvert with the following command line ' \
               '\n : bioconvert {}2{} {}'.format(filename, output_value, input_value, output_value, filename)


if __name__ == '__main__':
    app.run_server(debug=True)
