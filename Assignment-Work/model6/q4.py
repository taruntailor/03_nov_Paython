# . Sort a DataFrame by the 'Date' column in ascending order. (Take
# the dataset accordingly)

df['Date'] = pd.to_datetime(df['Date'])

df_sorted = df.sort_values(by='Date', ascending=True)

print(df_sorted)
