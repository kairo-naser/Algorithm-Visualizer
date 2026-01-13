# Algorithm Visualizer

This repository contains Python implementations of **Sorting** and **Searching** algorithms with detailed comments and step-by-step explanations for educational purposes.

## Folder Structure

algorithm-visualizer/
│
├── sorting/
│ ├── selection_sort.py
│ ├── bubble_sort.py
│ ├── insertion_sort.py
│ ├── merge_sort.py
│ ├── quick_sort.py
│ ├── counting_sort.py
│ └── radix_sort.py
│
├── searching/
│ ├── linear_search.py
│ ├── binary_search.py
│ ├── bfs.py
│ ├── dfs.py
│ ├── greedy_best_first.py
│ └── a_star_search.py
│
└── README.md



## Sorting Algorithms

1. **Selection Sort** – Selects the smallest element and moves it to the beginning of the array.  
2. **Bubble Sort** – Repeatedly swaps adjacent elements if they are in the wrong order.  
3. **Insertion Sort** – Builds a sorted section by inserting elements in the correct position.  
4. **Merge Sort** – Divide-and-conquer algorithm that splits, recursively sorts, and merges arrays.  
5. **Quick Sort** – Picks a pivot, partitions the array around it, and recursively sorts subarrays.  
6. **Counting Sort** – Counts occurrences of each element and rebuilds a sorted array based on counts.  
7. **Radix Sort** – Processes digits from least to most significant using counting sort for each digit.

## Searching Algorithms

1. **Linear Search** – Checks each element sequentially until the target is found.  
2. **Binary Search** – Works on sorted arrays by repeatedly dividing the search interval in half.  
3. **Breadth-First Search (BFS)** – Explores graph level by level using a queue. Finds the shortest path in unweighted graphs.  
4. **Depth-First Search (DFS)** – Explores graph as deep as possible before backtracking. Uses recursion and tracks visited nodes.  
5. **Greedy Best-First Search** – Always chooses the next node based on the lowest heuristic estimate to goal.  
6. **A* Search** – Combines actual cost (g) and heuristic (h) to compute f = g + h. Finds the optimal path in weighted graphs if heuristic is admissible.

## How to Use

1. Open any `.py` file in your IDE or terminal.  
2. Run the script to see **step-by-step explanations** and printed outputs in the console.  
3. Modify the input arrays or graphs to experiment with different datasets.  

## Purpose

- Educational tool for understanding classic **sorting** and **searching** algorithms.  
- Provides **detailed step-by-step console output** for tracing algorithm execution.  
- Suitable for students and beginners learning **Computer Science and Algorithms**.

---

**Author:** Kairo  
**Recommended Repository Name:** `algorithm-visualizer`
