# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # Algorithm
    # Start with current index = 0
    # For all indices EXCEPT the last index:
    # a. Loop through elements on right-hand-side of current index and find the smallest element
    # b. Swap the element at current index with the smallest element found in above loop
    for i in range(0, len(arr) - 1):
        # Start with current index = 0
        min_index = i
        # For all indices EXCEPT the last index:
        for j in range(i+1, len(arr)):
            # a. Loop through elements on right-hand-side of current index and find the smallest element
            if arr[j] < arr[min_index]:
                # b. Swap the element at current index with the smallest element found in above loop
                temp = arr[min_index]
                arr[min_index] = arr[j]
                arr[j] = temp
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Loop through your array
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    # Compare each element to its neighbor
    # If elements in wrong position (relative to each other, swap them)
    # If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
