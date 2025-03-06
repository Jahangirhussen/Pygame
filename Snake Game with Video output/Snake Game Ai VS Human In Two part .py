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

# Snake default position and body for both human and AI
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

ai_snake_position = [500, 50]
ai_snake_body = [[500, 50], [490, 50], [480, 50], [470, 50]]

# Fruit position
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True

# Directions
direction = 'RIGHT'
ai_direction = 'RIGHT'

# Scores
human_score = 0
ai_score = 0

# Timer
start_time = time.time()
game_duration = 60  # 1 minute

# Function to display text on the screen
def show_text(text, x, y, color, font_size):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    game_window.blit(text_surface, (x, y))

# Function to move a snake
def move_snake(direction, position):
    if direction == 'UP': position[1] -= 10
    elif direction == 'DOWN': position[1] += 10
    elif direction == 'LEFT': position[0] -= 10
    elif direction == 'RIGHT': position[0] += 10
    return position

# AI logic to follow the fruit
def ai_move():
    global ai_direction
    if ai_snake_position[0] < fruit_position[0]: ai_direction = 'RIGHT'
    elif ai_snake_position[0] > fruit_position[0]: ai_direction = 'LEFT'
    elif ai_snake_position[1] < fruit_position[1]: ai_direction = 'DOWN'
    elif ai_snake_position[1] > fruit_position[1]: ai_direction = 'UP'

# Game over function
def game_over(winner):
    font = pygame.font.Font(None, 50)
    game_over_surface = font.render(f'{winner} Wins!', True, red)
    game_over_rect = game_over_surface.get_rect(center=(window_x / 2, window_y / 4))
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main game loop
while True:
    # Check if game time has expired
    elapsed_time = time.time() - start_time
    if elapsed_time >= game_duration:
        if human_score > ai_score:
            game_over("Human")
        elif ai_score > human_score:
            game_over("AI")
        else:
            game_over("Draw")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN': direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP': direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT': direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT': direction = 'RIGHT'

    # Move human and AI snakes
    snake_position = move_snake(direction, snake_position)
    ai_move()
    ai_snake_position = move_snake(ai_direction, ai_snake_position)

    # Snake growth and fruit spawn
    for snake, body, score, position in [(snake_position, snake_body, human_score, fruit_position), 
                                         (ai_snake_position, ai_snake_body, ai_score, fruit_position)]:
        body.insert(0, list(snake))
        if snake == position:
            score += 10
            fruit_spawn = False
        else:
            body.pop()

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                              random.randrange(1, (window_y // 10)) * 10]
            fruit_spawn = True

    # Draw everything
    game_window.fill(black)

    # Draw the dividing line
    pygame.draw.line(game_window, white, (window_x // 2, 0), (window_x // 2, window_y), 5)

    # Show name and ID
    show_text("Jahangir Hussen", 10, window_y - 50, white, 30)
    show_text("CSE2201025011", 10, window_y - 30, white, 30)

    # Draw human snake (left side)
    for pos in snake_body: pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    
    # Draw AI snake (right side)
    for pos in ai_snake_body: pygame.draw.rect(game_window, red, pygame.Rect(pos[0], pos[1], 10, 10))
    
    # Draw fruit
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Game over conditions for both players (boundary check)
    if snake_position[0] < 0 or snake_position[0] >= window_x // 2 or \
       snake_position[1] < 0 or snake_position[1] >= window_y or \
       snake_position in snake_body[1:]:
        game_over("AI")

    if ai_snake_position[0] >= window_x // 2 or ai_snake_position[0] >= window_x or \
       ai_snake_position[1] < 0 or ai_snake_position[1] >= window_y or \
       ai_snake_position in ai_snake_body[1:]:
        game_over("Human")

    # Display scores
    show_text(f"Human Score: {human_score}", 10, 10, white, 20)
    show_text(f"AI Score: {ai_score}", window_x - 150, 10, white, 20)

    # Refresh screen
    pygame.display.update()
    fps.tick(snake_speed)
