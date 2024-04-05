import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Настройки окна игры
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Змейка')

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Настройки игры
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
food_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0

# Скорость игры
clock = pygame.time.Clock()
SPEED = 15


# Функция для обновления направления змейки
def change_direction(change_to, direction):
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    return direction


# Функция для отображения счета
def show_score():
    font = pygame.font.SysFont(None, 35)
    score_surface = font.render('Счет : ' + str(score), True, (0, 0, 0))
    screen.blit(score_surface, (10, 10))


# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Обработка ввода
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Обновление направления
    direction = change_direction(change_to, direction)

    # Обновление позиции головы змейки
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Логика змейки и еды
    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
    food_spawn = True

    # Отрисовка
    screen.fill(WHITE)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    show_score()  # Отображение счета

    # Обновление экрана
    pygame.display.flip()

    # Проверка столкновения с границами или с собой
    if snake_pos[0] < 0 or snake_pos[0] > SCREEN_WIDTH - 10:
        pygame.quit()
        sys.exit()
    if snake_pos[1] < 0 or snake_pos[1] > SCREEN_HEIGHT - 10:
        pygame.quit()
        sys.exit()
    for block in snake_body[1:]:
        if snake_pos == block:
            pygame.quit()
            sys.exit()

    clock.tick(SPEED)
