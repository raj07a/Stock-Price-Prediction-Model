# Stock-Price-Prediction-Model
Stock price prediction using Lstm

This project implements a Long Short-Term Memory (LSTM) network for predicting stock prices. It utilizes historical closing price data to train the model and forecast future trends.

Key functionalities:

Data Acquisition: Downloads historical closing prices for a specified stock symbol and date range using the yfinance library.
Data Preprocessing: Cleans and prepares the data for the model by:
Splitting it into training and testing sets.
Normalizing the price values using a MinMaxScaler for better model training.
Sequence Creation: Creates sequences of data points from the training and testing sets using a custom function create_sequences. This is crucial for LSTM models as they process data sequentially.
LSTM Model Building:
Constructs a sequential LSTM model with customizable architecture (currently uses two LSTM layers).
Compiles the model with the Adam optimizer and the mean squared error (MSE) loss function.
Trains the model on the training sequences for a specified number of epochs.
Evaluation and Prediction:
Evaluates the model's performance on the testing set using the MSE metric.
Generates predictions for closing prices on the testing data points.
Inverse-transforms the predicted values to obtain the actual price scale.
Visualization and Analysis:
Creates a candlestick chart to visualize the actual stock price movements.
Plots the predicted prices alongside actual prices to compare their trends.
Calculates and plots various technical indicators for further analysis:
Cumulative Returns: Shows how returns accumulate over time for actual and predicted prices.
Rolling Mean (e.g., 20-day): Highlights the overall price trend.
Exponential Moving Average (EMA) (e.g., 9-day): Identifies short-term trends.
Relative Strength Index (RSI): Assesses the stock price momentum.
Project Benefits:

Provides a framework for building LSTM-based stock price prediction models.
Offers functionalities for data acquisition, preprocessing, model training, evaluation, and visualization.
Enables exploration of different LSTM architectures and hyperparameters for potentially improved prediction accuracy.
Note: Stock price prediction is a complex task, and the model's performance may vary depending on market conditions and data quality.
