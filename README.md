# Movie Correlation Analysis
This project explores the relationship between movie budget, gross revenue and movie genre using Python.

## Scatter Plot
Insight

A positive relationship can be observed between budget and gross revenue.
Movies with larger budgets generally generated higher box office revenue.
However, several outliers can also be observed, suggesting that a high budget does not always guarantee commercial success.
![scatter Plot](scatter.png)

## Correlation Heatmap
Insight

Budget and gross revenue showed the strongest positive correlation (0.74).
This indicates that production budget is one of the most important factors associated with movie revenue.
![Correlation Heatmap](heatmap.png)

## Genre Analysis
Insight

Family movies showed the highest average gross revenue.
However, further investigation revealed that only four Family movies remained after data cleaning.
Therefore, the result should be interpreted with caution.
![Genre Analysis](genre_analysis.png)

## Genre Distribution
Insight

The dataset is highly imbalanced across genres.
Comedy and Action contain over 1,400 movies each, while Family contains only four movies.
This sample size difference may affect genre-level comparisons.
# Family Genre Investigation
Although the Family genre showed the highest average gross revenue, only four movies remained after data cleaning.

## Family Movies Included
Movie	Year
Beauty and the Beast	2017
E.T. the Extra-Terrestrial	1982
Raise Your Voice	2004
The Nutcracker	1993
##Insight
Further investigation revealed that the Family genre contained only four movies in the cleaned dataset.

The average gross revenue was heavily influenced by blockbuster titles such as Beauty and the Beast and E.T. the Extra-Terrestrial.

Therefore, the Family genre result should be interpreted with caution due to its very small sample size.
![Genre count](genre_count.png)

### Genre Sample Size

| Genre | Number of Movies |
|--------|----------------:|
| Comedy | 1496 |
| Action | 1415 |
| Drama | 863 |
| Animation | 277 |
| Family | 4 |

### Family Movies Included

| Movie | Year | Gross Revenue |
|--------|------|--------------:|
| Beauty and the Beast | 2017 | 1.26B USD |
| E.T. the Extra-Terrestrial | 1982 | 793M USD |
| Raise Your Voice | 2004 | 14.9M USD |
| The Nutcracker | 1993 | 2.1M USD |

# Code Used
```family_movies = (
    df.loc[
        df['genre'] == 'Family',
        ['name', 'year', 'gross']
    ]
)

print(family_movies)```