# Create a comprehensive modified_data DataFrame with all transformations

# Start with the base cleaned data
modified_data = data.copy()

# Add RFM analysis data
print("Adding RFM metrics to modified_data...")

# Calculate RFM metrics for each customer
analysis_date = data['Date'].max() + pd.Timedelta(days=1)

rfm_customer_data = data.groupby('CustomerID').agg({
    'Date': lambda x: (analysis_date - x.max()).days,  # Recency
    'InvoiceNo': 'nunique',  # Frequency
    'TotalPrice': 'sum'  # Monetary
}).reset_index()

rfm_customer_data.columns = ['CustomerID', 'Customer_Recency', 'Customer_Frequency', 'Customer_Monetary']

# Create RFM quintiles (1-5 scoring)
rfm_customer_data['Customer_R_Score'] = pd.qcut(rfm_customer_data['Customer_Recency'].rank(method='first'), 5, labels=[5,4,3,2,1])
rfm_customer_data['Customer_F_Score'] = pd.qcut(rfm_customer_data['Customer_Frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
rfm_customer_data['Customer_M_Score'] = pd.qcut(rfm_customer_data['Customer_Monetary'].rank(method='first'), 5, labels=[1,2,3,4,5])

# Combine RFM scores
rfm_customer_data['Customer_RFM_Score'] = (rfm_customer_data['Customer_R_Score'].astype(str) + 
                                          rfm_customer_data['Customer_F_Score'].astype(str) + 
                                          rfm_customer_data['Customer_M_Score'].astype(str))

# Define customer segments
def segment_customers(rfm_score):
    if rfm_score in ['555', '554', '544', '545', '454', '455', '445']:
        return 'Champions'
    elif rfm_score in ['543', '444', '435', '355', '354', '345', '344', '335']:
        return 'Loyal Customers'
    elif rfm_score in ['553', '551', '552', '541', '542', '533', '532', '531', '452', '451']:
        return 'Potential Loyalists'
    elif rfm_score in ['512', '511', '422', '421', '412', '411', '311']:
        return 'New Customers'
    elif rfm_score in ['155', '154', '144', '214', '215', '115', '114']:
        return 'At Risk'
    elif rfm_score in ['155', '254', '245']:
        return "Can't Lose Them"
    elif rfm_score in ['331', '321', '231', '241', '251']:
        return 'Hibernating'
    else:
        return 'Others'

rfm_customer_data['Customer_Segment'] = rfm_customer_data['Customer_RFM_Score'].apply(segment_customers)

# Merge RFM data with original data
modified_data = modified_data.merge(rfm_customer_data, on='CustomerID', how='left')

# Add purchase frequency analysis
print("Adding purchase frequency analysis...")

purchase_freq_data = data.groupby('CustomerID')['InvoiceNo'].nunique().reset_index()
purchase_freq_data.columns = ['CustomerID', 'Total_Purchase_Count']

# Categorize customer types
purchase_freq_data['Customer_Type'] = purchase_freq_data['Total_Purchase_Count'].apply(
    lambda x: 'One-time' if x == 1 else 'Repeat'
)

# Categorize purchase frequency
def categorize_frequency(freq):
    if freq == 1:
        return 'One-time (1)'
    elif freq <= 3:
        return 'Low (2-3)'
    elif freq <= 10:
        return 'Medium (4-10)'
    else:
        return 'High (11+)'

purchase_freq_data['Purchase_Frequency_Category'] = purchase_freq_data['Total_Purchase_Count'].apply(categorize_frequency)

# Merge purchase frequency data
modified_data = modified_data.merge(purchase_freq_data, on='CustomerID', how='left')

# Add order-level analysis
print("Adding order-level metrics...")

# Calculate order value for each invoice
order_values = data.groupby('InvoiceNo')['TotalPrice'].sum().reset_index()
order_values.columns = ['InvoiceNo', 'Order_Value']

# Merge order values
modified_data = modified_data.merge(order_values, on='InvoiceNo', how='left')

# Add customer-level order statistics
customer_order_stats = data.groupby(['CustomerID', 'InvoiceNo'])['TotalPrice'].sum().reset_index()
customer_avg_order = customer_order_stats.groupby('CustomerID')['TotalPrice'].agg([
    'mean', 'median', 'std', 'min', 'max'
]).reset_index()

customer_avg_order.columns = ['CustomerID', 'Avg_Order_Value', 'Median_Order_Value', 
                             'Std_Order_Value', 'Min_Order_Value', 'Max_Order_Value']

# Fill NaN in std with 0 (for customers with only one order)
customer_avg_order['Std_Order_Value'] = customer_avg_order['Std_Order_Value'].fillna(0)

# Merge customer order statistics
modified_data = modified_data.merge(customer_avg_order, on='CustomerID', how='left')

# Add product diversity analysis
print("Adding product diversity metrics...")

product_diversity = data.groupby('CustomerID')['StockCode'].nunique().reset_index()
product_diversity.columns = ['CustomerID', 'Unique_Products_Purchased']

# Categorize product diversity
def categorize_product_diversity(count):
    if count == 1:
        return 'Single Product'
    elif count <= 5:
        return 'Low Diversity (2-5)'
    elif count <= 20:
        return 'Medium Diversity (6-20)'
    else:
        return 'High Diversity (21+)'

product_diversity['Product_Diversity_Category'] = product_diversity['Unique_Products_Purchased'].apply(categorize_product_diversity)

# Merge product diversity
modified_data = modified_data.merge(product_diversity, on='CustomerID', how='left')

# Add time-based features
print("Adding temporal analysis features...")

# Customer's first and last purchase dates
customer_date_range = data.groupby('CustomerID')['Date'].agg(['min', 'max']).reset_index()
customer_date_range.columns = ['CustomerID', 'First_Purchase_Date', 'Last_Purchase_Date']

# Calculate customer lifespan
customer_date_range['Customer_Lifespan_Days'] = (customer_date_range['Last_Purchase_Date'] - 
                                               customer_date_range['First_Purchase_Date']).dt.days

# Merge date range data
modified_data = modified_data.merge(customer_date_range, on='CustomerID', how='left')

# Add seasonal features
modified_data['Is_Weekend'] = modified_data['DayOfWeek'].isin(['Saturday', 'Sunday'])
modified_data['Season'] = modified_data['Month'].map({
    'December': 'Winter', 'January': 'Winter', 'February': 'Winter',
    'March': 'Spring', 'April': 'Spring', 'May': 'Spring',
    'June': 'Summer', 'July': 'Summer', 'August': 'Summer',
    'September': 'Fall', 'October': 'Fall', 'November': 'Fall'
})

# Add time of day categories
def categorize_hour(hour):
    if 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

modified_data['Time_of_Day'] = modified_data['Hour'].apply(categorize_hour)

# Add country-level features
print("Adding geographical analysis...")

# Calculate country statistics
country_stats = data.groupby('Country').agg({
    'CustomerID': 'nunique',
    'TotalPrice': ['sum', 'mean'],
    'InvoiceNo': 'nunique'
}).reset_index()

country_stats.columns = ['Country', 'Country_Total_Customers', 'Country_Total_Revenue', 
                        'Country_Avg_Transaction_Value', 'Country_Total_Orders']

# Categorize countries by size
def categorize_country_size(customer_count):
    if customer_count >= 1000:
        return 'Large Market'
    elif customer_count >= 100:
        return 'Medium Market'
    elif customer_count >= 10:
        return 'Small Market'
    else:
        return 'Micro Market'

country_stats['Country_Market_Size'] = country_stats['Country_Total_Customers'].apply(categorize_country_size)

# Merge country statistics
modified_data = modified_data.merge(country_stats, on='Country', how='left')

# Add transaction-level features
print("Adding transaction-level features...")

# Calculate transaction metrics
modified_data['Items_Per_Transaction'] = modified_data.groupby('InvoiceNo')['Quantity'].transform('sum')
modified_data['Unique_Items_Per_Transaction'] = modified_data.groupby('InvoiceNo')['StockCode'].transform('nunique')

# Add price categories
modified_data['Price_Category'] = pd.cut(modified_data['UnitPrice'], 
                                       bins=[0, 2, 10, 50, float('inf')], 
                                       labels=['Low (£0-2)', 'Medium (£2-10)', 'High (£10-50)', 'Premium (£50+)'])

# Add quantity categories
modified_data['Quantity_Category'] = pd.cut(modified_data['Quantity'], 
                                          bins=[0, 1, 5, 20, float('inf')], 
                                          labels=['Single', 'Small (2-5)', 'Medium (6-20)', 'Bulk (21+)'])

# Add customer value categories based on total spending
customer_value_quantiles = modified_data['Customer_Monetary'].quantile([0.25, 0.5, 0.75])

def categorize_customer_value(monetary):
    if monetary <= customer_value_quantiles[0.25]:
        return 'Low Value'
    elif monetary <= customer_value_quantiles[0.5]:
        return 'Medium-Low Value'
    elif monetary <= customer_value_quantiles[0.75]:
        return 'Medium-High Value'
    else:
        return 'High Value'

modified_data['Customer_Value_Category'] = modified_data['Customer_Monetary'].apply(categorize_customer_value)

# Add days since last purchase (from analysis date)
modified_data['Days_Since_Last_Purchase'] = modified_data['Customer_Recency']

# Add purchase patterns
print("Adding purchase pattern analysis...")

# Calculate average days between purchases for repeat customers
customer_purchase_dates = data.groupby('CustomerID')['Date'].apply(lambda x: sorted(x.unique())).reset_index()
returning_customers = customer_purchase_dates[customer_purchase_dates['Date'].apply(len) > 1].copy()

def calculate_avg_gap(dates):
    if len(dates) <= 1:
        return None
    gaps = [(dates[i] - dates[i-1]).days for i in range(1, len(dates))]
    return np.mean(gaps)

returning_customers['Avg_Days_Between_Purchases'] = returning_customers['Date'].apply(calculate_avg_gap)
avg_gap_data = returning_customers[['CustomerID', 'Avg_Days_Between_Purchases']]

# Merge average gap data
modified_data = modified_data.merge(avg_gap_data, on='CustomerID', how='left')

# Add repeat product purchases
print("Adding repeat product analysis...")

product_repeat_purchases = data.groupby(['CustomerID', 'StockCode']).size().reset_index(name='Product_Purchase_Count')
customers_with_repeats = product_repeat_purchases[product_repeat_purchases['Product_Purchase_Count'] > 1]['CustomerID'].unique()

modified_data['Has_Repeat_Product_Purchases'] = modified_data['CustomerID'].isin(customers_with_repeats)

# Calculate number of repeat products per customer
repeat_products_count = product_repeat_purchases[product_repeat_purchases['Product_Purchase_Count'] > 1].groupby('CustomerID').size().reset_index(name='Num_Repeat_Products')
modified_data = modified_data.merge(repeat_products_count, on='CustomerID', how='left')
modified_data['Num_Repeat_Products'] = modified_data['Num_Repeat_Products'].fillna(0)

# Add final summary flags
print("Adding summary flags and categories...")

# Flag high-value customers (top 20% by monetary value)
high_value_threshold = modified_data['Customer_Monetary'].quantile(0.8)
modified_data['Is_High_Value_Customer'] = modified_data['Customer_Monetary'] >= high_value_threshold

# Flag at-risk customers (haven't purchased in 90+ days)
modified_data['Is_At_Risk_Customer'] = modified_data['Customer_Recency'] >= 90

# Flag new customers (first purchase within 30 days of analysis date)
modified_data['Is_New_Customer'] = modified_data['Customer_Recency'] <= 30

# Add CLV proxy (using total monetary value as simple CLV)
modified_data['CLV_Proxy'] = modified_data['Customer_Monetary']

# Add transaction recency (days since this specific transaction)
modified_data['Transaction_Recency'] = (analysis_date - modified_data['Date']).dt.days

# Final data summary
print("\n=== MODIFIED DATA SUMMARY ===")
print(f"Total rows: {len(modified_data):,}")
print(f"Total columns: {len(modified_data.columns)}")
print(f"Unique customers: {modified_data['CustomerID'].nunique():,}")
print(f"Date range: {modified_data['Date'].min().date()} to {modified_data['Date'].max().date()}")

# Display new columns added
original_columns = ['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 
                   'UnitPrice', 'CustomerID', 'Country', 'TotalPrice', 'Date', 'Time', 
                   'Hour', 'DayOfWeek', 'Month', 'Quarter']

new_columns = [col for col in modified_data.columns if col not in original_columns]
print(f"\nNew columns added ({len(new_columns)}):")
for i, col in enumerate(new_columns, 1):
    print(f"{i:2d}. {col}")

# Display sample of the modified data
print(f"\nSample of modified_data:")
print(modified_data[['CustomerID', 'Customer_Segment', 'Customer_Type', 'Customer_Value_Category', 
                    'Product_Diversity_Category', 'Customer_Monetary', 'Customer_Frequency']].head())

# Display data types
print(f"\nData types summary:")
print(modified_data.dtypes.value_counts())

modified_data.to_csv('new_data.csv', index=False)