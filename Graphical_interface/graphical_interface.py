import pygame

def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Sorting App")
    return screen

def create_fonts():
    font = pygame.font.Font(None, 25)
    button_font = pygame.font.Font(None, 30)
    menu_font = pygame.font.Font(None, 35)
    return font, button_font, menu_font

def create_input_box():
    input_box = pygame.Rect(50, 200, 300, 50)
    return input_box

def create_button():
    button_rect = pygame.Rect(550, 200, 200, 50)
    return button_rect

def create_dropdown_menu():
    menu_rect = pygame.Rect(270, 200, 250, 50)
    return menu_rect

def main():
    screen = init_pygame()
    font, button_font, menu_font = create_fonts()
    input_box = create_input_box()
    button_rect = create_button()
    menu_rect = create_dropdown_menu()

    sorting_methods = ["Selection Sort", "Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Heap Sort", "Comb Sort"]
    menu_open = False
    selected_method = None
    menu_options_rects = []

    def draw_input_field(text):
        pygame.draw.rect(screen, (139, 0, 0), input_box, 2)
        text_surface = font.render(text, True, (0, 0, 0))
        width = max(200, text_surface.get_width() + 10)
        input_box.w = width
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    def draw_start_button():
        pygame.draw.rect(screen, (139, 0, 0), button_rect)
        button_text = button_font.render("Start Sorting", True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, button_text_rect)

    def draw_dropdown_menu():
        pygame.draw.rect(screen, (139, 0, 0), menu_rect)
        menu_text = button_font.render(selected_method if selected_method else "Select Sorting Method", True, (0, 0, 0))
        menu_text_rect = menu_text.get_rect(center=menu_rect.center)
        screen.blit(menu_text, menu_text_rect)

    def draw_menu_options():
        for i, method in enumerate(sorting_methods):
            option_surface = menu_font.render(method, True, (0, 0, 0))
            option_rect = option_surface.get_rect(center=(menu_rect.centerx, menu_rect.y + 50 * (i + 1) + 25))
            menu_options_rects.append(option_rect)
            if selected_method == method:
                pygame.draw.rect(screen, (0, 255, 0), option_rect)
            else:
                pygame.draw.rect(screen, (139, 0, 0), option_rect, 2)  
            screen.blit(option_surface, option_rect)

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
        draw_input_field(text)
        draw_start_button()
        draw_dropdown_menu()
        if menu_open:
            draw_menu_options()
        pygame.display.flip()

if __name__ == "__main__":
    main()
