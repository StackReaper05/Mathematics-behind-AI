import matplotlib as pyplot
import pandas as pd


# Line Plot
plt.plot(df["sepal_length"])
plt.title("Line Plot of Sepal Length")
plt.xlabel("Index")
plt.ylabel("Sepal Length")
plt.show()


# Bar Chart
avg = df.groupby("species")["sepal_length"].mean()

plt.bar(avg.index, avg.values)
plt.title("Average Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Sepal Length")
plt.show()


# Histogram
plt.hist(df["sepal_length"], bins=10)
plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()


# Scatter Plot
plt.scatter(df["sepal_length"], df["petal_length"])
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()


# Box Plot
plt.boxplot(df["sepal_length"])
plt.title("Box Plot of Sepal Length")
plt.ylabel("Sepal Length")
plt.show()