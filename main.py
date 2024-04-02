import sorting
import time



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
        start_time = time.time()
        sorted_arr = sorting.selection_sort(arr)
        end_time = time.time()
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.selection_sort(sorted_arr)}")
        time_taken = (end_time - start_time) * 1000 
        print (f"Time taken: {time_taken:.6f} ms")
    elif choice == 2:
        start_time = time.time()
        sorted_arr = sorting.bubble_sort(arr)
        end_time = time.time()
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.bubble_sort(sorted_arr)}")
        time_taken = (end_time - start_time) * 1000
        print (f"Time taken: {time_taken:.6f} ms")
    elif choice == 3:
        start_time = time.time()
        sorted_arr = sorting.insertion_sort(arr)
        end_time = time.time()
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.insertion_sort(sorted_arr)}")
        time_taken = (end_time - start_time) * 1000
        print (f"Time taken: {time_taken:.6f} ms")
    elif choice == 4:
        start_time = time.time()
        sorted_arr = sorting.merge_sort(arr)
        end_time = time.time()
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.merge_sort(sorted_arr)}")
        time_taken = (end_time - start_time) * 1000
        print (f"Time taken: {time_taken:.6f} ms")
    elif choice == 5:
        start_time = time.time()
        sorted_arr = sorting.quick_sort(arr)
        end_time = time.time()
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.quick_sort(sorted_arr)}")
        time_taken = (end_time - start_time) * 1000
        print (f"Time taken: {time_taken:.6f} ms")
    elif choice == 6:
        start_time = time.time()
        sorted_arr = sorting.heap_sort(arr)
        end_time = time.time()
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.heap_sort(sorted_arr)}")
        time_taken = (end_time - start_time) * 1000
        print (f"Time taken: {time_taken:.6f} ms")
    elif choice == 7:
        start_time = time.time()
        sorted_arr = sorting.comb_sort(arr)
        end_time = time.time()
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorting.comb_sort(sorted_arr)}")
        time_taken = (end_time - start_time) * 1000
        print (f"Time taken: {time_taken:.6f} ms")
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

    

