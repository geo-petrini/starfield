import random
import pygame
from pygame.locals import *
from pygame.color import THECOLORS

# Constants
NUM_STARS = 140
SCREEN_SIZE = [1024, 900]
LEFT = 0
RIGHT = 1
X = 'x'
Y = 'y'

def initStars(screen):
    "Create the starfield"

    # The starfield is represented as a dictionary of x and y values.
    stars = []

    # Create a list of (x,y) coordinates.
    for loop in range(0, NUM_STARS):
        star = {X:random.randrange(0, screen.get_width() - 1), Y:random.randrange(0, screen.get_height() - 1)}
        # star = [random.randrange(0, screen.get_width() - 1),
        #         random.randrange(0, screen.get_height() - 1)]
        stars.append(star)

    return stars


def moveStars(screen, stars, start, end, direction):
    "Correct for stars hitting the screen's borders"

    for loop in range(start, end):
        moveStar(screen, stars, loop, direction)

    return stars

def moveStar(screen, stars, starindex, direction):
    if (direction == LEFT):
        if (stars[starindex][X] != 1):
            stars[starindex][X] = stars[starindex][X] - 1
        else:
            stars[starindex][Y] = random.randrange(0, screen.get_height() - 1)
            stars[starindex][X] = screen.get_width() - 1
    elif (direction == RIGHT):
        if (stars[starindex][X] != screen.get_width() - 1):
            stars[starindex][X] = stars[starindex][X] + 1
        else:
            stars[starindex][Y] = random.randrange(0, screen.get_height() - 1)
            stars[starindex][X] = 1

def process_first_field(screen, stars, direction):
    for index in range(0, 10):
        screen.set_at([stars[index][X], stars[index][Y]], THECOLORS['black'])

    stars = moveStars(screen, stars, 0, 10, direction)
    for index in range(0, 10):
        screen.set_at([stars[index][X], stars[index][Y]], THECOLORS['darkgoldenrod1'])

    return stars

def process_second_field(screen, stars, direction):
    for index in range(11, 20):
        screen.set_at([stars[index][X], stars[index][Y]], THECOLORS['black'])

    stars = moveStars(screen, stars, 11, 20, direction)

    for index in range(11, 20):
        screen.set_at([stars[index][X], stars[index][Y]], THECOLORS['red'])

    return stars

def process_third_field(screen, stars, direction):
    for index in range(21, NUM_STARS):
        screen.set_at([stars[index][X], stars[index][Y]], THECOLORS['black'])

    stars = moveStars(screen, stars, 21, NUM_STARS, direction)

    for index in range(21, NUM_STARS):
        screen.set_at([stars[index][X], stars[index][Y]], THECOLORS['grey'])

    return stars

def main():
    "Main starfield code"

    random.seed()

    # Initialize the pygame library.
    pygame.init()
    # screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE | DOUBLEBUF | FULLSCREEN)
    screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE|DOUBLEBUF)
    pygame.display.set_caption("Starfield")
    pygame.mouse.set_visible(0)

    # Set the background to black.
    screen.fill(THECOLORS['black'])

    # Simulation variables.
    delay = 8
    field_slow_factor = 2
    direction = LEFT

    # Create the starfield.
    stars = initStars(screen)

    # Main loop
    while True:
        # Handle input events.
        event = pygame.event.poll()
        if (event.type == QUIT):
            break
        elif (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                break
            elif (event.key == K_UP):
                if (delay >= 1):
                    delay = delay - 1
            elif (event.key == K_DOWN):
                if (delay <= 32):
                    delay = delay + 1
            elif (event.key == K_LEFT):
                direction = LEFT
            elif (event.key == K_RIGHT):
                direction = RIGHT

        # Used to slow down the second and third field.
        field_slow_factor = field_slow_factor + 1

        process_first_field(screen, stars, direction)

        # Second star field algorythms.
        if (field_slow_factor % 2 == 0):
            process_second_field(screen, stars, direction)

        # Third star field algorythms.
        if (field_slow_factor % 5 == 0):
            process_third_field(screen, stars, direction)

        # Control the starfield speed.
        pygame.time.delay(delay)

        # Make sure this variable doesn't get too large.
        # Reset slow factor
        if (field_slow_factor == 500):
            field_slow_factor = 2

        # Update the screen.
        pygame.display.update()


# Start the program.
if __name__ == '__main__':
    main()
