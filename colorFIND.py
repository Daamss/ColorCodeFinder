import pygame
import pyautogui

# initialize pygame and pyautogui
pygame.init()
pyautogui.PAUSE = 0

# create a window
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Color Code Finder")

# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # get current mouse position
    mouse_pos = pyautogui.position()
    # get RGB color at mouse position
    mouse_rgb = pyautogui.screenshot().getpixel(mouse_pos)
    # get hex color at mouse position
    mouse_hex = '#%02x%02x%02x' % mouse_rgb

    # display information
    screen.fill(WHITE)
    pygame.draw.rect(screen, mouse_rgb, (0, 0, 500, 500))
    font = pygame.font.SysFont("arial", 30)
    text_rgb = font.render("RGB: " + str(mouse_rgb), 1, BLACK)
    text_hex = font.render("HEX: " + str(mouse_hex), 1, BLACK)
    screen.blit(text_rgb, (10, 10))
    screen.blit(text_hex, (10, 40))
    pygame.display.update()

pygame.quit()