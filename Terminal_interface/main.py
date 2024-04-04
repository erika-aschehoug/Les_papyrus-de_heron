import sorting
import timeit
import matplotlib.pyplot as plt

def execution_times_graph(execution_times, arr, original_arr):
    plt.bar(execution_times.keys(), execution_times.values())
    plt.xlabel('Sorting Algorithms')
    plt.ylabel('Execution Time (in milliseconds)')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.title('execution time depending on different sorting algorithms')
    plt.text(0.5, 1.08, f'List before sorting: {original_arr}', transform=plt.gca().transAxes, ha='center')
    plt.text(0.5, 1.05, f'List after sorting: {arr}', transform=plt.gca().transAxes, ha='center')
    plt.text(0.5, 1.11, f'List length: {len(arr)}', transform=plt.gca().transAxes, ha='center')
    algorithm_names = {
    sorting.selection_sort.__name__: 'Selection',
    sorting.bubble_sort.__name__: 'Bubble',
    sorting.insertion_sort.__name__: 'Insertion',
    sorting.merge_sort.__name__: 'Merge',
    sorting.quick_sort.__name__: 'Quick',
    sorting.heap_sort.__name__: 'Heap',
    sorting.comb_sort.__name__: 'Comb'}
    plt.xticks(list(algorithm_names.keys()), list(algorithm_names.values()))
    plt.show()

def main():
    print (f"\nWelcome to the Sorting Algorithm command line interface!")
    print (f"\nEnter a list of real numbers separated by space:")
    arr = list(map(int, input().split()))
    original_arr = arr.copy()
    print (f"\nSelect a sorting algorithm:")
    print (f"1. Selection Sort")
    print (f"2. Bubble Sort")
    print (f"3. Insertion Sort")
    print (f"4. Merge Sort")
    print (f"5. Quick Sort")
    print (f"6. Heap Sort")
    print (f"7. Comb Sort")
    print(f"8. Compare all sorts")
    choice = int(input())

    if choice == 1:
        time_taken = timeit.timeit(lambda: sorting.selection_sort(arr), number=1)
        print (f"\nSelection_Sort")
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.selection_sort(arr)}")
        print (f"List length: {len(arr)}")
        print (f"Time taken: {time_taken:.10e} ms")
    elif choice == 2:
        time_taken = timeit.timeit(lambda: sorting.bubble_sort(arr), number=1)
        print (f"\nBubble_Sort")
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.bubble_sort(arr)}")
        print (f"List length: {len(arr)}")
        print (f"Time taken: {time_taken:.10e} ms")
    elif choice == 3:
        time_taken = timeit.timeit(lambda: sorting.insertion_sort(arr), number=1)
        print (f"\nInsertion_Sort")
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.insertion_sort(arr)}")
        print (f"List length: {len(arr)}")
        print (f"Time taken: {time_taken:.10e} ms")
    elif choice == 4:
        time_taken = timeit.timeit(lambda: sorting.merge_sort(arr), number=1)
        print (f"\nMerge_Sort")
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.merge_sort(arr)}")
        print (f"List length: {len(arr)}")
        print (f"Time taken: {time_taken:.10e} ms")
    elif choice == 5:
        time_taken = timeit.timeit(lambda: sorting.quick_sort(arr), number=1)
        print (f"\nQuick_Sort")
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.quick_sort(arr)}")
        print (f"List length: {len(arr)}")
        print (f"Time taken: {time_taken:.10e} ms")
    elif choice == 6:
        time_taken = timeit.timeit(lambda: sorting.heap_sort(arr), number=1)
        print(f"\nHeap_Sort")
        print(f"\nList before sorting: {original_arr}")
        print(f"List after sorting: {sorting.heap_sort(arr)}")
        print (f"List length: {len(arr)}")
        print(f"Time taken: {time_taken:.10e} ms")
    elif choice == 7:
        time_taken = timeit.timeit(lambda: sorting.comb_sort(arr), number=1)
        print (f"\nComb_Sort")
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.comb_sort(arr)}")
        print (f"List length: {len(arr)}")
        print (f"Time taken: {time_taken:.10e} ms")
    elif choice == 8:  
        execution_times = {}
        for sort_func in [sorting.selection_sort, sorting.bubble_sort, sorting.insertion_sort,
                          sorting.merge_sort, sorting.quick_sort, sorting.heap_sort, sorting.comb_sort]:
            arr = original_arr.copy()
            time_taken = timeit.timeit(lambda: sort_func(arr), number=1)
            execution_times[sort_func.__name__] = time_taken
            print(f"\n{sort_func.__name__}")
            print(f"\nList before sorting: {original_arr}")
            print(f"List after sorting: {arr}")
            print (f"List length: {len(arr)}")
            print(f"Time taken: {time_taken:.10e} ms")
        execution_times_graph(execution_times, arr, original_arr)
    else:
        print (f"\nInvalid choice!")
        return
    print (f"\nDo you want to continue sortings? (y/n)")
    choice = input()
    if choice == 'y' or choice == 'Y':
        main()
    else:
        print (f"\nThank you for using the Sorting Algorithm command line interface!\n")
        return
    

if __name__ == "__main__":
    main()
