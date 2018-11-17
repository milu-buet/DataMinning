# Md Lutfar Rahman
# mrahman9@memphis.edu
# DataMining Assingment 5

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import random
from helper import Helper
import pandas

import time
ratings_file = 'ratings.csv'
def addnewRating(userId, movieId, rating):
    timestamp = int(time.time())
    df = pandas.read_csv(ratings_file)
    a = df[(df.userId == userId) & (df.movieId == movieId)]
    if len(a) < 1:
        df = df.append({'userId' : userId , 'movieId' : movieId, 'rating': rating, 'timestamp': timestamp} , ignore_index=True)
        df.to_csv(ratings_file, index=False)

def getRandomUnseenMovie(userId):
    a = Helper().getRandomUnseenMovie(userId)
    #print(a)
    return a


def getRecommendedMovie(userId): 
    return Helper().getRecommendedMovie(userId)



def create_app():

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    app.config['suppress_callback_exceptions']=True
    setAppLayout(app)
    app.run_server(debug=True)


def getLayout(options):

    return html.Div(children=[
            html.H1(id='head', children='Q'+ str(options['qid'])+'. Rate this movie'),
            html.Div(children='Name: ' + options['movie']),
            'Rating: ',
            dcc.Input(
                id='input-box',
                placeholder='Enter ratings...',
                type='text',
                value=''
            ),
            html.Div(id='dum', children=''),
            html.Button('Submit', id='button1')

        ])

def getWelcomeLayout():
    
    return html.Div(children=[
            html.H1(id='head', children='Loading ....'),
            dcc.Input(
                id='input-box',
                placeholder='Enter ratings...',
                type='text',
                value='',
            ),
            html.Div(id='dum', children=''),
            html.Button('Submit', id='button1')

        ])

def getEndLayout():
    return html.Div(children="Thanks for the ratings")

qid=0
userId = 611
movie = 'Toy Story (1995)'
movieId = 1

def setAppLayout(app):

    options = {'qid':0, 'movie':'movie'}
    app.layout = html.Div(id ='page-content',children=getWelcomeLayout())

    @app.callback(
    Output(component_id='page-content', component_property='children'),
    [Input('button1', 'n_clicks')],
    [State('input-box', 'value')]
    )
    def rate(n_clicks, value):
        global qid, userId, movie, movieId

        if qid == 7:
            return getEndLayout()

        if qid > 0 and qid < 8:
            addnewRating(userId, movieId, value)

        if qid == 0:
            movieId, movie = getRandomUnseenMovie(userId)
        else:
            movieId, movie = getRecommendedMovie(userId)

        
        qid += 1
        options = {'qid':qid, 'movie':movie}
        return getLayout(options)

if __name__ == '__main__':
    create_app()
    #addnewRating(611, 170875, 3)