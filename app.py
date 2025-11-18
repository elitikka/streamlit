import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Oulu Kaukovainio, Avg Temperature (per hour)")

    df = pd.read_csv("Oulu Kaukovainio_ 1.11.2025 - 17.11.2025_sade.csv")

    df["datetime"] = pd.to_datetime(
        df["Year"].astype(str) + "-" +
        df["Month"].astype(str) + "-" +
        df["Date"].astype(str) + " " +
        df["Time [Local time]"].astype(str)
    )

    df.rename(columns={"Average temperature [C]": "temp"}, inplace=True)

    fig = px.line(
        df,
        x="datetime",
        y="temp",
        title="Hourly Average Temperature in Oulu (Kaukovainio)",
        labels={"datetime": "Date/Time", "temp": "Temperature (°C)"}
    )

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
