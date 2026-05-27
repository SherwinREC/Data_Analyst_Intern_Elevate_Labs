# Data Analyst Internship — Elevate Labs

**Duration:** 3 Months &nbsp;|&nbsp; **Role:** Data Analyst Intern &nbsp;|&nbsp; **Company:** Elevate Labs

---

## Overview

This repository contains all the tasks and projects completed during my 3-month Data Analyst Internship at Elevate Labs. The work spans the full data analytics workflow — from raw data cleaning and SQL database design to business dashboards in Power BI and a machine learning price prediction model for electric vehicles.

---

## Tech Stack

| Tool / Technology | Purpose |
|---|---|
| Python 3.x | Core programming language |
| Pandas, NumPy | Data manipulation and analysis |
| Matplotlib, Seaborn | Data visualization |
| Scikit-learn | Machine learning models |
| PostgreSQL | Relational database and SQL queries |
| SQLite | Lightweight local database |
| Power BI | Interactive dashboards and reporting |
| DAX | Calculated measures and KPIs in Power BI |
| Power Query (M Language) | Data transformation in Power BI |
| Tableau | Data visualization and dashboards |
| Excel | Reporting and quick analysis |
| Kaggle / KaggleHub | Dataset sourcing |

---

## Prerequisites

Before running any Python-based tasks, make sure the following are installed:

```
pip install pandas numpy matplotlib seaborn scikit-learn kagglehub
```

For SQL tasks, PostgreSQL must be installed and running locally. For Task 7, SQLite is built into Python — no separate installation needed.

For Power BI tasks (Task 2, Task 3), Power BI Desktop must be installed on Windows.

---

## Project Structure

```
elevate-labs-internship/
│
├── task1_data_cleaning.py
├── task2_dax_measures.dax
├── task3_dax_measures.dax
├── task3_power_query.pq
├── task4_sql_queries.sql
├── task5_eda_titanic.py
├── task6_sql_online_sales.sql
├── task7_sqlite_sales.py
├── task8_superstore_sales.py
└── EV_Project_Final.py
```

---

## Tasks

---

### Task 1 — Data Cleaning and Preprocessing

**File:** `task1_data_cleaning.py`
**Dataset:** Customer Personality Analysis — Kaggle (`pauloarruda/customer-personality-analysis`)
**Tool:** Python

#### Objective
Clean and preprocess a raw marketing campaign dataset to make it ready for analysis or machine learning. Address data quality issues including missing values, duplicates, incorrect data types, and outliers.

#### Prerequisites
```
pip install pandas kagglehub
```

#### How to Run
```
python task1_data_cleaning.py
```

#### What the Code Does
- Downloads the dataset directly from Kaggle using KaggleHub
- Explores shape, data types, and basic statistics
- Removes duplicate rows
- Fills missing numeric values with column medians
- Fills missing text values with mode and standardizes casing
- Converts the Dt_Customer column to datetime format
- Engineers two new columns: Age (from Year_Birth) and Customer_Tenure_Days (from Dt_Customer)
- Removes outliers in Income and Age using the IQR method
- Saves the cleaned dataset as cleaned_dataset.csv

#### Output
- `cleaned_dataset.csv` — cleaned and preprocessed dataset ready for analysis

---

### Task 2 — Sales Performance Measures in Power BI

**File:** `task2_dax_measures.dax`
**Tool:** Power BI Desktop (DAX)

#### Objective
Write DAX measures to calculate key business KPIs for a sales dashboard in Power BI, including revenue, profit, rankings, and time-based aggregations.

#### Prerequisites
- Power BI Desktop installed (Windows)
- A data source with an Orders table containing Sales, Profit, Quantity, Discount, and Order Date columns

#### How to Use
Open Power BI Desktop, load your dataset, open the DAX editor in the Modeling tab, and paste each measure individually.

#### Measures Included
- Total Sales, Total Profit, Total Orders, Total Quantity
- Profit Margin % (multiplied by 100 for percentage display)
- Average Order Value
- Monthly Sales (MTD), Quarterly Sales (QTD), YTD Sales
- Sales Growth % (month over month using DATEADD)
- Top Customer Rank and Top 10 Customers filter
- High Discount Flag (flags discounts above 30%)
- Profit Status (Profitable / Loss label)

---

### Task 3 — Vehicle Sales Dashboard

**Files:** `task3_dax_measures.dax`, `task3_power_query.pq`
**Tool:** Power BI Desktop (DAX + Power Query)

#### Objective
Build a vehicle sales performance dashboard in Power BI by combining Power Query for data transformation and DAX for calculated KPIs.

