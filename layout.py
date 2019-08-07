import dash_core_components as dcc
import dash_html_components as html
from stylesheet import *

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
        html.Div(
            html.Div(id='icon_first_step', children=
            [
                html.Div(className="cercle", id="cercle1",
                     children=[
                         html.Div('1', className="cercle_text")

                     ]
                ),
                html.Div('UPLOAD AN INPUT FILE',
                         style=text_icon()),
            ])

        )

])
