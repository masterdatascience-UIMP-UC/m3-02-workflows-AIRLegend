import pandas as pd
import matplotlib.pyplot as plt
import sys

dataset = pd.read_csv(sys.argv[1])

dataset.head(17).plot.bar(x='location', y='alcohol')

plt.show()