#### Prerequisites
- Power BI Desktop installed (Windows)
- CSV file: `vehicle_sales_clean.csv` with columns: Date, Sales, Profit, Quantity
- Update the file path in `task3_power_query.pq` to match your local path

#### How to Use

**Power Query:**
Open Power BI Desktop → Transform Data → Advanced Editor → paste the M code from `task3_power_query.pq`

**DAX:**
After loading data, paste each measure from `task3_dax_measures.dax` into the DAX editor

#### Power Query Steps
- Loads CSV with proper encoding
- Promotes headers and sets correct column types
- Removes duplicates and null rows
- Adds calculated columns: Profit Margin %, Year, Month, Quarter
- Sorts data by date ascending

#### DAX Measures Included
- Total Sales, Total Profit, Total Quantity, Total Transactions
- Avg Profit Margin %, Avg Order Value
- Sales Growth % and Profit Growth % (year over year)
- YTD Sales, YTD Profit, MTD Sales
- Profit Status label

---

### Task 4 — SQL Database Design and Querying

**File:** `task4_sql_queries.sql`
**Tool:** PostgreSQL

#### Objective
Design a normalized relational database schema for an e-commerce system and write SQL queries covering filtering, aggregations, joins, subqueries, views, and indexing.

#### Prerequisites
- PostgreSQL installed and running
- A database created (e.g., `internship_db`)

#### How to Run
```
psql -U your_username -d internship_db -f task4_sql_queries.sql
```

#### Schema
- `customers` — customer details with country
- `products` — product catalog with category, price, stock
- `orders` — order records linked to customers
- `order_items` — individual line items per order linked to products

#### Queries Included
- Filter customers by country
- Top 10 most expensive products
- Total sales grouped by country
- All orders with customer details (INNER JOIN)
- All customers including those without orders (LEFT JOIN)
- Customers who spent above average (subquery with HAVING)
- Monthly sales view (CREATE VIEW)
- Performance indexes on foreign key columns

---

### Task 5 — Exploratory Data Analysis on Titanic Dataset

**File:** `task5_eda_titanic.py`
**Dataset:** Titanic — Machine Learning from Disaster — Kaggle (`shuofxz/titanic-machine-learning-from-disaster`)
**Tool:** Python

#### Objective
Perform a full exploratory data analysis on the Titanic dataset to understand survival patterns and relationships between passenger features.

#### Prerequisites
```
pip install pandas matplotlib seaborn kagglehub
```

#### How to Run
```
python task5_eda_titanic.py
```

#### What the Code Does
- Downloads train and test datasets from Kaggle
- Explores shape, data types, missing values, and basic statistics
- Analyzes survival counts and class distribution
- Generates the following visualizations:
  - Age distribution histogram
  - Survival count plot
  - Passenger class distribution
  - Age vs Passenger Class box plot
  - Survival by gender
  - Survival by passenger class
  - Age vs Fare scatter plot colored by survival
  - Correlation heatmap
  - Pairplot of key features
- Fills missing Age values with median and Embarked with mode

#### Key Findings
- Females had significantly higher survival rates than males
- First-class passengers survived more than third-class passengers
- Younger passengers and children had better survival chances
- Higher fare was positively correlated with survival

---

### Task 6 — SQL Time Series Analysis

**File:** `task6_sql_online_sales.sql`
**Tool:** PostgreSQL

#### Objective
Create a sales table, insert transactional data, and write time-based SQL queries to extract monthly revenue trends and order counts.

#### Prerequisites
- PostgreSQL installed and running
- A database created (e.g., `internship_db`)

#### How to Run
```
psql -U your_username -d internship_db -f task6_sql_online_sales.sql
```

#### What the Code Does
- Creates the `online_sales` table with order_date, amount, and product_id
- Inserts 10 sales records from January to May 2023
- Query 1: Monthly revenue and order count for all years
- Query 2: Monthly revenue and order count filtered for the year 2023
- Uses EXTRACT for year and month aggregation with GROUP BY and ORDER BY

---

### Task 7 — SQLite Sales Analysis with Python

**File:** `task7_sqlite_sales.py`
**Tool:** Python, SQLite, Pandas, Matplotlib

#### Objective
Create and query a local SQLite database using Python, perform product-level sales analysis, and generate visualizations.

#### Prerequisites
```
pip install pandas matplotlib
```

SQLite is built into Python — no additional installation required.

#### How to Run
```
python task7_sqlite_sales.py
```

