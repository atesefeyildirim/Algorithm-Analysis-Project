import time
import random
from quicksort import quicksort
from shellsort import shellsort

def run_benchmarks():
    sizes = [1000, 2500, 5000, 10000]
    print(f"{'Size (n)':<10} | {'Quicksort (s)':<15} | {'Shellsort (s)':<15}")
    print("-" * 45)
    
    for n in sizes:
        data = [random.randint(1, 100000) for _ in range(n)]
        
        # Test Quicksort
        data_quick = data.copy()
        start = time.perf_counter()
        quicksort(data_quick)
        quick_time = time.perf_counter() - start
        
        # Test Shellsort
        data_shell = data.copy()
        start = time.perf_counter()
        shellsort(data_shell)
        shell_time = time.perf_counter() - start
        
        print(f"{n:<10} | {quick_time:<15.6f} | {shell_time:<15.6f}")

if __name__ == "__main__":
    print("--- Head-to-Head Benchmark ---")
    run_benchmarks()
