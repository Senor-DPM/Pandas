import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("4_Plotting\data.csv")

# To create a scatter graph, use the "kind = " attribute and select "scatter".
# Specify the x-axis and y-axis using the columns of the table.
# A good correlation's scatter graph will look ordered, with each set of points following a certain trend.

df.plot(kind = "scatter", x = "Duration", y = "Calories")

# A bad correlation's scatter graph will look chaotic with no rhyme or rhythm at all.

df.plot(kind = "scatter", x = "Duration", y = "Maxpulse")

plt.show()