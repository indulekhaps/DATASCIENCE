import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
iris = pd.read_csv("iris.csv")

# Plot the distribution of Sepal Length
sns.displot(iris["sepal_length"], kde=True, rug=True)

plt.title("\nDistribution of Sepal Length")
plt.xlabel("\nSepal Length (cm)")
plt.ylabel("\nDensity")
plt.show()

# Plot the histogram of Petal Width
sns.histplot(iris['petal_width'], kde=True, bins=20)

plt.title("\nHistogram of Petal Width")
plt.xlabel("\nPetal Width (cm)")
plt.ylabel("\nFrequency")
plt.show()

# Plot Sepal Length vs Sepal Width
sns.relplot(x="sepal_length", y="sepal_width", data=iris, hue="species", style="species")
plt.title("\nSepal Length vs Sepal Width")

plt.xlabel("\nSepal Length (cm)")

plt.ylabel("\nSepal Width (cm)")
plt.show()