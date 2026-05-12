import pandas as pd

df = pd.read_csv('sales.csv')
df.groupby('date').sum()