#### What the Code Does
- Creates a local SQLite database file `sales_data.db`
- Creates a `sales` table and inserts product sales records
- Queries total quantity, average price, and revenue per product using SQL via Pandas
- Prints a summary including total revenue, best-selling product, and highest revenue product
- Generates three side-by-side bar charts: Revenue, Quantity Sold, and Average Price by product
- Saves the chart as `sales_chart.png`

#### Output
- `sales_data.db` — local SQLite database
- `sales_chart.png` — saved visualization

---

### Task 8 — Superstore Sales Analysis

**File:** `task8_superstore_sales.py`
**Dataset:** Superstore Sales — Kaggle (`ishanshrivastava28/superstore-sales`)
**Tool:** Python

#### Objective
Perform a comprehensive sales analysis on the Superstore dataset by engineering new features and generating multiple business-level visualizations.

#### Prerequisites
```
pip install pandas matplotlib seaborn kagglehub
```

#### How to Run
```
python task8_superstore_sales.py
```

#### What the Code Does
- Downloads the dataset from Kaggle using KaggleHub
- Parses Order Date and Ship Date as datetime
- Engineers new columns: Month-Year, Year, Month, Quarter, Day of Week, Shipping Days, Profit Margin %, Revenue per Unit, Profit Status, Discount Band
- Removes duplicates and filters out zero-sales rows
- Prints business summaries: sales by region, category, sub-category, yearly sales, average shipping days, and overall profit margin
- Generates 8 visualizations saved as PNG files:
  - Monthly Sales Trend (line chart)
  - Sales by Region (horizontal bar)
  - Profit by Category (horizontal bar)
  - Sales by Sub-Category (bar chart)
  - Discount vs Profit (scatter plot)
  - Sales Distribution by Year (box plot)
  - Sales by Quarter (bar chart)
  - Correlation Heatmap

#### Output
- `Cleaned_Superstore_Sales.csv` — enriched and cleaned dataset
- 8 PNG chart files

---

### Task 9 — EV Price Prediction (Final Project)

**File:** `EV_Project_Final.py`
**Dataset:** Electric Vehicle Market and Pricing Dataset 2026 — Kaggle (`patelris/electric-vehicle-market-and-pricing-dataset-2026`)
**Tool:** Python, Scikit-learn

#### Objective
Build an end-to-end machine learning pipeline to predict electric vehicle prices based on vehicle specifications, brand, range, battery capacity, and other features.

#### Prerequisites
```
pip install pandas numpy matplotlib seaborn scikit-learn kagglehub
```

#### How to Run
```
python EV_Project_Final.py
```

#### What the Code Does

**Data Loading and Inspection**
- Downloads the dataset from Kaggle
- Prints column names, data types, shape, and missing value summary to verify the dataset structure before processing

**Data Cleaning**
- Removes duplicate rows
- Drops rows with missing target values (Price)
- Fills missing numeric values with column medians
- Fills missing categorical values with mode

**Exploratory Data Analysis**
- EV Price distribution histogram
- Feature correlation heatmap
- Average price by brand (top 15)
- Range vs Price scatter plot
- Battery Capacity vs Price scatter plot

**Model Building**
- Label encodes all categorical columns
- Applies StandardScaler to features for Linear Regression
- Splits data into 80% train and 20% test sets
- Trains three models: Linear Regression, Random Forest (100 estimators), Gradient Boosting (100 estimators, learning rate 0.1)

**Model Evaluation**
- Evaluates all models using MAE, RMSE, and R2 Score
- Automatically selects the best model based on R2 Score
- Prints a comparison table of all model results

**Visualizations**
- Actual vs Predicted Price scatter plot for the best model
- Top 10 Feature Importances bar chart (for tree-based models)

#### Output
- `ev_cleaned.csv` — cleaned dataset
- `ev_model_results.csv` — model comparison results
- PNG chart files for all visualizations

#### Note
Run the column name check printed at the start of the script to verify the exact column names in the dataset. If column names differ (e.g., Range_km, Battery_Capacity_kWh), update the relevant plot sections accordingly before running the full pipeline.

---

## Key Learnings

- Real-world datasets are messy — data cleaning and preprocessing always take the most time
- SQL and Python together cover most of the day-to-day data analyst workflow
- Power BI with DAX and Power Query is highly effective for business reporting and dashboards
- Feature engineering adds meaningful context that improves both analysis and model performance
- Tree-based models like Random Forest and Gradient Boosting consistently outperform Linear Regression on structured tabular data
- Visualizations are the most effective way to communicate data insights to stakeholders
