'''
A python dict mapping each band to its continent of origin

Example: {'Cairokee': 'Africa', 'The Beatles': 'Europe'}

The country-to-continent mapping is provided in the challenge as a dict, for example:

{'Egypt': 'Africa', ...}
'''

def test():
  df = pd.read_csv('music.csv')
  continents = {'UK': 'Europe', 'US': 'North America', 'Egypt': 'Africa', 'Finland': 'Europe'}
  df['continent'] = df['country'].map(continents)
  return df.set_index('artist')['continent'].to_dict()

print(test())
'''
to assign nicknames to each band based on the first two letters of their name. Can you help them with that?
A python dict, mapping the artist names to the first two letters of their names

Example: {'The Beatles': 'Th', 'Cairokee': 'Ca'}
'''
def test():
  df = pd.read_csv('music.csv')
  df['init'] = df['artist'].map(lambda x: x[:2])
  return df.set_index('artist')['init'].to_dict()

print(test())

'''
Your music analyst wants to identify which bands are very popular/popular/not popular based on the rules below:

A band is very popular if they have greater than 1000 plays OR if they have greater than 50 fans.
A band is popular if they don’t meet the above conditions, but have plays greater than or equal to 500.
A band is not popular if they don’t meet any of the above conditions.


A dict mapping each band name to one of the following: popular, very popular or not popular

Example: {'The Beatles': 'not popular', 'Pink Floyd': 'very popular'}
'''

def is_popular(plays, fans):
    if plays > 1000 or fans > 50:
        return 'very popular'
    elif plays >= 500:
        return 'popular'
    else:
        return 'not popular'

def test():
    df = pd.read_csv('music.csv')
    df['popular'] = df.apply(lambda x: is_popular(x.plays, x.fans), axis=1)
    return df.set_index('artist')['popular'].to_dict()

print(test())

'''
Given a new dataset that maps bands to how much sales they’ve made in different markets, you are required to do the following tasks:

Clean the dataset sales values in each cell to remove the k suffix, and replace it with the value in thousands (example: 1k --> 1000).
Return the maximum sales amount that each market had from any 

A dict mapping each market to its sales value in thousands

Example: {'US Sales': 10000}

'''

def test():
  df = pd.read_csv('sales.csv').set_index('Band')
  replaced = df.applymap(lambda x: int(x.replace('k', '')) * 1000)
  mx = replaced.apply(lambda x: max(x), axis=0)
  return mx.to_dict()

print(test())