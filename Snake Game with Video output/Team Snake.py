# Importing libraries
import pygame
import time
import random

# Initialize pygame
pygame.init()

# Game variables
snake_speed = 15
window_x, window_y = 720, 480

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Initialize game window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS controller
fps = pygame.time.Clock()

# Snake default position and body
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Fruit position
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True

# Default direction
direction = 'RIGHT'
change_to = direction

# Score
score = 0

# Function to display text on the screen
def show_text(text, x, y, color, font_size):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    game_window.blit(text_surface, (x, y))

# Game over function
def game_over():
    font = pygame.font.Font(None, 50)
    game_over_surface = font.render('Your Score: ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect(center=(window_x / 2, window_y / 4))
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main game loop
while True:
    # Handling key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    # Update direction
    direction = change_to

    # Move the snake
    if direction == 'UP':
        snake_position[1] -= 10
    elif direction == 'DOWN':
        snake_position[1] += 10
    elif direction == 'LEFT':
        snake_position[0] -= 10
    elif direction == 'RIGHT':
        snake_position[0] += 10

    # Snake growth
    snake_body.insert(0, list(snake_position))
    if snake_position == fruit_position:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]
        fruit_spawn = True

    # Draw everything
    game_window.fill(black)
    
    # Show name and ID in the background
    show_text("Jahangir Hussen", 10, window_y - 50, white, 30)
    show_text("CSE2201025011", 10, window_y - 30, white, 30)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Game over conditions
    if snake_position[0] < 0 or snake_position[0] >= window_x or \
       snake_position[1] < 0 or snake_position[1] >= window_y:
        game_over()

    # Check if snake collides with itself
    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    # Display score
    show_text(f"Score: {score}", 10, 10, white, 20)

    # Refresh screen
    pygame.display.update()
    fps.tick(snake_speed)
