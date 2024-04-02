import sorting
import timeit



def main():
    print (f"\nWelcome to the Sorting Algorithm Visualizer !")
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
    choice = int(input())

    if choice == 1:
        time_taken = timeit.timeit(lambda: sorting.selection_sort(arr), number=1)
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.selection_sort(arr)}")
        print (f"Time taken: {time_taken:.10e} ms")
    elif choice == 2:
        time_taken = timeit.timeit(lambda: sorting.bubble_sort(arr), number=1)
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.bubble_sort(arr)}")
        print (f"Time taken: {time_taken:.10e} ms")
    elif choice == 3:
        time_taken = timeit.timeit(lambda: sorting.insertion_sort(arr), number=1)
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.insertion_sort(arr)}")
        print (f"Time taken: {time_taken:.10e} ms")
    elif choice == 4:
        time_taken = timeit.timeit(lambda: sorting.merge_sort(arr), number=1)
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.merge_sort(arr)}")
        print (f"Time taken: {time_taken:.10e} ms")
    elif choice == 5:
        time_taken = timeit.timeit(lambda: sorting.quick_sort(arr), number=1)
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.quick_sort(arr)}")
        print (f"Time taken: {time_taken:.10e} ms")
    elif choice == 6:
        time_taken = timeit.timeit(lambda: sorting.heapify(arr), number=1)
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.heapify(arr)}")
        print (f"Time taken: {time_taken:.10e} ms")
    elif choice == 7:
        time_taken = timeit.timeit(lambda: sorting.comb_sort(arr), number=1)
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.comb_sort(arr)}")
        print (f"Time taken: {time_taken:.10e} ms")
    else:
        print (f"\nInvalid choice !")
        return
    print (f"\nThank you for using the Sorting Algorithm Visualizer !")
    print (f"\nDo you want to continue ? (y/n)")
    choice = input()
    if choice == 'y' or choice == 'Y':
        main()
    else:
        return
    

if __name__ == "__main__":
    main()

    

