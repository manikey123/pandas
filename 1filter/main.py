import pandas as pd
df = pd.read_csv('music.csv')
uk_artists = df[df['country']=='UK']
#print(uk_artists)
#Multiple filters
out = df[(df['genre']=='rock') & (df['plays']>=200)]
#print(out)
#Not 
out = df[~((df.country=='US') & (df.plays >= 500))]
#print(out)
'''
Artists outside the UK who have > 100 plays
Artists inside the UK who have > 200 plays
'''
out = df[((df['country']=='UK') & (df['plays'] > 200) ) | ((df['country']!='UK') &( df['plays'] > 100))]

#Filtering by list
countries = ['UK', 'US']
out = df[df.country.isin(countries)]
#Filtering by string
out = df[df['artist'].str.startswith('The')]
'''
Your music data analyst is getting more curious; they want to know a list of all artists from the UK or Finland whose name contains the word The.

Expected output
A Python list with the names of the artists matching the above filters.

Example: ["ACDC", "The Doors"]
'''
def test():
    out = df[df.artist.str.contains('The')]
    out = out[out['country'].isin(['UK', 'Finland'])]
    return list(out.artist.values)

print(test())

'''
Your music analyst is getting more selective about the countries of origin of artists. They want to exclude artists from the UK or Finland, with the exception of still returning artists who have >= 10000 plays.
'''

def test():
    df = pd.read_csv('music.csv')
    filtered = df[(~df.country.isin(['UK', 'Finland'])) | (df.plays >= 10000)]
    return list(filtered.artist.values)

print(test())

'''
TBD TODO
.query() function, which allows filtering by a Python str. An example: df.query('name == 'Pink Floyd'). It can be less verbose in its syntax.
The use of .loc, .iloc in selecting specific rows/columns based on their name/index.
'''

