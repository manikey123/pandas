import pandas as pd

'''
Your music analyst is interested in finding the sum of plays of artists by country. Can you return the total number of plays for each country?
'''
df = pd.read_csv('music_group.csv')
def test():
  return df.groupby('country').plays.sum().to_dict()
print(test())

'''Group by 2 items'''

def test():
  return df.groupby(['country', 'genre']).plays.sum().to_dict()

print(test())
'''
 Countries with >1000 Plays
'''
import pandas as pd

def test():
  df = pd.read_csv('music_group.csv')
  reset = df.groupby('country').plays.sum().reset_index()
  return list(reset[reset.plays>1000].country.values)

print(test())

#SolutionB
def test():
  df = pd.read_csv('music_group.csv')
  reset = df.groupby('country').plays.sum()
  filtered = reset[reset > 1000]
  print(list(filtered.index))
  return list(filtered.index)

test()

#Plays-to-Fans Ratio (Medium)
def test():
  df = pd.read_csv('music_group.csv')
  return df.groupby('country').apply(lambda x: x.plays.sum() / x.fans.sum()).to_dict()
print(test())

'''
Multiple Aggregations (Difficult)
Your music analyst is interested in knowing multiple statistics at once, grouped by country.These are as follows:

Sum of plays
Average of plays
Maximum fans from all artists in the country
'''
def test():
  df = pd.read_csv('music_group.csv')
  grp = df.groupby('country').agg({'plays': ['sum', 'mean'], 'fans': ['max']})
  grp.columns = ['_'.join(col) for col in grp.columns.values]
  res = grp.to_dict(orient='index')
  return res

print(test())
#Can apply multiple functions to multiple columns in a DataFrameGroupBy object

'''
Passing as_index=False while applying a groupby function: When aggregating and applying a reset_index function afterwards, the grouped by column will not be the index of the resultant DataFrame.
Applying filters on groups using .filter() with a lambda function: This would allow more concise filters, such as keeping groups with only a count of records greater than a certain value.
'''

