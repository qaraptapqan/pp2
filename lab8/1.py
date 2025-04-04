import pygame
import sys
import random

pygame.init()

we = 600
he = 800
FPS = 60

screen = pygame.display.set_mode((we, he))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

car = pygame.image.load("car.png")
car = pygame.transform.scale(car, (140, 70))
car = pygame.transform.rotate(car, -90)

car_x = we // 2 - 30
car_y = he - 150
speed = 7

enemy = pygame.image.load("enemy.png")
enemy = pygame.transform.scale(enemy, (140, 70))
enemy = pygame.transform.rotate(enemy, 90)

enemy_x = random.randint(50, we - 140 - 50)
enemy_y = -100
enemy_speed = 3

coin = pygame.image.load("coin.png")
coin = pygame.transform.scale(coin, (50, 50))
coin_x = random.randint(50, we - 140 - 50)
coin_y = -100
coin_speed = 3

coin_cnt = 0
score_font = pygame.font.SysFont("Arial", 30)


font = pygame.font.SysFont("Arial", 60)

game_over = False

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x -= speed
        if keys[pygame.K_RIGHT] and car_x < we - 60:
            car_x += speed
        if keys[pygame.K_UP] and car_y > 0:
            car_y -= speed
        if keys[pygame.K_DOWN] and car_y < he - 120:
            car_y += speed

        enemy_y += enemy_speed
        if enemy_y > he:
            enemy_y = -100
            enemy_x = random.randint(50, we - 140 - 50)

        coin_y += coin_speed
        if coin_y > he:
            coin_y = -100
            coin_x = random.randint(50, we - 50 - 50)

        car_rect = pygame.Rect(car_x + 10, car_y + 10, car.get_width() - 20, car.get_height() - 10)
        enemy_rect = pygame.Rect(enemy_x + 10, enemy_y + 10, enemy.get_width() - 20, enemy.get_height() - 10)
        coin_rect = pygame.Rect(coin_x, coin_y, coin.get_width(), coin.get_height())

        if car_rect.colliderect(coin_rect):
            coin_cnt += 1
            coin_y = -100
            coin_x = random.randint(50, we - 50 - 50)

        if car_rect.colliderect(enemy_rect):
            game_over = True

    screen.fill((100, 100, 100))
    screen.blit(car, (car_x, car_y))
    screen.blit(enemy, (enemy_x, enemy_y))
    screen.blit(coin, (coin_x, coin_y))
    score = score_font.render(f"Coins: {coin_cnt}", True, (255, 0, 0))
    screen.blit(score, (we - 150, 20))
    if game_over:
        text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(text, (we // 2 - text.get_width() // 2, he // 2 - text.get_height() // 2))
    pygame.display.flip()

pygame.quit()
sys.exit()
