import pandas as pd

We_1 = {'Student':['Ice Bear', 'Panda', 'Grizzly'], 'Math':[80,95,79]}
Bears_1 = pd.DataFrame(We_1, columns=['Student','Math'])

We_2 = {'Student':['Ice Bear', 'Panda', 'Grizzly'], 'Electronics':[81,85,83]}
Bears_2 = pd.DataFrame(We_2, columns=['Student','Electronics'])

We_3 = {'Student':['Ice Bear', 'Panda', 'Grizzly'], 'GEAS':[90,79,93]}
Bears_3 = pd.DataFrame(We_3, columns=['Student','GEAS'])

We_4 = {'Student':['Ice Bear', 'Panda', 'Grizzly'], 'ESAT':[93,89,88]}
Bears_4 = pd.DataFrame(We_4, columns=['Student','ESAT'])

Bare_Bears_1 = pd.merge(Bears_1, Bears_2, how='outer', on = 'Student')
Bare_Bears_2 = pd.merge(Bears_3, Bears_4, how='outer', on = 'Student')
We_Bare_Bears_Result = pd.merge(Bare_Bears_1, Bare_Bears_2, how='outer', on='Student')
print('By merging the four dataframes the resulting dataframe is :\n', We_Bare_Bears_Result, '\n')

tidy = pd.melt(We_Bare_Bears_Result, id_vars=['Student'], value_vars = ['Math', 'Electronics', 'GEAS', 'ESAT'])
tidy_rename = tidy.rename(columns={'variable':'Subjects', 'value': 'Grades'})
tidy_sort = tidy_rename.sort_values('Student')
tidy_final = tidy_sort.reset_index().drop(columns=['index'])
print('Long format of dataframe is:\n', tidy_final, '\n')