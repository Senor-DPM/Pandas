import pandas as pd

# head(x) method returns x number of rows from the top of the DataFrame along with the headings.
# Default value of x is 5

df = pd.read_csv("1_Introduction\data.csv")
print(df.head(10),"\n")

# tail(x) method returns x number of rows from the bottom of the DataFrame along with the headings.
# Default value of x is 5
print(df.tail(10),"\n")

# info() method gives you more information about your data set.
print(df.info())