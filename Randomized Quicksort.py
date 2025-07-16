"""Defines the Randomized Quicksort algorithm, which improves performance by selecting a pivot element 
randomly from the subarray being sorted. A helper function handles partitioning by placing elements 
smaller than the pivot to the left and larger ones to the right. The algorithm is applied recursively 
to the subarrays on both sides of the pivot. The implementation also checks for edge cases such as 
empty arrays, repeated elements, and already sorted data to ensure robustness."""

import random

def randomized_quicksort(arr):
    # Function to perform the quicksort recursively
    def quicksort(arr, low, high):
        # Base condition: proceed only if the subarray has more than one element
        if low < high:
            # Get a pivot index by choosing a random pivot and partitioning
            pivot_index = randomized_partition(arr, low, high)
            # Recursively apply quicksort to the left of pivot
            quicksort(arr, low, pivot_index - 1)
            # Recursively apply quicksort to the right of pivot
            quicksort(arr, pivot_index + 1, high)

    # Function to select pivot randomly and call the partition function
    def randomized_partition(arr, low, high):
        # Select a pivot index randomly within the current subarray
        pivot_index = random.randint(low, high)
        # Swap the randomly selected pivot with the last element
        arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
        # Partition the array using the chosen pivot
        return partition(arr, low, high)

    # Standard partition function to place pivot at correct position
    def partition(arr, low, high):
        pivot = arr[high]  # Pivot is the last element after swap
        i = low - 1  # Index of smaller element
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                # Swap elements to maintain the partition property
                arr[i], arr[j] = arr[j], arr[i]
        # Place pivot in the correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    # Handle edge cases like empty or single-element array
    if arr is not None and len(arr) > 1:
        quicksort(arr, 0, len(arr) - 1)

# Example usage
example_array = [5, 3, 8, 5, 2, 1, 10, 7, 6]  # Includes repeated and unsorted elements
randomized_quicksort(example_array)
print("Sorted array:", example_array)
