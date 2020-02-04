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
starting_circles = 25
max_circles = 10 * starting_circles

circles = []
circle_deathrate = 0.005
circle_birthrate = 0.015

deaths = 0


class Circle():
    def __init__(self, x=None, y=None):
        if x is None and y is None:
            self.x = random.randint(0, screen_width)
            self.y = random.randint(0, screen_height)
        else:
            self.x = x
            self.y = y
        self.screen = screen
        self.radius = circle_radius
        self.birthrate = circle_birthrate
        self.deathrate = circle_deathrate
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        x = self.x
        y = self.y

        self.x = x + random.randint(-1, 1)
        self.y = y + random.randint(-1, 1)


def death(person):
    if random.random() < person.deathrate:
        return True
    return False


def birth(person):
    if random.random() < person.birthrate:
        return True
    return False


# creates the initial population
for i in range(0, starting_circles):
    circles.append(Circle())

pygame.display.init()
# game loop
while running:
    screen.fill((0, 0, 0))
    # on event handling (clicks)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONUP:
            posx, posy = pygame.mouse.get_pos()
            if len(circles) >= max_circles:
                circles = circles[1:]
                circles.append(Circle(posx, posy))
            else:
                circles.append(Circle(posx, posy))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                circles = []
                corpses = []
            if event.key == pygame.K_BACKQUOTE:
                if not console:
                    console = True
                elif console:
                    console = False

    # displays console information
    if console:
        textsurface = font.render('Last clicked : ' + str(pos), False, (255, 255, 255))
        screen.blit(textsurface, (0, 0))

        textsurface = font.render('Circles : ' + str(circles), False, (255, 255, 255))
        screen.blit(textsurface, (0, 50))

    # calculates the population for the next game tick.
    nextcirclepop = []
    popcount = len(circles)
    for circle in circles:
        # moves the circles
        circle.move()
        # does the circle produce offspring?
        if birth(circle) is True and popcount < max_circles:
            nextcirclepop.append(Circle(circle.x, circle.y))
        # does the circle die?
        if death(circle) is False:
            nextcirclepop.append(circle)
            circle.draw()
    circles = nextcirclepop

    textsurface = font.render('Alive: ' + str(len(circles)) + ', Dead: ' + str(deaths), False, (255, 255, 255))
    screen.blit(textsurface, (0, screen_height - 70))

    textsurface = font.render('` : console', False, (255, 255, 255))
    screen.blit(textsurface, (0, screen_height - 50))

    textsurface = font.render('C : clears all circles', False, (255, 255, 255))
    screen.blit(textsurface, (0, screen_height - 30))

    pygame.display.flip()
    clock.tick(PROGRAM_FPS)
pygame.quit()




