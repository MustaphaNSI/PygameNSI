import pygame
import random

pygame.init()
pygame.display.set_caption("Shoot")
fenetre = pygame.display.set_mode((800,800))
imagelunette = pygame.image.load("Crosshair.png")
imagelunette = pygame.transform.scale(imagelunette, (20,20))
pygame.mouse.set_visible(False)
check = False
check1 = False
positionlunette = (-10,-10)
bord1 = pygame.Rect(47,622,130,120)
bord2 = pygame.Rect(210,622,380,120)
bord3 = pygame.Rect(623,622,130,120)
balle0 = pygame.image.load("Ammo0.png")
balle1 = pygame.image.load("Ammo1.png")
balle2 = pygame.image.load("Ammo2.png")
balle3 = pygame.image.load("Ammo3.png")
balle4 = pygame.image.load("Ammo4.png")
balle5 = pygame.image.load("Ammo5.png")
balle = [balle0,balle1,balle2,balle3,balle4,balle5]
totballes = 25
balles = 5
score = 0
icona = pygame.image.load("iconalive.png")
icona = pygame.transform.scale(icona, (30,30,))
icond = pygame.image.load("icondead.png")
icond = pygame.transform.scale(icond, (30,30,))
iconligne1 = [icona,icona,icona,icona,icona,icona,icona,icona,icona,icona]
iconligne2 = [icona,icona,icona,icona,icona,icona,icona,icona,icona,icona]
fond = pygame.image.load("Fond.png")
fond = pygame.transform.scale(fond, (800,800))
daydream20 = pygame.font.Font("Daydream.ttf",20)
daydream27 = pygame.font.Font("Daydream.ttf",27)
ducka1 = pygame.image.load("duckA1.png")
ducka1 = pygame.transform.scale(ducka1, (150,150))
ducka2 = pygame.image.load("duckA2.png")
ducka2 = pygame.transform.scale(ducka2, (150,150))
ducka3 = pygame.image.load("duckA3.png")
ducka3 = pygame.transform.scale(ducka3, (150,150))
duckb1 = pygame.image.load("duckB1.png")
duckb1 = pygame.transform.scale(duckb1, (150,150))
duckb2 = pygame.image.load("duckB2.png")
duckb2 = pygame.transform.scale(duckb2, (150,150))
duckb3 = pygame.image.load("duckB3.png")
duckb3 = pygame.transform.scale(duckb3, (150,150))
animducka = [ducka1,ducka2,ducka3]
animduckb = [duckb1,duckb2,duckb3]
frame = 0
duckad = pygame.image.load("duckAD.png")
duckbd = pygame.image.load("duckBD.png")
ducks = []
difficulty = 0

def dessins():
    global imagelunette, positionlunette, balles, bord1, totballes
    fenetre.fill((125,125,200))
    fenetre.blit(fond,(0,0))
    pygame.draw.rect(fenetre, (30,30,150) , bord1, 8)
    pygame.draw.rect(fenetre, (30,30,150) , bord2, 8)
    pygame.draw.rect(fenetre, (30,30,150) , bord3, 8)
    pygame.draw.rect(fenetre, (20,20,20) , (55,630,114,104))
    pygame.draw.rect(fenetre, (20,20,20) , (218,630,364,104))
    pygame.draw.rect(fenetre, (20,20,20) , (631,630,114,104))
    surfaceballe = daydream20.render("Ammo left :" + str(totballes),True,pygame.Color(255,120,120))
    surfacescore1 = daydream20.render("score",True,pygame.Color(255,255,255))
    surfacescore2 = daydream27.render(str(score),True,pygame.Color(255,255,120))
    scorect = surfacescore2.get_rect(topright = (740,675))
    fenetre.blit(balle[balles],(57,629))
    fenetre.blit(surfaceballe,(280,702))
    fenetre.blit(surfacescore1,(633,635))
    fenetre.blit(surfacescore2, scorect)
    for i in range(len(iconligne1)):
        x = 222 + i * 36
        fenetre.blit(iconligne1[i], (x, 632))
    for y in range(len(iconligne2)):
        x = 222 + y * 36
        fenetre.blit(iconligne2[y], (x, 667))
    """for positionduck in ducks:
        if random.randint(1,100)>50:
           fenetre.blit(animduckb[frame], positionduck)
        else:
           fenetre.blit(animducka[frame], positionduck)"""
    fenetre.blit(imagelunette, positionlunette)
    pygame.display.flip()

def controles():
    global positionlunette, check, balles, score, rounds, totballes, check1
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           continuer = False
    if pygame.key.get_pressed()[pygame.K_r] == False:
       check1 = False
    if pygame.key.get_pressed()[pygame.K_r] == True and check1 == False:
       check1 = True
       pygame.mixer.music.load("recharge.mp3")
       pygame.mixer.music.play()
       balles=5
       totballes = totballes - (5-balles)
    if pygame.mouse.get_pressed()[0] == False:
       check = False
    if pygame.mouse.get_pressed()[0] == True and check == False :
       check = True
       if balles>0:  
           pygame.mixer.music.load("tir.mp3")
           pygame.mixer.music.play()
           balles = balles - 1
       else:
          pygame.mixer.music.load("outofammo.wav")
          pygame.mixer.music.play()
         
tic = 0
intervalle = 10
clock = pygame.time.Clock()
Continuer = True
while Continuer == True:
   clock.tick(50)
   dessins()
   controles()
   positionlunette = pygame.mouse.get_pos()
   tic += 1
   if tic >= intervalle:
        tic = 0
        frame = (frame + 1) % 3


pygame.quit()    
