#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests

    # base case 1
    if index >= len(array):     # we searched through the entire list and never found the item
        return None

    # base case 2
    if array[index] == item:     # we found the index, return it
        return index

    # recursive case
    else:
        return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # array.sort()
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    # [5, 6, 7, 10, 12] target = 6
    #steps:
    # binary search only works if the array is sorted (array.sort())
    # start at the middle of the array (len(array)/2)
    # check if the middle item is the target, if so return 
    # compare the target to the item at the middle
    # if the target is less than the item at the middle, then we can ignore the entire right half of the array (7 is greater than 6)
    # if the target is greater we ignore the left half
    # repeat util target is found or we looked through everything

    array.sort()

    left_index = 0      # first index
    right_index = len(array) - 1    # last index

    while left_index <= right_index:
        mid_index = (right_index + left_index) // 2        # last index - first index // 2 == middle index, double // returns an integer, / returns a float
        if array[mid_index] == item:    # if the item at the mid_index is equal to the item
            print("Found!")
            return mid_index    # return the index
        # if item < array[mid_index] ignore right
        elif item < array[mid_index]:
            right_index = mid_index - 1     # reassign the right index
        # if item > array[mid_index] ignore left 
        elif item > array[mid_index]:
            left_index = mid_index + 1
    return None



def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

    array.sort() # must sort the array for a binary search 
    mid_index = (right + left) // 2 

    # base case
    if right < left:    # if there are no more items to look through, the item was not found
        return None
    elif array[mid_index] == item:   
            print("Found!")
            return mid_index 

    # recursive case 1
    if array[mid_index] > item:
        return binary_search_recursive(array, item, left, mid_index - 1)
    # recursive case 2    
    else:
        return binary_search_recursive(array, item, mid_index + 1, right)


# print(binary_search_iterative([5, 12, 6, 10, 7], 6))    # 1
# print(linear_search_iterative([12, 32, 11, 4, 5, 9], 9))      # 5
# print(linear_search_iterative([12, 32, 11, 4, 5, 9], 33))     # None