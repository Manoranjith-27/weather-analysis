import matplotlib.pyplot as plt
from load_data import load_weather_data
from avg_temp import calculate_avg_temp

def plot_yearly_avg(df):
    plt.figure(figsize=(12, 6))
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
    plot_yearly_avg(df)
