# AI INFINITY SQUAD - Climate Change Dashboard

## TEAM NAME -
**AI INFINITY SQUAD**

## Prject title:
**Climate Change Dashboard**

## Description:
Analyze global temperature anomalies and visualize their impact on regions

## Group Members:
~DUDANI JIYA [KU2407U400]
~MAHI SHAH [KU2407U422]
~KRISHNA LATHIYA [KU2407U421]
~SATVIK JOSHI [KU2407U439]

## Project Overview
The **Climate Change Dashboard** is a Python-based project that analyzes global temperature anomalies and visualizes their trends and regional impacts. It highlights the effect of climate change through statistical analysis and interactive visualizations, enabling better understanding and awareness of global warming.

## Project Objectives
1. Analyze global temperature anomalies over time.
2. Visualize temperature trends and their distribution.
3. Highlight the impacts of climate change on specific regions.

## Tools and Libraries Used
- **Programming Language**: Python
- **Libraries**:
  - NumPy
  - Pandas
  - Matplotlib
  - Seaborn

## Data Source
The dataset is a sample representing global temperature anomalies, inspired by publicly available climate datasets:
- [NASA GISS Surface Temperature Analysis](https://data.giss.nasa.gov/gistemp/)
- [NOAA Global Temperature Data](https://www.ncei.noaa.gov/access/monitoring/global-temperature-anomalies)

## steps of execution:
1. Initial Setup and Imports:
Libraries such as os, pandas, numpy, matplotlib, and seaborn are imported.
File paths are defined for the data (global_temp_anomalies.csv) and where visualizations will be saved (visuals/).
The visuals/ directory is created if it does not already exist using os.makedirs.
2. Main Execution Flow:
The main() function is where the script starts executing, and the following sequence of steps is performed:

Step 1: Loading the Data
python
Copy code
data = load_data(DATA_FILE)
Action: The load_data() function is called to load the global temperature anomaly data from the global_temp_anomalies.csv file.
Possible outcomes:
If the file is found, the function returns a pandas DataFrame containing the data, and a message "Data loaded successfully." is printed.
If the file is not found, it prints an error message and returns None.
Step 2: Preprocessing the Data
python
Copy code
data = preprocess_data(data)
Action: The preprocess_data() function is called to clean and preprocess the loaded data.
Missing values (NaN) are dropped from the DataFrame.
The columns Year and Temperature_Anomaly are converted to the correct data types (int for year and float for temperature anomalies).
A message "Data preprocessing complete." is printed.
Step 3: Performing Data Analysis
python
Copy code
analyze_data(data)
Action: The analyze_data() function is called to perform basic analysis on the temperature anomaly data.
The average temperature anomaly is computed using np.mean().
The maximum temperature anomaly and the corresponding year are identified using max() and idxmax().
The results are printed out in a readable format:
The average temperature anomaly in degrees Celsius (°C).
The year with the maximum temperature anomaly and the value of the anomaly in °C.
Step 4: Visualizing the Trends
python
Copy code
visualize_trends(data)
Action: The visualize_trends() function is called to generate visualizations.
Plot 1: A line plot of global temperature anomalies over time (years), showing how anomalies have changed over the years.
Plot 2: A histogram with a Kernel Density Estimate (KDE) to show the distribution of temperature anomalies across the dataset.
Both plots are saved as PNG files in the visuals/ folder, and they are also displayed using plt.show().
3. Script Execution Summary:
Flow of Execution:
Load Data: The data is loaded from a CSV file into a pandas DataFrame.
Preprocess Data: The data is cleaned by dropping missing values and ensuring correct data types.
Analyze Data: Basic analysis (average and max anomalies) is computed and printed.
Visualize Data: Two visualizations (line plot and histogram) are created and saved.
4. Key Functions and Their Roles:
load_data(filepath): Reads the CSV file and returns the data as a pandas DataFrame.
preprocess_data(data): Cleans the data by removing missing values and ensuring correct column data types.
analyze_data(data): Computes basic statistical metrics on the temperature anomalies (mean, max, year of max).
visualize_trends(data): Creates and saves visualizations of the temperature anomaly trends and their distribution.
5. Execution Start (if __name__ == "__main__":)
The script will only run when executed directly (not when imported as a module).
The main() function is called to trigger the sequence of steps: load data, preprocess, analyze, and visualize.
Example Flow Through the Program:
Assuming the data file (global_temp_anomalies.csv) exists and is properly formatted, here's an example of how the script executes:

The main() function is triggered.
The load_data() function loads the data from global_temp_anomalies.csv.
If successful, it prints: Data loaded successfully.
The preprocess_data() function cleans the data.
It prints: Data preprocessing complete.
The analyze_data() function computes the average temperature anomaly, maximum anomaly, and year of maximum anomaly, and prints something like:
yaml
Copy code
Average Temperature Anomaly: 0.82 °C
Maximum Temperature Anomaly: 1.22 °C in 2016
The visualize_trends() function generates and saves:
A line plot of temperature anomalies over time.
A histogram of the distribution of anomalies.
Error Handling and Debugging:
If the file is not found:
The script prints an error message and halts further execution.
If there are missing values in the data:
These are dropped during preprocessing (dropna()), and the analysis will proceed with the cleaned data.
Suggestions for Improvement:
Data Validation: Add checks for data consistency, such as ensuring the 'Year' and 'Temperature_Anomaly' columns exist before preprocessing.
Error Handling for Other Issues: Handle potential issues like incorrect data types, missing columns, or unexpected data formats.
User Input for File Path: Allow the user to specify the file path for greater flexibility, instead of hardcoding it.
## Folder Structure
