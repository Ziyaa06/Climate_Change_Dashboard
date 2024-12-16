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
Start the Program:

The main() function is called when the script is executed directly.
Load Data:

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
## Folder Structure
