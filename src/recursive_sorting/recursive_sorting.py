# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(left_array, right_array):
    total_elements_in_both_lists = len(left_array) + len(right_array)
    merged_arr = [0] * total_elements_in_both_lists
    # TO-DO
    left_pointer_index = 0
    right_pointer_index = 0
    for item in range(0, total_elements_in_both_lists):
        # checking to see if there are any remaining elements in left_array
        # if not then move on to right_array
        # so basically if we are finished merging left_array the only elements left to merge is in right_array
        if left_pointer_index >= len(left_array):
            merged_arr[item] = right_array[right_pointer_index]
            # increment the pointer index since this item is now in the merged list
            right_pointer_index += 1
        # checking to see if there are any remaining elements in right_array
        elif right_pointer_index >= len(right_array):
            merged_arr[item] = left_array[left_pointer_index]
            # increment the pointer index since this item is now in the merged list
            left_pointer_index += 1
        elif left_array[left_pointer_index] < right_array[right_pointer_index]:
            merged_arr[item] = left_array[left_pointer_index]
            # increment the pointer index since this item is now in the merged list
            left_pointer_index += 1
        else:
            merged_arr[item] = right_array[right_pointer_index]
            # increment the pointer index since this item is now in the merged list
            right_pointer_index += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # 1. While your data set contains more than one item, split it in half
    if len(arr) > 1:
        mid_point = (len(arr) // 2)
        left_half = arr[:mid_point]
        right_half = arr[mid_point:]
        # 2. Once you have gotten down to a single element, you have also *sorted* that element
        # (a single element cannot be "out of order")
        left_array = merge_sort(left_half)
        right_array = merge_sort(right_half)
        # 3. Start merging your single lists of one element together into larger, sorted sets
        arr = merge(left_array, right_array)
        # 4. Repeat step 3 until the entire data set has been reassembled

    return arr


# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr


# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):

#     return arr
