import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from stylesheet import *
from bioconvert.core.registry import Registry


def get_input_format():
    """This function allows to fill the input_dropdown

    : return: all the input format available in bioconvert
    : rtype: dict
    """

    r = Registry()
    all_converter = list(r.get_converters_names())
    list_format = []
    #  We collect input file by splitting the converters
    for converter in all_converter:
        input_format, output_format = converter.split('2', 1)
        list_format.append(input_format)
    list_format = list(set(list_format))
    #  to have sorted input format in the dropdown
    list_format.sort()
    options = []
    #  the dropdown option take a dictionnary as argument, so convert the list in dict. Label and value is the same
    for format in list_format:
        options.append(
            {
                'label': format,
                'value': format
            }
        )
    return options


def input_dropdown():
    #  This fonction return the input dropdown by calling the get_input_format function
    return html.Div(children=[

        html.Div('INPUT FORMAT : ', style={'display': 'inline-block', 'color': '#FF8C00', "font-weight": "bold"}),
        html.Div(dcc.Dropdown(id='input-dropdown',
            options=get_input_format(),
            placeholder='Select an input format ...'),
                 style={'display': 'inline-block', 'width': '500px', 'verticalAlign': 'middle'})],
            style={'display': 'block'})


def output_dropdown():
    #  This fonction return the output dropdown componnent
    return html.Div(children=[

        html.Div('OUTPUT FORMAT : ', style={'display': 'inline-block', 'color': '#FF8C00', "font-weight": "bold",}),
        html.Div(dcc.Dropdown(id='output-dropdown',
            placeholder='Select an output format ...'),
                 style={'display': 'inline-block', 'width': '500px', 'verticalAlign': 'middle'})],
            style={'display': 'block'})


def get_div_title():
    data = html.Div(id='Logo', children=[
        html.Div(id='Title', children=[
            html.H1('Bioconvert ', style=title()),
            html.H1('|', style={'color': '#050D36','fontSize': 100, 
                'font-family': "", 'display': 'inline-block'}),
        html.Div(children=[
            html.P('Bioinformatics ', style={'color': '#050D36','fontSize': 25, }),
            html.P(' formats converter', style={'color': '#050D36','fontSize': 25,})
            ], style={'display': 'inline-block', 'text-align':'center', }),
        ], style={'vertical-align':'middle' }),
        ])
    return data


def get_div_first_step():
    # Div for first step
    data = html.Div(id='first_step', children=
        [

            html.Div(id='icon_first_step', children=
            [
                # BEGIN CERCLE
                html.Div(className="circle", id="circle1",
                    children=
                    [
                        html.Div('1', className="circle_text")  # END CERCLE_TEXT
                    ]),  # END CERCLE
                html.Div('UPLOAD AN INPUT FILE', style=text_icon()),
            ], style={'display': 'inline-block', "background-color": "yellow"}  # END TEXT_ICON

            ),  # END ICON_FIRST_STEP

            html.Div(id="DRAG_and_DROP", className='rectangle', children=
                [
                    dcc.Upload(id="upload_file", children=
                    [
                        html.Img(src='/assets/upload.png', 
                            style={'height': '70px', 'width': '70px','display': 
                                    'inline-block', 'vertical-align':'middle', 
                                    'marginRight':'24px'}),
                        html.Div("Drag and drop or select a file", 
                            style={'display': 'inline-block','color': '#FF8C00', 
                            "fontSize": 35, 'vertical-align':'middle'})
                    ], style={"textAlign": "center", 'lineHeight': '90px'}),  # END upload_file
                    html.Div(id='guess_format', style={"textAlign": "center"})
                ]
            ),  # END DRAG and DROP
            html.Br(),
            html.Br(),

        ])
    return data

def get_div_second_step():
    # Div for second step
    data=    html.Div(id='second_step', children=
        [
            html.Div(id='icon_second_step', children=
            [
                html.Div(className="circle", id="circle2",
                         children=[
                             html.Div('2', className="circle_text")  # END CERCLE_TEXT

                         ]),  # END CERCLE
                html.Div('SELECT THE INPUT AND OUTPUT FORMAT', style=text_icon()),  # END TEXT_ICON
            ], style={'display': 'inline-block'}
                     ),  # END ICON_SECOND_STEP

            html.Div(id="InOut", className='rectangle', children=
            [
                input_dropdown(),
                html.Br(),
                output_dropdown(),
                html.Br(),
                html.Div(id='converter', style={"textAlign": "center"}),

            ], style={"textAlign": "center"}  # END upload_file
                     ),  # END DRAG and DROP

        ])
    return data

