import pandas as pd
df = pd.read_csv('IMDB-Movie-Data.csv')
print('___________')

df.dropna()

print(df.info())

temp = df.groupby(by = "Year")["Rating"].mean
print(temp)