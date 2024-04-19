import numpy as np

my_arr = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
my_idxs = [[0, 1], [2]]

norms = [np.linalg.norm(my_arr[:, idx], axis=1) for idx in my_idxs]
result = np.column_stack(norms)

print(result)