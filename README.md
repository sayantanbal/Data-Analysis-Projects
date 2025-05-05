# Online Retail Data Analysis Project

## Overview
This project analyzes an online retail dataset to uncover customer behavior patterns, product performance, and transaction trends. The data contains transactions from an online retailer spanning approximately one year, including information about products, customers, and sales across multiple countries.

## Dataset
The dataset was sourced from Kaggle ([Online Retail Dataset](https://www.kaggle.com/datasets/vijayuv/onlineretail)) and includes the following fields:
- InvoiceNo: Invoice number for each transaction
- StockCode: Product code
- Description: Product description
- Quantity: Quantity of items purchased
- InvoiceDate: Date and time of purchase
- UnitPrice: Price per unit
- CustomerID: Customer identifier
- Country: Country where the customer resides

## Project Structure
The analysis is organized into the following sections:

### 1. Data Overview and Quality Assessment
- Determined the time period covered (approximately 1 year)
- Analyzed unique transactions, customers, and products
- Identified and addressed data quality issues (missing values, duplicates, outliers)
- Cleaned data by removing negative quantities and zero prices
- Created derived fields like TotalPrice, Date, Time, Hour, DayOfWeek, and Month

### 2. Customer Behavior Analysis
- Examined sales distribution across different countries
  - Created bar charts showing total invoice amounts by country
  - United Kingdom represented the highest sales volume
- Analyzed distribution of order sizes (items per transaction)
  - Used histograms to visualize the distribution
- Calculated typical basket values (total transaction amounts)
  - Identified average purchase values and outlier transactions
- Investigated seasonal patterns in purchasing behavior
  - Created a seasonal analysis by grouping transactions by Winter, Spring, Summer, and Fall
  - Visualized sales trends by season

### 3. Product Analysis
- Identified most frequently purchased products
  - "PAPER CRAFT, LITTLE BIRDIE" and "MEDIUM CERAMIC TOP STORAGE JAR" were among top items
- Analyzed highest revenue-generating products
  - Created bar charts showing total revenue by product
- Examined diversity of product catalog and sales distribution
  - Visualized how sales are spread across the product range
- Attempted to identify natural product groupings/categories

### 4. Transaction Patterns
- Analyzed distribution of transaction times and days
  - Created visualizations showing transaction volume by:
    - Day of week (Monday through Sunday)
    - Hour of day (24-hour format)
    - Month of year
  - Generated a daily transaction volume chart over time
- Compared transaction patterns across countries
  - Calculated average transaction value by country
- Identified shopping peaks during the week/month
  - Analyzed revenue patterns by day of week
  - Found that Thursday and Tuesday generated the highest revenue

## Methodology
1. **Data Preprocessing**:
   - Filtered out rows with zero or negative quantities and prices
   - Converted data types (e.g., InvoiceNo to int)
   - Created calculated fields for analysis
   - Handled outliers using IQR method

2. **Exploratory Data Analysis**:
   - Descriptive statistics
   - Visualization using matplotlib and seaborn
   - Temporal analysis by day, week, and month
   - Geographic analysis by country

3. **Visualization Techniques**:
   - Bar charts for comparing categories
   - Histograms for distributions
   - Time series plots for temporal trends

## Key Findings
- Weekdays showed stronger sales than weekends, with Thursday and Tuesday being the strongest revenue days
- Clear hourly patterns in shopping behavior, with peaks during business hours
- Significant country differences in both transaction volume and average transaction value
- Seasonal variations in purchasing patterns
- A small subset of products generated a disproportionate amount of revenue

## Technologies Used
- Python
- pandas for data manipulation
- matplotlib and seaborn for visualization
- NumPy for numerical operations
- dateutil for date manipulations

## How to Run the Project
1. Clone this repository
2. Install the required dependencies: `requirements.txt`
   ```bash
   pip install -r requirements.txt
   ```
3. Download the dataset from Kaggle using opendatasets or manually place the CSV file in the "onlineretail" folder
4. Run the Jupyter notebook: `jupyter notebook main.ipynb`

## Future Work
- Implement customer segmentation analysis (RFM analysis)
- Perform market basket analysis to find product associations
- Forecast future sales using time series analysis
- Develop product recommendations based on purchasing patterns
- Conduct cohort analysis to track customer retention

## License
This project is open-sourced under the MIT license.