import pygame
import random
import sys

pygame.init()

# Config 
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Better snake')
BLACK = (0, 0, 0)
GREEN = (50, 205, 50) 
RED = (255, 69, 0)  
WHITE = (255, 255, 255)
BLUE = (100, 149, 237) 
GOLD = (255, 215, 0) 
font = pygame.font.SysFont("Verdana", 20)

# Game config
snake = [(100, 100), (80, 100), (60, 100)]
direction = 'RIGHT'
speed = 10
score = 0
level = 1
food_timer = 0
food_timeout = 100

# Стены
walls = []
for x in range(0, WIDTH, CELL_SIZE):
    walls.append((x, 0))
    walls.append((x, HEIGHT - CELL_SIZE))
for y in range(0, HEIGHT, CELL_SIZE):
    walls.append((0, y))
    walls.append((WIDTH - CELL_SIZE, y))

# Food generation
def generate_food():
    while True:
        x = random.randint(1, (WIDTH // CELL_SIZE) - 2) * CELL_SIZE
        y = random.randint(1, (HEIGHT // CELL_SIZE) - 2) * CELL_SIZE
        if (x, y) not in snake and (x, y) not in walls:
            # Food value 
            weight = random.choices([1, 2, 3], weights=[0.6, 0.3, 0.1])[0]
            return (x, y, weight)

food = generate_food()

# Drawing
def draw_elements():
    screen.fill(BLACK)

    # Snake generation + gradient
    for i, segment in enumerate(snake):
        color_intensity = 150 + (i * 10) % 100  # Изменение интенсивности цвета
        color = (0, color_intensity, 0)  # Градиентный цвет
        pygame.draw.rect(screen, color, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # Food generation value based
    if food[2] == 1:
        pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))
    elif food[2] == 2:
        pygame.draw.rect(screen, GOLD, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))
    else:
        pygame.draw.rect(screen, BLUE, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))

    # Walls generation
    for wall in walls:
        pygame.draw.rect(screen, BLUE, pygame.Rect(wall[0], wall[1], CELL_SIZE, CELL_SIZE))

    # Counter display
    score_text = font.render(f"Счет: {score}", True, WHITE)
    level_text = font.render(f"Уровень: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 120, 10))

# Collision listener
def check_collision():
    head = snake[0]
    if head in walls or head in snake[1:]:
        return True
    return False

# Game cycle
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(speed)

    # Event listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Snake coordination
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != 'DOWN':
        direction = 'UP'
    elif keys[pygame.K_DOWN] and direction != 'UP':
        direction = 'DOWN'
    elif keys[pygame.K_LEFT] and direction != 'RIGHT':
        direction = 'LEFT'
    elif keys[pygame.K_RIGHT] and direction != 'LEFT':
        direction = 'RIGHT'

    # Snake movement
    x, y = snake[0]
    if direction == 'UP':
        y -= CELL_SIZE
    elif direction == 'DOWN':
        y += CELL_SIZE
    elif direction == 'LEFT':
        x -= CELL_SIZE
    elif direction == 'RIGHT':
        x += CELL_SIZE
    new_head = (x, y)
    snake.insert(0, new_head)

    # Food collision
    if new_head == (food[0], food[1]):
        score += food[2]  # Update score
        food = generate_food()
        food_timer = 0
        if score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    # Food deletion timer
    food_timer += 1
    if food_timer > food_timeout:
        food = generate_food()
        food_timer = 0

    # Wall, body collision checker
    if check_collision():
        print("Игра окончена")
        running = False

    # Drawings
    draw_elements()
    pygame.display.update()

# Exit
pygame.quit()
sys.exit()
