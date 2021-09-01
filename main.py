import pygame
import random
from variables import *
from player import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Gra SNAKE')

clock = pygame.time.Clock()

FONT = pygame.font.SysFont("comicsansms", 35)


def snakeSegments(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], SNAKE_SIZE, SNAKE_SIZE])


def showMessage(text, color, line):
    message = FONT.render(text, False, color)
    screen.blit(message, [WIDTH / 6, (HEIGHT / 3) + line])


def showScore(score):
    message = FONT.render("Wynik: " + str(score), False, BLACK)
    screen.blit(message, [0, 0])


snake_x = WIDTH / 2
snake_y = HEIGHT / 2
snake = player(snake_x, snake_y)


def game():
    run = True
    closeGame = False
    changeX = 0
    changeY = 0
    snakeList = []
    food_x = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0

    while run:
        while closeGame:
            screen.fill(BACKGROUND_COLOR)
            showMessage("Przegrałeś!", RED, 0)
            showMessage("Q - Zamknij", RED, 40)
            showScore(snake.size - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run = False
                        closeGame = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and snake.direction != "DOWN":
                    changeY = -SNAKE_SIZE
                    changeX = 0
                    snake.direction = "UP"
                if event.key == pygame.K_s and snake.direction != "UP":
                    changeY = SNAKE_SIZE
                    changeX = 0
                    snake.direction = "DOWN"
                if event.key == pygame.K_a and snake.direction != "RIGHT":
                    changeX = -SNAKE_SIZE
                    changeY = 0
                    snake.direction = "LEFT"
                if event.key == pygame.K_d and snake.direction != "LEFT":
                    changeX = SNAKE_SIZE
                    changeY = 0
                    snake.direction = "RIGHT"

        if snake.x >= WIDTH or snake.x < 0 or snake.y >= HEIGHT or snake.y < 0:
            closeGame = True
        snake.x += changeX
        snake.y += changeY

        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, GREEN, [food_x, food_y, SNAKE_SIZE, SNAKE_SIZE])
        snakeHead = []
        snakeHead.append(snake.x)
        snakeHead.append(snake.y)
        snakeList.append(snakeHead)
        if len(snakeList) > snake.size:
            del snakeList[0]

        for x in snakeList[:-1]:
            if x == snakeHead:
                closeGame = True

        snakeSegments(snakeList)
        showScore(snake.size - 1)

        pygame.display.update()

        if snake.x == food_x and snake.y == food_y:
            food_x = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0
            snake.size += 1

        clock.tick(FPS)
    pygame.quit()
    quit()


game()
