import pandas as pd

file1 = '1.csv'
file2 = '2.csv'

Data1 = pd.read_csv(file1)
Data2 = pd.read_csv(file2)



Merge1 = pd.merge(Data1,Data2,left_on=['datetime','ENODEB','cellname'],right_on=['datetime','ENODEB','cellname'],how='outer')
Merge2	=Merge1.drop('',axis=1)
Merge2.to_csv('Merged1.csv')

