import pandas as pd
csv_path = 'pandas/bike-sharing.csv'
df = pd.read_csv(csv_path)
#print(df.head()) # first five rows

xls_path = 'pandas/excell.xlsx'

df2 = pd.read_excel(xls_path)

#print(df2.head())

songs = {
    'album' :['thriller','suck it and see','back in black','kashmir'],
    'released' :[1982,1993,1994,1665],
    'length' : ['00.42.11', '00.13.14','00.23.21',None]
}

songs_frame =  pd.DataFrame(songs)

songs_frame=songs_frame.fillna('00.13.15')
print(songs_frame)
print(songs_frame['length'])
print(songs_frame)

  
myset=set(songs_frame['length'])

#print(myset)

#print(songs_frame['length'].unique())




#print(type(songs_frame['length']))


#print(type(songs_frame))


print(songs_frame.iloc[2])
print(songs_frame['length'].values) # converting into a numpy array
print(songs_frame['length'].index)
print(songs_frame['length'].shape)
print(songs_frame['length'].sum())


print(songs_frame)

index_list = ['a','b','c','d']

songs_frame.index  = index_list;

print(songs_frame.iloc[0:4])
print(songs_frame.loc['a':'c'])


filtered =  songs_frame['released'] >1980

