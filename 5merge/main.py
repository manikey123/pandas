import pandas as pd
#Basic Merge [Countries & Bands]
def test():
  df = pd.read_csv('music.csv')
  countries = pd.read_csv('countries.csv')
  merged = df.merge(countries, left_on='country', right_on='country_id')

  return merged.groupby('name').plays.sum().to_dict()

print(test())
# Merge with Missing Values (Medium)
def test():
  df = pd.read_csv('music.csv')
  countries = pd.read_csv('countries.csv')
  merged = pd.merge(df, countries, how='left', left_on='country', right_on='country_id')
  return merged[merged.name.isnull()].plays.sum()
print(test())

#Basic Concat [Bands] (Trivial)
def test():
  df = pd.read_csv('music.csv')
  df_2 = pd.read_csv('music_2.csv')

  return pd.concat([df, df_2]).plays.sum()

print(test())

#Challenge 4: Concat on Columns [Bands] (Medium)
def test():
  df = pd.read_csv('music.csv')
  df_monthly = pd.read_csv('music_monthly.csv')
  df.set_index('artist', inplace=True)
  df_monthly.set_index('artist', inplace=True)
  merged = pd.concat([df, df_monthly], axis=1)
  merged['ratio'] = merged['monthly_listeners']/merged['fans']
  return list(merged[merged.ratio >= 0.5].index.values)

print(test())

