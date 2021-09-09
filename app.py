import json
import csv
import streamlit as st
import pandas as pd
import graph as g
import datetime
import requests
token = 'pk_ba53db3c184a4c2c843e21f96c0403f0'

with open('Stock List.json') as json_file:
    jsondata = json.load(json_file)
    
data_file = open('convert_csv.csv', 'w', newline='')
csv_writer = csv.writer(data_file)
count = 0
for data in jsondata:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())

data_file.close()


df = pd.read_csv('convert_csv.csv')
symbol_names = df['symbol'].unique()

st.sidebar.subheader('Query parameters')
start_date = st.sidebar.date_input("Start date", datetime.date(2021, 1, 4))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 8, 25))

def main():
    html_temp=""" <div style="background-color:#025247; padding:10px"> <h2 style="color:white;text-align:center;">OHLC Engine</h2></div> """
    st.markdown(html_temp, unsafe_allow_html=True)
    symbol = st.selectbox("Enter company symbol",symbol_names)
    graph_type = st.selectbox("Select graph type",['OHLC','Candlestick charts','Vertex Line','Hollow Candle'])
    if st.button('SHOW CHART'):
        from select_stock import select
        select(symbol,start_date,end_date)
        if graph_type == 'OHLC':
            fig = g.ohlc_gen()
            st.plotly_chart(fig)
        elif graph_type == 'Candlestick charts':
            fig = g.candle_gen()
            st.plotly_chart(fig)
        elif graph_type == 'Colored Bar':
            fig = g.coloured_bar()
            st.plotly_chart(fig)
        elif graph_type == 'Vertex Line':
            fig = g.vertex_line()
            st.plotly_chart(fig)
        elif graph_type == 'Hollow Candle':
            fig = g.hollow_gen()
            st.plotly_chart(fig)

    st.sidebar.subheader('Want to know more about company')
    api_url = f'https://cloud.iexapis.com/stable/stock/{symbol}/company/?token={token}'
    data = requests.get(api_url).json()
    if st.sidebar.button('DETAILS'):
        n = data["symbol"]
        company_name = data["companyName"]
        exchange = data["exchange"]
        industry = data["industry"]
        website = data["website"]
        ceo = data["CEO"]
        city = data["city"]
        country = data["country"]
        st.sidebar.write("Company Name: ",company_name)
        st.sidebar.write("Industry: ",industry)
        st.sidebar.write("Exchange: ",exchange)
        st.sidebar.write("Website: ",website)
        st.sidebar.write("CEO: ",ceo)
        st.sidebar.write("City: ", city)
        st.sidebar.write("Country: ",country)

if __name__=='__main__':
    main()






