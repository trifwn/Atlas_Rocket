from importing_modules import *

data = pd.read_csv(os.path.join(DATA_PATH,'BNO_samples.csv'))
df = pd.DataFrame(data, columns=['Date','Temperature','Humidity','Pressure'])

temperature = df['Temperature'].values.tolist()
pressure = df['Pressure'].values.tolist()
humidity = df['Humidity'].values.tolist()
time = np.arange(0,len(temperature))


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#FFFF',
    'text': '#7FDB45'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='DashBoard',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Label('Choose graph', style={'color': colors['text'], 'fontSize': '24px'}),
    dcc.Dropdown(
        options=[
            {'label': 'Temperature', 'value': 'Temperature'},
            {'label': 'Pressure', 'value': 'Pressure'},
            {'label': 'Humidity', 'value': 'Humidity'}
        ],
        multi=True,
        placeholder='Choose graphs',
        value=['Temperature', 'Pressure']
    ),

    dcc.Graph(
        id='example-graph-1',
        figure={
            'data': [
                {'x': time[:10000], 'y': temperature[:10000], 'type': 'line', 'name': 'Temperature'}
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    ),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': time[:10000], 'y': pressure[:10000], 'type': 'line', 'name': 'Pressure'}
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])


if __name__ == '__main__':
    
    # pyqtgraph.examples.run()
    app.run_server(debug=True)