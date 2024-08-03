import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("4_Plotting\data.csv")

# Finally, we can plot DataFrames in diagrams and visualize this data. This helps a lot in Data Analysis.
# To create a Line Graph, simply use plot() method

df.plot()

plt.show()