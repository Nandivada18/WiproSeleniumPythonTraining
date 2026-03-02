#dataframe is a 2-dimensioanl labeled data sturcture (rows and columns)
#like an excel Sql tables
import pandas as pd
#create Dataframes from List of Dictionaries

data = [
    {"Name": "ram","Age":25},
    {"Name": "Sam", "Age": 30},
    {"Name": "John", "Age":28}
]

df = pd.DataFrame(data)
print(df)

#create dataframe from dictionary of series
s1 = pd.Series([1,2,3])
s2 = pd.Series([4,5,6])
df = pd.DataFrame({"A":s1,"B":s2})
print(df)

#create Dataframe from Numpy array
import numpy as np
arr = np.array([[1,2],[3,4],[5,6]])
df = pd.DataFrame(arr,columns=["A","B"])
print(df)

#Create data frame using CSV file
#df = pd.read_csv("employees.csv")
#print(df)

#create empty of
df = pd.DataFrame()
print(df)

#create dataframes custom index
data = {
    "Name":["Ram","Sam"],
    "Age": [25,30]
}
df= pd.DataFrame(data, index=["Emp1","Emp2"])
print(df)