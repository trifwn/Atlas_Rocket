from importing_modules import *

# data = pd.read_csv(os.path.join(DATA_PATH,'BNO_samples.csv'))
# df = pd.DataFrame(data, columns=['Date','Temperature','Humidity','Pressure'])

# temperature = df['Temperature'].values.tolist()
# pressure = df['Pressure'].values.tolist()
# humidity = df['Humidity'].values.tolist()
# time = np.arange(0,len(temperature))

# Initialize global variables
config.init() 

# external JavaScript files
external_scripts = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']

# external CSS stylesheets
external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css']


app = dash.Dash('Telemetry GUI',
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)


def update_metrics(times, temperature, pressure, humidity, altitude, orientation, velocity, acceleration):

    times.append(time.time())
    if len(times) == 1:
        #starting relevant values
        temperature.append(random.uniform(75,110))
        pressure.append(random.uniform(960,1000))
        humidity.append(random.uniform(17,40))
        altitude.append(random.uniform(1,3000))

        orientation.append(random.uniform(1,10))
        velocity.append(random.uniform(1,1000))
        acceleration.append(random.uniform(1,1000))
        # orientation.append( (random.uniform(1,10), random.uniform(1,1000), random.uniform(1,3000)) )
        # velocity.append( (random.uniform(1,1000), random.uniform(1,10000), random.uniform(1,30000)) )
        # acceleration.append( (random.uniform(1,1000), random.uniform(1,10000), random.uniform(1,30000)) )

    else:
        for data_of_interest in [temperature, pressure, humidity, altitude, orientation, velocity, acceleration]:

            data_of_interest.append(data_of_interest[-1]+data_of_interest[-1]*random.uniform(-0.0001,0.0001))

    return times, temperature, pressure, humidity, altitude, orientation, velocity, acceleration

app.layout = html.Div([
    html.Div([
        html.H2('Telemetry GUI',
            style={'textAlign': 'center'}
        )
    ], className="row"),
    html.Div([
        html.Div([
            dcc.Dropdown(id='sensor-data-name', 
                options=[{'label': s, 'value': s} for s in config.data_dict.keys()],
                 value=['Temperature','Pressure','Humidity'],
                 placeholder='Choose graphs',
                 multi=True
            )
        ], className="six columns", style={'display': 'block'})
    ], className="row"),
    
    html.Div(children=html.Div(id='graphs'), className='row'),

    dcc.Interval(id='graph-update',
        interval=800, # in milliseconds
        n_intervals=0
    )
], className="container", style={'width':'98%','margin-left':10,'margin-right':10,'max-width':50000})

@app.callback(Output('graphs','children'),
    [Input('sensor-data-name', 'value'),
     Input('graph-update', 'n_intervals')])
def update_graphs_live(chosen_graphs, n):
    graphs = []
    update_metrics(config.times, 
                    config.temperature, 
                    config.pressure, 
                    config.humidity, 
                    config.altitude, 
                    config.orientation, 
                    config.velocity, 
                    config.acceleration)
                    
    if len(chosen_graphs)>2:
        class_choice = 'col s12 m6 l4'
    elif len(chosen_graphs) == 2:
        class_choice = 'col s12 m6 l6'
    else:
        class_choice = 'col s12'


    for graph_name in chosen_graphs:

        data = go.Scatter(
            x=list(config.times),
            y=list(config.data_dict[graph_name]),
            mode = 'lines',
            name = 'lines'
        )

        graphs.append(html.Div(dcc.Graph(
            id=graph_name,
            animate=True,
            figure={'data': [data], 'layout' : go.Layout(xaxis=dict(range=[min(config.times),max(config.times)]),
                                                        yaxis=dict(range=[min(config.data_dict[graph_name]),max(config.data_dict[graph_name])]),
                                                        margin={'l':50,'r':1,'t':45,'b':1},
                                                        title='{}'.format(graph_name))}
            ), className=class_choice)
        )

    return graphs

if __name__ == '__main__':
    config.times, config.temperature, config.pressure, config.humidity, config.altitude, config.orientation, config.velocity, config.acceleration = \
        update_metrics(config.times, config.temperature, config.pressure, config.humidity, config.altitude, config.orientation, config.velocity, config.acceleration)
    # pyqtgraph.examples.run()
    app.run_server(debug=True)