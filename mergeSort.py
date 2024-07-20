import math
import random
import time


# this refers to the input array by reference, so it will modify the original array from wherever you
# originally called merge_sort
def merge_sort(input_array):
    input_array_size = len(input_array)
    midpoint = math.floor(input_array_size / 2)

    # if we're down to one element, just return the whole thing
    if midpoint == 0:
        return input_array

    # otherwise, split into two and do recursively sort
    # (this makes new arrays - modifying them won't modify input_array)
    sub_array_1 = merge_sort(input_array[:midpoint])
    sub_array_2 = merge_sort(input_array[midpoint:])

    # now merge the two sorted lists and return the result
    array_pos = 0
    array_1_pos = 0
    array_2_pos = 0
    while True:

        # if we're off the end of array_1...
        if array_1_pos == midpoint:
            # just append the rest of array_2
            for k in range(array_2_pos, input_array_size - midpoint):
                input_array[array_pos] = sub_array_2[k]
                array_pos += 1
            break

        # if we're off the end of array 2...
        if array_2_pos == input_array_size - midpoint:
            # append the rest of array 1
            for k in range(array_1_pos, midpoint):
                input_array[array_pos] = sub_array_1[k]
                array_pos += 1
            break

        # otherwise, compare the leftmost two elements of each, and append the smaller to the combined array
        if sub_array_1[array_1_pos] < sub_array_2[array_2_pos]:
            input_array[array_pos] = sub_array_1[array_1_pos]
            array_1_pos += 1
        else:
            input_array[array_pos] = sub_array_2[array_2_pos]
            array_2_pos += 1
        array_pos += 1

    return input_array


show_results = False
array_size = 60000
orig_array = []
for i in range(array_size):
    orig_array.append(random.randint(1, 75))

start_time_ms = time.time() * 1000

if show_results:
    # do the procedures on a copy of the original array, since Python passes lists by reference.
    # We want to retain the original so we can compare them
    sorted_array = merge_sort(orig_array.copy())

    elapsed_time = math.floor(time.time() * 1000 - start_time_ms)
    print("Success! Sorted array of size " + f"{array_size:,}" + " in " + f"{elapsed_time:,}" + " milliseconds")

    print("\nOriginal array (length " + str(len(orig_array)) + "):")
    print(orig_array)

    print("\nSorted array (length " + str(len(sorted_array)) + "):")
    print(sorted_array)

    # one by one, search for elements from the original array in the sorted array, then
    # remove them from the sorted array
    for i in range(len(orig_array)):
        to_find = orig_array[i]
        found_index = sorted_array.index(to_find)
        sorted_array.pop(found_index)
else:
    merge_sort(orig_array)
    elapsed_time = math.floor(time.time() * 1000 - start_time_ms)
    print("Success! Sorted array of size " + f"{array_size:,}" + " in " + f"{elapsed_time:,}" + " milliseconds")
