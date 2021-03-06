import pandas as pd

# READING THE VALUES FROM A CSV FILE
df = pd.read_csv('somecsvfile.csv')

# SENDING BACK VALUES TO A CSV FILE
df.to_csv('anothercsvfile.csv')

#SENDING ONLY ONE COLUMN TO A CSV FILE
df['somecolumn'].to_csv('yetanothercsvfile.csv')


#KEEPING SPECIFIC COLUMNS AND DROPPING ALL THE REST
df = pd.read_csv('somecsvfile.csv', usecols = ['column_name', 'another_column_name'])


# ADJUSTING THE INDEX VALUE EVERY TIME WITH A CSV FILE
df = pd.read_csv('somecsvfile.csv', index_col = 0)

# RENAMING ONLY A SPECIFIED COLUMN
df.rename(columns = {'originalname' : 'newname'}, inplace = True)