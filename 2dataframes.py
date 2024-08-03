import pandas as pd

data = {
    "Actual Names" : ["Aniket", "Dhruv M", "Mragank", "Roshni", "Soubhagya"],
    "Nicknames" : ["Raniket", "Kaptaan", "Mrigu", "Pikachu", "Sobby"],
    "Age" : [83, 18, 19, 18, 18]
}

# A dataframe is a 2D data structure.
# If a series is a column of a table, then a dataframe is an entire table

df1 = pd.DataFrame(data) # Creating a data frame.

print(df1,"\n")

# loc attribute helps us locate one or multiple rows of a table. It returns a series

print(df1.loc[0],"\n")
print(df1.loc[[1,2]],"\n")

# With index argument, you can name your own rows

df2 = pd.DataFrame(data, index = ["name1",'name2','name3','name4','name5'])

print(df2,"\n")
print(df2.loc["name2"])