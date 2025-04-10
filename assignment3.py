import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [88, 75, 95, 65, 85],
    'Science': [92, 78, 90, 70, 88],
    'English': [85, 72, 94, 60, 90],
    'History': [79, 80, 92, 58, 86]
}

df = pd.DataFrame(data)

# Total and average
df['Total'] = df[['Math', 'Science', 'English', 'History']].sum(axis=1)
df['Average'] = df['Total'] / 4

print(df)
