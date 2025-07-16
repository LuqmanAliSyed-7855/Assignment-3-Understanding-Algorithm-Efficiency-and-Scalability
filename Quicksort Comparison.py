"""Implements two sorting algorithms, Randomized Quicksort and Deterministic Quicksort using the first element as the pivot. 
Each algorithm is tested on arrays with varying characteristics including random, sorted, reverse-sorted, and repeated elements. 
The code measures execution time for each case using the time module and compares performance across three 
input sizes. Randomized Quicksort selects a pivot randomly to improve partition balance, while Deterministic Quicksort 
always selects the first element, risking unbalanced partitions. The benchmarking function generates and 
tests each array type, printing execution times to evaluate efficiency."""


import random
import time
import sys

# Optional: Increase recursion limit for large inputs
sys.setrecursionlimit(10000)

# Randomized Quicksort Implementation
def randomized_quicksort(arr):
    def quicksort(arr, low, high):
        if low < high:
            pivot_index = randomized_partition(arr, low, high)
            if pivot_index > low:
                quicksort(arr, low, pivot_index - 1)
            if pivot_index < high:
                quicksort(arr, pivot_index + 1, high)

    def randomized_partition(arr, low, high):
        pivot_index = random.randint(low, high)
        arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
        return partition(arr, low, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    if arr is not None and len(arr) > 1:
        quicksort(arr, 0, len(arr) - 1)

# Deterministic Quicksort Implementation 
def deterministic_quicksort(arr):
    def quicksort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            if pivot_index > low:
                quicksort(arr, low, pivot_index - 1)
            if pivot_index < high:
                quicksort(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        pivot = arr[low]
        i = low + 1
        for j in range(low + 1, high + 1):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[low], arr[i - 1] = arr[i - 1], arr[low]
        return i - 1

    if arr is not None and len(arr) > 1:
        quicksort(arr, 0, len(arr) - 1)

# Benchmarking Function
def benchmark_sorting_algorithms():
    input_sizes = [100, 500, 1000]  # Choose sizes suitable for your system

    for size in input_sizes:
        print(f"\nInput Size: {size}")

        # Randomly generated array
        random_array = [random.randint(1, 10000) for _ in range(size)]
        arr1 = random_array[:]
        arr2 = random_array[:]

        start = time.time()
        randomized_quicksort(arr1)
        print(f"Randomized Quicksort - Random array: {time.time() - start:.6f} sec")

        start = time.time()
        deterministic_quicksort(arr2)
        print(f"Deterministic Quicksort - Random array: {time.time() - start:.6f} sec")

        # Already sorted array
        sorted_array = list(range(size))
        arr1 = sorted_array[:]
        arr2 = sorted_array[:]

        start = time.time()
        randomized_quicksort(arr1)
        print(f"Randomized Quicksort - Sorted array: {time.time() - start:.6f} sec")

        start = time.time()
        deterministic_quicksort(arr2)
        print(f"Deterministic Quicksort - Sorted array: {time.time() - start:.6f} sec")

        # Reverse sorted array
        reverse_array = list(range(size, 0, -1))
        arr1 = reverse_array[:]
        arr2 = reverse_array[:]

        start = time.time()
        randomized_quicksort(arr1)
        print(f"Randomized Quicksort - Reverse array: {time.time() - start:.6f} sec")

        start = time.time()
        deterministic_quicksort(arr2)
        print(f"Deterministic Quicksort - Reverse array: {time.time() - start:.6f} sec")

        # Array with repeated elements
        repeated_array = [5] * size
        arr1 = repeated_array[:]
        arr2 = repeated_array[:]

        start = time.time()
        randomized_quicksort(arr1)
        print(f"Randomized Quicksort - Repeated elements: {time.time() - start:.6f} sec")

        start = time.time()
        deterministic_quicksort(arr2)
        print(f"Deterministic Quicksort - Repeated elements: {time.time() - start:.6f} sec")

# Call the benchmark function to generate output
benchmark_sorting_algorithms()
