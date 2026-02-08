# Group a DataFrame by the 'Department' column and calculate the
# average salary in each department.

avg_salary = df.groupby('Department')['Salary'].mean()
print(avg_salary)
