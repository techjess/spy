import streamlit as st
from datetime import datetime,timedelta
import yfinance as yf
from joblib import load
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, f1_score, recall_score
import numpy
import pandas as pd

# my modules
from data_fetch import basic_df, df_with_target
from predict import backtest

# Load your trained model (adjust the path as necessary)
model = load('/home/jgarcia/Capstone/jgarcia_model.pkl')

# Fetch and prepare the data
df = df_with_target(basic_df())
# st.write(df)
predictors = list(df.columns[:-1])

# Cached function wrapper to ensure it runs once a day after the days trading period
time= timedelta(days=1)
@st.cache_resource(show_spinner=False,ttl=time)
def daily_backtest():
    # This function only runs when called with a new date or when the cache is cleared
    return backtest(df,model,predictors)

predictions = daily_backtest()


st.title('SPY Direction Predictor')
st.write('This model is trained on price going UP ONLY, not down. Upon hitting predict, the model will '
         'ouput whether it\'s prediction for today based on the completed trading calndar day. So if you are checking while trading is still open'
         'for the day, it will be based on data up to yesterday and output for tomorrow.')
if st.button('Predict Direction'):

    # Predict the direction
    direction = predictions.tail(1).iloc[0]["Predictions"]

    # Display the prediction
    if direction == 1:
        st.success('The model predicts the price will go UP tomorrow.')
    else:
        st.error('The model does not predict the stock will go up in a couple days.....\n NOTE::This is not a prediction for '
                 'the price going down!!!!')



    precis_score = precision_score(predictions["Target"], predictions["Predictions"])
    st.write(f'Precision score is {precis_score}. This is the accuracy of the model predicting price will go up. '
             f'So it was {precis_score:.0%} successful when it thought the price would go up')

    st.write(predictions["Predictions"].value_counts() / predictions.shape[0])
    recall = recall_score(predictions["Target"], predictions["Predictions"])
    st.write(f'Recall (Sensitivity): {recall}')
    f1 = f1_score(predictions["Target"], predictions["Predictions"])
    st.write(f'F1 Score: {f1}')
    st.write(f"This is the predictions to actual price movedment for the last five days\n"
             "'Target' is what really happened\n '0's mean that it did not predict anything"
             "\n Predictions are for every other day. The date shows the previous close, so I can take a position for tomorrow",
             predictions.tail(5))






