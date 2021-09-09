
import pandas as pd
import plotly.graph_objects as go

def candle_gen():
    df = pd.read_csv('output.csv')
    fig = go.Figure(data=go.Candlestick(x=df['date'], open=df['open'], high=df['high'], low=df['low'], close=df['close']))
    return fig

def ohlc_gen():
    df = pd.read_csv('output.csv')
    fig = go.Figure(data=go.Ohlc(x=df['date'], open=df['open'], high=df['high'], low=df['low'], close=df['close']))
        # fig.show()
    return fig

def vertex_line():

    df = pd.read_csv('output.csv')
    fig = go.Figure(go.Scatter(x=df['date'], y=df['close']))
    fig.update_layout(plot_bgcolor='rgb(230, 230,230)', showlegend=True)
    return fig

def hollow_gen():
    df = pd.read_csv('output.csv')
    fig = go.Figure(data=go.Candlestick(x=df['date'], open=df['open'], high=df['high'], low=df['low'],close=df['close'], increasing_line_color='blue', decreasing_line_color='white'))
    return fig






