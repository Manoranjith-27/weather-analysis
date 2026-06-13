# load_data.py
import pandas as pd

def load_weather_data(filename="Weather Data in India from 1901 to 2017.csv"):
    df = pd.read_csv(filename, index_col=0)
    df.columns = ['Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return df

if __name__ == "__main__":
    df = load_weather_data()
    print(df.head())
