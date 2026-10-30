import pandas as pd

columns = ["orderid", "productid", "sales", "quantity", "discount", "profit"]

data = [
    [1001, "P101", 250.00, 2, 0.10, 40.00],
    [1002, "P102", 500.00, 5, 0.15, 75.00],
    [1003, "P103", 150.00, 1, 0.05, 20.00],
    [1004, "P104", 300.00, 3, 0.20, 50.00]
]

orderdetails = pd.DataFrame(data, columns=columns)

# print(orderdetails)
 

# statment ways total sale


total_sales = orderdetails['sales'].sum()
print("Total Sales:", total_sales)




# counsumer ways min and max profit

orders = pd.read_csv("orders.csv")
orderdetails = pd.read_csv("orderdetails.csv")

merged_df = pd.merge(orderdetails, orders[['orderid','customerid']], on='orderid')

customer = pd.read_csv("customer.csv")
merged_df = pd.merge(merged_df, customer[['customerid','customername']], on='customerid')

print(merged_df)
