import pandas as pd

# head(x) method returns x number of rows from the top of the DataFrame along with the headings.

df = pd.read_csv("data.csv")
print(df.head(5),"\n")

# tail(x) method returns x number of rows from the bottom of the DataFrame along with the headings.
print(df.tail(5),"\n")

# info() method gives you more information about your data set.
print(df.info())