def get_div_third_step():
    data = html.Div(id='third_step', children=
        [
            html.Div(id='icon_third_step', children=
            [
                html.Div(className="circle", id="circle3",
                         children=[
                             html.Div('3', className="circle_text")  # END CERCLE_TEXT

                         ]),  # END CERCLE
                html.Div('SUBMIT YOUR JOB',
                         style=text_icon()),  # END TEXT_ICON
            ], style={'display': 'inline-block'}
                     ),  # END ICON_SECOND_STEP

            html.Div(id="Submit", className='rectangle', children=
            [
                html.Button('SUBMIT', id='submit_button', style=submit()),  # END upload_file
            ], style={'lineHeight': '100px'}),
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Tooltip(children=[
                html.Img(src='/assets/attention.png', style=icon_style()),
                html.P("You can also encourage us"),
                html.P("by putting a star on"),
                html.P("the bioconvert project on GitHub"),
            ],
                target="Submit", placement='right', style=tooltip_style()),
            html.Div(id='convertion', style={"textAlign": "center"}),
            html.Div(id="fake", style={"display": "none"}
                     ),  # END DRAG and DROP
        ])
    return data


def get_div_footer():


    data =     html.Div(id='footer', children=
        [
            html.Div(id='Contact_us', children=
            [
                html.Div(className="puce", id="puce1", style={'display': 'inline-block'}),
                html.Div("Conctact us", id="title_puce", style={'display': 'inline-block', 
                    'marginLeft': '5px'}),
                html.P(' For questions about conversions contact '
                       ' Thomas Cokelaer(thomas.cokelaer _at_ pasteur.fr)'
                       ' or Bertrand Néron (bneron _at_ pasteur.fr) '
                       'or post an issue on <a href="https://github.com/bioconvert/issues">github</a>',
                      style={'fontSize': ".9em"}),
            ], style={'float': "left", 'width': "30%", 'margin': '10px 10px 20px', 'display': 'inline-block'}  
            ),  # END contact
            html.Div(id='how_to_cite', children=
            [
                html.Div(className="puce", id="puce2", style={'display': 'inline-block'}),
                html.Div("How to cite", id="title_puce2", style={'display': 'inline-block', 
                    'marginLeft': '5px'}),
                html.P(' Sulyvan Dollin, Anne Biton, Bryan Brancotte, Yoann Dufresne, Kenzo-Hugo Hillion, '
                       ' Etienne Kornobis, Pierre Lechat, Rachel Legendre, Frédéric Lemoine, Blaise Li, '
                       ' Nicolas Maillet, Amandine Perrin, Rachel Torchet1, Nicolas Traut, Anna Zhukova, '
                       ' Bertrand Néron, Thomas Cokelaer: '
                       ' Bioconvert: a collaborative bioinformatics format converter library',
                       style={'fontSize': "0.9em"}),
            ], style={'float':"right", 'width': "50%", 'margin': '10px 50px 20px', 'display': 'inline-block'}  # END TEXT_ICON
                     ),  # END citation

            ], style=footer())
    return data

def get_div_fourth_step():
    data = html.Div(id='fourth_step', children=
        [
            html.Div(id='icon_fourth_step', children=
            [
                html.Div(className="circle", id="circle4",
                         children=[
                             html.Div('4', className="circle_text")  # END CERCLE_TEXT

                         ]),  # END CERCLE
                html.Div('DOWNLOAD YOUR DATA',
                         style=text_icon()),  # END TEXT_ICON
            ]
                     , style={'display': 'inline-block'}
                     ),  # END ICON_SECOND_STEP

            html.Div(id="link", className='rectangle', style={'lineHeight': '100px'}),
        ])
    return data


def get_div_banner():
    data= html.Div(id='Banner', children=
        [
            # Div for menu home
            html.Div(id='Image_home',
                children=
                [
                    html.Img(src='/assets/home.png', style=icon_style()),
                    # Div for text menu home
                    html.Div('Home', style={'display': 'block'}),

                ], style=home_div()),  # END menu home
            # Div for menu
            html.Div(id='section',
                children=
                [
                    html.Div('How it works', id="how_section",
                        style={'display': 'inline-block', "marginRight": "20px"}),
                    html.Div("About", id="about_section",
                        style={'display': 'inline-block'}),
                ], style=header()),  # END menu

        ], style={'display': 'inline-block', 'width': "100%"}
        )
    return data

def mainframe():
    return html.Div(id='Main_frame',
    children=[
        dcc.Store(id='input_file', storage_type='session'),

        # Div for Title
        get_div_title(),
        html.Hr(),

        get_div_first_step(),

        html.Br(),
        html.Br(),
        dbc.Tooltip(children=[
            html.Img(src='/assets/attention.png', style=icon_style()),
            html.P("Be careful, you are limited"),
            html.P("to a file of less than 100 MB."),
            html.P(" For heavier input file"),
            html.P("please install bioconvert")
            ],
            target="DRAG_and_DROP", placement='right', 
            className='arrow: : before', style=tooltip_style()
        ),


        get_div_second_step(),

        html.Br(),
        html.Br(),
        dbc.Tooltip(children=[
            html.Img(src='/assets/attention.png', style=icon_style()),
            html.P("If the formats you want are"),
            html.P("not available. It is possible to"),
            html.P("add new converter through"),
            html.P("GitHub or to make an issue.")
            ],
            target="InOut", placement='right', style=tooltip_style()),

        # Div for third step
        get_div_third_step(),


        html.Br(),
        # Div for fourth step
        get_div_fourth_step(),

        html.Br(),
        html.Br(),
        get_div_footer()
        ])
