import dash_core_components as dcc
import dash_html_components as html
from stylesheet import *



def input_dropdown():
    return html.Div([dcc.Dropdown(id = 'input-dropdown',
                        options = [
                            {'label':'FASTA', 'value':'fasta'},
                            {'label': 'SAM', 'value': 'bam'},
                            {'label': 'FASTQ', 'value': 'fastq'}
                        ],
                        value = 'Select an input format ...',
                        placeholder = 'Select an input format ...'
                        )], style = {'float':'left', 'width':'500px'})

def output_dropdown():
    return html.Div([dcc.Dropdown(id = 'output-dropdown',
                        options = [
                            {'label':'CLUSTAL', 'value':'fasta'},
                            {'label': 'BAM', 'value': 'bam'},
                            {'label': 'FASTA', 'value': 'fastq'}
                        ],
                        value = 'Select an output format ...',
                        placeholder = 'Select an output format ...'
                        )], style = {'float':'right', 'width':'500px'})



def mainpanel():
	return html.Div( id = 'Main_frame',
    children=[
        html.Div(id='Banner' ,children=
        [
            # Div for image
            html.Div(id='Image_home',
                children=[
                    html.Img(src='/assets/home.png', style = image_home_style()),
            # Div for text
            html.Div('Home',
                style = {'display':'block'}),

            ], style = home_div()),
            # Div for menu
            html.Div('salut',id='Menu',
                style = header()

            ),

        ],
            style={'display':'inline-block',}
    ),
        # Div for Title
        html.Div(id = 'Logo',
            children=[
                html.Div(id = 'Title',children =[
                    html.H1('Bioconvert', style = title()),
                ])

            ]),

        # Div for first step
        html.Div(id='first_step', children=
            [
            html.Div(id='icon_first_step', children=
                [
                html.Div(className="cercle", id="cercle1",
                     children=[
                         html.Div('1', className="cercle_text")  # END CERCLE_TEXT

                     ]), # END CERCLE
                html.Div('UPLOAD AN INPUT FILE',
                     style=text_icon()), # END TEXT_ICON
                ]
                   , style={'display': 'inline-block'}
            ), # END ICON_FIRST_STEP

            html.Div(id= "DRAG and DROP",className='rectangle',children=
                [
                dcc.Upload(id="upload_file", children=
                ["Drag and drop or", html.A(" select a file")
                 ],style= {"textAlign": "center"}) # END upload_file
                ]
            ), # END DRAG and DROP


        ]), # END FIRST STEP


        html.Br(),

        # Div for second step
        html.Div(id='second_step', children=
        [
            html.Div(id='icon_second_step', children=
            [
                html.Div(className="cercle", id="cercle2",
                         children=[
                             html.Div('2', className="cercle_text")  # END CERCLE_TEXT

                         ]),  # END CERCLE
                html.Div('SELECT THE INPUT AND OUTPUT FORMAT',
                         style=text_icon()),  # END TEXT_ICON
            ]
                     , style={'display': 'inline-block'}
                     ),  # END ICON_SECOND_STEP

            html.Div(id="InOut", className='rectangle', children=
            [
                input_dropdown(),
                output_dropdown()

            ],style= {"textAlign": "center"}  # END upload_file
                     ),  # END DRAG and DROP

        ]),  # END SECOND STEP

        html.Br(),

        # Div for third step

        html.Div(id='third_step', children=
        [
            html.Div(id='icon_third_step', children=
            [
                html.Div(className="cercle", id="cercle3",
                         children=[
                             html.Div('3', className="cercle_text")  # END CERCLE_TEXT

                         ]),  # END CERCLE
                html.Div('SUBMIT YOUR JOB',
                         style=text_icon()),  # END TEXT_ICON
            ]
                     , style={'display': 'inline-block'}
                     ),  # END ICON_SECOND_STEP

            html.Div(id="Submit", className='rectangle', children=
            [
                dcc.Upload(id="SUBM", children=
                ["Drag and drop or", html.A(" select a file")
                 ], style={"textAlign": "center"})  # END upload_file
            ]
                     ),  # END DRAG and DROP

        ]),  # END SECOND STEP


])
