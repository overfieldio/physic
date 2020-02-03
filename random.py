import pygame

pygame.init()

screen_width = 500
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont('Comic Sans Ms', 15)

pos = None
running = True
console = False

circle_radius = 5
max_clicks = 4
clicks = []


pygame.display.init()
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if len(clicks) == max_clicks:
                clicks = clicks[1:]
                clicks.append(pos)
            else:
                clicks.append(pos)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                clicks = []
            if event.key == pygame.K_BACKQUOTE:
                if not console:
                    console = True
                elif console:
                    console = False

    #displays console information
    if console:
        textsurface = font.render('Last clicked : ' + str(pos), False, (255, 255, 255))
        screen.blit(textsurface, (0, 0))

        textsurface = font.render('Clicks : ' + str(clicks), False, (255, 255, 255))
        screen.blit(textsurface, (0, 50))

    for i in clicks:
        pygame.draw.circle(screen, (255, 255, 255), i, circle_radius)

    if len(clicks) >= 2:
        pygame.draw.lines(screen, (255, 255, 255), True, clicks)

    textsurface = font.render('` : console', False, (255, 255, 255))
    screen.blit(textsurface, (0, screen_height - 50))

    textsurface = font.render('C : clears all squares', False, (255, 255, 255))
    screen.blit(textsurface, (0, screen_height - 30))

    pygame.display.flip()
pygame.quit()




