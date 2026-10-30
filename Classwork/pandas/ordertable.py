import pandas as  pd

columns=[
      "orderid", "orderdate", "shipdate", "shipmodel",
    "customer", "city", "state", "postalcode", "region"
]

df=pd.DataFrame(columns=columns)


data = [
    [1001, "2024-01-05", "2024-01-08", "First Class", "John Smith", "New York", "NY", "10001", "East"],
    [1002, "2024-01-07", "2024-01-10", "Second Class", "Alice Brown", "Los Angeles", "CA", "90001", "West"],
    [1003, "2024-01-10", "2024-01-15", "Standard Class", "David Wilson", "Chicago", "IL", "60601", "Central"],
    [1004, "2024-01-12", "2024-01-14", "Same Day", "Emma Davis", "Houston", "TX", "77001", "South"]
]

df = pd.DataFrame(data, columns=columns)
print(df)