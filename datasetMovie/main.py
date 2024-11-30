import pandas as pd
df = pd.read_csv('IMDB-Movie-Data.csv')
print('___________')

df.dropna()

print(df.info())

#Середній рейтинг всіх фільмів за роки 
temp = df.groupby("Year")["Rating"].mean()
print(temp)

#Довші фільми мають кращий рейтинг
length = df.groupby("Runtime (Minutes)")["Rating"].max()
print(length)
