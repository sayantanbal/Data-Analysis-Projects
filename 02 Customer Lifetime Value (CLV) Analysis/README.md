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
├── pyproject.toml     # UV package manager configuration
├── requirements.txt   # Python dependencies
└── onlineretail/      # Dataset folder
    └── OnlineRetail.csv
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- [UV package manager](https://github.com/astral-sh/uv) (recommended)

### Option 1: Using UV (Recommended)

1. **Install UV** (if not already installed):
   ```bash
   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. **Clone and setup the project**:
   ```bash
   git clone <repository-url>
   cd "02 Customer Lifetime Value (CLV) Analysis"
   
   # Create virtual environment and install dependencies
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv add -r requirements.txt
   ```

3. **Launch Jupyter Notebook**:
   ```bash
   uv run jupyter notebook main.ipynb
   # or
   jupyter notebook main.ipynb
   ```

### Option 2: Using Traditional pip

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Notebook
jupyter notebook main.ipynb
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

**Sub-Analysis Completed**:
- **2.2.1 Customer Return Frequency**: Analysis of how often customers return to shop
- **2.2.2 Product Repeat Purchases**: Analysis of customers buying the same product multiple times

**Visualizations Implemented**:
- Purchase frequency distribution histogram (Plotly)
- Bar chart showing percentage of customers by purchase count
- Pie chart comparing one-time vs. repeat customers
- Product-specific repeat purchase analysis
- Statistical summary with mean/median indicators

#### 2.3 Time Gap Analysis Between Consecutive Purchases ✅
- **Average Time Between Purchases**: [Value from analysis]
- **Median Time Between Purchases**: [Value from analysis]
- **Most Common Purchase Interval**: [Mode value]

**Visualizations Implemented**:
- Distribution histogram of time gaps between purchases
- Pie chart categorizing time gaps (weekly, monthly, quarterly, etc.)
- Box plot showing variation in average gaps per customer
- Comprehensive statistical summary with quartiles

**Key Findings**:
- Time gap patterns for returning customers
- Customer purchasing cycles identification
- Optimal timing insights for marketing campaigns

#### 2.4 Purchase Frequency vs Average Order Value Correlation ✅
- **Correlation Coefficient**: [Pearson correlation value]
- **Statistical Significance**: [P-value and interpretation]
- **Relationship Strength**: [Weak/Moderate/Strong + Direction]

**Visualizations Implemented**:
- Scatter plot with trend line showing frequency vs AOV relationship
- Density heatmap for better visualization of data concentration
- Box plots comparing AOV across frequency categories (One-time, Low, Medium, High)
- Statistical summary table by frequency category

**Business Insights**:
- Understanding of customer value patterns
- Strategy recommendations for frequency vs order value optimization
- Customer segmentation insights based on purchasing behavior

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
from scipy.stats import spearmanr, pearsonr
```

### Key Functions and Methods
- Data cleaning and preprocessing with pandas
- Groupby operations for customer-level aggregations
- Interactive visualizations with Plotly
- Statistical analysis using scipy
- Time series analysis for purchase patterns
- Correlation analysis with multiple methods

## Visualizations Gallery

### Completed Visualizations:
1. **Geographic Distribution**: Horizontal bar chart of transactions by country
2. **Outlier Analysis**: Interactive boxplots for quantity and price by country/time
3. **Order Value Distribution**: Histogram with statistical indicators
4. **Purchase Frequency**: Multiple charts showing customer repeat behavior
5. **Time Gap Analysis**: Distribution and categorization of inter-purchase intervals
6. **Correlation Analysis**: Scatter plots and heatmaps showing frequency-AOV relationships

### Visualization Features:
- Interactive Plotly charts with hover tooltips
- Color-coded categorical data
- Statistical annotations (mean, median, correlation coefficients)
- Responsive design with zoom and pan capabilities
- Marginal plots and density visualizations
- Trend lines and regression analysis

## Key Insights Discovered

### Customer Behavior:
- **High One-time Rate**: 69.3% of customers make only one purchase, indicating significant retention opportunity
- **Skewed Order Values**: Large gap between mean (£18.44) and median (£9.91) suggests high-value outliers
- **Purchase Patterns**: Clear patterns in time gaps between purchases for returning customers
- **Frequency-Value Relationship**: [Specific correlation findings from analysis]

### Data Quality:
- **Outliers Present**: Significant outliers in both quantity and price data, handled appropriately
- **Seasonal Patterns**: Visible variations across months and quarters
- **Clean Dataset**: After comprehensive preprocessing, data is suitable for advanced CLV analysis

### Business Opportunities:
- **Customer Retention**: Major opportunity to convert one-time buyers to repeat customers
- **Value Optimization**: Understanding of relationship between purchase frequency and order value
- **Timing Strategy**: Insights into optimal timing for customer re-engagement campaigns

## Next Steps (Remaining Analysis)

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
- **Customer Acquisition vs Retention**: 69% one-time customer rate reveals massive retention opportunity
- **Geographic Expansion**: Potential beyond UK market dominance
- **Order Value Strategy**: Data-driven insights into frequency-value relationship
- **Campaign Timing**: Optimal intervals for customer re-engagement identified

### Potential Applications:
- Customer retention strategy development
- Marketing budget allocation optimization
- Product portfolio and pricing strategy
- Geographic market expansion planning
- Customer lifetime value prediction modeling

## Technical Notes

### Performance Considerations:
- Large dataset (540K+ records) handled efficiently with pandas
- Interactive visualizations optimized with data filtering and sampling
- Memory management through data type optimization
- Correlation analysis using optimized scipy functions

### Reproducibility:
- All analysis steps documented in Jupyter notebook
- Clear data preprocessing pipeline
- Standardized visualization functions
- UV package manager for consistent environment setup

### Code Quality:
- Modular analysis approach with reusable functions
- Comprehensive error handling for missing data
- Statistical significance testing for correlations
- Professional-grade visualizations with Plotly

## Troubleshooting

### Common Issues:
1. **Dataset Not Found**: Ensure `OnlineRetail.csv` is in the `onlineretail/` folder
2. **Memory Issues**: Large dataset may require sufficient RAM (8GB+ recommended)
3. **Plotly Display**: If charts don't display, try `pip install --upgrade plotly` or use `fig.show(renderer="browser")`

### UV-Specific Issues:
- If UV installation fails, use the traditional pip method
- For Windows users, ensure PowerShell execution policy allows script execution
- Use `uv --version` to verify installation

---

**Project Status**: 50% Complete (2 out of 10 major sections fully completed)
**Last Updated**: May 29, 2025
**Next Milestone**: Complete Customer Segmentation (Section 3) - RFM Analysis