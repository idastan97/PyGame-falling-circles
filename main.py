import pygame
import random

pygame.init()

w, h = 400, 300
size = w, h

screen = pygame.display.set_mode(size)

running = True
screen_bottom = pygame.Surface(screen.get_size())
clock = pygame.time.Clock()
moving_circles = []
new_circles = []
SPEED = 100
RADIUS = 10

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_circles.append((
                event.pos,
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            ))
    screen.fill(pygame.Color("black"))
    screen.blit(screen_bottom, (0, 0))
    new_moving_circles = []
    for pos, color in new_circles:
        pygame.draw.circle(screen, color, (pos[0], pos[1]), RADIUS)
        new_moving_circles.append((pos, color))
    for pos, color in moving_circles:
        pygame.draw.circle(screen, color, (pos[0], int(pos[1])), RADIUS)

    global_ticks = clock.tick()
    for pos, color in moving_circles:
        new_pos = pos[0], pos[1] + SPEED * global_ticks / 1000
        if new_pos[1] >= h - RADIUS:
            pygame.draw.circle(screen_bottom, color, (pos[0], h - RADIUS), RADIUS)
        else:
            # pygame.draw.circle(screen, color, new_pos, RADIUS)
            new_moving_circles.append((new_pos, color))

    moving_circles = new_moving_circles
    new_circles = []

    pygame.display.flip()

pygame.quit()
