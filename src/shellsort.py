import time
import random
import tracemalloc

def shellsort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def trace_shellsort():
    print("--- Shellsort Trace ---")
    data = [48, 12, 79, 35, 91, 24, 60, 17]
    print(f"Initial: {data}")
    sorted_data = shellsort(data.copy())
    print(f"Sorted:  {sorted_data}\n")

def benchmark():
    n = 1000
    data = [random.randint(1, 10000) for _ in range(n)]
    tracemalloc.start()
    start = time.perf_counter()
    shellsort(data)
    end = time.perf_counter()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Shellsort Benchmark (n={n}):")
    print(f"Time: {end - start:.6f} seconds")
    print(f"Peak Memory: {peak / 1024:.2f} KB\n")

if __name__ == "__main__":
    trace_shellsort()
    benchmark()
