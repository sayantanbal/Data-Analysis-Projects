# Customer Lifetime Value (CLV) Analysis

## Project Overview

This project analyzes customer lifetime value using an online retail dataset to understand customer behavior, purchasing patterns, and identify high-value customer segments. The analysis provides insights for customer retention strategies and business growth optimization.

## Dataset

- **Source**: Online Retail Dataset (Kaggle)
- **Format**: CSV file with transaction-level data
- **Time Period**: December 1, 2010 to December 9, 2011
- **Records**: 541,909 transactions (after cleaning)
- **Customers**: 4,372 unique customers

## Project Structure

```
02 Customer Lifetime Value (CLV) Analysis/
├── main.ipynb          # Main analysis notebook
├── README.md          # Project documentation
└── onlineretail/      # Dataset folder
    └── OnlineRetail.csv
```

## Data Schema

| Column | Description |
|--------|-------------|
| InvoiceNo | Unique identifier for each transaction |
| StockCode | Product code |
| Description | Product description |
| Quantity | Number of items purchased |
| InvoiceDate | Date and time of transaction |
| UnitPrice | Price per unit |
| CustomerID | Unique customer identifier |
| Country | Customer's country |

## Data Preprocessing

### Cleaning Steps Implemented:
- Removed transactions with negative or zero quantities
- Removed transactions with zero or negative unit prices
- Excluded specific problematic invoice (A563185)
- Converted InvoiceNo to integer type
- Handled missing CustomerID values

### Feature Engineering:
- **TotalPrice**: Calculated as UnitPrice × Quantity
- **Date**: Extracted date from InvoiceDate
- **Time**: Extracted time from InvoiceDate
- **Hour**: Extracted hour of transaction
- **DayOfWeek**: Day name of transaction
- **Month**: Month name of transaction
- **Quarter**: Quarter of transaction

## Analysis Completed

### 1. Data Quality & Overview ✅

#### 1.1 Time Period and Customer Count
- **Dataset Coverage**: December 1, 2010 - December 9, 2011 (1 year)
- **Unique Customers**: 4,372 customers
- **Total Transactions**: 541,909 records

#### 1.3 Geographical Distribution
- **Visualization**: Horizontal bar chart showing top countries by transaction volume
- **Key Finding**: UK dominates with majority of transactions
- **Implementation**: Matplotlib visualization

#### 1.4 Outlier Analysis
- **Quantity Outliers**: Interactive boxplots by country and month using Plotly
- **Price Outliers**: Interactive boxplots by country and quarter using Plotly
- **Features**: 
  - Color-coded by time periods (Month/Quarter)
  - Interactive filtering and zooming
  - Hover tooltips with detailed information
  - Grouped boxplot display

### 2. Purchase Behavior Analysis ✅

#### 2.1 Average Order Value Analysis
- **Average Order Value**: £18.44
- **Median Order Value**: £9.91
- **Total Orders**: 25,900 unique invoices

**Visualizations Implemented**:
- Static histogram with KDE using Seaborn
- Interactive histogram with marginal boxplot using Plotly
- Mean and median lines with annotations
- 99th percentile axis limiting for better outlier handling

#### 2.2 Customer Purchase Frequency Analysis
- **Average Purchases per Customer**: 2.92
- **Median Purchases per Customer**: 1.00
- **One-time Customers**: 3,030 (69.3%)
- **Repeat Customers**: 1,342 (30.7%)

**Visualizations Implemented**:
- Purchase frequency distribution histogram (Plotly)
- Bar chart showing percentage of customers by purchase count
- Pie chart comparing one-time vs. repeat customers
- Statistical summary with mean/median indicators

## Technical Implementation

### Libraries Used
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from dateutil.relativedelta import relativedelta
```

### Key Functions and Methods
- Data cleaning and preprocessing
- Groupby operations for aggregating customer-level metrics
- Interactive visualizations with Plotly
- Statistical analysis and summary reporting

## Visualizations Gallery

### Completed Visualizations:
1. **Geographic Distribution**: Horizontal bar chart of transactions by country
2. **Outlier Analysis**: Interactive boxplots for quantity and price by country/time
3. **Order Value Distribution**: Histogram with statistical indicators
4. **Purchase Frequency**: Multiple charts showing customer repeat behavior

### Visualization Features:
- Interactive Plotly charts with hover tooltips
- Color-coded categorical data
- Statistical annotations (mean, median)
- Responsive design with zoom and pan capabilities
- Marginal plots for additional insights

## Key Insights Discovered

### Customer Behavior:
- **High One-time Rate**: 69.3% of customers make only one purchase
- **Skewed Order Values**: Large gap between mean (£18.44) and median (£9.91) suggests high-value outliers
- **Geographic Concentration**: UK market dominance in transaction volume

### Data Quality:
- **Outliers Present**: Significant outliers in both quantity and price data
- **Seasonal Patterns**: Visible variations across months and quarters
- **Clean Dataset**: After preprocessing, data is suitable for CLV analysis

## Next Steps (Remaining Analysis)

### 2. Purchase Behavior (Remaining)
- [ ] 2.3: Time gap analysis between consecutive purchases
- [ ] 2.4: Correlation between purchase frequency and average order value

### 3. Customer Segmentation
- [ ] 3.1: One-time vs. repeat customer detailed analysis
- [ ] 3.2: RFM (Recency, Frequency, Monetary) analysis
- [ ] 3.3: RFM segment proportions
- [ ] 3.4: Revenue contribution by segment

### 4. CLV Analysis
- [ ] 4.1: CLV distribution across customer base
- [ ] 4.2: Average and median CLV calculation
- [ ] 4.3: Pareto analysis (80/20 rule)
- [ ] 4.4: CLV variation by geography

### 5-10. Advanced Analysis
- [ ] Temporal patterns and seasonality
- [ ] Product analysis in relation to CLV
- [ ] Customer lifecycle patterns
- [ ] Business impact modeling
- [ ] Relationship analysis
- [ ] Advanced visualizations (heatmaps, cohort analysis, etc.)

## Business Value

### Current Findings:
- High customer acquisition opportunity (reduce 69% one-time rate)
- Geographic expansion potential beyond UK market
- Order value optimization needed (address mean-median gap)

### Potential Applications:
- Customer retention strategy development
- Marketing budget allocation
- Product portfolio optimization
- Geographic market expansion planning

## Technical Notes

### Performance Considerations:
- Large dataset (540K+ records) handled efficiently with pandas
- Interactive visualizations optimized with data filtering
- Memory management through data type optimization

### Reproducibility:
- All analysis steps documented in Jupyter notebook
- Clear data preprocessing pipeline
- Standardized visualization functions

---

**Project Status**: 25% Complete (2 out of 10 major sections)
**Last Updated**: May 26, 2025
**Next Milestone**: Complete Purchase Behavior Analysis (Section 2)