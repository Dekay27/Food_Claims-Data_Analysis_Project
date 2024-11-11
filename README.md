# Analyzing Insurance Claims

## Table of Contents

  -  [Project Overview](#project-overview)
  -  [Data Sources](#sata-sources)
  -  [Tools](#tools)
  -  [Cleaning and validating the data](#cleaning-and-validating-the-data)
  -  [Exploratory Data Analysis](#exploratory-data-analysis)
  -  [Data Analysis](#data-analysis)
  -  [Findings](#findings)
  -  [Recommendations](#recommendations)
  -  [References](#references) 

### Project Overview

Vivendo is a fast food chain in Brazil with over 200 outlets. As with many fast food establishments, customers make claims against the company. For example, they blame Vivendo for suspected food poisoning.
The legal team, who processes these claims, is currently split across four locations. The new head of the legal department wants to see if there are differences in the time it takes to close claims across the locations.
The food chain company Vivendo wants a report on how each location differs in the time it takes to close claims. 
We seek to uncover insights to help them improve their processes. 

### Data Sources

The primary dataset used for this analysis is the ['claims.csv'] file. Our data was provided in a CSV format, containing detailed information about each claim.

### Tools

a. Python  -  Data Cleaning, Data Analysis, Data Visualization

### Cleaning and validating the data

Our data was provided in a CSV format, having a total of 2000 entries and 8 columns. To prepare the data we performed the following tasks:
1. Data loading and inspection
2. Handling missing values
3. Data cleaning
4. Data formatting

### Exploratory Data Analysis

EDA explored the food claims data to answer key questions such as:
  -  The category of place with the most observations
  -  The distribution of all the number of reviews
  -  The relationship between the type of store and the number of reviews

### Data Analysis

Some interesting features worked with are: 
```matplotlib.pyplot ```
```pandas ```
```seaborn```
```numpy ```

### Findings

**Average Time to Close:** The average time to close a claim across the four cities (Fortaleza, Natal, Recife, and Sao Luis) is similar, ranging from 184.61 to 187.17 days. Recife has the shortest average time to close at 184.61 days.
**Range and Variability:** The time to close varies in spread:
  **Natal** has the narrowest range, with a standard deviation of 47.06 days, although the average is slightly higher at 185.93 days.
  **Sao Luis** shows the widest spread in time to close values, indicating more variability.
**Median Time to Close:** The median time to close across the cities ranges from 178 to 180 days.
**Minimum and Maximum Times:** Claims close as quickly as 76 to 93 days but can take up to 361 to 518 days.
**Outliers:** Each city has potential outliers, suggesting there may be specific cases with unusually long closing times.

### Recommendations

**Further Investigation of Outliers:** Investigate cases identified as outliers to understand any unique factors affecting longer closing times.
**Targeted Improvements in Sao Luis:** Since Sao Luis has the widest spread in closing times, it may benefit from strategies to reduce variability and streamline claim processing.
**Monitoring and Optimization:** Monitor high and low-performing locations (e.g., Recife and Sao Luis) to identify best practices or areas for improvement, potentially standardizing procedures to narrow the range of time to close across all cities.

### References
1. [DataCamp](https://app.datacamp.com/)
2. [FreeCodeCamp](https://www.freecodecamp.org/learn/data-analysis-with-python)
3. Python for Data Analysis (3rd ed.), W. McKinney, O'Reilly (2022)
