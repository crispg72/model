import pygame

from random import random

susceptible_people = []
infected_people = []
recovered_people = []

CIRCLE_SIZE = 5
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

SUSCEPTIBLE = 0
IN_RANGE = 1
INFECTED = 2
RECOVERED = 3

TIME_TO_INFECTION = 10


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

        self.count = 0
        self.status = SUSCEPTIBLE


def init_people(count):
    for c in range(count):
        susceptible_people.append(
            Person(random() * WINDOW_WIDTH, random() * WINDOW_HEIGHT)
        )


def close_to_infected(person):
    for infected_person in infected_people:
        if abs(infected_person.x - person.x) > CIRCLE_SIZE:
            continue

        if abs(infected_person.y - person.y) <= CIRCLE_SIZE:
            return True

    return False


def update_people():
    for person in susceptible_people + infected_people:
        person.x += person.xvel
        person.y += person.yvel

        if (person.x < 0) or (person.x > WINDOW_WIDTH):
            person.xvel = -person.xvel

        if (person.y < 0) or (person.y > WINDOW_HEIGHT):
            person.yvel = -person.yvel

    # See if any of the susceptible people are near an infected person
    new_infections = []
    for person in susceptible_people:
        if close_to_infected(person):
            if person.status == IN_RANGE:
                person.count -= 1
                if person.count < 0:
                    # another infection
                    person.status = INFECTED
                    new_infections.append(person)
            else:
                person.status = IN_RANGE
                person.count = TIME_TO_INFECTION
        else:
            if person.status == IN_RANGE:
                person.status = SUSCEPTIBLE

    if len(new_infections) > 0:
        for person in new_infections:
            susceptible_people.remove(person)
            infected_people.append(person)


def main():
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

    # Run until the user asks to quit
    running = True

    init_people(20)

    # Start with one infection
    infected_people.append(susceptible_people.pop())

    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((255, 255, 255))

        update_people()

        for person in susceptible_people:
            # Draw a solid blue circle
            pygame.draw.circle(
                screen, (0, 0, 255), (int(person.x), int(person.y)), CIRCLE_SIZE
            )
        for person in infected_people:
            pygame.draw.circle(
                screen, (255, 0, 0), (int(person.x), int(person.y)), CIRCLE_SIZE
            )

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()


if __name__ == "__main__":
    main()
