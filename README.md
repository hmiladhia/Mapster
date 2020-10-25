# Mapster

Python module to cluster different ( yet similar ) datasets based on  their columns in order to merge them with the same column names. 

```python
from mapster import mapster

cols1 = ['col1', 'id', 'col2']
cols2 = ['col1', 'id']
cols3 = ['col3', 'idx', 'col2']
cols4 = ['col4', 'idr']

result = mapster([cols1, cols2, cols3, cols4])
print(result)
```

