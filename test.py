from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
from dash import callback_context

# Make sure to import your page module correctly
import page  # Assuming page.py is in the same directory

app = Dash(__name__)
app.title = 'TOR+'
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# ... (Your home layout code remains unchanged)

@app.callback(
    Output('page-content', 'children'),
    [Input('load', 'n_clicks'),
     Input('setting', 'n_clicks'),
     Input('url', 'pathname')],
    State('input', 'value')
)
def update_output(n_clicks_load, n_clicks_setting, pathname, input_value):
    ctx = callback_context
    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'load':
        # Assuming page.load is a function that takes a URL and returns content
        return page.load(input_value)
    elif button_id == 'setting':
        # Assuming page.setting is a function that returns setting content
        return page.setting()
    elif pathname:
        # If there's a pathname, load that page
        return page.load(pathname)
    else:
        # Default to home page
        return home

# The save callback should have an Output defined
@app.callback(
    Output('save-output', 'children'),  # Assuming you have an element with id 'save-output'
    [Input('save', 'n_clicks')],
    [State('ip', 'value'),
     State('port', 'value')]
)
def save(n_clicks, ip, port):
    if n_clicks:
        page.ip = ip
        page.port = port
        # Return some feedback, e.g., "Settings saved."
        return "Settings saved."

if __name__ == '__main__':
    try:
        app.run_server(debug=True)
    except Exception as e:
        pass
