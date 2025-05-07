# Online Retail Data Analysis Project

## Overview
This project analyzes an online retail dataset to uncover customer behavior patterns, product performance, and transaction trends. The data contains transactions from an online retailer spanning approximately one year and includes information about products, customers, and sales across multiple countries.

## Dataset
The dataset was sourced from Kaggle ([Online Retail Dataset](https://www.kaggle.com/datasets/vijayuv/onlineretail)) and includes the following fields:
- **InvoiceNo:** Invoice number for each transaction
- **StockCode:** Product code
- **Description:** Product description
- **Quantity:** Quantity of items purchased
- **InvoiceDate:** Date and time of purchase
- **UnitPrice:** Price per unit
- **CustomerID:** Customer identifier
- **Country:** Country where the customer resides

## Project Structure
The analysis is organized into the following sections:

### 1. Data Overview and Quality Assessment
- Determined the time period covered (approximately 1 year)
- Analyzed unique transactions, customers, and products
- Identified and addressed data quality issues (missing values, duplicates, outliers)
- Cleaned data by removing negative quantities and zero prices
- Created derived fields such as TotalPrice, Date, Time, Hour, DayOfWeek, and Month

### 2. Customer Behavior Analysis
- Examined sales distribution across different countries with bar charts showing total invoice amounts
- Analyzed the distribution of order sizes (items per transaction) using histograms
- Calculated typical basket values (total transaction amounts) to identify average purchase values and outliers
- Investigated seasonal patterns by grouping transactions by Winter, Spring, Summer, and Fall

### 3. Product Analysis
- Identified the most frequently purchased products based on quantity sold
- Analyzed highest revenue-generating products with visualizations of total revenue by product
- Explored the diversity of the product catalog and sales distribution across products
- Made initial observations regarding potential natural groupings among products

### 4. Transaction Patterns
- Analyzed distribution of transaction times and days:
  - Visualized transaction volume by day of week, hour of day, and month
  - Created a daily transaction volume time series chart
- Compared transaction patterns across countries by calculating average transaction values
- Examined revenue patterns by day of week and identified peak shopping periods
- **Heatmap Analysis:** A detailed heatmap visualization of hourly patterns by day of week was generated. The heatmap provides insights into peak sales hours, enabling targeted promotions and improved resource allocation.

### 5. Association Analysis
- Implemented market basket analysis to identify product combinations frequently purchased together
- Calculated association rule metrics for product pairs:
  - **Support:** Percentage of transactions containing both products
  - **Confidence:** Probability of buying product B when buying product A
  - **Lift:** How much more likely products appear together than by random chance
- Visualized the strongest product associations using horizontal bar charts
- Identified high-lift product pairs for potential cross-selling opportunities
- Ranked associations by different metrics to provide multiple business perspectives

## Methodology
1. **Data Preprocessing**
   - Filtered out rows with zero or negative quantities and prices
   - Converted data types (e.g., InvoiceNo to int)
   - Created calculated fields for effective analysis
   - Handled outliers using the IQR method

2. **Exploratory Data Analysis**
   - Generated descriptive statistics
   - Built visualizations with matplotlib and seaborn
   - Conducted temporal and geographic analyses

3. **Visualization Techniques**
   - Used bar charts, histograms, and time series plots
   - Implemented a heatmap for detailed hourly transaction pattern analysis
   - Employed seasonal grouping and box plots to highlight trends and anomalies

4. **Association Rule Mining**
   - Grouped products by transaction
   - Generated product pairs using combinations
   - Calculated standard association metrics (support, confidence, lift)
   - Prioritized associations by different business-relevant metrics

## Key Findings
- **Temporal Trends:** Weekdays generally demonstrate stronger sales, with Thursday and Tuesday recording the highest revenue.
- **Hourly Patterns:** Clear peaks during business hours were observed in the heatmap, offering opportunities for targeted promotional efforts during off-peak periods.
- **Geographical Variation:** There are significant differences in transaction volume and average transaction value across countries.
- **Product Impact:** A small selection of products contributes disproportionately to total revenue.
- **Product Associations:** Strong associations were discovered between complementary products, providing clear opportunities for cross-selling and store layout optimization.
- **Data Quality:** Some challenges with missing data and outliers were identified, and various cleaning methods were successfully applied.

## Technologies Used
- Python
- pandas for data manipulation
- matplotlib and seaborn for data visualization
- NumPy for numerical operations
- dateutil for date management
- collections.Counter for efficient frequency counting
- itertools.combinations for association analysis

## How to Run the Project
1. **Clone the Repository**
   ```bash
   git clone https://your.repository.url.git
   ```
2. **Navigate to the Project Folder**
   ```bash
   cd "01 Market Basket Analysis"
   ```
3. **Install Required Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Analysis**
   - Launch the Jupyter Notebook:
     ```bash
     jupyter notebook main.ipynb
     ```
   - Follow the notebook cells to execute the analysis and visualize results.

## Future Work
- Implement a detailed market basket analysis to uncover strong product associations.
- Extend customer segmentation using RFM (Recency, Frequency, Monetary) analysis.
- Forecast future sales with advanced time series analysis.
- Develop product recommendations based on purchasing behavior.
- Perform cohort analysis to monitor customer retention trends.

## License
This project is open-sourced under the MIT license.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request when adding new features or improvements.

---

Happy analyzing!