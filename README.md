Movie Correlation Analysis

Project Overview
This project explores the relationships between movie budget, gross revenue, audience votes, ratings, and genres using Python and data analysis techniques.

The goal is to identify factors associated with box office success and investigate how different movie genres perform financially.

Tools Used
Python
Pandas
Seaborn
Matplotlib
GitHub
Dataset
Movie dataset containing:

7,668 movie records
15 columns
Main variables analyzed:

Budget
Gross Revenue
Votes
Score
Genre
Runtime
Year
Data Cleaning
Missing values were examined using:

df.isnull().sum()
Rows containing missing values were removed:

df = df.dropna()
Dataset Size
Stage	Rows
Original Dataset	7,668
After Cleaning	5,421
Correlation Analysis
Correlation was calculated to understand relationships between numerical variables.

Key Correlations
Variables	Correlation
Budget vs Gross Revenue	0.74
Votes vs Gross Revenue	0.61
Budget vs Score	0.07
Key Findings
Budget and Gross Revenue showed a strong positive correlation (0.74).
Movies with more audience votes tended to generate higher revenue.
Higher budgets did not necessarily result in higher audience ratings.
Scatter Plot
The scatter plot below illustrates the relationship between movie budget and gross revenue.

Scatter Plot
![alt text](image-3.png)

Insight
A clear upward trend can be observed, indicating that higher-budget movies generally achieve higher box office revenue.

Correlation Heatmap
The heatmap visualizes correlations among all numerical variables.

Correlation Heatmap

Insight
The strongest relationship found in the dataset was between:

Budget and Gross Revenue (0.74)
This suggests that movie budget is one of the strongest indicators of box office performance.

Genre Analysis
Average gross revenue was calculated for each movie genre.

df.groupby('genre')['gross'].mean()
Genre Analysis

Initial Finding
Genres with the highest average gross revenue:

Genre	Average Gross Revenue
Family	518M USD
Animation	281M USD
Action	168M USD
Genre Distribution
To validate the reliability of genre-level conclusions, the number of movies in each genre was analyzed.

Genre Distribution

Sample Size Observation
Genre	Movie Count
Comedy	1496
Action	1415
Drama	863
Animation	277
Family	4
Additional Investigation
The Family genre appeared to have the highest average gross revenue.

However, only 4 Family movies remained after data cleaning:

Beauty and the Beast
E.T. the Extra-Terrestrial
Raise Your Voice
The Nutcracker
Further inspection revealed that:

Beauty and the Beast generated approximately 1.26 billion USD
E.T. generated approximately 793 million USD
These blockbuster movies heavily influenced the average revenue calculation.

Conclusion
Although the Family genre had the highest average revenue, the small sample size makes the result less reliable.

Among genres with substantial sample sizes, Animation demonstrated the strongest overall financial performance.

Limitations
The dataset contained missing values, requiring row removal.
Data cleaning reduced the dataset from 7,668 to 5,421 records.
Removing missing values may introduce selection bias.
Some genres contain very few observations, making averages sensitive to extreme values.
What I Learned
Through this project, I practiced:

Data cleaning with Pandas
Correlation analysis
Data visualization
Heatmap interpretation
GroupBy operations
Mean vs Median comparison
Sample size validation
Exploring potential bias in analytical results
Future Improvements
Potential next steps:

Compare Mean vs Median across genres
Analyze production companies
Build a movie revenue prediction model
Apply Linear Regression
Compare Linear Regression with Random Forest models