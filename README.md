# Data Analysis Projects

This repository contains a collection of data analysis projects. Each subfolder in this repository represents a separate project with its own code, datasets, and documentation.

## Projects Overview

### 01 Market Basket Analysis
- **Description:** Analyzes online retail transaction data to uncover customer behavior patterns, product performance, transaction trends, and product associations using association rule mining.
- **Key Features:**
  - Comprehensive data cleaning and quality assessment
  - Exploratory data analysis with advanced visualizations
  - Customer behavior and spending pattern analysis
  - Product performance and catalog insights
  - Market basket analysis using association rules
  - Cross-selling and bundling recommendations
  - Seasonal and geographical trend analysis
- **Technologies:** Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly, NetworkX, Jupyter Notebook
- **Dataset:** Online retail transaction data with 541,909 records spanning December 2010 - December 2011
- **Instructions:** See the README in the [01 Market Basket Analysis folder](./01%20Market%20Basket%20Analysis/README.md) for detailed setup and execution instructions.

### 02 Customer Lifetime Value (CLV) Analysis
- **Description:** Calculates and predicts customer value over time, helping companies identify high-value customers and tailor their marketing strategies.
- **Status:** In Development
- **Dataset:** OnlineRetail.csv
- **Instructions:** See the README in the [02 Customer Lifetime Value (CLV) Analysis folder](./02%20Customer%20Lifetime%20Value%20(CLV)%20Analysis/README.md) for more details.

### Future Projects
- **Project 03:** Geographical Sales Performance Dashboard  
  _Description: Provides a detailed visual analysis of sales data by region, enabling the identification of market trends and growth opportunities._

- **Project 04:** Social Media Campaign Analysis  
  _Description: Examines social media engagement and sentiment to evaluate campaign performance and inform future digital marketing efforts._

*Additional projects will be added over time.*

## Setup and Execution

### Prerequisites
- Python 3.12 or higher
- `uv` (Python package installer and virtual environment manager) - Install from [astral.sh/uv](https://astral.sh/uv)
- Git for cloning the repository

### General Setup Steps

1. **Clone the Repository**  
   ```bash
   git clone https://your.repository.url.git
   cd Data-Analysis-Projects
   ```

2. **Navigate to a Specific Project Folder**  
   ```bash
   cd "01 Market Basket Analysis"
   # or
   cd "02 Customer Lifetime Value (CLV) Analysis"
   ```

3. **Set up Environment using `uv`**  
   ```bash
   # Create a virtual environment
   uv venv

   # Activate the virtual environment
   # On macOS/Linux:
   source .venv/bin/activate
   # On Windows (PowerShell):
   # .\.venv\Scripts\Activate.ps1

   # Install dependencies
   uv pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook**  
   ```bash
   jupyter notebook main.ipynb
   # or for JupyterLab:
   jupyter lab main.ipynb
   ```

5. **Run the Analysis**
   - Open the `main.ipynb` notebook in your Jupyter environment
   - Run cells individually or use "Restart Kernel and Run All Cells" for complete execution
   - Follow project-specific instructions in each folder's README

## Directory Structure

```plaintext
Data-Analysis-Projects/
├── 01 Market Basket Analysis/
│   ├── main.ipynb                 # Main analysis notebook
│   ├── README.md                  # Project documentation
│   ├── Report.md                  # Detailed findings report
│   ├── requirements.txt           # Python dependencies
│   ├── pyproject.toml            # Project configuration
│   ├── uv.lock                   # Dependency lock file
│   ├── .python-version           # Python version specification
│   ├── .gitignore                # Git ignore rules
│   └── onlineretail/             # Dataset folder
│       ├── OnlineRetail.csv      # Original dataset
│       └── OnlineRetail_Cleaned.csv # Processed dataset
├── 02 Customer Lifetime Value (CLV) Analysis/
│   ├── main.ipynb                 # Main analysis notebook
│   ├── README.md                  # Project documentation
│   ├── requirements.txt           # Python dependencies
│   ├── pyproject.toml            # Project configuration
│   ├── uv.lock                   # Dependency lock file
│   ├── .python-version           # Python version specification
│   └── onlineretail/             # Dataset folder
│       └── OnlineRetail.csv      # Dataset
└── README.md                     # This file
```

## Key Technologies Used

- **Python Libraries:** pandas, numpy, matplotlib, seaborn, plotly, networkx, scikit-learn
- **Development Environment:** Jupyter Notebook/Lab
- **Package Management:** uv
- **Visualization:** Interactive plots with Plotly, statistical plots with Seaborn
- **Analysis Techniques:** Association rule mining, statistical analysis, data visualization

## Project Highlights

### Market Basket Analysis Results
- Identified strong product associations for cross-selling opportunities
- Analyzed customer behavior patterns across different time periods and countries
- Generated actionable business recommendations for marketing and inventory management
- Created comprehensive visualizations including network graphs, heatmaps, and interactive plots

## License

This repository is open-sourced under the MIT License.

## Contributing

Contributions are welcome! Please follow these guidelines:
- Open an issue to discuss potential changes
- Submit pull requests with clear descriptions
- Include proper documentation for new projects
- Ensure code quality and reproducibility

When adding new projects:
1. Create a dedicated folder with a descriptive name
2. Include a detailed README with setup instructions
3. Add requirements.txt with all dependencies
4. Update this main README to include the new project

---

Happy analyzing! 📊