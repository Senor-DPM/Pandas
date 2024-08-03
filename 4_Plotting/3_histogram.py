import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("4_Plotting\data.csv")

# Histograms are graphs that are used to calculate the frequency beteen each interval.
# They require only one column, and use intervals like 15-20, 20-25, etc.

df["Duration"].plot(kind = "hist")

# This graph shows that over 100 workouts lasted between 45-70 minutes

plt.show()