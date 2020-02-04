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
    def __init__(self, x=None, y=None, color=None):
        if x is None and y is None:
            self.x = random.randint(0, screen_width)
            self.y = random.randint(0, screen_height)
        else:
            self.x = x
            self.y = y

        if color is None:
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            self.color = color

        self.screen = screen
        self.radius = circle_radius
        self.birthrate = circle_birthrate
        self.deathrate = circle_deathrate

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        x = self.x
        y = self.y

        xn = (x + random.randint(-1, 1))
        yn = (y + random.randint(-1, 1))

        # bounds the individual to the screen
        if xn > screen_width:
            xn = screen_width
        elif xn < 0:
            xn = 0
        if yn > screen_height:
            yn = screen_height
        elif yn < 0:
            yn = 0

        self.x = xn
        self.y = yn



def death(person):
    if random.random() < person.deathrate:
        return True
    return False


def birth(person):
    if random.random() < person.birthrate:
        return True
    return False


def mutatecolor(color):
    r, g, b = color
    r = (r + random.randint(-10, 10)) % 256
    g = (g + random.randint(-10, 10)) % 256
    b = (b + random.randint(-10, 10)) % 256

    colormutated = (r, g, b)
    return colormutated


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
        textsurface = font.render('C : clears all circles', False, (255, 255, 255))
        screen.blit(textsurface, (0, 30))

        #rendering text to console screen
        textsurface = font.render('Alive: ' + str(len(circles)) + ', Dead: ' + str(deaths), False, (255, 255, 255))
        screen.blit(textsurface, (0, 70))

    # calculates the population for the next game tick.
    nextcirclepop = []
    popcount = len(circles)
    for circle in circles:
        # moves the circles
        circle.move()
        # does the circle produce offspring?
        if birth(circle) is True and popcount < max_circles:
            # creates offspring and slightly mutates the color
            nextcirclepop.append(Circle(x=circle.x, y=circle.y, color=mutatecolor(circle.color)))
        # does the circle die?
        if death(circle) is False:
            nextcirclepop.append(circle)
            circle.draw()
    circles = nextcirclepop

    textsurface = font.render('` : console', False, (255, 255, 255))
    screen.blit(textsurface, (0, 0))

    pygame.display.flip()
    clock.tick(PROGRAM_FPS)
pygame.quit()




