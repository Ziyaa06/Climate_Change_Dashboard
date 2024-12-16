# AI INFINITY SQUAD - Climate Change Dashboard

## TEAM NAME -
**AI INFINITY SQUAD**

## Prject title:
**Climate Change Dashboard**

## Description:
Analyze global temperature anomalies and visualize their impact on regions

## Group Members:
- DUDANI JIYA [KU2407U400]
- MAHI SHAH [KU2407U422]
- KRISHNA LATHIYA [KU2407U421]
- SATVIK JOSHI [KU2407U439]

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
-Start the Program:

The main() function is called when the script is executed directly.
-Load Data:

The load_data() function attempts to load the global temperature anomaly data from global_temp_anomalies.csv.
If successful, it prints "Data loaded successfully.", otherwise, it prints an error and stops execution.
Preprocess Data:

The preprocess_data() function cleans the data by dropping missing values and ensuring correct data types for the Year and Temperature_Anomaly columns.
It prints "Data preprocessing complete.".
Analyze Data:

The analyze_data() function calculates basic statistics:
Average temperature anomaly.
Maximum temperature anomaly and the year it occurred.
It prints these results to the console.
Visualize Data:

The visualize_trends() function generates two plots:
A line plot showing temperature anomalies over time.
A histogram with a KDE showing the distribution of anomalies.
Both plots are saved as PNG files in the visuals/ directory and displayed on screen.
End of Execution:

The program finishes once the visualizations are displayed and saved.

## Summary:
The code is a Python script for analyzing and visualizing global temperature anomalies over time. It follows these key steps:

Load Data: Reads temperature anomaly data from a CSV file.
Preprocess Data: Cleans the data by removing missing values and ensuring correct data types.
Analyze Data: Computes the average and maximum temperature anomalies and identifies the year with the highest anomaly.
Visualize Data: Creates and saves two visualizations:
A line plot showing temperature anomalies over time.
A histogram with a Kernel Density Estimate (KDE) for the anomaly distribution.
The script saves the visualizations in the visuals/ folder and prints key analysis results to the console.

## Challenges faced in execution:
Here are some potential challenges that could be faced during execution of the provided code:

File Not Found: If the global_temp_anomalies.csv file is missing or incorrectly specified, the script will fail at the data loading step (FileNotFoundError).

Data Issues:

Missing Values: The dropna() function removes rows with missing values, which could result in loss of important data if many rows are missing.
Incorrect Data Types: If the CSV data contains incorrect formats for the Year or Temperature_Anomaly columns (e.g., text or malformed numbers), the astype() conversion could raise errors.
Plotting Issues:

Empty or Invalid Data: If the data is empty after preprocessing (e.g., due to too many missing values), the plots might not render correctly.
Matplotlib/Seaborn Issues: If the libraries are not installed or if there’s an issue with the environment (e.g., incompatible versions), plotting might fail.
Directory Issues: If the visuals/ directory cannot be created (due to permissions or file system issues), saving plots will fail.

Performance: If the dataset is too large, processing and plotting might become slow or cause memory issues, especially with large amounts of data or complex operations.
## Folder Structure

