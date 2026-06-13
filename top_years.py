# top_years.py
import matplotlib.pyplot as plt
from load_data import load_weather_data
from avg_temp import calculate_avg_temp


def plot_top_years(top_years, cold_years):
    fig, ax = plt.subplots(1, 2, figsize=(14,6))

    ax[0].bar(top_years['Year'].astype(str), top_years['AvgTemp'], color='red')
    ax[0].set_title("Top 5 Hottest Years")
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Avg Temperature (°C)")

    ax[1].bar(cold_years['Year'].astype(str), cold_years['AvgTemp'], color='blue')
    ax[1].set_title("Top 5 Coldest Years")
    ax[1].set_xlabel("Year")
    ax[1].set_ylabel("Avg Temperature (°C)")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = load_weather_data()
    df = calculate_avg_temp(df)

    top_years = df[['Year', 'AvgTemp']].sort_values(by='AvgTemp', ascending=False).head(5)
    cold_years = df[['Year', 'AvgTemp']].sort_values(by='AvgTemp', ascending=True).head(5)

    print("\nTop 5 Hottest Years:")
    print(top_years.to_string(index=False))

    print("\nTop 5 Coldest Years:")
    print(cold_years.to_string(index=False))

    plot_top_years(top_years, cold_years)
