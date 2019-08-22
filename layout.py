import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from stylesheet import *
from bioconvert.core.registry import Registry


def get_input_format(): 
    """This function allow to fill the input_dropdown

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

        html.Div('Input Format : ', style={'display': 'inline-block'}), 
        html.Div(dcc.Dropdown(id='input-dropdown', 
            options=get_input_format(),
            placeholder='Select an input format ...'),
                 style={'display': 'inline-block', 'width': '500px', 'verticalAlign': 'middle'})],
            style={'display': 'block'})


def output_dropdown(): 
    #  This fonction return the output dropdown componnent
    return html.Div(children=[

        html.Div('Output Format : ', style={'display': 'inline-block'}), 
        html.Div(dcc.Dropdown(id='output-dropdown', 
            placeholder='Select an output format ...'), 
                 style={'display': 'inline-block', 'width': '500px', 'verticalAlign': 'middle'})], 
            style={'display': 'block'})


def mainframe(): 
    return html.Div(id='Main_frame', 
    children=[
        dcc.Store(id='input_file', storage_type='session'), 
        html.Div(id='Banner', children=
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
                    html.Div('How it works', id="how_section", style={'display': 'inline-block', "marginRight": "20px"}), 
                    html.Div("About", id="about_section", style={'display': 'inline-block'}), 
                ], style=header()),  # END menu

        ], style={'display': 'inline-block', 'width': "100%"}
        ), 

        # Div for Title
        html.Div(id='Logo', 
            children=
            [
                html.Div(id='Title', children=
                [
                    html.H1('Bioconvert', style=title()), 
                ])

            ]), 


        # Div for first step
        html.Div(id='first_step', children=
        [

            html.Div(id='icon_first_step', children=
            [
                # BEGIN CERCLE
                html.Div(className="cercle", id="cercle1", 
                    children=
                    [
                        html.Div('1', className="cercle_text")  # END CERCLE_TEXT
                    ]),  # END CERCLE
                html.Div('UPLOAD AN INPUT FILE', 
                         style=text_icon()), 
            ], style={'display': 'inline-block'}  # END TEXT_ICON

            ),  # END ICON_FIRST_STEP

            html.Div(id="DRAG_and_DROP", className='rectangle', children=
                [
                    dcc.Upload(id="upload_file", children=
                    [
                        "Drag and drop or", html.A(" select a file"),
                    ], style={"textAlign": "center", 'lineHeight': '100px'}),  # END upload_file
                    html.Div(id='guess_format', style={"textAlign": "center"})
                ]
            ),  # END DRAG and DROP
            html.Br(), 
            html.Br(), 

        ]),  # END FIRST STEP

        html.Br(), 
        html.Br(), 
        dbc.Tooltip(children=[
            html.Img(src='/assets/attention.png', style=icon_style()), 
            html.P("Be careful, you are limited"), 
            html.P("to a file of less than 100 MB."), 
            html.P(" For heavier input file"), 
            html.P("please install bioconvert")
        ], 
        target="DRAG_and_DROP", placement='right', className='arrow: : before', style=tooltip_style()),


        # Div for second step
        html.Div(id='second_step', children=
        [
            html.Div(id='icon_second_step', children=
            [
                html.Div(className="cercle", id="cercle2", 
                         children=[
                             html.Div('2', className="cercle_text")  # END CERCLE_TEXT

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

        ]),  # END SECOND STEP

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
                target="Submit", placement='right', style={"color": "red",
                                                            'background-color': 'white', 'text-align': 'center'}),
            html.Div(id='convertion', style={"textAlign": "center"}),
            # html.Div(id='link', style={"textAlign": "center"}), 



                     ),  # END DRAG and DROP

        ]),  # END third STEP

        html.Br(), 

        # Div for third step

        html.Div(id='fourth_step', children=
        [
            html.Div(id='icon_fourth_step', children=
            [
                html.Div(className="cercle", id="cercle4", 
                         children=[
                             html.Div('4', className="cercle_text")  # END CERCLE_TEXT

                         ]),  # END CERCLE
                html.Div('DOWNLOAD YOUR DATA', 
                         style=text_icon()),  # END TEXT_ICON
            ]
                     , style={'display': 'inline-block'}
                     ),  # END ICON_SECOND_STEP

            html.Div(id="link", className='rectangle', style={'lineHeight': '100px'}), 
        ]), 

        html.Br(), 
        html.Br(), 

        html.Div(id='footer', children=
        [
            html.Div(id='Contact_us', children=
            [
                html.Div(className="puce", id="puce1", style={'display': 'inline-block'}), 
                html.Div("Conctact us", id="title_puce", style={'display': 'inline-block', 'marginLeft': '5px'}), 
                html.P(' For questions about conversions contact Thomas Cokelaer(thomas.cokelaer@pasteur.fr)'
                    ' or Bertrand Néron (bneron@pasteur.fr) '
                    'You can also make an issue on GitHub (https: //github.com/bioconvert)', 
                      style={'fontSize': 10}), 
            ], style={'width': "20%", 'margin': '10px 50px 20px', 'display': 'inline-block'}  # END TEXT_ICON
                  ),  # END ICON_FIRST_STEP
            html.Div(id='how_to_cite', children=
            [
                html.Div(className="puce", id="puce2", style={'display': 'inline-block'}), 
                html.Div("How to cite", id="title_puce2", style={'display': 'inline-block', 'marginLeft': '5px'}), 
                html.P(' Sulyvan Dollin, Anne Biton, Bryan Brancotte, Yoann Dufresne, Kenzo-Hugo Hillion, '
                       ' Etienne Kornobis, Pierre Lechat, Rachel Legendre, Frédéric Lemoine, Blaise Li, '
                       ' Nicolas Maillet, Amandine Perrin, Rachel Torchet1, Nicolas Traut, Anna Zhukova, '
                       ' Bertrand Néron, Thomas Cokelaer: '
                       ' Bioconvert: a collaborative bioinformatics format converter library', 
                       style={'fontSize': 10}), 
            ], style={'width': "20%", 'margin': '10px 50px 20px', 'display': 'inline-block'}  # END TEXT_ICON
                     ),  # END ICON_FIRST_STEP

            ], style=footer()), 

])
