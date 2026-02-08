# Load a CSV file into a Pandas DataFrame and display the first 5
# rows


import pandas as pd

df = pd.read_csv("data.csv")

# Display the first 5 rows
print(df.head())
