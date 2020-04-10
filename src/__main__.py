import pygame

from random import random

circles = []

CIRCLE_SIZE = 5
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


class Circle(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.xvel = 0.0
        while self.xvel == 0.0:
            self.xvel = random() - 0.5
        self.yvel = 0.0
        while self.yvel == 0.0:
            self.yvel = random() - 0.5


def init_circles(count):
    for c in range(count):
        circles.append(Circle(random() * WINDOW_WIDTH, random() * WINDOW_HEIGHT))


def update_circles():
    for circle in circles:
        circle.x += circle.xvel
        circle.y += circle.yvel

        if (circle.x < 0) or (circle.x > WINDOW_WIDTH):
            circle.xvel = -circle.xvel

        if (circle.y < 0) or (circle.y > WINDOW_HEIGHT):
            circle.yvel = -circle.yvel


def main():
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

    # Run until the user asks to quit
    running = True

    init_circles(20)

    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((255, 255, 255))

        update_circles()

        for circle in circles:
            # Draw a solid blue circle
            pygame.draw.circle(
                screen, (0, 0, 255), (int(circle.x), int(circle.y)), CIRCLE_SIZE
            )

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()


if __name__ == "__main__":
    main()
