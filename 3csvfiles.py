import pandas as pd

#You can also read CSV files into a DataFrame.

df = pd.read_csv("data.csv")
print(df.to_string(),"\n") #.to__string() prints the entire file.
#Note : Without to_string, it will only print the first 5 and last 5 rows of the dataframe.

#One can check the default max rows the computer can print from a dataframe using this command :
print(pd.options.display.max_rows,"\n")

#You can change this value to your need by assigning the number of rows needed to the command like this :
pd.options.display.max_rows = 2
print(df)