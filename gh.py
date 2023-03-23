from pygame import *
from random import *
class vjy(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,x,y):
        super(). __init__()
        self.image = transform.scale(image.load(player_image), (x, y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
class Player(vjy):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def lyktxu(self):
        s = vjyx("iu.jpg", self.rect.centerx, self.rect.top, 10, 30 , 70)
        piy.add(s)
class vra(vjy):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1
class vjyx(vjy):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

        
lost = 0       
scr = 0
win_width=500
win_height=500
okno = display.set_mode((win_width, win_height))
display.set_caption("?#########?##?##?#/3#?#??#?#?#??#//33//")
rui = transform.scale(image.load("yui.jpg"), (win_width , win_height))
ppaapp=Player("ocr (1).jpg",0,0,5,50,50)
monstr = sprite.Group()
piy = sprite.Group()
for i in range(1,30):
    yu = vra("lav.jpg", randint(80, win_width), 0, randint(1 , 40), 10, 60)
    monstr.add(yu)
game = True
finish=False
font.init()
font2 = font.Font(None, 20)

while game:  
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ppaapp.lyktxu()
             
    if not(finish):
        okno.blit(rui,(0, 0))
        ppaapp.reset()
        ppaapp.update()
        monstr.update()
        monstr.draw(okno)
        piy.update()
        piy.draw(okno)
        collides = sprite.groupcollide(monstr, piy, True, True)
        for c in collides:
            # этот цикл повторится столько раз, сколько монстров подбито
            scr = scr + 1
            yu = vra("lav.jpg", randint(80, win_width), 0, randint(1 , 40), 10, 60)
            monstr.add(yu)
        text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        okno.blit(text_lose, (10, 50))
        text = font2.render("Счет: " + str(scr), 1, (255, 255, 255))
        okno.blit(text, (10, 20))


        # возможный проигрыш: пропустили слишком много или герой столкнулся с врагом
        #if sprite.spritecollide(ppaapp, monstr, False):
        #    finish = True # проиграли, ставим фон и больше не управляем спрайтами.
            #okno.blit(lose, (200, 200))    
        display.update()