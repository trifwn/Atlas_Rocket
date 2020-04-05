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


def update_metrics(times, temperature, pressure, humidity, altitude, or_x, or_y, or_z, vel_x, vel_y, vel_z, acc_x, acc_y, acc_z):
    '''
    Temporary function to generate random data. Later, it will be removed because we will receive the data from the sensors.
    '''

    times.append(time.time())
    if len(times) == 1:
        #starting relevant values
        temperature.append(random.uniform(75,110))
        pressure.append(random.uniform(960,1000))
        humidity.append(random.uniform(17,40))
        altitude.append(random.uniform(1,3000))

        or_x.append(random.uniform(1,10))
        or_y.append(random.uniform(1,1000))
        or_z.append(random.uniform(1,3000))

        vel_x.append(random.uniform(1,1000))
        vel_y.append(random.uniform(1,10000))
        vel_z.append(random.uniform(1,30000))

        acc_x.append(random.uniform(1,1000))
        acc_y.append(random.uniform(1,10000))
        acc_z.append(random.uniform(1,30000))


    else:
        for data_of_interest in [temperature, pressure, humidity, altitude, or_x, or_y, or_z, vel_x, vel_y, vel_z, acc_x, acc_y, acc_z]:

            data_of_interest.append(data_of_interest[-1]+data_of_interest[-1]*random.uniform(-0.01,0.01))

    return times, temperature, pressure, humidity, altitude, or_x, or_y, or_z, vel_x, vel_y, vel_z, acc_x, acc_y, acc_z

# Control panel elements
velocity = html.Div([
        daq.Gauge(
            id="panel-velocity",
            label={"style": {"color": "#fff"}, "label": "Speed"},
            min=0,
            max=50,
            showCurrentValue=True,
            value=0,
            size=175,
            units="km/h",
            color="#00f9ff",
        )
    ], n_clicks=0, className="controlElement col m2"
)

altitude = html.Div([
        daq.Tank(
            id="panel-altitude",
            label={"style": {"color": "#fff"}, "label": "Altitude"},
            min=0,
            max=4000,
            value=0,
            units="meters",
            showCurrentValue=True,
            color="#00f9ff",
        )
    ], n_clicks=0, className="controlElement col m2"
)

temperature = html.Div([
        daq.Tank(
            id="panel-temperature",
            label={"style": {"color": "#fff"}, "label": "Temperature"},
            min=0,
            max=150,
            value=0,
            units="ºC",
            showCurrentValue=True,
            color="#00f9ff",
        )
    ], n_clicks=0, className="controlElement col m2"
)

fuel = html.Div([
        daq.GraduatedBar(
            id="panel-fuel",
            label={"style":{"color": "#fff"}, "label":"Fuel level"},
            labelPosition="bottom",
            min=0,
            max=100,
            value=100,
            step=1,
            showCurrentValue=True,
            color="#00f9ff",
        )
    ], n_clicks=0, className="controlIndicator col m3"
)

onAir = html.Div([
        daq.Indicator(
            id="panel-onAir",
            label={"style": {"color": "#fff"}, "label": "On air"},
            labelPosition="bottom",
            value=False,
            color="#00f9ff",
            style={"color": "#black"}
        )
    ], className="controlIndicator col m1"
)

parachute = html.Div([
        daq.Indicator(
            id="panel-parachute",
            label={"style": {"color": "#fff"}, "label": "Parachute"},
            labelPosition="bottom",
            value=False,
            color="#00f9ff",
            style={"color": "#black"},
        )
    ], className="controlIndicator col m1"
)

parachute2 = html.Div([
        daq.Indicator(
            id="panel-parachute2",
            label={"style": {"color": "#fff"}, "label": "Parachute (backup)"},
            labelPosition="bottom",
            value=False,
            color="#00f9ff",
            style={"color": "#black"},
       )
    ], className="controlIndicator col m1"
)

# The html layout
app.layout = html.Div([
    html.Div([
        html.Div([

            html.Div([
                html.Img(
                    src=app.get_asset_url("rocket.png"),
                    id="logo"
                )
            ], className="col m3"),

            html.Div([
                html.H2(
                    'Telemetry GUI',
                    id="appName"
                )
            ], className="col m6"),
            
            html.Div(className="col m3")

        ], className="row header"),

        html.Div([
            html.Div([

                html.P(
                    "Choose graphs:"
                ),

                dcc.Dropdown(
                    id='sensor-data-name', 
                    options=[{'label': s, 'value': s} for s in config.data_dict.keys()],
                    value=['Temperature','Pressure','Humidity'],
                     placeholder='Choose graphs',
                     multi=True
                )
            ], className="col m12 dropdown")
        ], className="row"),
        
        html.Div(
            children=html.Div(id='graphs'),
            className='row'
        )
    ], className="content"),

    html.Footer([
        html.Div([

            html.Div([
                html.Div([               
                    velocity,
                    altitude, 
                    temperature,
                    fuel,
                    onAir,
                    parachute,
                    parachute2
                ], className="controlPanel")
            ], className="row")
        ], className="container")
    ], className="footer"),

    dcc.Interval(
        id='graph-update',
        interval=800, # in milliseconds
        n_intervals=0
    )
], className="container", style={'width':'98%','marginLeft':10,'marginRight':10,'maxWidth':50000})

