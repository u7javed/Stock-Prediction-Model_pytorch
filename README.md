# Stock-Prediction-Model_pytorch
An GRU (Gated Recurrent Unit) model that can predict stops to an extremely well accuracies. Relies on Memory retention ability of LSTM/GRU models. The model being used to predict stock prices is an Autoregressive integrated moving average model. This model evaluates or predicts time series based on past data and behaviours.

Dataset for stock prediction was retrieved from https://github.com/nageshsinghc4/stock-market-forecasting

Files:
  - model.py 
    - contains the model architecture being used in time-series stock prediction.
  
  - utilities.py 
    - contains functions for preprocessing data such as converting stock values to specific length time-series vectors to feed into the network
  
  - stock_predictor
    - a complete walkthrough of the entire process of training a time-series GRU model for predicting time-series data. 
    
It is important to note that this model will work with any timeseries stock prices dataset as long as the data is preprocessed accordingly.

After a certain number of epochs, the loss of the model starts stagnating at which point, the model has converged:

## Loss Graph:

![](data/uploads/loss.png)

## Here is the result from the trained GRU model:

![](data/uploads/prediction_result.png)
