import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_resource 
def mySql(): 
     
    # Initialize connection. 
    conn = st.connection('mysql', type='sql') 
 
    # Perform query. 
    df = conn.query('SELECT `Year`, `Month`, `Date`, `Time`, `AvgTemp` FROM weather ORDER BY `Year`, `Month`, `Date`, `Time`;', ttl=600) 
    df['datetime'] = pd.to_datetime(
            df['Year'].astype(str) + '-' +
            df['Month'].astype(str) + '-' +
            df['Date'].astype(str) + ' ' +
            df['Time'].astype(str)
        )    
    return df 
 
# Streamlit 
def main(): 
    st.title("Temperature from MySQL") 
     
    data = mySql() 
     
    #plot data 
    fig = px.line(
        data,
        x='datetime',
        y='AvgTemp',
        title="Temperature in Oulu (Kaukovainio)",
        labels={'datetime': 'Date/Time', 'AvgTemp': 'Temperature (°C)'}
    )
    
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main() 