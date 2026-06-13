# plot_monthly_avg.py
import matplotlib.pyplot as plt
from load_data import load_weather_data

def plot_monthly_avg(df):
    monthly_avg = df[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']].mean()
    plt.figure(figsize=(10,5))
    monthly_avg.plot(kind='bar', color='skyblue')
    plt.title("Average Monthly Temperature (All Years Combined)")
    plt.xlabel("Month")
    plt.ylabel("Average Temperature (°C)")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = load_weather_data()
    plot_monthly_avg(df)
