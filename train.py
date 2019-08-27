import pandas as pd

data = pd.read_csv('trainms.csv')
print(data.columns)
print(data.treatment.unique())