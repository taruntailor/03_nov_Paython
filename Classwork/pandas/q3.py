import pandas as pd

# df = pd.read_csv("C:/Users/pc/sample.csv")
# print (df)

# prodect name ways total quantity sale

orderdetails = pd.DataFrame({
    "orderid": [1001,1002,1003,1004,1001],
    "productid": ["P101","P102","P103","P104","P101"],
    "sales": [250,500,150,300,125],
    "quantity": [2,5,1,3,1],
    "discount": [0.1,0.15,0.05,0.2,0.1],
    "profit": [40,75,20,50,20]
})

product = pd.DataFrame({
    "productid": ["P101","P102","P103","P104"],
    "category": ["Furniture","Technology","Office Supplies","Furniture"],
    "sub_category": ["Chairs","Phones","Paper","Tables"],
    "productname": ["Office Chair","Smartphone X","A4 Paper Pack","Wooden Desk"]
})

# Merge orderdetails with product on productid
merged_df = pd.merge(orderdetails, product, on="productid")

# Group by productname and sum quantity
total_quantity_by_product = merged_df.groupby("productname")["quantity"].sum().reset_index()

print(total_quantity_by_product)



