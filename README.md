# Comparative Analysis of Quicksort and Shellsort

**Course:** 2019G3009 Algorithm Analysis  
**Department:** Software Engineering (English)  
**Institution:** Istanbul Esenyurt University  
**Lecturer:** Dr. Coşkun Şahin  
**Student:** ATEŞ EFE YILDIRIM (Student ID: 2322190021)  
**Submission:** Shared with `drcoskuns` as collaborator via GitHub  

## 📌 Project Overview
This repository contains the Midterm Project for the Algorithm Analysis course. The project delivers an in-depth theoretical and empirical comparison of two fundamental sorting algorithms:

1. **Quicksort** — A highly efficient, divide-and-conquer, in-place, non-stable sorting algorithm. It generally exhibits $O(n \log n)$ average-case time complexity but can degrade to $O(n^2)$ in the worst case without proper pivot selection.
2. **Shellsort** — An in-place, non-stable comparison sort that generalizes insertion sort by allowing the exchange of items that are far apart. Its time complexity heavily depends on the gap sequence used, typically ranging from $O(n \log^2 n)$ to $O(n^{1.5})$.

Both algorithms are implemented from scratch in Python, accompanied by step-by-step trace routines on identical test datasets, comprehensive asymptotic proofs, and empirical profiling across CPU runtime, memory allocation, and comparison counts.

## 📁 Repository Structure
```text
SortingAlgorithms_Quicksort_Shellsort/
├── README.md              # Project documentation and execution guide
├── REPORT.md              # Comprehensive academic midterm report
└── src/
    ├── quicksort.py       # Quicksort implementation, trace, and benchmarks
    ├── shellsort.py       # Shellsort implementation, trace, and benchmarks
    └── benchmark.py       # Comparative head-to-head benchmarking suite
