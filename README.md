# **Stock Volatility Forecast**

[![Language](https://img.shields.io/badge/Python-darkblue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Framework](https://img.shields.io/badge/sklearn-darkorange.svg?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Framework](https://img.shields.io/badge/FastAPI-darkgreen.svg?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Framework](https://img.shields.io/badge/Streamlit-red.svg?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
![hosted](https://img.shields.io/badge/Heroku-430098?style=flat&logo=heroku&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-blue?style=flat&logo=docker&logoColor=white)

An end-to-end Machine Learning Project to detect fraud in credit card transactions.

## Problem Statement


The App can be viewed through this [link]()

[NoteBook]()

## Data Preparation

Credit card transaction is a syntetic financial dataset created using a simulator called PaySim. In this sense, PaySim uses aggregated data from the private dataset to generate a synthetic dataset that resembles the normal operation of transactions and injects malicious behaviour to later evaluate the performance of fraud detection methods.

#### Data preprocessing stets:
 - Clean the data: removed duplicate values, missing values, unnecessary and leakage variables
 - Transform no-numerical variables to numerical variables
 - Split the data into train, validation and test sets

Source dataset: [Credit card data](https://www.kaggle.com/datasets/ealaxi/paysim1)

#### Model
**Generalized Autoregressive conditional heroskekedasticity (GARCH)**

Generalized AutoRegressive Conditional Heteroskedasticity (GARCH) is a statistical model used in analyzing time-series data where the variance error is believed to be serially autocorrelated. GARCH models assume that the variance of the error term follows an autoregressive moving average process.

Usually a GARCH(p = 1, q = 1) is specified as:

\begin{equation}
\sigma_{t}^{2}=\omega+\alpha_{1}\varepsilon_{t-1}^{2}+\beta_{1}\sigma_{t-1}^{2},\tag{10.15}
\end{equation}



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

