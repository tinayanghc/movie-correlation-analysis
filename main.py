import pandas as pd

#Data cleaning
df=pd.read_csv('movies.csv')
df=df.dropna()


#Scatter Plot
import seaborn as sns
import matplotlib.pyplot as plt 
sns.regplot(
    data=df,
    x='budget',
    y='gross',
    scatter_kws={'color':'blue'},
    line_kws={'color':'red'}
)
plt.title('Budget vs Gross Revenue')
plt.savefig('scatter.png')
plt.show()

#Correlation Analysis
print(df[['budget','gross']].sort_values(by='budget', ascending=False).head())
print(df[['budget','gross']].corr())


corr_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(8,6))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm'
)

plt.title('Correlation Matrix')
plt.savefig('heatmap.png')

plt.show()


# Genre Analysis

genre_gross =(
    df.groupby('genre')['gross'].mean().sort_values(ascending=False)
)

print(genre_gross)

plt.figure(figsize=(10,6))

genre_gross.plot(kind='bar')

plt.title('Average Gross Revenue bny Genre')
plt.xlabel('Genre')
plt.ylabel('Average Gross Revenue')

plt.savefig('genre_analysis.png')

plt.show()

print(
    df.groupby('genre')['gross'].count().sort_values(ascending=False)
)

print(
    df[df['genre'] =='Family'][['name','year','gross']]
)

print(df.groupby('genre')['gross'].median())

# Family類型電影票房收入最高

print(df.groupby('genre')['gross'].count())

comparison=pd.DataFrame({
    'Mean':df.groupby('genre')['gross'].mean(),
    'Median':df.groupby('genre')['gross'].mean(),
    'Count':df.groupby('genre')['gross'].count()
})
print(
    comparison.sort_values(
        by='Mean',
        ascending=False
    )
)

genre_count = (
    df.groupby('genre')['gross'].count().sort_values(ascending=False)
)
plt.figure(figsize=(10,6))

genre_count.plot(kind='bar')
plt.title('Number of Movies by Genre')
plt.xlabel('Genre')
plt.ylabel('Movie count')

plt.savefig('genre_count.png')

plt.show()