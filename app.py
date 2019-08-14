import base64
import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_html_components as html
from flask import Flask, send_from_directory, send_file
import io
import layout
import os
import subprocess
from subprocess import Popen, PIPE, STDOUT
from stylesheet import *
from urllib.parse import quote as urlquote


UPLOAD_DIRECTORY = "./"

server = Flask(__name__)
app = dash.Dash(__name__, server=server)

# home_image = 'images/home.png'
# encoded_image = base64.b64encode(open(home_image, 'rb').read())

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app.layout = layout.mainframe()


@app.callback(
    Output('input_file', 'data'),
    [Input('upload_file','filename'),
     Input('upload_file', 'contents')])

def collect_file(filename, contents):
    """Decode and store a file uploaded with Plotly Dash."""
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
    p = subprocess.Popen(cmd)
    p.wait()
    p.returncode

@app.callback(
    Output('convertion', 'children'),
    [Input('upload_file','filename'),
     Input('input-dropdown', 'value'),
     Input('output-dropdown', 'value'),
     Input('submit_button','n_clicks')])
def convert(filename, input_value, output_value, button):
    if button:
        converter = input_value+"2"+output_value
        converter = converter.lower()
        bash_command(["singularity", "run", "bioconvert.img", converter, filename, "--force", "-v", "INFO"])
        return 'Your file "{}" will be convert into "{}" format Using bioconvert with the following command line ' \
               '\n : bioconvert {}2{} {}'.format(filename, output_value, input_value, output_value, filename)


@app.callback(
    Output('fake','children'),
    [Input('upload_file','filename'),
     Input('output-dropdown', 'value')]
)
def converted_file_name(filename,format):
    if filename and format:
        filename_converted = filename.split(".")[0]
        filename_converted = filename_converted+"."+format.lower()
        #  print(filename_converted)
        return filename_converted

@app.callback(
    Output('link','children'),
    [Input('fake','children')]
)
def file_download_link(filename):
    """Create a Plotly Dash 'A' element that downloads a file from the app."""
    # download_file = get_file(filename)

    location = "/download/{}".format(filename)
    #  print(location, type(location))
    return html.A("Download Data", href=location)


@app.server.route("/download/<path:filename>")
def get_file(filename):
    """Download a file."""
    #  print(filename)
    return send_from_directory(UPLOAD_DIRECTORY, filename, as_attachment=True)


if __name__ == '__main__':
    app.run_server(debug=True)
