import pandas as pd

df = pd.read_csv("3_Correlations\data.csv")

# Correlation between two columns is defined by how related/proportional two columns are with each other.
# The correlation coefficient ranges from -1 to 1
# 1 is a perfect correlation that means that if we increase the value of one column's data, the other will increase too.
# 0.9 is also a good correlation. If one value is increased, the other will probably increase too.
# -0.9 is good correlation, but in a different way. If one value is increased, the other will probably decrease.
# 0.1 is a bad correlation. If one value is increased, it does not mean that the other value will increase too.
# Typically a correlation should more than 6 or less than -6 to be a good correlation.

# To calculate correlation, we use corr() in Pandas

print(df.corr())