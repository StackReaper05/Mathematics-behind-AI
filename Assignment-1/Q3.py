import pandas as pd

df = pd.read_csv("iris.csv")

print("First five records:")
print(df.head())

print("\nLast five records:")
print(df.tail())

print("\nNumber of rows and columns:")
print(df.shape)

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nSummary statistics:")
print(df.describe())