
from dash import Dash, html, dcc
from dash.dependencies import Output, Input
# Create example app.
app = Dash()
app.layout = html.Div([
    html.H1('Toronto Neighbourhood Map'),
    html.Div([
        dcc.Dropdown(
                        options=[
                        {'label':'Price', "value": './opendata_neighbourhoods/price_map.html'},
                        {'label':'Crime', "value": './opendata_neighbourhoods/crime_map.html'},
                        ], 
                        value='./opendata_neighbourhoods/price_map.html',
                        id='selection'
                        )

    ], style={'width': '30%'}),


    html.Iframe(id = 'map',width='100%', height='1000')
])

@app.callback(
    Output("map", "srcDoc"), Input("selection", "value"))
def update_map(input_value):
    return open(input_value).read()

if __name__ == '__main__':
    app.run_server()
