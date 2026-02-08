# 6. Difference between iloc and loc function , explain with example.

import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'Salary': [50000, 60000, 45000]
}, index=['a', 'b', 'c'])

print(df.loc['a'])     
print(df.loc['a':'b'])    
print(df.loc[:, ['Name', 'Salary']])  
