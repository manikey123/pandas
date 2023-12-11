import pandas as pd
'''
The analyst now wants to know the total number of concerts held in the month of September in 2019 and 2020.
'''
def test():
  df = pd.read_csv('dates.csv')
  df['date'] = df['date'].map(lambda x: pd.to_datetime(x))
  df['month'] = df['date'].dt.month
  return len(df[df['month']==9])

print(test())
'''
Your music analyst would like to know how many concerts were held in the year 2019.
A single int representing the number of concerts in 2019

Example: 20

'''
def test():
  df = pd.read_csv('dates.csv')
  df['date'] = pd.to_datetime(df['date'])
  start = pd.to_datetime('2019-01-01')
  end = pd.to_datetime('2020-01-01')
  filtered = df[(df.date >= start) & (df.date < end)]
  return len(filtered)

print(test())
'''
a list of dates to set the concert schedule of a new band, starting 1 January 2019, up-to and including 31 December 2019, all separated by exactly 7 days.
Example: ["2019-01-01", "2019-01-08"]

'''
def test():
  return ([x.strftime("%Y-%m-%d") for x in pd.date_range(start='2019-01-01', end='2019-12-31', freq='7D')])

print(test())

def test():
  df = pd.read_csv('dates.csv')
  df['date'] = pd.to_datetime(df['date'])
  resampled = df.set_index('date').resample('MS').size()
  resampled.index = resampled.index.map(lambda x: x.strftime("%Y-%m"))
  return resampled.to_dict()

print(test())
