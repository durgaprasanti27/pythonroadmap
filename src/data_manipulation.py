# NumPy & Pandas Data Manipulation (Phase 2)

## NumPy: Numerical Computing
```python
import numpy as np

# Arrays
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Shape:", arr.shape)
print("Dtype:", arr.dtype)

# Basic operations
arr2 = arr * 2
print("Doubled:", arr2)

# Indexing & slicing
print("First element:", arr[0])
print("Last 3:", arr[-3:])

# Pandas: Data Analysis
import pandas as pd

# Series
s = pd.Series([10, 20, 30, 40], name='scores')
print("Series:", s)
print("Index:", s.index)

# DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'math': [85, 92, 78],
    'science': [88, 90, 81]
})
print("DataFrame:\n", df)
```

## Key Operations
- Loading CSV: `pd.read_csv('data.csv')`
- Filtering: `df[df['math'] > 80]`
- Grouping: `df.groupby('name').mean()`
- Merging: `pd.merge(df1, df2, on='id')`

## Exercises
1. Create a DataFrame tracking study hours vs. scores
2. Calculate average scores per subject
3. Filter to show only students studying > 15 hours/week

**Goal**: Manipulate data efficiently for AI/ML workflows