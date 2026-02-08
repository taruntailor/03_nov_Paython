# 5. Add one new New column with into a existing DataFrame .

import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22]
})

# Add a new column called 'Salary'
df['Salary'] = [50000, 60000, 45000]

print(df)
