import sorting
import time
import matplotlib.pyplot as plt

def main():
    print("\nWelcome to the Sorting Algorithm Visualizer!")
    print("\nEnter a list of real numbers separated by space:")
    arr = list(map(int, input().split()))

    print("Select a sorting algorithm:")
    print("1. Selection Sort")
    print("2. Bubble Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")
    print("6. Heap Sort")
    print("7. Comb Sort")
    print("8. Compare all sorts")
    choice = int(input())

    start_time = time.time()

    if choice == 1:
        sorting.selection_sort(arr)
    elif choice == 2:
        sorting.bubble_sort(arr)
    elif choice == 3:
        sorting.insertion_sort(arr)
    elif choice == 4:
        sorting.merge_sort(arr)
    elif choice == 5:
        sorting.quick_sort(arr)
    elif choice == 6:
        sorting.heap_sort(arr)
    elif choice == 7:
        sorting.comb_sort(arr)
    elif choice == 8:  
        execution_times = {}
        for sort_func in [sorting.selection_sort, sorting.bubble_sort, sorting.insertion_sort,
                          sorting.merge_sort, sorting.quick_sort, sorting.heap_sort, sorting.comb_sort]:
            start_time = time.time()
            sort_func(arr.copy())
            end_time = time.time()
            execution_time = end_time - start_time
            execution_times[sort_func.__name__] = execution_time
            print(f"{sort_func.__name__}: Execution time - {execution_time} seconds")
        return execution_times  
    else:
        print("Invalid choice")
        return {}  
if __name__ == "__main__":
    execution_times = main()
    if execution_times:  
        algorithms = list(execution_times.keys())  
        times = list(execution_times.values())
        plt.bar(algorithms, times)
        plt.xlabel("Sorting Algorithms")
        plt.ylabel("Execution Time (seconds)")
        plt.title("Comparison of Sorting Algorithms")
        plt.show()
    else:
        print("No data to plot.")