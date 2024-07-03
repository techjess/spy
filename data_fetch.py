#initial dataframe
import yfinance as yf
import numpy
import pandas as pd


def basic_df():
    ticker_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    spy = yf.Ticker("SPY")
    xlk = yf.Ticker("XLK")
    nikk = yf.Ticker("^N225")
    dji = yf.Ticker("^DJI")

    df_nikk = nikk.history(period="max")
    df_nikk = df_nikk.loc["1993-01-29":].copy()
    df_nikk.index = df_nikk.index.date

    df_spy = spy.history(period="max")
    df_spy = df_spy.loc["1993-01-29":].copy()
    df_spy.index = df_spy.index.date

    df_dji = dji.history(period="max")
    df_dji = df_dji.loc["1993-01-29":].copy()
    df_dji.index = df_dji.index.date

    df_xlk = xlk.history(period="max")
    df_xlk = df_xlk.loc["1993-01-29":].copy()
    df_xlk.index = df_xlk.index.date

    # Example: Remove unnecessary columns or calculate any additional indicators
    df_spy = df_spy[ticker_columns]
    df_nikk = df_nikk[ticker_columns]
    df_dji = df_dji[ticker_columns]
    df_xlk = df_xlk[ticker_columns]

    spy_columns = {col: f"{col}_SPY" for col in df_spy.columns}
    nikk_dat_columns = {col: f"{col}_nikk" for col in df_nikk.columns}
    dji_dat_columns = {col: f"{col}_dji" for col in df_dji.columns}
    xlk_dat_columns = {col: f"{col}_xlk" for col in df_xlk.columns}

    df_spy = df_spy.rename(columns={**spy_columns})
    df_nikk = df_nikk.rename(columns={**nikk_dat_columns})
    df_dji = df_dji.rename(columns={**dji_dat_columns})
    df_xlk = df_xlk.rename(columns={**xlk_dat_columns})

    df = pd.concat([df_spy, df_nikk,df_dji,df_xlk], axis=1, join="inner")

    pd.set_option('display.max_columns', None)
    return df

def df_with_target(df):
    df['2_day_dir'] = (df["Close_SPY"].shift(1) < df['Close_SPY']).astype(int)

    df['2_day_dir_nikk'] = (df["Close_nikk"].shift(1) < df['Close_nikk']).astype(int)

    df['2_day_dir_dji'] = (df["Close_dji"].shift(1) < df['Close_dji']).astype(int)

    df['2_day_dir_xlk'] = (df["Close_xlk"].shift(1) < df['Close_xlk']).astype(int)

    df['spy_daily_range'] = df["High_SPY"] - df["Low_SPY"]
    df["nikk_daily_range"] = df["High_nikk"] - df["Low_nikk"]
    df['dji_daily_range'] = df["High_dji"] - df["Low_dji"]
    df["xlk_daily_range"] = df["High_xlk"] - df["Low_xlk"]

    # Calculate Fibonacci levels spy
    fib_levels = [0, 23.6, 38.2, 50, 61.8, 100]  # Expressed as percentages
    fib_retracement_levels = {}

    for level in fib_levels:
        if level == 0:
            df[f'Fib_Level_{level}%spy'] = df['High_SPY']
        elif level == 100:
            df[f'Fib_Level_{level}%spy'] = df['Low_SPY']
        else:
            df[f'Fib_Level_{level}%spy'] = df['High_SPY'] - (df['spy_daily_range'] * (level / 100))

    # Calculate Fibonacci levels spy
    fib_levels = [0, 23.6, 38.2, 50, 61.8, 100]  # Expressed as percentages
    fib_retracement_levels = {}

    for level in fib_levels:
        if level == 0:
            df[f'Fib_Level_{level}%nikk'] = df['High_nikk']
        elif level == 100:
            df[f'Fib_Level_{level}%nikk'] = df['Low_nikk']
        else:
            df[f'Fib_Level_{level}%nikk'] = df['High_nikk'] - (df['nikk_daily_range'] * (level / 100))

    # Calculate Fibonacci levels spy
    fib_levels = [0, 23.6, 38.2, 50, 61.8, 100]  # Expressed as percentages
    fib_retracement_levels = {}

    for level in fib_levels:
        if level == 0:
            df[f'Fib_Level_{level}%dji'] = df['High_dji']
        elif level == 100:
            df[f'Fib_Level_{level}%dji'] = df['Low_dji']
        else:
            df[f'Fib_Level_{level}%dji'] = df['High_dji'] - (df['dji_daily_range'] * (level / 100))

    # Calculate Fibonacci levels spy
    fib_levels = [0, 23.6, 38.2, 50, 61.8, 100]  # Expressed as percentages
    fib_retracement_levels = {}

    for level in fib_levels:
        if level == 0:
            df[f'Fib_Level_{level}%xlk'] = df['High_xlk']
        elif level == 100:
            df[f'Fib_Level_{level}%xlk'] = df['Low_xlk']
        else:
            df[f'Fib_Level_{level}%xlk'] = df['High_xlk'] - (df['xlk_daily_range'] * (level / 100))

    #creating my target of two days
    next_day = df["Close_SPY"].shift(-2)
    df["Target"] = (next_day > df["Close_SPY"]).astype(int)
    df.dropna()

    return df


