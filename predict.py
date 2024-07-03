
import yfinance as yf
import numpy
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, f1_score, recall_score
def predict(train, test, predictors, model):
    model.fit(train[predictors], train["Target"])
    preds = model.predict_proba(test[predictors])[:,1]
    preds[preds >= .60] = 1
    preds[preds < .60] = 0
    preds = pd.Series(preds, index=test.index, name="Predictions")
    combined = pd.concat([test["Target"], preds], axis=1)
    return combined

def backtest(data, model, predictors, start=2500, step=250):
    all_predictions=[]
    for i in range(start, data.shape[0], step):
        # grabbing first ten years of data
        train = data.iloc[:i].copy()
        # predict next year
        test = data.iloc[i:(i+step)].copy()
        predictions = predict(train, test, predictors,model)
        all_predictions.append(predictions)
    return pd.concat(all_predictions)

# Cached function wrapper to ensure it runs once a day

