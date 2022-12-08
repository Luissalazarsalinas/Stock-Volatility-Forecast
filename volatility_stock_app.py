import json
import sqlite3
import requests

import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
from app.data import AlphaVantageApi
from  app.forecast import forecast_volatility


# App title
st.title("Stock Volatility Forecast App")

#some image
st.image("img/Volatility.jpg")

# Description
st.write(
    """
    ## About
    
    The main motivation for studying conditional heroskedasticity in finance is that of volatility of asset returns. 
    Volatility is an important concept in finance because it is highly synonymous with risk. 
    Hense, if we can effectively forecast volatility then we will be able to price options more accurately, 
    create more sophisticated risk management tools for the algorithmic trading portfolios and even come up with new strategies taht trade volatility directly.

    **This Streamlit App  utilizes a Statistical model to forecast the stocks volatility.**
    
    All documentations are available on [Github](https://github.com/Luissalazarsalinas/Fraud-Detection)
    
    **Made by Luis Fernando Salazar S.**
    """
)

################################# INPUT DATA ###########################################
########################################################################################
st.sidebar.header(" Input data")


ticker = st.sidebar.text_input("Symbol")
#num_observation = st.sidebar.slider("Number Observations (Optional)", min_value= 100, max_value= 3000)

st.sidebar.subheader("Model Parameters")

p = st.sidebar.slider("Lag order of the symmetric innovation - P", min_value=1, max_value=10)
q = st.sidebar.slider("Lag order of lagged volatility or equivalent - q", min_value=1, max_value=10)

st.sidebar.subheader("Forecasting")

n_days = st.sidebar.slider("Horizon (days)", min_value=5, max_value=10)

################################### PLOTS #################################
###########################################################################

if not ticker:
    st.write("## **Please insert a stock symbol**")
    st.stop()

else:
    # Intance 
    av = AlphaVantageApi()
    # Get a dataframe
    df = av.get_daily(ticker)
    # sort index values
    df.sort_index(ascending=True, inplace=True)
    # Add returns
    df["returns"] = df["close"].pct_change()*100
    # drop missing value
    df.dropna(inplace = True)
    # Computing  annual volatility
    volatility_annual = df["returns"].rolling(window=50).std().dropna()


######################################################################
######################## Close price chart ###########################
# Line chart - Close price
st.markdown(f"#### **{ticker} - Close Price**")
def line_chart(data):

    figure = px.line(
        data_frame = data,
        x= data.index,
        y= "close",
    )

    figure.update_layout( xaxis_title = "Date", yaxis_title = "Stock Price Close [$]")

    return figure

st.plotly_chart(line_chart(df), use_container_width= True)

###########################################################################
############################ Returns and volatility################################

def hist_plot(data):

    figure = px.histogram(
        data_frame= data,
        x="returns",
        nbins= 10
    )
    figure.update_layout(xaxis_title = "Date", yaxis_title = "Frequency")

    return figure


st.markdown("###")
fig = go.Figure([

    go.Scatter(
        name='Daily Returns',
        x=df.index,
        y=df['returns'],
        mode='lines',
        marker=dict(color="#444"),
        line=dict(width=1),
        showlegend=True
    ),
    go.Scatter(
        name='50 DS Volatility',
        x=volatility_annual.index,
        y=volatility_annual,
        mode='lines',
        marker=dict(color='red', size=2),
        showlegend=True
    )

    ])
fig.update_layout(
    xaxis_title = 'Date'
)

with st.expander("Display Daily Returns Plots"):
    
    st.markdown("### Histogram - Daily Returns")
    st.plotly_chart(hist_plot(df), use_container_width= True)

    st.markdown("### Daily Returns and Annual Volatility")
    st.plotly_chart(fig, use_container_width=True)

################################# Correclations Plots###########################
################################################################################
with st.expander("Display Autocorreclations Plots"):

    st.markdown("### Autocorrelaction Funtion Plot - Squared Returns")
    fig, ax = plt.subplots()
    plot_acf(df["returns"]**2, ax = ax)
    st.pyplot(fig)

    st.markdown("### Partial Autocorrelaction Funtion Plot - Squared Returns")
    fig2, ax2 = plt.subplots()
    plot_pacf(df["returns"]**2, ax = ax2)
    st.pyplot(fig2)

#################################### FORECASTING #########################
###########################################################################

forecast = st.button("Detect Results")

if forecast:

    # Forecasting
    st.write("## Volatility Forecast")

    forecasting = forecast_volatility(
       ticker=ticker,
       p=p,
       q=q,
       n_days=n_days 
    )
    # Metrics
    metrics = forecasting["metrics"] 
    aic = metrics["AIC"]
    bic = metrics["BIC"]

    # Message
    message = forecasting["message"]


      # summary
    st.write(
          f""" 
        ### **Model Details**

        Stock Symbol: {ticker}\n
        Model: "GRACH"\n
        Model parameter - p: {p}\n
        Model parameter - q: {q}

        ##### **Metrics**:
        AIC: {aic}\n
        BIC: {bic}\n

        """
    )
    # result
    st.write(f"### {message} Results")

    ## Create a dataframe from the dict response that has the forecast result and end this project
    result_forecast = forecasting["forecast"]
    df_result = pd.DataFrame(result_forecast, dtype=float, index = ["Volatility Forecast"]).T
    
    st.dataframe(df_result)




   
        