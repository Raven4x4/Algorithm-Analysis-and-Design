import os
import time
import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False
        if already_sorted:
            break
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:]
    result += right[right_index:]
    return result


def measure_sort_performance(sort_func, data):
    start_time = time.time()
    sort_func(data.copy())  # Use a copy to prevent in-place sorting from affecting other tests
    end_time = time.time()
    return (end_time - start_time) * 1000  # Convert to milliseconds

def create_sorted_data(size):
    return list(range(size))

def create_random_data(size):
    return [random.randint(0, 1000) for _ in range(size)]

def create_reversed_data(size):
    return list(range(size, 0, -1))

def get_next_attempt_number():
    attempt = 1
    while os.path.exists(f'sorting_algorithm_performance_attempt_{attempt}.txt'):
        attempt += 1
    return attempt

def main():
    data_sizes = [2000, 4000, 6000, 8000, 10_000]
    datasets = {
        "Sorted": create_sorted_data,
        "Random": create_random_data,
        "Reversed": create_reversed_data
    }
    algorithms = [("Merge Sort", merge_sort), ("Quick Sort", quick_sort), ("Bubble Sort", bubble_sort)]

    attempt_number = get_next_attempt_number()
    filename = f'sorting_algorithm_performance_attempt_{attempt_number}.txt'

    with open(filename, 'w') as file:
        file.write(f"Sorting Algorithm Performance: Attempt #{attempt_number}\n")
        for name, algorithm in algorithms:
            file.write(f"\n{name} Results:\n")
            for size in data_sizes:
                file.write(f"  Input Size: {size}\n")
                for dataset_name, dataset_func in datasets.items():
                    data = dataset_func(size)
                    time_taken = measure_sort_performance(algorithm, data)
                    file.write(f"    Dataset: {dataset_name} - {time_taken:.3f} ms\n")

if __name__ == "__main__":
    main()