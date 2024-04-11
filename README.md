# Sorting Algorithm

## Description
This project explores sorting algorithms with both terminal and graphical interfaces. It provides a hands-on approach to visualize and analyze the performance of various sorting algorithms in both graphical and textual forms.

## Features
- Implements popular sorting algorithms like selection, bubble, insertion, merge, quick, heap, and comb sort.
- Terminal interface for detailed performance analysis (execution time, comparisons, etc.).
- Graphical interface using pygame for an interactive, visual understanding of sorting processes.
- Comparative analysis and graphical representation of different algorithms' efficiency using matplotlib.

## Sorting Algorithms
### Selection Sort
Divides the input list into two parts: a sorted and an unsorted sublist. Repeatedly selects the smallest (or largest) element from the unsorted sublist and moves it to the sorted sublist.

### Bubble Sort
Repeatedly steps through the list, compares adjacent elements, and swaps them if in the wrong order. The process continues until the list is sorted, with smaller elements "bubbling" to the top.

### Insertion Sort
Builds the final sorted array one item at a time. It takes each element and inserts it into its appropriate position within the sorted subarray, efficient for small data sets.

### Merge Sort
A divide-and-conquer algorithm that divides the input array into two halves, sorts each half, and merges them. Known for efficiency, particularly good at handling large datasets.

### Quick Sort
Selects a 'pivot' element and partitions other elements into two sub-arrays based on whether they are less than or greater than the pivot, then sorts the sub-arrays recursively.

### Heap Sort
Builds a heap data structure from the input data and repeatedly removes the largest element from the heap, placing it at the end of the sorted section of the array.

### Comb Sort
Improves on Bubble Sort by using a gap sequence to compare and swap elements, eliminating small values at the end of the list quickly. The gap starts large and decreases with each iteration.

## Installation
You'll need Python along with matplotlib and pygame libraries.

```bash
pip install matplotlib pygame
```

## Usage
The `main.py` serves as the entry point to choose between the graphical and terminal interfaces:

```bash
python main.py
```

- For the terminal interface: Choose to run `terminal_interface.py` for analysis and comparisons.
- For the graphical interface: Choose to run `graphical_interface.py` for a visual representation of sorting algorithms.

## Project Structure
- `main.py`: Entry point to select the preferred interface.
- `sorting.py`: Contains implementations of various sorting algorithms.
- `terminal_interface.py`: Provides terminal-based analysis and comparisons of algorithms.
- `graphical_interface.py`: Offers a GUI for interactive visualization of sorting.

## Contributing
Feel free to contribute!

## License
Erika, Pierre, Sabrenne