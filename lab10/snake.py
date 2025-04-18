import pygame
import random
import sys
import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    host = "localhost",
    user = "www",
    password = "12345",
    database = "pp2",
)
cur = conn.cursor()

# Логин пользователя
username = input("Enter your username: ")
cur.execute("SELECT id, level FROM users WHERE username = %s", (username,))
user = cur.fetchone()

if user:
    user_id, level = user
    print(f"Welcome back, {username}! Current level: {level}")
else:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()
    level = 1
    print(f"Welcome, new player {username}!")

# Инициализация pygame
pygame.init()
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game with Levels')
font = pygame.font.SysFont("Verdana", 20)
clock = pygame.time.Clock()

# Цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)
YELLOW = (255, 255, 0)

# Стены
walls = []
def load_walls(level):
    walls.clear()
    thickness = level
    for x in range(0, WIDTH, CELL_SIZE):
        for t in range(thickness):
            walls.append((x, t * CELL_SIZE))
            walls.append((x, HEIGHT - CELL_SIZE * (t + 1)))
    for y in range(0, HEIGHT, CELL_SIZE):
        for t in range(thickness):
            walls.append((t * CELL_SIZE, y))
            walls.append((WIDTH - CELL_SIZE * (t + 1), y))

# Начальные значения
load_walls(level)
snake = [(100, 100), (80, 100), (60, 100)]
direction = 'RIGHT'
speed = 10 + (level - 1) * 2
score = 0

# Генерация еды
def generate_food():
    while True:
        x = random.randint(1, (WIDTH // CELL_SIZE) - 2) * CELL_SIZE
        y = random.randint(1, (HEIGHT // CELL_SIZE) - 2) * CELL_SIZE
        if (x, y) not in snake and (x, y) not in walls:
            weight = random.choice([1, 2, 3])
            timer = random.randint(300, 600)
            return (x, y, weight, timer)

foods = [generate_food() for _ in range(3)]

# Отрисовка
def draw_elements():
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))
    for food in foods:
        color = RED if food[2] == 1 else YELLOW if food[2] == 2 else WHITE
        pygame.draw.rect(screen, color, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))
    for wall in walls:
        pygame.draw.rect(screen, BLUE, pygame.Rect(wall[0], wall[1], CELL_SIZE, CELL_SIZE))
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 120, 10))

def check_collision():
    head = snake[0]
    return head in walls or head in snake[1:]

# Основной игровой цикл
running = True
while running:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != 'DOWN':
        direction = 'UP'
    elif keys[pygame.K_DOWN] and direction != 'UP':
        direction = 'DOWN'
    elif keys[pygame.K_LEFT] and direction != 'RIGHT':
        direction = 'LEFT'
    elif keys[pygame.K_RIGHT] and direction != 'LEFT':
        direction = 'RIGHT'
    elif keys[pygame.K_p]:  # Сохранение игры
        cur.execute(
            "INSERT INTO user_score (user_id, score) VALUES (%s, %s)",
            (user_id, score)
        )
        cur.execute("UPDATE users SET level = %s WHERE id = %s", (level, user_id))
        conn.commit()
        print("Game paused & progress saved!")
        running = False

    # Движение змейки
    x, y = snake[0]
    if direction == 'UP': y -= CELL_SIZE
    elif direction == 'DOWN': y += CELL_SIZE
    elif direction == 'LEFT': x -= CELL_SIZE
    elif direction == 'RIGHT': x += CELL_SIZE
    new_head = (x, y)
    snake.insert(0, new_head)

    ate = False
    for food in foods:
        if new_head[0] == food[0] and new_head[1] == food[1]:
            score += food[2]
            foods.remove(food)
            foods.append(generate_food())
            ate = True
            if score % 5 == 0:
                level += 1
                speed += 2
                load_walls(level)
            break

    if not ate:
        snake.pop()

    # Таймер еды
    for food in foods[:]:
        index = foods.index(food)
        new_timer = food[3] - 1
        if new_timer <= 0:
            foods.remove(food)
            foods.append(generate_food())
        else:
            foods[index] = (food[0], food[1], food[2], new_timer)

    if check_collision():
        print("Game Over!")
        cur.execute("INSERT INTO user_score (user_id, score) VALUES (%s, %s)", (user_id, score))
        cur.execute("UPDATE users SET level = %s WHERE id = %s", (level, user_id))
        conn.commit()
        running = False

    draw_elements()
    pygame.display.update()

# Завершение
pygame.quit()
cur.close()
conn.close()
sys.exit()
