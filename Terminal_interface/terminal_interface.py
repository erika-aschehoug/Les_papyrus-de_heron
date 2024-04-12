import sorting
import timeit
import matplotlib.pyplot as plt
import random

def execution_times_graph(execution_times, sorted_arr, original_arr, num_runs):
    plt.bar(execution_times.keys(), execution_times.values())
    plt.xlabel('Sorting Algorithms')
    plt.ylabel('Average Execution Time (in milliseconds)')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.title(f'Average execution time over {num_runs} runs depending on different sorting algorithms')
    if len(sorted_arr) > 20:
        sorted_arr_str = f'{sorted_arr[:10]} ... {sorted_arr[-10:]}'
        original_arr_str = f'{original_arr[:10]} ... {original_arr[-10:]}'
    else:
        sorted_arr_str = str(sorted_arr)
        original_arr_str = str(original_arr)
    plt.text(0.5, 1.08, f'List before sorting: {original_arr_str}', transform=plt.gca().transAxes, ha='center')
    plt.text(0.5, 1.05, f'List after sorting: {sorted_arr_str}', transform=plt.gca().transAxes, ha='center')
    plt.text(0.5, 1.11, f'List length: {len(sorted_arr)}', transform=plt.gca().transAxes, ha='center')
    plt.text(0.5, 1.14, f'Sorting oder: {"Ascending" if sorted_arr == sorted(sorted_arr) else "Descending"}', transform=plt.gca().transAxes, ha='center')
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

def generate_random_list(length):
    return [random.randint(-1000, 1000) for _ in range(length)]



