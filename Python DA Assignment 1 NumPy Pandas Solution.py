# Python DA Assignment 1: Data Analysis using NumPy and Pandas
# Complete solution based on the supplied assignment PDF.
#
# Required libraries:
#   pip install numpy pandas

import numpy as np
import pandas as pd


# ============================================================
# PART 1: NUMPY ARRAY OPERATIONS
# ============================================================

print("=" * 65)
print("PART 1: NUMPY ARRAY OPERATIONS")
print("=" * 65)

# 1. Create a 1D NumPy array for Week 1
temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])

# 2. Inspect array properties
print("\n1. Week 1 temperatures:")
print(temperatures_w1)
print("Shape:", temperatures_w1.shape)
print("Data type:", temperatures_w1.dtype)
print("Number of elements:", temperatures_w1.size)

# 3. Convert Celsius to Fahrenheit and calculate statistics
temperatures_fahrenheit = (temperatures_w1 * 9 / 5) + 32
print("\n2. Week 1 temperatures in Fahrenheit:")
print(temperatures_fahrenheit)
print("Maximum temperature (Celsius):", np.max(temperatures_w1))
print("Minimum temperature (Celsius):", np.min(temperatures_w1))
print("Mean temperature (Celsius):", np.mean(temperatures_w1))

# 4. Slicing and indexing
print("\n3. First three days:", temperatures_w1[:3])
print("Weekend temperatures (last two days):", temperatures_w1[-2:])
print("Middle three days:", temperatures_w1[2:5])

# 5. Create a 2D array for two weeks
temperatures = np.array([
    [22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9],
    [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1]
])

# 6. Inspect and slice the 2D array
print("\n4. Two-week temperature array:")
print(temperatures)
print("Shape:", temperatures.shape)
print("Data type:", temperatures.dtype)
print("Total number of elements:", temperatures.size)
print("Week 1:", temperatures[0])
print("Week 2:", temperatures[1])
print("Week 1 weekend:", temperatures[0, -2:])
print("Week 2 weekend:", temperatures[1, -2:])


# ============================================================
# PART 2: PANDAS SERIES
# ============================================================

print("\n" + "=" * 65)
print("PART 2: PANDAS SERIES")
print("=" * 65)

# 1. Create a Series with custom index labels
marks = pd.Series(
    [95, 92, 89, 85, 80],
    index=["Rank1", "Rank2", "Rank3", "Rank4", "Rank5"],
    name="Marks"
)
print("\n1. Original marks Series:")
print(marks)

# 2. Indexing and slicing
print("\n2. Mark of 1st rank student using integer position:")
print(marks.iloc[0])

print("\nMarks of top 3 ranks using loc:")
print(marks.loc[["Rank1", "Rank2", "Rank3"]])

print("\nMark of 3rd rank student using iloc:")
print(marks.iloc[2])

print("\nRanks with marks greater than 90:")
print(marks[marks > 90])

# 3. Manipulating Series
marks.loc["Rank1"] = 100
print("\n3. After modifying Rank1 mark to 100:")
print(marks)

marks = marks.drop("Rank5")
print("\nAfter removing Rank5:")
print(marks)

cgpa = marks / 10
print("\nCGPA (marks divided by 10):")
print(cgpa)


# ============================================================
# PART 3: PANDAS DATAFRAME
# ============================================================

print("\n" + "=" * 65)
print("PART 3: PANDAS DATAFRAME")
print("=" * 65)

# 1. Create the transactions DataFrame using the assignment data
transactions = pd.DataFrame({
    "TransactionID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "ProductCategory": [
        "Electronics", "Clothing", "Electronics", "Furniture", "Clothing",
        "Electronics", "Furniture", "Clothing", "Furniture", "Electronics"
    ],
    "Region": [
        "North", "South", "North", "East", "West",
        "North", "East", "West", "South", "North"
    ],
    "Amount": [200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
})

print("\n1. Transactions DataFrame:")
print(transactions)

# 2. Data exploration
print("\n2. First five rows (head):")
print(transactions.head())

print("\nLast five rows (tail):")
print(transactions.tail())

print("\nShape:")
print(transactions.shape)

print("\nColumn names:")
print(transactions.columns)

print("\nData types:")
print(transactions.dtypes)

print("\nBasic information:")
transactions.info()

print("\nProductCategory and Amount columns:")
print(transactions[["ProductCategory", "Amount"]])

print("\nLast three columns using iloc:")
print(transactions.iloc[:, -3:])

print("\nRows where Region is North and Amount is greater than 200:")
print(transactions[(transactions["Region"] == "North") &
                   (transactions["Amount"] > 200)])

print("\nValue counts for ProductCategory:")
print(transactions["ProductCategory"].value_counts())

print("\nUnique Region values:")
print(transactions["Region"].unique())

print("\nMean Amount grouped by Region:")
print(transactions.groupby("Region")["Amount"].mean())

# 3. Manipulating the DataFrame
transactions.loc[transactions["TransactionID"] == 102, "Amount"] = 165
print("\n3. After updating Amount for TransactionID 102 to 165:")
print(transactions)

transactions["Discount"] = transactions["Amount"] * 0.10
print("\nAfter adding Discount (10% of Amount):")
print(transactions)

transactions = transactions[transactions["TransactionID"] != 109].copy()
print("\nAfter removing TransactionID 109:")
print(transactions)

transactions = transactions.drop(columns=["Discount"])
print("\nAfter deleting the Discount column:")
print(transactions)

print("\nAssignment completed.")
