import numpy as np
import pandas as pd

arr1 = [[1, 2, 3], [3, 4, 5]]
arr = np.array(arr1)
print(arr.std())

df = pd.DataFrame({"Hello": [1, 2, 3], "World": [4, 5, 6]})
print(df.loc[0, "Hello"])