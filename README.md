### README.md

# SPY Direction Predictor

This project is a machine learning application that predicts the direction of the SPY ETF based on historical stock data. The model is designed to forecast whether the price will go up or not using a Random Forest Classifier. The predictions are presented through a Streamlit web application.

## Project Structure

- `app.py`: The main application script that runs the Streamlit web interface.
- `data_fetch.py`: Script to fetch and preprocess historical stock data.
- `predict.py`: Contains the functions for training the model and making predictions.

## Installation

To run this project, you'll need Python 3.x and the following Python libraries:

- streamlit
- yfinance
- joblib
- scikit-learn
- numpy
- pandas

You can install the required libraries using pip:

```bash
pip install streamlit yfinance joblib scikit-learn numpy pandas
```

## Usage

1. **Fetch and Prepare Data**: The `data_fetch.py` script fetches historical data for SPY, XLK, NIKKEI, and DJI from Yahoo Finance and prepares it for training and prediction.

2. **Train and Predict**: The `predict.py` script includes functions to train a Random Forest model and make predictions on the stock direction.

3. **Run the Application**: Use the `app.py` script to launch the Streamlit web application. The application displays the prediction for the SPY ETF based on the most recent trading data.

### Running the Streamlit Application

To run the Streamlit application, execute the following command in your terminal:

```bash
streamlit run app.py
```

This will start a local web server and open the application in your default web browser.

## Detailed Descriptions

### app.py

This script is the main entry point for the Streamlit application. It includes the following features:

- **Title and Description**: Displays the title and a brief description of the model and its predictions.
- **Data Fetching**: Calls functions from `data_fetch.py` to fetch and prepare the data.
- **Prediction**: Uses the trained model to predict whether the SPY price will go up the next day.
- **Metrics**: Shows precision, recall, and F1 score of the model based on historical predictions.

### data_fetch.py

This script fetches historical stock data and prepares it for model training and prediction:

- **basic_df()**: Fetches historical data for SPY, XLK, NIKKEI, and DJI from Yahoo Finance and combines them into a single DataFrame.
- **df_with_target()**: Adds target variables and technical indicators to the DataFrame, such as daily range and Fibonacci retracement levels.

### predict.py

This script contains functions to train the model and make predictions:

- **predict()**: Trains the model on the provided data and makes predictions.
- **backtest()**: Simulates predictions over a historical period to evaluate model performance.

## Contributing

If you would like to contribute to this project, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---

Feel free to customize this README to better fit your project's needs. If you have any questions or need further assistance, don't hesitate to ask!
