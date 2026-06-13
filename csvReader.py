import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the CSV file, skip unnamed index column
df = pd.read_csv("Weather Data in India from 1901 to 2017.csv", index_col=0)

# 2. Rename the columns properly (13 columns: Year + 12 months)
df.columns = ['Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# 3. Calculate Average Temperature for each Year
df['AvgTemp'] = df.loc[:, 'Jan':'Dec'].mean(axis=1)

# 4. Plot: Average Yearly Temperature over the years
plt.figure(figsize=(12, 6))
plt.plot(df['Year'], df['AvgTemp'], color='orange', marker='o', label='Avg Yearly Temp')
plt.title("Average Yearly Temperature in India (1901–2017)")
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# 5. Plot: Average Monthly Temperatures (across all years)
monthly_avg = df.loc[:, 'Jan':'Dec'].mean()
plt.figure(figsize=(10, 5))
monthly_avg.plot(kind='bar', color='skyblue')
plt.title("Average Monthly Temperature in India (1901–2017)")
plt.xlabel("Month")
plt.ylabel("Avg Temperature (°C)")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# 6. Plot: Heatmap of monthly temperatures by year
plt.figure(figsize=(14, 10))
sns.heatmap(df.loc[:, 'Jan':'Dec'], cmap='coolwarm', cbar_kws={'label': 'Temperature (°C)'})
plt.title("Monthly Temperature Heatmap (1901–2017)")
plt.xlabel("Month")
plt.ylabel("Year Index")
plt.tight_layout()
plt.show()

# 7. Decade-wise Average Temperature
df['Decade'] = (df['Year'] // 10) * 10
decade_avg = df.groupby('Decade')['AvgTemp'].mean()

plt.figure(figsize=(10, 5))
decade_avg.plot(kind='bar', color='teal')
plt.title("Decade-wise Average Temperature in India")
plt.xlabel("Decade")
plt.ylabel("Average Temperature (°C)")
plt.tight_layout()
plt.show()

# 8. Print top 5 hottest and coldest years based on average temperature
print("\nTop 5 Hottest Years:")
print(df[['Year', 'AvgTemp']].sort_values(by='AvgTemp', ascending=False).head())

print("\nTop 5 Coldest Years:")
print(df[['Year', 'AvgTemp']].sort_values(by='AvgTemp', ascending=True).head())

# 9. Save DataFrame with calculated averages and decade info to a new CSV file
df.to_csv("weather_with_avg_and_decade.csv", index=False)
