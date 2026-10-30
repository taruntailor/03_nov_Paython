import pandas as pd

# Define columns
columns = ["productid", "category", "sub_category", "productname"]

# Insert sample data
data = [
    ["P101", "Furniture", "Chairs", "Office Chair"],
    ["P102", "Technology", "Phones", "Smartphone X"],
    ["P103", "Office Supplies", "Paper", "A4 Paper Pack"],
    ["P104", "Furniture", "Tables", "Wooden Desk"]
]

# Create DataFrame
product = pd.DataFrame(data, columns=columns)

print(product)
