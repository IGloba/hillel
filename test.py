import pandas as pd
my_series = pd.Series([5, 6, 7, 8, 9, 10])
print(my_series)
my_series.index
my_series.values
my_series2 = pd.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
my_series2['f']
my_series2[['a', 'b', 'f']]
my_series2[['a', 'b', 'f']] = 0
var = my_series2[my_series2 > 0]
my_series2[my_series2 > 0] * 2
my_series3 = pd.Series({'a': 5, 'b': 6, 'c': 7, 'd': 8})
my_series3.name = 'numbers'
my_series3.index.name = 'letters'
my_series3
df = pd.DataFrame({'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]})
df['country']
type(df['country'])
df.columns
df.index
df = pd.DataFrame({
     'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
     'population': [17.04, 143.5, 9.5, 45.5],
     'square': [2724902, 17125191, 207600, 603628]
 }, index=['KZ', 'RU', 'BY', 'UA'])
df.index = ['KZ', 'RU', 'BY', 'UA']
df.index.name = 'Country Code'
df.loc['KZ']
df.iloc[1]
df.loc[['KZ', 'RU'], 'population']
df.index
df.columns
df.loc['KZ':'BY', :]
df.iloc[:, 1:]
df[df.population > 10][['country', 'square']]
df['density'] = df['population'] / df['square'] * 1000000
df.drop(['density'], axis='columns')


df.index.name = 'Country Code'

df  = df.rename(columns={'Country Code': 'country_code'})


df = pd.read_csv('titanic.csv', sep=',')
df.shape
df.columns

df.iloc[:4]
df.groupby(['Sex', 'Survived'])['PassengerID'].count()
df.groupby(['PClass', 'Survived'])['PassengerID'].count()
titanic_df = pd.read_csv('titanic.csv')
pvt = titanic_df.pivot_table(index=['Sex'], columns=['PClass'], values='Name', aggfunc='count')
pvt.loc['female', ['1st', '2nd', '3rd']]

df = pd.read_csv('apple.csv', index_col='Date', parse_dates=True)
df = df.sort_index()
print(df.info())
df.loc['2012-Feb', 'Close'].mean()
df.loc['2012-Feb':'2015-Feb', 'Close'].mean()
df[:4]
df.resample('W')['Close'].mean()
import matplotlib
montly_average = df.resample('M')['Close'].mean()
montly_average.columns = ['Date', 'Average Price']

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('apple.csv', index_col='Date', parse_dates=True)
df = df.sort_index()

new_sample_df = df.loc['2012-Feb':'2017-Feb', ['Close']]
new_sample_df.plot()
plt.show()

