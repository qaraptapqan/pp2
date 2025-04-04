import pygame
import sys
import random
import time

pygame.init()

we, he = 800, 600
c_size = 20
screen = pygame.display.set_mode((we, he))
pygame.display.set_caption("Snake")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

clock = pygame.time.Clock()
snake_speed = 5
snake = [(100, 100), (80, 100), (60,100)]

direction = "RIGHT"

def random_food():
    while True:
        x = random.randint(0, (we - c_size) // c_size) * c_size
        y = random.randint(0, (he - c_size) // c_size) * c_size
        if (x, y) not in snake:
            return (x, y)

food_pos = random_food()
game_over = False
cnt = 4
q = 0
level = 1
font = pygame.font.SysFont("Arial", 60)
score_font = pygame.font.SysFont("Arial", 30)
running = True

while running:
    clock.tick(snake_speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    if not game_over:
        head_x, head_y = snake[0]
        if direction == 'UP':
            head_y -= c_size
        elif direction == 'DOWN':
            head_y += c_size
        elif direction == 'LEFT':
            head_x -= c_size
        elif direction == 'RIGHT':
            head_x += c_size

        if head_x < 0:
            head_x = we - c_size
        elif head_x >= we:
            head_x = 0
        if head_y < 0:
            head_y = he - c_size
        elif head_y >= he:
            head_y = 0

        new_head = (head_x, head_y)

        if new_head in snake[1:]:
            game_over = True
        else:
            snake.insert(0, new_head)

            if new_head == food_pos:
                food_pos = random_food()
                cnt += 1
                k = cnt // 5
                if k > q:
                    q += 1
                    snake_speed += 2 * k
                    level += 1
            else:
                snake.pop()

    
    screen.fill(BLACK)

    pygame.draw.rect(screen, RED, (food_pos[0], food_pos[1], c_size, c_size))

    for seg in snake:
        pygame.draw.rect(screen, GREEN, (seg[0], seg[1], c_size, c_size))

    score = score_font.render(f"Score: {cnt}", True, WHITE)
    screen.blit(score, (we - 120, 20))

    lvl = score_font.render(f"Level: {level}", True, WHITE)
    screen.blit(lvl, (we - 120, 50))

    if game_over:
        text = font.render("Game Over!", True, RED)
        screen.blit(text, (we // 2 - 150, he // 2 - 30))

    pygame.display.update()


pygame.quit()
sys.exit()
