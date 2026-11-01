Movie Correlation Analysis
Project Objective
Analyze the relationship between movie budget, gross revenue, audience votes, and ratings using Python.

Dataset
7,668 movie records
15 columns
Data Cleaning
Missing values were identified using:

df.isnull().sum()
Rows containing missing values were removed:

df = df.dropna()
Dataset size:

Before cleaning: 7668 rows
After cleaning: 5421 rows
Key Findings
Budget vs Gross Revenue
Correlation = 0.74

Higher-budget movies generally generate higher box office revenue.

Votes vs Gross Revenue
Correlation = 0.61

Movies with higher audience engagement tend to have higher revenue.

Budget vs Score
Correlation = 0.07

Higher budgets do not necessarily result in higher audience ratings.

Visualizations
Scatter Plot
Correlation Heatmap
Tools Used
Python
Pandas
Seaborn
Matplotlib
Limitations
The budget column contained 2,171 missing values.

Rows with missing values were removed using dropna().

This may introduce selection bias because movies without budget information were excluded from the analysis.

Key Findings

1. Budget and Gross Revenue showed a strong positive correlation (0.74).

2. Higher movie budgets do not necessarily result in higher audience ratings (0.07).

3. Animation movies generated the highest average gross revenue among all genres.