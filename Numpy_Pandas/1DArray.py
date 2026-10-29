"""
Apply NumPy to create a one-dimensional array containing the numbers from 1 to 10, perform slicing operations, 
compute statistical measures (sum, mean, maximum, and minimum), and apply broadcasting to modify the array elements.
"""

import numpy as np

#array using a list
def array_from_list():
    return np.array([1,2,3,4,5,6,7,8,9,10])

def array_from_range():
    return np.arange(1,11)

def describe_array(array):
    print ("Array               :   ", array)
    print ("Array size          :   ", array.size)
    print ("Data Type           :   ", array.dtype)
    print ("No. of Dimension    :   ", array.ndim)
    print ("Shape               :   ", array.shape)

if __name__ == "__main__":

    arr1 = array_from_list()
    print("Array created with np.array([1, 2, ..., 10]):", "\n")
    describe_array(arr1)

    arr2 = array_from_range()
    print("Array created with np.arange(1, 11):")
    describe_array(arr2)

#checking if arrays are equal
    print()
    print("both arrays equal:", np.array_equal(arr1, arr2))

#Vector operations
    print()
    print("vectorized operations:")
    print(f"arr1 * 2       : {arr1 * 2}")
    print(f"arr1 + 100     : {arr1 + 100}")
    print(f"sum(arr1)      : {arr1.sum()}")
    print(f"mean(arr1)     : {arr1.mean()}")

#slicing and indexing
    print()
    print("indexing and slicing:")
    print(f"First element  : {arr1[0]}")
    print(f"Last element   : {arr1[-1]}")
    print(f"First 5 values : {arr1[:5]}")
    print(f"Every other    : {arr1[::2]}")
