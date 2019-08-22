import base64
import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_html_components as html
from flask import Flask, send_from_directory, send_file
import layout
import os
import subprocess
from subprocess import Popen, PIPE, STDOUT
from stylesheet import *
from bioconvert.core.registry import Registry
from bioconvert.io.sniffer import Sniffer

UPLOAD_DIRECTORY = "./"

server = Flask(__name__)
app = dash.Dash(__name__, server=server)


if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app.layout = layout.mainframe()

@app.callback(
    [Output('guess_format', 'children'), Output('input-dropdown','value')],
    [Input('upload_file', 'filename')]
)
def sniffer(filename):
    if filename:
        s = Sniffer()
        file_format = s.sniff(filename)
        if file_format is None:
            return ["", ""]
        else:
            return [r"Your input file is probably in {} format. If not, please change the format here below".format(file_format), file_format]
    else:
        #  Two outputs are defined in the callback, so you have to return a list of two. Otherwise we have an error.
        #  Since we do not want to display anything when the user has not yet uploaded this list is empty
        return [None,None]

@app.callback(
    Output('output-dropdown', 'options'),
    [Input('input-dropdown', 'value')])
def get_output_format(input_value):
    options = []
    try:
        r = Registry()
        all_converter = list(r.get_converters_names())
        list_format = []
        for converter in all_converter:
            if converter.startswith(input_value):
                input_format, output_format = converter.split('2', 1)
                list_format.append(output_format)
        list_format = list(set(list_format))
        list_format.sort()
        for format in list_format:
            options.append(
                {
                    'label': format,
                    'value': format
                }
            )
        return options
    except TypeError:
        return options

@app.callback(
    Output('input_file', 'data'), 
    [Input('upload_file', 'filename'), 
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
def update_output(value_input, value_output):
    if value_input and value_output:
        return 'You have selected "{}" as input format and "{}" as output format'.format(value_input, value_output)


def bash_command(cmd):
    p = subprocess.Popen(cmd)
    p.wait()
    p.returncode


@app.callback(
    Output('convertion', 'children'), 
    [Input('upload_file', 'filename'), 
     Input('input-dropdown', 'value'), 
     Input('output-dropdown', 'value'), 
     Input('submit_button', 'n_clicks')])
def convert(filename, input_value, output_value, button):
    if button and input_value and output_value:
        converter = input_value+"2"+output_value
        converter = converter.lower()
        bash_command(["singularity", "run", "bioconvert.img", converter, filename, "--force", "-v", "INFO"])
        return html.P('The conversion is complete, your file "{}" has been converted in "{}" '
                      'format using bioconvert with the following command line : '.format(filename, output_value)), \
               html.P(' bioconvert {}2{} {}'.format(input_value, output_value, filename), style= {"font-weight":"bold"})

@app.callback(
    Output('fake', 'children'), 
    [Input('upload_file', 'filename'), 
     Input('output-dropdown', 'value')]
)
def converted_file_name(filename, format):
    if filename and format:
        filename_converted = filename.split(".")[0]
        filename_converted = filename_converted+"."+format.lower()
        #  print(filename_converted)
        return filename_converted


@app.callback(
    Output('link', 'children'), 
    [Input('fake', 'children'),Input('submit_button','n_clicks')]
)
def file_download_link(filename,button):
    """Create a Plotly Dash 'A' element that downloads a file from the app."""
    # download_file = get_file(filename)
    if button:
        location = "/downloads/{}".format(filename)
        #  print(location, type(location))
        return html.A(html.Button("Download", style=download()), href=location)


@app.server.route("/downloads/<path:filename>")
def get_file(filename):
    """Download a file."""
    #  print(filename)
    return send_from_directory(UPLOAD_DIRECTORY, filename, as_attachment=True)


if __name__ == '__main__':
    app.run_server(debug=True)
