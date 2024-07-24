import pandas as pd

# Sample DataFrame df1
df1 = pd.DataFrame({
    'Group': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40, 50, 60]
})

# Sample DataFrame df2 with the same groups
df2 = pd.DataFrame({
    'Group': ['A', 'B', 'A', 'B', 'A', 'B'],
    'OtherValue': [1, 2, 3, 4, 5, 6]
})

# Compute the mean value for each group in df1
mean_values = df1.groupby('Group')['Value'].mean()

# Map the mean values to df2 based on the group
df2['MeanValue'] = df2['Group'].map(mean_values)

print(df2)
