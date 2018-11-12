import pandas as pd
dat = pd.read_csv('titanic.csv')
dat['Age']
def norm_arr(arr):
    mean = arr.mean()
    std = arr.std()

    normalized = (arr - mean) / std
    return normalized
dat['norm'] = norm_arr(dat['Age'])
print(dat)


dat1=dat[dat['Age'].notnull()]
dat1['norm'] = norm_arr(dat1['Age'])
print(dat1)
print(len(dat1['Age']))
print(len(dat['Age']))


dat2=dat1['Age'].iloc[0:3].replace(1000)
dat2['norm_1'] = norm_arr(dat2['Age'])
print(dat2)

n=dat1.Age.quantile(0.025)
m=dat1.Age.quantile(0.975)
dat1_0=dat1[dat1.Age<m][dat1.Age>n]
print(n)
print(dat1_0)

def norm_df(df):
    result = df.copy()

    for feature in df.columns:
        result[feature] = norm_arr(result[feature])

    return result