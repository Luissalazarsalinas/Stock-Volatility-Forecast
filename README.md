# **Stock Volatility Forecast**

[![Language](https://img.shields.io/badge/Python-darkblue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Framework](https://img.shields.io/badge/sklearn-darkorange.svg?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Framework](https://img.shields.io/badge/FastAPI-darkgreen.svg?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Framework](https://img.shields.io/badge/Streamlit-red.svg?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
![hosted](https://img.shields.io/badge/Heroku-430098?style=flat&logo=heroku&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-blue?style=flat&logo=docker&logoColor=white)

An end-to-end Data Science Project to forecast stock volatilities.

## Problem Statement
The main motivation for studying conditional heroskedasticity in finance is that of volatility of asset returns. Volatility is an important concept in finance because it is highly synonymous with risk. Hense, if we can effectively forecast volatility then we will be able to price options more accurately, create more sophisticated risk management tools for the algorithmic trading portfolios and even come up with new strategies taht trade volatility directly.

Therefore, in this project we develop a Streamlit App that utilizes a Statistical model as an API to forecast the stocks volatility. 

The App can be viewed through this [link]()

## Data 

Finance data (daily trading) were extracted from [Alpha Vantage API](https://www.alphavantage.co/). 

#### Data preprocessing stets:
 - Transform the data from json format to a dataframe format
 - Clean and wrangle the data
 - Stored the data in a relational database
 - calculate daily stock returns from close prices

#### Model
**Generalized Autoregressive conditional heroskekedasticity (GARCH)**

Generalized AutoRegressive Conditional Heteroskedasticity (GARCH) is a statistical model used in analyzing time-series data where the variance error is believed to be serially autocorrelated. GARCH models assume that the variance of the error term follows an autoregressive moving average process.

Usually a GARCH(p = 1, q = 1) is specified as:
![model](https://github.com/Luissalazarsalinas/Stock-Volatility-Forecast/blob/master/img/2022-12-05.png)

For more informations over GARCH model visit the following [link](https://www.quantstart.com/articles/Generalised-Autoregressive-Conditional-Heteroskedasticity-GARCH-p-q-Models-for-Time-Series-Analysis/)

## Deployment
The API was deployed using docker container on Heroku and the Streamlit App was deployed on Streamlit Cloud

<details> 
  <summary><b>💻 Deploying the API</b></summary>

1. Heroku logging 

```
Heroku login
```

2. Create a heroku app

```
heroku create <app-name> 
```

3. Set the heroku cli git remote to that app

``` 
heroku git:remote <app-name>
```

4. Set the heroku stack setting to container

```
heroku stack:set container
```

5. Push to herokuPush to heroku
 
```
git push heroku branch <master/main>
```
</details>

