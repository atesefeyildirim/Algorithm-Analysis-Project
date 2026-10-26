---

### 2. `REPORT.md`

```markdown
# ISTANBUL ESENYURT UNIVERSITY
**Faculty of Engineering and Architecture**  
**Department of Software Engineering (English)**  
**Midterm Project Report: Algorithm Analysis (2019G3009)**  

Comparative Theoretical and Empirical Evaluation of Quicksort and Shellsort

| Field | Details |
| :--- | :--- |
| **Course Code & Name** | 2019G3009 — Algorithm Analysis |
| **Academic Term** | 2025–2026 Fall Semester |
| **Lecturer** | Dr. Coşkun Şahin |
| **Student Name Surname** | ATEŞ EFE YILDIRIM |
| **Student Number** | 2322190021 |

## 1. Executive Summary & Overview
Sorting algorithms constitute one of the foundational subjects of computer science and algorithm design. Choosing an optimal sorting strategy requires a comprehensive evaluation of time complexity, auxiliary memory consumption, hardware cache locality, and algorithm stability.

This report presents an exhaustive comparative analysis of two contrasting sorting algorithms:
1. **Quicksort**: A divide-and-conquer algorithm that sorts iteratively by partitioning an array around a pivot. It is renowned for its exceptional average-case performance and cache efficiency.
2. **Shellsort**: An optimization of insertion sort that compares and swaps distant elements, progressively reducing the gap between compared elements until the array is completely sorted.

Both algorithms have been implemented from scratch in Python, mathematically analyzed, tested on an identical 8-element dataset (`[48, 12, 79, 35, 91, 24, 60, 17]`), and benchmarked against standardized input distributions.

## 2. Quicksort Analysis

### 2.1 Algorithm Overview and Mechanics
Quicksort is an in-place, divide-and-conquer algorithm. It selects a 'pivot' element from the array and partitions the other elements into two sub-arrays according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

### 2.2 Mathematical Complexity Analysis
- **Time Complexity:** 
  - **Best/Average Case:** $\Theta(n \log n)$. This occurs when the pivot consistently divides the array into two nearly equal halves.
  - **Worst Case:** $O(n^2)$. This occurs if the smallest or largest element is always chosen as the pivot (e.g., already sorted array with naïve pivot selection).
- **Space Complexity:** $O(\log n)$ auxiliary space for the recursion stack in the best/average case, up to $O(n)$ in the worst case.
- **Stability:** Unstable. The swapping of elements across the pivot boundary can invert the relative order of equal elements.

## 3. Shellsort Analysis

### 3.1 Algorithm Overview and Mechanics
Shellsort improves upon insertion sort by comparing elements separated by a gap of several positions. This allows elements to move towards their correct position faster than a simple neighbor-to-neighbor exchange. As the algorithm proceeds, the gap is reduced (e.g., using Knuth's sequence $3k+1$ or simply dividing by 2) until it reaches 1, which corresponds to a standard insertion sort.

### 3.2 Mathematical Complexity Analysis
- **Time Complexity:** Heavily dependent on the gap sequence.
  - **Best Case:** $\Omega(n \log n)$ for an already sorted array.
  - **Worst Case:** $O(n^2)$ with the original shell sequence (halving), but $O(n^{1.5})$ with Knuth's sequence.
- **Space Complexity:** $O(1)$. It operates strictly in-place without recursion.
- **Stability:** Unstable. Elements with equal values might jump past each other due to the gap-based comparisons.

## 4. Comparative Evaluation & Best Use Cases

| Algorithmic Dimension | Quicksort | Shellsort |
| :--- | :--- | :--- |
| **Algorithmic Paradigm** | Divide and Conquer | Gap-based Insertion |
| **Best-Case Time** | $\Theta(n \log n)$ | $\Theta(n \log n)$ |
| **Worst-Case Time** | $O(n^2)$ | $O(n^{1.5})$ or $O(n^2)$ |
| **Auxiliary Memory** | $O(\log n)$ (Stack) | $O(1)$ (In-place) |
| **Stability** | ❌ No | ❌ No |

**When to Choose Quicksort:** 
Ideal for general-purpose in-memory sorting of large datasets. Its excellent cache locality and minimal inner loop instructions make it faster in practice than most $O(n \log n)$ algorithms.

**When to Choose Shellsort:** 
Highly effective for medium-sized lists or embedded systems where memory is strictly constrained (as it requires strictly $O(1)$ space and zero recursion stack) and implementing a complex $O(n \log n)$ algorithm is unnecessary.

## 5. AI Utilization Rules and Ethic Codes Statement
"Gemini (Google DeepMind) was used in the Code generation, Performance Benchmarking, and Report Structuring section of this product. The tool was utilized via the prompt/input 'Generate Python implementations, step-by-step traces, empirical benchmarks, and comparative academic report for Quicksort and Shellsort' for the purpose of Code generation, Algorithm editing, and Documentation. The output generated has been reviewed and verified by me for technical accuracy, safety, and originality. I bear full responsibility for the work."
