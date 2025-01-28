from dash import Dash,html,dcc
from dash.dependencies import Input, Output, State
from dash import callback_context
import page
app = Dash(__name__)
app.title = 'TOR+'
home = html.Div(
    # id='page-co
    style={
        'text-align':'center',
        'width':'100%',
        'top':'0px',
        'left':'0px',
        'height':'100%',
        'background':'#1a1a1a',
        'color':'#fff',
        'margin':'0px',
        # 'padding-left':'10px',
        # 'padding-right':'10px',
        # 'padding-top':'10px',
        'padding-bottom':'100%',
        },
    children=[
        dcc.Location(id='url', refresh=False),
        dcc.Interval(
            id='interval',
            interval=0.1*1000,
            n_intervals=0
        ),
        html.Br(),
        # html.H1(style={'text-align':'center','color':'green','font-family':'verdana'},children='TOR+'),
        html.Div(style={'display':'flex','justify-content':'center'},children=[
        html.H3(style={'text-align':'center','color':'green','font-family':'verdana','margin':'25px'},children=['TOR+']),
        html.Div(
            style={
                'margin':'15px',
                'padding':'15px',
                'width':'90%',
                'display':'flex',
                'border-color':'white',
                'border-radius':'20px',
                'background':'#252526',
                'height':'25px',
                }
            ,
            children=[
                dcc.Input(style={'text-weight':'900','type':'text','width':'89%','border':'none','border-radius':'10px','placeholder': 'URL','background-color':'#2b2c2e','color':'green','font-family':'verdana'},id='input'),
                html.Div(style={'width':'2%'}),
                html.Button('LOAD',style={'text-weight':'900','text-align':'center','width':'10%','border':'none','border-radius':'10px','background-color':'#2b2c2e','color':'green','font-family':'verdana'},id='load'),
                # html.Button('RESET',style={'text-weight':'900','text-align':'center','width':'5%','border':'none','border-radius':'10px','background-color':'#2b2c2e','color':'red','font-family':'verdana'},id='reset'),
            ]
        ),
        html.Div(style={'margin':'25px','width':'5%','height':'25px'},id='setting',children=[html.Img(src='http://assets.csec.top/s.svg')]),
        ]),
        html.Div(id='page-content',style={'padding':'5px','margin':'25px','width':'95%','height':'90%','border':'2px solid white','border-radius':'10px',}),
        html.P('We recomend u to visit sites more than 4 chars, because hackers can use about 5 seconds to crack your secure link,that has big lettera,small letters and numbers! But they need to use mode than 5 mins to crack long links that are about 8 chars long!')
    ],
)
app.layout = home
# when the user clicks on the button, get the value of the input and load the page
# make the app run
@app.callback(
    Output('page-content', 'children'),
    Input('load', 'n_clicks'),
    Input('setting', 'n_clicks'),
    State('input', 'value'),
)
def update_output(n_clicks_load, n_clicks_setting, value):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    
    if 'load.n_clicks' in changed_id:
        # Validate the URL (simple check for 'http://' or 'https://')
        # if value.startswith('http://') or value.startswith('https://'):
        #     return "Please don't enter a URL starting with 'http://' or 'https://'. \n TOR+ will automatically add 'https://' to the URL."
           return page.load(value)

    elif 'setting.n_clicks' in changed_id:
        page.setting()
        return None



if __name__ == '__main__':
    try:
     app.run_server(debug=True)
    except Exception as e:
        pass