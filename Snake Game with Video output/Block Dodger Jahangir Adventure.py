import pygame
import sys
import random

# Initialize
pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Simple Dodge Game")
clock = pygame.time.Clock()

# Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Font
font = pygame.font.SysFont(None, 24)
big_font = pygame.font.SysFont(None, 40)

# Player and Box sizes
player_width = 40
player_height = 20
box_size = 20

# Player position
player_x = 180
player_y = 580
player_speed = 5

# Create 10 falling boxes
boxes = []
for _ in range(10):
    x = random.randint(0, 400 - box_size)
    y = random.randint(-600, 0)
    boxes.append([x, y])

speed = 3
game_over = False

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key Press
    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < 400 - player_width:
            player_x += player_speed

        # Update boxes
        for i in range(len(boxes)):
            boxes[i][1] += speed
            if boxes[i][1] > 600:
                boxes[i][0] = random.randint(0, 400 - box_size)
                boxes[i][1] = random.randint(-100, 0)

            # Collision check
            if (boxes[i][1] + box_size >= player_y and
                boxes[i][0] + box_size > player_x and
                boxes[i][0] < player_x + player_width):
                game_over = True
                speed = 0

    # Drawing
    screen.fill(BLACK)

    # Draw player
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))

    # Draw player's name (moving with player)
    name_surface = font.render("jahangirhussen", True, WHITE)
    screen.blit(name_surface, (player_x, player_y - 20))

    # Draw falling boxes
    for box in boxes:
        pygame.draw.rect(screen, RED, (box[0], box[1], box_size, box_size))

    # Game Over message
    if game_over:
        death_text = big_font.render("jahangirhussen died for this game", True, RED)
        screen.blit(death_text, (20, 250))

    pygame.display.flip()
    clock.tick(60)
