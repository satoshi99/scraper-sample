import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1(children='Markdown', style={'textAlign': 'center'}),
    dcc.Markdown('''
    # h1
    ## h2
    
    - item1
    - item2
    - item3
    '''),

    html.H1(children='Dropdown', style={'textAlign': 'center'}),
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'sato', 'value': 'sato'},
            {'label': 'suzuki', 'value': 'suzuki'},
            {'label': 'Mike', 'value': 'Mike'}
        ],
        value='suzuki'
    ),

    html.H1(children='Multi-Select Drowdown', style={'textAlign': 'center'}),
    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'sato', 'value': 'sato'},
            {'label': 'suzuki', 'value': 'suzuki'},
            {'label': 'Mike', 'value': 'Mike'}
        ],
        value=['suzuki', 'sato'],
        multi=True
    ),

    html.H1(children='Radio Items', style={'textAlign': 'center'}),
    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': 'sato', 'value': 'sato'},
            {'label': 'suzuki', 'value': 'suzuki'},
            {'label': 'Mike', 'value': 'Mike'}
        ],
        value='sato'
    ),
    html.H1(children='Checkboxes', style={'textAlign': 'center'}),
    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': 'sato', 'value': 'sato'},
            {'label': 'suzuki', 'value': 'suzuki'},
            {'label': 'Mike', 'value': 'Mike'}
        ],
        value=['sato', 'suzuki']
    ),

    html.H1(children='Text Input', style={'textAlign': 'center'}),
    html.Label('Text Input'),
    dcc.Input(value='Satoshi', type='text'),

    html.H1(children='Slider', style={'textAlign': 'center'}),
    html.Label('Slider'),
    dcc.Slider(
        min=0, max=5,
        marks={i: str(i) for i in range(1, 6)},
        value=3
    )
], style={'columnCount': 2})

if __name__ == '__main__':
    app.run_server(debug=True)
