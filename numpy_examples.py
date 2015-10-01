# Importing module
import numpy as np


def defining_arrays():
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)

    narr = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
    print(narr)

    new_array = np.append(narr, [[9, 10, 11]], axis=0)
    print(new_array)


if __name__ == "__main__":
    defining_arrays()
