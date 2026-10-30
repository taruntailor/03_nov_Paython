import pandas as pd
import matplotlib.pyplot as plt

# Corrected data
data = {
    'cut': ['fair', 'premium', 'good'],
    'price': [5000, 7000, 4500]  # assuming 50000 was typo
}

df = pd.DataFrame(data)
print(df)

# Bar chart for categorical x-axis
plt.figure(figsize=(8,5))
plt.bar(df['cut'], df['price'], color='skyblue',linestyle='--')
plt.xlabel('Cut')
plt.ylabel('Price')
plt.title('Price vs Cut')
plt.show()



data = {
    'cleartiy'
    'cut': ['fair', 'premium', 'good'],
    'price': [5000, 7000, 4500]  # assuming 50000 was typo
}