import requests, six
import lxml.html as lh
import pandas as pd

from itertools import cycle, islice
from matplotlib import colors

from data_cleaning import data_cleaning
from statistical_analysis import statistical_analysis

url = 'https://pokemondb.net/pokedex/all'

page = requests.get(url)
document = lh.fromstring(page.content)
tr_elements = document.xpath('//tr')

columns = []; i = 0

for header in tr_elements[0]:
    i += 1
    name = header.text_content()
    # print('%d: "%s"' %(i, name))
    columns.append((name,[]))
    
for row_index in range(1, len(tr_elements)):
    row = tr_elements[row_index]
    
    if len(row) != 10:
        break
    
    column_index = 0
    
    for element in row.iterchildren():
        data = element.text_content()
        if column_index > 0:
            try:
                data = int(data)
            except:
                pass
        columns[column_index][1].append(data); column_index += 1

Dict = {title:column for (title, column) in columns}
df = pd.DataFrame(Dict)

df['Name'] = df['Name'].apply(data_cleaning.str_bracket)
df['Type'] = df['Type'].apply(data_cleaning.str_break)

df.to_json('PokemonData.json')
print(df.head())

stats=['Attack', 'Defense','HP', 'Sp. Atk','Sp. Def','Speed','Total']

print(statistical_analysis.max_stats(df, stats))
print(statistical_analysis.min_stats(df, stats))

from pandas.plotting import scatter_matrix
scatter_matrix(df[stats], alpha=0.2, figsize=(10, 10), diagonal='kde')

new_dict = {}
stats_col = ["#", "Name", "Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]

Dict['Type'] = df['Type'].values
for col in stats_col:
    new_dict[col] = []
    new_dict['Type'] = []

for row in range(len(Dict['#'])):
    for t in Dict['Type'][row]:
        for col in stats_col:
            new_dict[col].append(Dict[col][row])
        new_dict['Type'].append(t)
        
new_df = pd.DataFrame(new_dict)
print(new_df.head())

types = new_df['Type'].unique()
colors_list = list(six.iteritems(colors.cnames))
colors_list = list(islice(cycle(colors_list), None, len(new_df)))

# statistical_analysis.barh_stats(new_df, types, colors_list)