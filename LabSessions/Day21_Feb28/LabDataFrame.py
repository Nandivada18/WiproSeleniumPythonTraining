#1. Create a DataFrame containing missing (None/NaN) values.
import pandas as pd
import numpy as np

data = {
    "Name": ["Prasad", "Ravi", "Sita", "Anu", "Kiran"],
    "Age": [28, None, 24, 30, None],
    "Salary": [50000, 40000, None, 60000, 45000],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "City": ["Bangalore", "Hyderabad", "Bangalore", "Chennai", None]
}

df = pd.DataFrame(data)
print(df)

#2. Detect missing values using appropriate function
print(df.isnull())

#3. Replace missing values with 0.
df_filled = df.fillna(0)
print(df_filled)

#4. Drop rows containing missing values.
df_dropped = df.dropna()
print(df_dropped)

#5. Sort the DataFrame by Age in ascending order.
sorted_age = df.sort_values(by="Age", ascending=True)
print(sorted_age)

#6. Sort the DataFrame by Salary in descending order.
sorted_salary = df.sort_values(by="Salary", ascending=False)
print(sorted_salary)

#7. Perform groupby on Department and find average Salary per department.
avg_salary = df.groupby("Department")["Salary"].mean()
print(avg_salary)

#8. Find total Salary per department using groupby.
total_salary = df.groupby("Department")["Salary"].sum()
print(total_salary)

#9. Filter employees where Age > 25 AND City = 'Bangalore'.
filtered = df[(df["Age"] > 25) & (df["City"] == "Bangalore")]
print(filtered)

#10. Create a new column 'Tax' which is 10% of Salary using apply().
df["Tax"] = df["Salary"].apply(lambda x: x * 0.10 if pd.notnull(x) else x)
print(df)