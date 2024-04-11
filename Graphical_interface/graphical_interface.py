import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sorting App"
MENU_FONT_SIZE = 35
BUTTON_FONT_SIZE = 30
MENU_COLOR = (139, 0, 0)
TEXT_COLOR = (0, 0, 0)
BUTTON_COLOR = (139, 0, 0)
SELECTED_METHOD_COLOR = (0, 255, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)
font = pygame.font.Font(None, 25)
button_font = pygame.font.Font(None, BUTTON_FONT_SIZE)
menu_font = pygame.font.Font(None, MENU_FONT_SIZE)

# Input box
input_box_width = 300
input_box_height = 50
input_box_x = 50
input_box_y = 200
input_box = pygame.Rect(input_box_x, input_box_y, input_box_width, input_box_height)

# Button
button_width = 200
button_height = 50
button_x = 550
button_y = 200
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# Dropdown Menu
sorting_methods = ["Selection Sort", "Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Heap Sort", "Comb Sort"]
menu_open = False
selected_method = None
menu_rect = pygame.Rect(270, 200, 250, input_box_height)  
menu_options_rects = []

# Functions
def draw_input_field():
    pygame.draw.rect(screen, MENU_COLOR, input_box, 2)
    text_surface = font.render(text, True, TEXT_COLOR)
    width = max(200, text_surface.get_width() + 10)
    input_box.w = width
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

def draw_start_button():
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
    button_text = button_font.render("Start Sorting", True, TEXT_COLOR)
    button_text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_text_rect)

def draw_dropdown_menu():
    pygame.draw.rect(screen, MENU_COLOR, menu_rect)
    menu_text = button_font.render(selected_method if selected_method else "Select Sorting Method", True, TEXT_COLOR)
    menu_text_rect = menu_text.get_rect(center=menu_rect.center)
    screen.blit(menu_text, menu_text_rect)

def draw_menu_options():
    for i, method in enumerate(sorting_methods):
        option_surface = menu_font.render(method, True, TEXT_COLOR)
        option_rect = option_surface.get_rect(center=(menu_rect.centerx, menu_rect.y + 50 * (i + 1) + 25))
        menu_options_rects.append(option_rect)
        if selected_method == method:
            pygame.draw.rect(screen, SELECTED_METHOD_COLOR, option_rect)
        else:
            pygame.draw.rect(screen, MENU_COLOR, option_rect, 2)  
        screen.blit(option_surface, option_rect)

# Main loop
running = True
active = False
text = ''
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            if menu_rect.collidepoint(event.pos):
                menu_open = not menu_open
            else:
                menu_open = False
            for i, option_rect in enumerate(menu_options_rects):
                if option_rect.collidepoint(event.pos):
                    selected_method = sorting_methods[i]
                    draw_menu_options()
        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print(text)
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    screen.fill((255, 255, 255))
    draw_input_field()
    draw_start_button()
    draw_dropdown_menu()
    if menu_open:
        draw_menu_options()
    pygame.display.flip()

# Quit Pygame
pygame.quit()
