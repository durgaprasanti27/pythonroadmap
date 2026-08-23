# Data Visualization (Phase 2)

## Matplotlib
```python
import matplotlib.pyplot as plt

# Line plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("Linear Growth")
plt.xlabel("Steps")
plt.ylabel("Value")
plt.show()

# Scatter plot
plt.scatter([1, 2, 3], [2, 3, 5])
plt.title("Data Points")
plt.show()
```

## Seaborn
```python
import seaborn as sns
import pandas as pd

tips = sns.load_dataset("tips")
sns.histplot(tips["total_bill"], kde=True)
plt.title("Bill Distribution")
plt.show()

# Pairplot for multi-dimensional visualization
sns.pairplot(tips, hue="day")
plt.show()
```

## Key Visualizations for AI
- **Learning curves**: Training vs validation loss
- **Confusion matrix**: Classification performance
- **Feature distributions**: Data exploration
- **Correlation heatmap**: Feature relationships

## Exercises
1. Plot training accuracy vs epochs from a mock history
2. Create a confusion matrix heatmap for a simple classifier
3. Visualize feature correlations in a dataset

**Goal**: Communicate AI/ML results effectively