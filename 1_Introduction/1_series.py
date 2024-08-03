import pandas as pd

a=[1,7,2]
b={"Maths":99, "Science":87, "English":100, "Social Studies":94}


# Series is like a column of a database
# Labels can be used to access elements from a series, like a key-value pair

ser1 = pd.Series(a, index = ["x", "y", 'z']) # Making series from a list with labels "x", "y" and "z"
ser2 = pd.Series(b) # Making series from a dictionary

print(ser1, "\n\n")
print(ser1['z'], "\n\n")
print(ser2, "\n\n")
print(ser2["Maths"])