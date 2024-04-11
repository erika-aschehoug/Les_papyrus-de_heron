import pygame
import sorting
import timeit

# initialize the pygame module
def pygame_init():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Sorting algorithms visualizer")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("comicsans", 20)  # Reduced font size
    return screen, clock, font

# create text zone to add number list separated by space
def create_text_zone(screen, font):
    text = ''
    text_zone = pygame.Rect(50, 10, 700, 50)
    pygame.draw.rect(screen, (255, 255, 255), text_zone)
    pygame.draw.rect(screen, (0, 0, 0), text_zone, 2)
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (text_zone.x + 10, text_zone.y + 10))
    return text_zone, text

# create list to choose sorting algorithm
def create_sorting_list(screen, font, selected=None):
    sorting_list = ['Selection sort', 'Bubble sort', 'Insertion sort', 'Merge sort', 'Quick sort', 'Heap sort', 'Comb sort']
    sorting_rects = []
    for i, sorting_name in enumerate(sorting_list):
        rect = pygame.Rect(50, 200 + 50 * i, 200, 50)
        sorting_rects.append(rect)
        color = (255, 0, 0) if i == selected else (255, 255, 255)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 2)
        text_surface = font.render(sorting_name, True, (0, 0, 0))
        screen.blit(text_surface, (rect.x + 10, rect.y + 10))
    return sorting_rects

# create list to choose sorting order
def create_order_list(screen, font, selected=None):
    order_list = ['Ascending sort', 'Descending sort']
    order_rects = []
    smaller_font = pygame.font.SysFont("comicsans", 10)  # Reduced font size
    for i, order_name in enumerate(order_list):
        rect = pygame.Rect(50 + 100 * i, 150, 100, 25)  # Adjusted x-coordinate for side-by-side placement
        order_rects.append(rect)
        color = (255, 0, 0) if i == selected else (255, 255, 255)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 2)
        text_surface = smaller_font.render(order_name, True, (0, 0, 0))  # Use the smaller font
        text_rect = text_surface.get_rect(center=rect.center)  # Get the rectangle of the text surface and set its center to the center of the button
        screen.blit(text_surface, text_rect)  # Blit the text surface at the position of the text rectangle
    return order_rects

# create button to launch the sorting algorithm
def create_sort_button(screen, font, selected=False):
    sort_button = pygame.Rect(550, 500, 200, 50)
    color = (255, 0, 0) if selected else (255, 255, 255)
    pygame.draw.rect(screen, color, sort_button)
    pygame.draw.rect(screen, (0, 0, 0), sort_button, 2)
    text_surface = font.render("Sort", True, (0, 0, 0))
    screen.blit(text_surface, (sort_button.x + 10, sort_button.y + 10))
    return sort_button

# create zone to display results and executing time of the sorting algorithm
def create_result_zone(screen, font):
    result_zone = pygame.Rect(300, 100, 450, 400)
    pygame.draw.rect(screen, (255, 255, 255), result_zone)
    pygame.draw.rect(screen, (0, 0, 0), result_zone, 2)
    return result_zone

# create button to return to the main menu
def create_return_button(screen, font, selected=False):
    return_button = pygame.Rect(560, 550, 200, 50)
    color = (255, 0, 0) if selected else (255, 255, 255)
    pygame.draw.rect(screen, color, return_button)
    pygame.draw.rect(screen, (0, 0, 0), return_button, 2)
    text_surface = font.render("Return to main page", True, (0, 0, 0))
    screen.blit(text_surface, (return_button.x + 10, return_button.y + 10))
    return return_button

# display the results of the sorting algorithm
def display_results(screen, font, result_zone, original_arr, sorted_arr, time_taken):
    pygame.draw.rect(screen, (255, 255, 255), result_zone)
    pygame.draw.rect(screen, (0, 0, 0), result_zone, 2)
    text_surface = font.render(f"Original list: {original_arr}", True, (0, 0, 0))
    screen.blit(text_surface, (result_zone.x + 10, result_zone.y + 10))
    text_surface = font.render(f"Sorted list: {sorted_arr}", True, (0, 0, 0))
    screen.blit(text_surface, (result_zone.x + 10, result_zone.y + 50))
    text_surface = font.render(f"Time taken: {time_taken:.10e} ms", True, (0, 0, 0))
    screen.blit(text_surface, (result_zone.x + 10, result_zone.y + 90))

# copy the original list to avoid modifying it
def copy_list(arr):
    original_arr = arr.copy()
    return original_arr

# create button to clear the list
def create_clear_button(screen, font, selected=False):
    clear_button = pygame.Rect(300, 500, 200, 50)
    color = (255, 0, 0) if selected else (255, 255, 255)
    pygame.draw.rect(screen, color, clear_button)
    pygame.draw.rect(screen, (0, 0, 0), clear_button, 2)
    text_surface = font.render("Clear", True, (0, 0, 0))
    screen.blit(text_surface, (clear_button.x + 10, clear_button.y + 10))
    return clear_button

