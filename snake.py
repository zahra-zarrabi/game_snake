import random
import time
import pygame

class my_snake:
    def __init__(self):
        self.w=10
        self.h=15
        self.x=width/2
        self.y=height/2
        self.color=(5,5,5)
        self.speed=3
        self.score=0
        self.x_change=0
        self.y_change=0

    def show_snake(self):
        pygame.draw.rect(my_screen,self.color,[self.x,self.y,self.w,self.h])

    def move_snake(self):
        if self.x_change == -1:
            self.x -= self.speed
        elif self.x_change == 1:
            self.x += self.speed
        elif self.y_change == -1:
            self.y -= self.speed
        elif self.y_change == 1:
            self.y += self.speed

    def eatapple(self):
        if (apple.x-apple.r <= self.x <= apple.x + apple.r) and (apple.y - apple.r <= self.y <= apple.y + apple.r):
            return True
        else:
            return False

    def eatpear(self):
        if (pear.x-pear.r <= self.x <= pear.x + pear.r) and (pear.y - pear.r <= self.y <= pear.y+pear.r):
            return True
        else:
            return False

    def eatbomb(self):
        if (bomb.x-bomb.r <= self.x <= bomb.x + bomb.r) and (bomb.y - bomb.r <= self.y <= bomb.y+bomb.r):
            return True
        else:
            return False

class Apple:
    def __init__(self):
        self.r=10
        self.x=random.randint(0,width-3)
        self.y=random.randint(0,height-3)
        # self.color=(255,0,0)
        self.image_apple=pygame.image.load('apple.png')

    def show_apple(self):
        my_screen.blit(self.image_apple,[self.x,self.y])
        # pygame.draw.circle(my_screen,self.color,[self.x,self.y],self.r)

class Pear:
    def __init__(self):
        self.r = 10
        self.x=random.randint(0,width-3)
        self.y=random.randint(0,height-3)
        self.image_pear=pygame.image.load('pear.png')

    def show_pear(self):
        my_screen.blit(self.image_pear,[self.x,self.y])

class Bomb:
    def __init__(self):
        self.r = 10
        self.x = random.randint(0, width-3)
        self.y = random.randint(0, height-3)
        self.image_bomb=pygame.image.load('bomb.png')
    def show_bomb(self):
        my_screen.blit(self.image_bomb,[self.x,self.y])

if __name__=="__main__":

    width=900
    height=600
    my_screen=pygame.display.set_mode((width,height))
    bg = pygame.image.load('background.jpg')
    pygame.mixer.init()
    snake = my_snake()
    apple=Apple()
    pear = Pear()
    bomb=Bomb()
    pygame.mixer.music.load("sound.wav")
    pygame.mixer.music.play()
    clock=pygame.time.Clock()

    while True:
        pygame.display.set_caption('python game made by zahra     score:%d' % snake.score)
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    snake.x_change= -1
                    snake.y_change=0
                elif event.key == pygame.K_RIGHT:
                    snake.x_change = 1
                    snake.y_change = 0
                elif event.key == pygame.K_UP:
                    snake.y_change = -1
                    snake.x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake.y_change = 1
                    snake.x_change = 0

                elif event.key == pygame.quit():
                    pygame.quit()
                    quit()

        if width-snake.w < snake.x or snake.x<0 or height-snake.h<snake.y or snake.y<0 or snake.score<0:
            time.sleep(1)
            print('gameover')
            pygame.quit()
            quit()

        snake.move_snake()
        if snake.eatapple() == True:
            sound=pygame.mixer.Sound("soundeat.wav")
            pygame.mixer.Sound.play(sound)
            snake.h += 2
            snake.speed+=1
            snake.score += 1
            apple = Apple()
        elif snake.eatpear()==True:
            sound = pygame.mixer.Sound("soundeat.wav")
            pygame.mixer.Sound.play(sound)
            snake.h +=2
            snake.speed+=2
            snake.score+=2
            pear=Pear()
        elif snake.eatbomb()==True:
            sound = pygame.mixer.Sound("soundeat.wav")
            pygame.mixer.Sound.play(sound)
            snake.h +=2
            snake.speed+=1
            snake.score -= 1
            bomb=Bomb()

        # my_screen.fill((3,200,0))
        my_screen.blit(bg, (0, 0))
        snake.show_snake()
        apple.show_apple()
        pear.show_pear()
        bomb.show_bomb()
        pygame.display.update()
        clock.tick(30)


