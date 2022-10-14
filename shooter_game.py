from pygame import*
from random import randint

max_width = 700
max_height = 500
num_of_enemies = 3


class Sprite:
    # конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (80, 80))
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        # класс главного игрока


class Player(Sprite):
    # метод, в котором реализовано управление спрайтом по кнопкам стрелочкам клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y < max_height -5:
            self.rect.y += self.speed

    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < max_height -5:
            self.rect.y += self.speed


# класс мяча
class Ball(Sprite):

    def __init__(self, player_image, player_speed_x, player_speed_y):
        # рандомный спавн:
        self.player_x = max_width/2
        self.player_y = max_height/2
        self.player_y = player_speed_y
        self.player_x = player_speed_x
        Sprite.__init__(self, player_image, self.player_x, self.player_y, player_speed)

    def update(self):
        # движение Y
        if self.rect.y < max_height - 5:
            self.rect.y += self.speed_y
        else:
            self.rect.y *=-1
            self.rect.y+= self.speed_y

#движение X
        if self.rect.x < max_weight - 5 and self.rect.x>5:

            self.rect.x += self.speed_x
        else:
            self.rect.x *=-1
            self.rect.x+= self.player_x
            


# Создаем окошко
display.set_caption("Шутер")
window = display.set_mode((max_width, max_height))

# создаем спрайты
board1 = Player('green_triangle.jpg', 5, 420, 10)
board2 = Player('green_triangle.jpg', max_width-5, 420, 10)
ball= Ball('red_circle.jpg',randint(10,20),randint(10,20))
 
# переменная, отвечающая за то, как кончилась игра
finish = False

fon_img = image.load('background.jpg')
# игровой цикл
while not finish:
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)

    # перебираем все события, которые могли произойти
    for x in event.get():

      #событие нажатия на крестик окошка
        if x.type == QUIT:
            finish = True

    # обновляем фон каждую итерацию
    window.blit(fon_img,(0,0))

    #запускаем движения спрайтов и обновляем их в новом местоположении при каждой итерации цикла
    board1.update_l()
    board1.reset()
    board2.update_r()
    board2.reset()


        ball.update()
        ball.reset()



    # игровая логика

    k=0
    if sprite.collide_rect(ball, board1):
        ball.speed_x *=-1
        ball.speed_y *=-1
    if sprite.collide_rect(ball, board2):
    ball.speed_x *=-1
    ball.speed_y *=-1


        break
    if k ==1:
        break


    for i in range(len(enemies)):
        if sprite.collide_rect(player, enemies[i]) and enemies[i].rect.x - player.rect.x < 90 and enemies[i].rect.x - player.rect.x > -90:
            enemies.pop(i)
            finish = True
            break

    display.update()
