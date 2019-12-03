import pandas as pd

data = {'Box':['Box 1', 'Box 1', 'Box 1', 'Box 2', 'Box 2', 'Box 2'], 
        'Dimension':['Length', 'Width', 'Height', 'Length', 'Width', 'Height'], 
        'Value':[6,4,2,5,3,4]}
        
df = pd.DataFrame(data, columns=['Box', 'Dimension', 'Value'])
tidy = df.pivot_table(index=['Box'], columns='Dimension', values='Value').reset_index().rename_axis(None, axis=1)
print('Tidy Data Format:\n', tidy, '\n')

new_column = tidy.assign(Volume = lambda tidy: tidy.Height*tidy.Length*tidy.Width)
print('Dataframe with "Volume" column: \n', new_column)