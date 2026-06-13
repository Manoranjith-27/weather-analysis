# avg_temp.py
import pandas as pd
import matplotlib.pyplot as plt
from load_data import load_weather_data

def calculate_avg_temp(df):
    df['AvgTemp'] = df[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']].mean(axis=1)
    return df

def plot_avg_temp(df):
    plt.figure(figsize=(12,6))
    plt.plot(df['Year'], df['AvgTemp'], color='orange', marker='o', label='Avg Temp')
    plt.title("Average Yearly Temperature (1901 onwards)")
    plt.xlabel("Year")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = load_weather_data()
    df = calculate_avg_temp(df)
    plot_avg_temp(df)
