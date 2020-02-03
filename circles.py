import pygame
import random
import math

pygame.init()
clock = pygame.time.Clock()

PROGRAM_FPS = 30
screen_width = 500
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont('Comic Sans Ms', 15)

pos = None
running = True
console = False

circle_radius = 5
max_clicks = 10
max_circles = 10
circles = []


pygame.display.init()
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if len(circles) == max_circles:
                circles = circles[1:]
                circles.append(pos)
            else:
                circles.append(pos)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                circles = []
            if event.key == pygame.K_BACKQUOTE:
                if not console:
                    console = True
                elif console:
                    console = False

    #displays console information
    if console:
        textsurface = font.render('Last clicked : ' + str(pos), False, (255, 255, 255))
        screen.blit(textsurface, (0, 0))

        textsurface = font.render('Circles : ' + str(circles), False, (255, 255, 255))
        screen.blit(textsurface, (0, 50))


    #slightly changes the location of each circle
    circles_perturbed = []
    for i in circles:
        x = i[0] + random.randint(-1,1)
        y = i[1] + random.randint(-1,1)
        if x < 0:
            x = 0
        elif x > screen_width:
            x = screen_width
        if y < 0:
            y = 0
        elif y > screen_height:
            y = screen_height
        circles_perturbed.append((x, y))
        circles = circles_perturbed

        pygame.draw.circle(screen, (255, 255, 255), (x, y), circle_radius)

    textsurface = font.render('` : console', False, (255, 255, 255))
    screen.blit(textsurface, (0, screen_height - 50))

    textsurface = font.render('C : clears all circles', False, (255, 255, 255))
    screen.blit(textsurface, (0, screen_height - 30))

    pygame.display.flip()

    clock.tick(PROGRAM_FPS)
pygame.quit()




