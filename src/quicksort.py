import time
import random
import tracemalloc

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def trace_quicksort():
    print("--- Quicksort Trace ---")
    data = [48, 12, 79, 35, 91, 24, 60, 17]
    print(f"Initial: {data}")
    sorted_data = quicksort(data)
    print(f"Sorted:  {sorted_data}\n")

def benchmark():
    n = 1000
    data = [random.randint(1, 10000) for _ in range(n)]
    tracemalloc.start()
    start = time.perf_counter()
    quicksort(data)
    end = time.perf_counter()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Quicksort Benchmark (n={n}):")
    print(f"Time: {end - start:.6f} seconds")
    print(f"Peak Memory: {peak / 1024:.2f} KB\n")

if __name__ == "__main__":
    trace_quicksort()
    benchmark()