@app.callback(Output('graphs','children'),
    [Input('sensor-data-name', 'value'),
     Input('graph-update', 'n_intervals')])
def update_graphs_live(chosen_graphs, n):
    '''
    A function that dynamically fills the html page.
    '''

    graphs = []
    update_metrics(config.times, 
                config.temperature, 
                config.pressure, 
                config.humidity, 
                config.altitude, 
                config.or_x, 
                config.or_y, 
                config.or_z, 
                config.vel_x, 
                config.vel_y, 
                config.vel_z, 
                config.acc_x, 
                config.acc_y, 
                config.acc_z)
                
    if len(chosen_graphs) > 2:
        class_choice = 'col s12 m6 l4'
    elif len(chosen_graphs) == 2:
        class_choice = 'col s12 m6 l6'
    else:
        class_choice = 'col s12'


    for graph_name in chosen_graphs:
        # exei kapoio provlima kai den emfanizei ta shmeia
        # if graph_name == '3D Cone plot':
        #     data = go.Cone(
        #         x = list(config.data_dict[graph_name][0]),
        #         y = list(config.data_dict[graph_name][1]),
        #         z = list(config.data_dict[graph_name][2]),
        #         u = list(config.data_dict[graph_name][3]),
        #         v = list(config.data_dict[graph_name][4]),
        #         w = list(config.data_dict[graph_name][5]),
        #         colorscale='Blues',
        #         sizemode="absolute",
        #         sizeref=40)

        #     graphs.append(html.Div(dcc.Graph(
        #         id=graph_name,
        #         animate=True,
        #         figure={'data': [data], 'layout' : go.Layout(scene=dict(aspectratio=dict(x=1, y=1, z=0.8),
        #                                                      camera_eye=dict(x=1.2, y=1.2, z=0.6)),
        #                                                     title='{}'.format(graph_name))}
        #         ), className=class_choice)
        #     )
        #     continue

        isTuple = type(config.data_dict[graph_name]) is tuple
        
        if isTuple and len(config.data_dict[graph_name]) == 3:
            trace1 = go.Scatter(
                x=list(config.times),
                y=list(config.data_dict[graph_name][0]),
                mode = 'lines',
                name = 'x-coordinate'
            )
            trace2 = go.Scatter(
                x=list(config.times),
                y=list(config.data_dict[graph_name][1]),
                mode = 'lines',
                name = 'y-coordinate'
            )
            trace3 = go.Scatter(
                x=list(config.times),
                y=list(config.data_dict[graph_name][2]),
                mode = 'lines',
                name = 'z-coordinate'
            )

            graphs.append(html.Div(dcc.Graph(
                id=graph_name,
                animate=True,
                figure={'data': [trace1, trace2, trace3], 'layout' : go.Layout(xaxis=dict(range=[min(config.times),max(config.times)]),
                                                            margin={'l':50,'r':1,'t':45,'b':1},
                                                            title='{}'.format(graph_name))}
                ), className=class_choice)
            )

        elif (not isTuple):
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
        else:
            print('Wrong data structure')

    return graphs

@app.callback([
        Output("panel-velocity", "value"),
        Output("panel-altitude", "value"),
        Output("panel-temperature", "value"),
    ],
    [Input('graph-update', 'n_intervals')]
)
def update_control_panel(n):
    '''
    A function that dynamically fills the control panel.
    '''
    return [config.vel_z[-1]/1e3, int(config.altitude[-1]), int(config.temperature[-1])]


if __name__ == '__main__':
    config.times, config.temperature, config.pressure, config.humidity, config.altitude, config.or_x, config.or_y, config.or_z, config.vel_x, config.vel_y, config.vel_z, config.acc_x, config.acc_y, config.acc_z = \
        update_metrics(config.times, config.temperature, config.pressure, config.humidity, config.altitude, config.or_x, config.or_y, config.or_z, config.vel_x, config.vel_y, config.vel_z, config.acc_x, config.acc_y, config.acc_z)
    # pyqtgraph.examples.run()
    app.run_server(debug=True)