# create button to compare all sorting algorithms
def create_compare_button(screen, font, selected=False):
    compare_button = pygame.Rect(300, 550, 200, 50)
    color = (255, 0, 0) if selected else (255, 255, 255)
    pygame.draw.rect(screen, color, compare_button)
    pygame.draw.rect(screen, (0, 0, 0), compare_button, 2)
    text_surface = font.render("Compare All", True, (0, 0, 0))
    screen.blit(text_surface, (compare_button.x + 10, compare_button.y + 10))
    return compare_button

# function to compare all sorting algorithms
def compare_algorithms(screen, font, result_zone, arr, ascending):
    algorithms = [sorting.selection_sort, sorting.bubble_sort, sorting.insertion_sort, sorting.merge_sort, sorting.quick_sort, sorting.heap_sort, sorting.comb_sort]
    times = []
    for algorithm in algorithms:
        start_time = timeit.default_timer()
        algorithm(arr.copy(), ascending)  # Use a copy of the array to sort
        end_time = timeit.default_timer()
        time_taken = (end_time - start_time) * 1000
        times.append(time_taken)
    max_time = max(times)
    for i, time in enumerate(times):
        bar_height = (time / max_time) * (result_zone.height - 20)  # Scale the bar height according to the maximum time and the height of the result zone
        bar_rect = pygame.Rect(result_zone.x + 10 + 60 * i, result_zone.y + result_zone.height - bar_height, 50, bar_height)
        pygame.draw.rect(screen, (255, 0, 0), bar_rect)
        text_surface = font.render(f"{algorithms[i].__name__}", True, (0, 0, 0))  # Only draw the name of the algorithm
        screen.blit(text_surface, (bar_rect.x, bar_rect.y - 20))  # Draw the name above the bar
        
# main function to launch the graphical interface
def main():
    ascending = True
    screen, clock, font = pygame_init()
    text_zone, text = create_text_zone(screen, font)
    sorting_rects = create_sorting_list(screen, font)
    sort_button = create_sort_button(screen, font)
    clear_button = create_clear_button(screen, font)  # Added clear button
    compare_button = create_compare_button(screen, font)  # Create the compare button
    result_zone = create_result_zone(screen, font)
    return_button = create_return_button(screen, font)
    order_rects = create_order_list(screen, font)
    arr = []
    original_arr = []
    sorted_arr = []
    sorting_algorithm = None
    sorting_order = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_zone.collidepoint(event.pos):
                    text = ''
                for i, rect in enumerate(sorting_rects):
                    if rect.collidepoint(event.pos):
                        sorting_algorithm = i
                        sorting_rects = create_sorting_list(screen, font, selected=i)
                for i, rect in enumerate(order_rects):
                    if rect.collidepoint(event.pos):
                        sorting_order = i
                        order_rects = create_order_list(screen, font, selected=i)
                if sort_button.collidepoint(event.pos) and sorting_algorithm is not None:
                    ascending = (sorting_order == 0)
                    if sorting_algorithm == 0:
                        sorting_algorithm = sorting.selection_sort
                    elif sorting_algorithm == 1:
                        sorting_algorithm = sorting.bubble_sort
                    elif sorting_algorithm == 2:
                        sorting_algorithm = sorting.insertion_sort
                    elif sorting_algorithm == 3:
                        sorting_algorithm = sorting.merge_sort
                    elif sorting_algorithm == 4:
                        sorting_algorithm = sorting.quick_sort
                    elif sorting_algorithm == 5:
                        sorting_algorithm = sorting.heap_sort
                    elif sorting_algorithm == 6:
                        sorting_algorithm = sorting.comb_sort
                    start_time = timeit.default_timer()
                    sorted_arr = sorting_algorithm(arr, ascending)
                    end_time = timeit.default_timer()
                    time_taken = (end_time - start_time) * 1000
                    display_results(screen, font, result_zone, original_arr, sorted_arr, time_taken)
                if compare_button.collidepoint(event.pos):  # If the compare button is clicked
                    compare_algorithms(screen, font, result_zone, arr, ascending)  # Compare all algorithms
                if clear_button.collidepoint(event.pos):  # Added clear event
                    arr = []
                    original_arr = []
                    sorted_arr = []
                    text = ''
                    pygame.draw.rect(screen, (255, 255, 255), text_zone)
                    pygame.draw.rect(screen, (0, 0, 0), text_zone, 2)
                    text_surface = font.render(text, True, (0, 0, 0))
                    screen.blit(text_surface, (text_zone.x + 10, text_zone.y + 10))
                    pygame.draw.rect(screen, (255, 255, 255), result_zone)  # Clear the result zone
                    pygame.draw.rect(screen, (0, 0, 0), result_zone, 2)
                if return_button.collidepoint(event.pos):
                    return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
                text_surface = font.render(text, True, (0, 0, 0))
                screen.blit(text_surface, (text_zone.x + 10, text_zone.y + 10))
                if event.key == pygame.K_RETURN:
                    arr = list(map(int, text.split()))
                    original_arr = copy_list(arr)
                    text = ''
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