def main():
    print (f"\nWelcome to the Sorting Algorithm Visualizer !")
    while True:
        try:
            choice = input("\nDo you want to insert a list(1), or generate a random list between -1000 and 1000 inclusive(2)? (1/2): ").lower()
            if choice == "1":
                arr = list(map(int, input("Enter a list of real numbers separated by space: ").split()))
                if not arr:
                    raise ValueError("List cannot be empty.")
                original_arr = arr.copy()
                break
            elif choice == "2":
                length = int(input("Enter the desired length of the random list: "))
                arr = original_arr = generate_random_list(length)
                break
            else:
                print("Invalid choice. Please enter '1' or '2'.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid list of real numbers separated by space.")
    print (f"\nSelect a sorting algorithm:")
    print (f"1. Selection Sort")
    print (f"2. Bubble Sort")
    print (f"3. Insertion Sort")
    print (f"4. Merge Sort")
    print (f"5. Quick Sort")
    print (f"6. Heap Sort")
    print (f"7. Comb Sort")
    print(f"8. Compare all sorts")
    choice = int(input(f"Enter your choice (1-8): "))
    if choice == 1:
        print("\nChoose sorting order:")
        print("1. Ascending")
        print("2. Descending")
        order_choice = int(input(f"Enter your choice (1 or 2): "))
        if order_choice != 1 and order_choice != 2:
            print(f"\nInvalid choice please start again !")
            return main()
        ascending = order_choice == 1
        start_time = timeit.default_timer()
        sorted_arr = sorting.selection_sort(arr, ascending)
        end_time = timeit.default_timer()
        time_taken = end_time - start_time
        print (f"\nSelection_Sort")
        print(f"\nList before sorting: {original_arr}")
        print(f"List after sorting: {sorted_arr}")
        print(f"Time taken: {time_taken:.10e} ms")
    elif choice == 2:
        print("\nChoose sorting order:")
        print("1. Ascending")
        print("2. Descending")
        order_choice = int(input(f"Enter your choice (1 or 2): "))
        if order_choice != 1 and order_choice != 2:
            print(f"\nInvalid choice please start again !")
            return main()      
        ascending = order_choice == 1
        start_time = timeit.default_timer()
        sorted_arr = sorting.bubble_sort(arr, ascending)
        end_time = timeit.default_timer()
        time_taken = end_time - start_time
        print (f"\nBubble_Sort")
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorted_arr}")
        print (f"Time taken: {time_taken:.10e} ms")
    elif choice == 3:
        print("\nChoose sorting order:")
        print("1. Ascending")
        print("2. Descending")
        order_choice = int(input(f"Enter your choice (1 or 2): "))
        if order_choice != 1 and order_choice != 2:
            print(f"\nInvalid choice please start again !")
            return main()
        ascending = order_choice == 1
        start_time = timeit.default_timer()
        sorted_arr = sorting.insertion_sort(arr, ascending)
        end_time = timeit.default_timer()
        time_taken = end_time - start_time
        print (f"\nInsertion_Sort")
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorted_arr}")
        print (f"Time taken: {time_taken:.10e} ms")
    elif choice == 4:
        print("\nChoose sorting order:")
        print("1. Ascending")
        print("2. Descending")
        order_choice = int(input(f"Enter your choice (1 or 2): "))
        if order_choice != 1 and order_choice != 2:
            print(f"\nInvalid choice please start again !")
            return main()
        ascending = order_choice == 1
        start_time = timeit.default_timer()
        sorted_arr = sorting.merge_sort(arr, ascending)
        end_time = timeit.default_timer()
        time_taken = end_time - start_time
        print (f"\nMerge_Sort")
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorted_arr}")
        print (f"Time taken: {time_taken:.10e} ms")
    elif choice == 5:
        print("\nChoose sorting order:")
        print("1. Ascending")
        print("2. Descending")
        order_choice = int(input(f"Enter your choice (1 or 2): "))
        if order_choice != 1 and order_choice != 2:
            print(f"\nInvalid choice please start again !")
            return main()
        ascending = order_choice == 1
        start_time = timeit.default_timer()
        sorted_arr = sorting.quick_sort(arr, ascending)
        end_time = timeit.default_timer()
        time_taken = end_time - start_time
        print (f"\nQuick_Sort")
        print (f"\nList before sorting: {original_arr}")
        print(f"List after sorting: {sorted_arr}")
        print (f"Time taken: {time_taken:.10e} ms")
    elif choice == 6:
        print("\nChoose sorting order:")
        print("1. Ascending")
        print("2. Descending")
        order_choice = int(input(f"Enter your choice (1 or 2): "))
        if order_choice != 1 and order_choice != 2:
            print(f"\nInvalid choice please start again !")
            return main()
        ascending = order_choice == 1
        start_time = timeit.default_timer()
        sorted_arr = sorting.heap_sort(arr, ascending)
        end_time = timeit.default_timer()
        time_taken = end_time - start_time
        print(f"\nHeap_Sort")
        print(f"\nListe avant le tri : {original_arr}")
        print(f"Liste après le tri : {sorted_arr}")
        print(f"Temps écoulé : {time_taken:.10e} ms")
    elif choice == 7:
        print("\nChoose sorting order:")
        print("1. Ascending")
        print("2. Descending")
        order_choice = int(input(f"Enter your choice (1 or 2): "))
        if order_choice != 1 and order_choice != 2:
            print(f"\nInvalid choice please start again !")
            return main()
        ascending = order_choice == 1
        start_time = timeit.default_timer()
        sorted_arr = sorting.comb_sort(arr, ascending)
        end_time = timeit.default_timer()
        time_taken = end_time - start_time
        print (f"\nComb_Sort")
        print (f"\nList before sorting: {original_arr}")
        print (f"List after sorting: {sorted_arr}")
        print (f"Time taken: {time_taken:.10e} ms")
    elif choice == 8:
        print("\nChoose sorting order:")
        print("1. Ascending")
        print("2. Descending")
        order_choice = int(input(f"Enter your choice (1 or 2): "))
        if order_choice != 1 and order_choice != 2:
            print(f"\nInvalid choice please start again !")
            return main()
        num_runs = int(input(f"Enter the number of runs to calculate average execution time: "))
        ascending = order_choice == 1
        execution_times = {}
        for sort_func in [sorting.selection_sort, sorting.bubble_sort, sorting.insertion_sort,
                        sorting.merge_sort, sorting.quick_sort, sorting.heap_sort, sorting.comb_sort]:
            total_time = 0
            for _ in range(num_runs):
                arr = original_arr.copy()
                start_time = timeit.default_timer()
                sorted_arr = sort_func(arr, ascending)
                end_time = timeit.default_timer()
                total_time += end_time - start_time
            average_time = total_time / num_runs
            execution_times[sort_func.__name__] = average_time
            print(f"\n{sort_func.__name__}")
            print(f"\nList before sorting: {original_arr}")
            print(f"List after sorting: {sorted_arr}")
            print(f"Average time taken over {num_runs} runs: {average_time:.10e} ms")
        execution_times_graph(execution_times, sorted_arr, original_arr, num_runs)
    else:
        print (f"\nInvalid choice please start again !")
        return main()
    print (f"\nDo you want to continue sortings ? (y/n)")
    choice = input()
    if choice == 'y' or choice == 'Y':
        main()
    else:
        print (f"\nThank you for using the Sorting Algorithm Visualizer !\n")
        return False

if __name__ == "__main__":
   main()