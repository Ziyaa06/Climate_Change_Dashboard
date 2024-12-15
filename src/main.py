# Climate Change Dashboard Project

## Directory Structure
# - data/
#   - global_temp_anomalies.csv (Placeholder for raw data file)
# - src/
#   - main.py (Main project file for analysis and visualization)
# - visuals/
#   - (Generated plots will be saved here)
# - README.md

# Required Libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# File Paths
DATA_FILE = "data/global_temp_anomalies.csv"
VISUALS_PATH = "visuals/"

# Ensure the visuals directory exists
os.makedirs(VISUALS_PATH, exist_ok=True)

# 1. Load Data
def load_data(filepath):
    """Load the global temperature anomaly data from CSV."""
    try:
        data = pd.read_csv(filepath)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None

# 2. Preprocess Data
def preprocess_data(data):
    """Clean and preprocess the data."""
    # Drop missing values
    data = data.dropna()

    # Ensure data types are correct
    data['Year'] = data['Year'].astype(int)
    data['Temperature_Anomaly'] = data['Temperature_Anomaly'].astype(float)

    print("Data preprocessing complete.")
    return data

# 3. Analysis
def analyze_data(data):
    """Perform basic analysis on the data."""
    avg_anomaly = np.mean(data['Temperature_Anomaly'])
    max_anomaly = data['Temperature_Anomaly'].max()
    max_anomaly_year = data.loc[data['Temperature_Anomaly'].idxmax(), 'Year']

    print(f"Average Temperature Anomaly: {avg_anomaly:.2f} \u00b0C")
    print(f"Maximum Temperature Anomaly: {max_anomaly:.2f} \u00b0C in {max_anomaly_year}")

    return avg_anomaly, max_anomaly, max_anomaly_year

# 4. Visualization
def visualize_trends(data):
    """Generate visualizations for temperature trends."""
    # Line plot of temperature anomalies over time
    plt.figure(figsize=(10, 6))
    plt.plot(data['Year'], data['Temperature_Anomaly'], marker='o', label='Anomaly (\u00b0C)')
    plt.title('Global Temperature Anomalies Over Time')
    plt.xlabel('Year')
    plt.ylabel('Temperature Anomaly (\u00b0C)')
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join(VISUALS_PATH, 'temp_anomalies_trend.png'))
    plt.show()

    # Distribution of anomalies
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Temperature_Anomaly'], kde=True, color='blue')
    plt.title('Distribution of Temperature Anomalies')
    plt.xlabel('Temperature Anomaly (\u00b0C)')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(VISUALS_PATH, 'anomaly_distribution.png'))
    plt.show()

# Main Execution
def main():
    # Load the data
    data = load_data(DATA_FILE)
    if data is None:
        return

    # Preprocess the data
    data = preprocess_data(data)

    # Analyze the data
    analyze_data(data)

    # Visualize the trends
    visualize_trends(data)

if __name__ == "__main__":
    main()
