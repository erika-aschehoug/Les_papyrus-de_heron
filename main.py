import pygame
import Graphical_interface.main
import Terminal_interface.main

def display_window():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Sorting Algorithm Visualizer")
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    # create buttons for the two interfaces to choose from 
    button_g = pygame.Rect(100, 200, 400, 50)
    button_t = pygame.Rect(100, 300, 400, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check if the mouse click is within the button
                if button_g.collidepoint(event.pos):
                    Graphical_interface.main.main()
                    return
                elif button_t.collidepoint(event.pos):
                    pygame.quit() # close the pygame window before opening the terminal interface 
                    result = Terminal_interface.main.main()
                    if result is False:
                        return

        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (200, 200, 200), button_g)
        pygame.draw.rect(screen, (200, 200, 200), button_t)
        text_g = font.render("Use the GUI", True, (0, 0, 0))
        text_t = font.render("Use the command line interface", True, (0, 0, 0))
        screen.blit(text_g, (button_g.x + 10, button_g.y + 10))
        screen.blit(text_t, (button_t.x + 10, button_t.y + 10))
        pygame.display.flip()
        clock.tick(60)

def main():
    while True:
        result = display_window()
        if result is False:
            return

if __name__ == "__main__":
    main()
