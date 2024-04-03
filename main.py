import pygame
import Graphical_interface.main
import Terminal_interface.main

def display_window():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Choisissez l'interface")
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    Graphical_interface.main.main()
                    return
                if event.key == pygame.K_t:
                    Terminal_interface.main.main()
                    return
        screen.fill((255, 255, 255))
        text = font.render("Appuyez sur 'g' pour utiliser l'interface graphique", True, (0, 0, 0))
        screen.blit(text, (100, 200))
        text = font.render("Appuyez sur 't' pour utiliser l'interface en ligne de commande", True, (0, 0, 0))
        screen.blit(text, (100, 300))
        pygame.display.flip()
        clock.tick(60)

def main():
    display_window()

if __name__ == "__main__":
    main()
