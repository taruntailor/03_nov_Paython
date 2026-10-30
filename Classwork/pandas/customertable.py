import pandas as pd

# Define columns
columns = ["customerid", "customername", "segment", "country"]

# Sample data
data = [
    ["C001", "John Smith", "Consumer", "USA"],
    ["C002", "Alice Brown", "Corporate", "USA"],
    ["C003", "David Wilson", "Home Office", "Canada"],
    ["C004", "Emma Davis", "Consumer", "UK"]
]

# Create DataFrame
customer = pd.DataFrame(data, columns=columns)

print(customer)
