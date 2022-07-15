import pygame
import os
import random

pygame.mixer.init()
pygame.init()
# colours
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)


screen_width = 900
screen_height = 600

gameWindow = pygame.display.set_mode((screen_width, screen_height))
# background image
backimg = pygame.image.load('backpic.jpg')
backimg = pygame.transform.scale(backimg, (screen_width, screen_height)).convert_alpha()
welcm = pygame.image.load('Welcome_txt.jpg')
welcm = pygame.transform.scale(welcm, (screen_width, screen_height)).convert_alpha()
eog = pygame.image.load('end_game.jpg')
eog = pygame.transform.scale(eog, (screen_width, screen_height)).convert_alpha()


pygame.display.set_caption("SnakesByNabeel")
pygame.display.update()
font = pygame.font.SysFont(None, 55)
clock = pygame.time.Clock()



def plot_snake(gameWindow, colour, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, colour, [x, y, snake_size, snake_size])


def text_screen(text, colour, x, y):
    screen_text = font.render(text, True, colour)
    gameWindow.blit(screen_text, [x, y])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(black)
        gameWindow.blit(welcm, (0, 0))
        # text_screen("Welcome to Snakes", white, 260, 250)
        # text_screen("Press SpaceBar to Play", white, 235, 285)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # pygame.mixer.music.load('snake_song.mp3.mp3')
                    # pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)


# Game loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 45
    snake_size = 20
    fps = 60
    velocity_x = 0
    velocity_y = 0
    score = 0
    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(20, screen_height - 20)
    init_velocity = 2
    # speed = 2
    snake_list = []
    snake_length = 1
    pygame.mixer.music.load('snake_song.mp3.mp3')
    pygame.mixer.music.play()
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")

    with open("highscore.txt", "r")as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w")as f:
                f.write(str(highscore))
            gameWindow.fill(black)
            gameWindow.blit(eog, (0, 0))
            # text_screen("Game Over!!!Press Enter to Continue", white, 100, 300)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score += 10
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x - food_x) < 20 and abs(snake_y - food_y) < 20:
                food_x = random.randint(20, screen_width - 20)
                food_y = random.randint(20, screen_height - 20)
                # pygame.mixer.music.pause()
                food_eat = pygame.mixer.Sound('food_eat.wav.wav')
                food_eat.play()
                # pygame.mixer.music.unpause()
                score += 10
                snake_length += 5
                if score > int(highscore):
                    highscore = score

                # for score in range(50, 100):
                #     init_velocity += 2
                # for score in range(100, 150):
                #     init_velocity += 2
                # if score >= 50 and score <= 100:
                #     speed = init_velocity + 2
                #     init_velocity = init_velocity + 2

                if score == 50:
                    init_velocity = init_velocity + 1
                if score == 1000:
                    init_velocity = init_velocity + 1
                if score == 150:
                    init_velocity = init_velocity + 1
                if score == 2000:
                    init_velocity = init_velocity + 1
                if score == 250:
                    init_velocity = init_velocity + 1
                if score == 300:
                    init_velocity = init_velocity + 1
                if score == 350:
                    init_velocity = init_velocity + 1


            gameWindow.fill(black)
            gameWindow.blit(backimg, (0, 0))
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            text_screen("Score:" + str(score) + "  Highscore: "+str(highscore), red, 5, 5)


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('snake_crash2.mp3.mp3')
                pygame.mixer.music.play()
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load('snake_crash2.mp3.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow, white, snake_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
