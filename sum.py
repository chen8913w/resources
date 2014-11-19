import pandas as pd

file1 = '1.csv'

Data1 = pd.read_csv(file1)
Data1=Data1.drop(['A','B'],axis=1)
Data2=Data1.groupby(['C','D']).sum()
Data2.to_csv('2.csv')

