# Online Retail Data Analysis Project

## Overview
This project analyzes an online retail dataset to uncover customer behavior patterns, product performance, transaction trends, and product associations. The primary goal is to derive actionable insights that can inform business strategies, such as marketing campaigns, store layout optimization, and product recommendations. The data contains transactions from an online retailer spanning approximately one year and includes information about products, customers, and sales across multiple countries.

## Dataset
The dataset was sourced from Kaggle ([Online Retail Dataset](https://www.kaggle.com/datasets/vijayuv/onlineretail)) and includes the following fields:
- **InvoiceNo:** Invoice number for each transaction (categorical). A unique number assigned to each transaction.
- **StockCode:** Product (item) code (nominal). A unique number assigned to each distinct product.
- **Description:** Product (item) name (nominal).
- **Quantity:** The quantities of each product (item) per transaction (numeric).
- **InvoiceDate:** Invice Date and time (numeric). The day and time when each transaction was generated.
- **UnitPrice:** Unit price (numeric). Product price per unit in sterling (£).
- **CustomerID:** Customer number (nominal). A unique number assigned to each customer.
- **Country:** Country name (nominal). The name of the country where each customer resides.

## Project Structure and Analysis Steps

The analysis is performed in a Jupyter Notebook (`main.ipynb`) and is structured as follows:

### 1. Data Loading and Initial Setup
- Importing necessary Python libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`, `networkx`, `collections`, `itertools`, `dateutil`, and `opendatasets`.
- Loading the dataset from the CSV file.

### 2. Data Pre-processing and Cleaning
- Filtering out transactions with non-positive `UnitPrice` or `Quantity`.
- Resetting the DataFrame index.
- Correcting `InvoiceNo` data types and removing specific anomalous `InvoiceNo` entries.
- Calculating `TotalPrice` (`UnitPrice` * `Quantity`).
- Parsing `InvoiceDate` to create separate `Date`, `Time`, `Hour`, `DayOfWeek`, and `Month` columns for temporal analysis.
- Identifying and assessing missing values, duplicates, and potential outliers.

### 3. Exploratory Data Analysis (EDA)

#### 3.1. Data Overview and Quality Assessment
- Determining the time period covered by the dataset.
- Calculating the number of unique transactions, customers, and products.
- Identifying unique countries present in the dataset.
- Quantifying duplicates and outliers in `UnitPrice`.
- Checking for unusual patterns like negative quantities or zero prices (after initial filtering).
- Visualizing sales distribution by country using a choropleth map and a treemap.

#### 3.2. Customer Behavior Analysis
- Analyzing sales distribution across different countries.
- Visualizing the distribution of order sizes (number of items per transaction) using histograms and violin plots.
- Examining the distribution of basket values (total transaction amount).
- Investigating seasonal purchasing patterns (Winter, Spring, Summer, Fall) using bar charts, sunburst charts, and radar charts.

#### 3.3. Product Analysis
- Identifying the most frequently purchased products by quantity.
- Visualizing top products by quantity sold (bar chart) and by revenue (treemap).
- Identifying the highest revenue-generating products.
- Analyzing the diversity of the product catalog and sales distribution.
- Visualizing the distribution of transaction values using histograms with percentile markers.

#### 3.4. Transaction Patterns
- Analyzing the distribution of transactions by `DayOfWeek`, `Hour` of the day, and `Month`.
- Visualizing daily transaction volume over time.
- Creating heatmaps and bubble charts to show hourly sales/transaction patterns by day of the week.
- Comparing average transaction values by country.
- Examining revenue patterns and average order value by day of the week.
- Visualizing seasonal sales breakdowns using sunburst and radar charts.

### 4. Association Analysis (Market Basket Analysis)
- Grouping products by `InvoiceNo` to create transaction lists.
- Generating pairs of products purchased together in each transaction.
- Calculating association rule metrics:
    - **Support:** The proportion of transactions that contain a particular itemset.
    - **Confidence:** The conditional probability of purchasing item B given that item A is purchased.
    - **Lift:** The ratio of observed support to that expected if the two items were independent.
- Creating a `metrics_df` DataFrame to store these association metrics for product pairs.
- Visualizing product associations using a network graph (nodes representing products, edges representing associations, with edge weight/color indicating lift/confidence).
- Identifying frequently co-occurring product pairs and visualizing their frequencies.

### 5. Business Recommendations
- **Cross-Selling Opportunities:** Identifying product pairs with high confidence and support for cross-selling. Visualizing these opportunities using scatter plots and 3D plots.
- **Product Recommendation Improvements:** Analyzing recommendation quality based on confidence tiers and suggesting personalized recommendations by country.
- **Pricing or Bundling Strategies:** Identifying bundle candidates based on high lift, support, and confidence. Calculating potential bundle prices with discounts and visualizing these strategies.
- **Targeted Marketing Campaigns:**
    - Identifying seasonal top products for targeted campaigns.
    - Analyzing product preferences of high-value customers.
    - Visualizing seasonal product trends and high-value customer preferences.

## Key Findings
- **Temporal Trends:** Significant variations in sales and transaction volumes were observed across different times of the day, days of the week, and months, highlighting peak shopping periods.
- **Geographical Variation:** Sales and average transaction values differ notably across countries, with the UK being the dominant market.
- **Product Performance:** A small subset of products accounts for a large portion of sales and revenue.
- **Customer Spending:** Order sizes and transaction values vary, with identifiable patterns in typical spending.
- **Product Associations:** Strong associations (high lift and confidence) exist between certain products, offering clear opportunities for cross-selling, bundling, and marketing. For example, "ROSES REGENCY TEACUP AND SAUCER" and "GREEN REGENCY TEACUP AND SAUCER" are frequently bought together.
- **Seasonal Impact:** Purchasing behavior shows seasonal variations, which can be leveraged for targeted promotions.
- **Data Quality:** The dataset required cleaning due to missing values, zero/negative prices/quantities, and outliers, which were addressed to ensure reliable analysis.

## Technologies Used
- Python 3.12.7
- pandas: For data manipulation and analysis.
- NumPy: For numerical operations.
- Matplotlib: For static, animated, and interactive visualizations.
- Seaborn: For statistical data visualization.
- Plotly (Express and Graph Objects): For interactive visualizations, including choropleth maps, treemaps, sunburst charts, network graphs, and 3D plots.
- NetworkX: For creating and analyzing complex networks (used for product association graphs).
- collections.Counter: For efficient frequency counting.
- itertools.combinations: For generating product pairs in association analysis.
- dateutil.relativedelta: For date calculations.
- opendatasets: For downloading datasets from Kaggle (used initially).
- Jupyter Notebook: As the environment for analysis and presentation.

## How to Run the Project

### Prerequisites
- Python 3.12 or higher.
- `uv` (Python package installer and virtual environment manager). If you don't have `uv`, you can install it by following the instructions at [astral.sh/uv](https://astral.sh/uv).
- Git for cloning the repository.

### Steps

1.  **Clone the Repository**
    ```bash
    git clone https://your.repository.url.git # Replace with the actual repository URL
    cd "01 Market Basket Analysis"
    ```

2.  **Set up the Environment and Install Dependencies using `uv`**
    ```bash
    # Create a virtual environment
    uv venv

    # Activate the virtual environment
    # On Linux/macOS:
    source .venv/bin/activate
    # On Windows (PowerShell):
    # .\.venv\Scripts\Activate.ps1
    # On Windows (CMD):
    # .venv\Scripts\activate.bat

    # Install the required packages from requirements.txt
    uv pip install -r requirements.txt
    ```

3.  **Launch the Jupyter Notebook**
    ```bash
    jupyter notebook main.ipynb
    ```
    Alternatively, if you prefer JupyterLab:
    ```bash
    jupyter lab main.ipynb
    ```

4.  **Run the Analysis**
    - Open the `main.ipynb` notebook in your Jupyter environment.
    - You can run cells individually or use the "Run All" option from the Kernel or Cell menu.
    - **Note on Cell Execution:** Some visualization cells, particularly those involving complex calculations like the product association network graph (cell 55/56 in the notebook), are designed to be self-contained by re-calculating necessary DataFrames. If you encounter errors due to undefined variables when running cells out of order, try running cells sequentially from the beginning or use the "Restart Kernel and Run All Cells" option.

## Future Work
- **Advanced Customer Segmentation:** Implement RFM (Recency, Frequency, Monetary) analysis for more granular customer segmentation.
- **Predictive Modeling:** Develop models to forecast future sales or predict customer churn.
- **Recommendation System:** Build a more sophisticated product recommendation engine based on collaborative filtering or content-based approaches.
- **Interactive Dashboard:** Create an interactive dashboard (e.g., using Dash or Streamlit) to present the findings and allow for dynamic exploration of the data.
- **A/B Testing Analysis:** If applicable, analyze results from A/B tests for different marketing strategies or website layouts.

## License
This project is open-sourced under the MIT License. (If applicable, otherwise state the correct license).

## Contributing
Contributions are welcome! Please open an issue to discuss potential changes or submit a pull request with your improvements.

---

Happy analyzing!