import pygame

from random import random

people = []

CIRCLE_SIZE = 5
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


class Person(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.xvel = 0.0
        while self.xvel == 0.0:
            self.xvel = random() - 0.5
        self.yvel = 0.0
        while self.yvel == 0.0:
            self.yvel = random() - 0.5


def init_people(count):
    for c in range(count):
        people.append(Person(random() * WINDOW_WIDTH, random() * WINDOW_HEIGHT))


def update_people():
    for person in people:
        person.x += person.xvel
        person.y += person.yvel

        if (person.x < 0) or (person.x > WINDOW_WIDTH):
            person.xvel = -person.xvel

        if (person.y < 0) or (person.y > WINDOW_HEIGHT):
            person.yvel = -person.yvel


def main():
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

    # Run until the user asks to quit
    running = True

    init_people(200)

    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((255, 255, 255))

        update_people()

        for person in people:
            # Draw a solid blue circle
            pygame.draw.circle(
                screen, (0, 0, 255), (int(person.x), int(person.y)), CIRCLE_SIZE
            )

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()


if __name__ == "__main__":
    main()
