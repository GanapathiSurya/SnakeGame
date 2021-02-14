import pygame
import time
import random
#initialize the pygame window
pygame.init()
clock = pygame.time.Clock()
orangecolor = (255, 123, 7)
blackcolor = (0,0,0)
redcolor = (213,80,0)
greencolor = (0,255,0)
bluecolor = (50,153,213)
#display's window width and height
display_width = 600
display_height = 400
dis = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("snake game")
snake_block=10
snake_speed = 15

snake_list = []
#defines the snake's structure and position
def snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, orangecolor, [x[0],x[1], snake_block, snake_block])

def snake_game():
    game_over = False
    game_end = False
    #coordinates of the snake
    x1 = display_width / 2
    y1 = display_height / 2
    #when snake moves
    x1_change = 0
    y1_change = 0

    snake_list =[]
    length_of_snake = 1

    foodx = round(random.randrange(0,display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_end == True:
            dis.fill(bluecolor)
            font_style = pygame.font.SysFont("comicsansms",25)
            msg = font_style.render("You lost!Wanna play again Press P",True,redcolor)
            dis.blit(msg,[display_width / 6,display_height / 3])


            score = length_of_snake - 1
            score_font = pygame.font.SysFont("comicsansms",35)
            value = score_font.render("Your score:" + str(score), True, greencolor)
            dis.blit(value,[display_width / 3,display_height / 5])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        snake_game()
                if event.type == pygame.QUIT:
                    game_over = True #game window is still open
                    game_end =  False #game has ended


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_end = True
        #updates coordinates with changes in positions
        x1 += x1_change
        y1 += y1_change

        dis.fill(blackcolor)
        pygame.draw.rect(dis,greencolor,[foodx,foody,snake_block,snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if(len(snake_list) > length_of_snake):
            print("Snake list",snake_list)
            del snake_list[0]
        for x in snake_list[:-1]:
            print("snake list[:-1]",snake_list[:-1])
            print("snake head",snake_head)
            if x == snake_head:
                game_end = True
        snake(snake_block,snake_list)
        pygame.display.update()

        #when snake hits food length is increased by 1
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0,display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
snake_game()