import sorting

def main():
    print (f"\nWelcome to the Sorting Algorithm Visualizer !")
    print (f"\nEnter a list of real numbers separated by space:")
    arr = list(map(int, input().split()))
    print (f"Select a sorting algorithm:")
    print (f"1. Selection Sort")
    print (f"2. Bubble Sort")
    print (f"3. Insertion Sort")
    print (f"4. Merge Sort")
    print (f"5. Quick Sort")
    print (f"6. Heap Sort")
    print (f"7. Comb Sort")
    choice = int(input())

    if choice == 1:
        print (sorting.selection_sort(arr))
    elif choice == 2:
        print (sorting.bubble_sort(arr))
    elif choice == 3:
        print (sorting.insertion_sort(arr))
    elif choice == 4:
        print (sorting.merge_sort(arr))
    elif choice == 5:
        print (sorting.quick_sort(arr))
    elif choice == 6:
        print (sorting.heap_sort(arr))
    elif choice == 7:
        print (sorting.comb_sort(arr))
    else:
        print (f"Invalid choice")

if __name__ == "__main__":
    main()


