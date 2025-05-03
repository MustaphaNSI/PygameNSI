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
bord4 = pygame.Rect(632,-10,250,50)
bord5 = pygame.Rect(-10,-10,150,50)
balle0 = pygame.image.load("Ammo0.png")
balle1 = pygame.image.load("Ammo1.png")
balle2 = pygame.image.load("Ammo2.png")
balle3 = pygame.image.load("Ammo3.png")
balle4 = pygame.image.load("Ammo4.png")
balle5 = pygame.image.load("Ammo5.png")
balle = [balle0,balle1,balle2,balle3,balle4,balle5]
totballes = 20
balles = 5
score = 0
icona = pygame.image.load("iconalive.png")
icona = pygame.transform.scale(icona, (30,30))
icond = pygame.image.load("icondead.png")
icond = pygame.transform.scale(icond, (30,30))
iconligne1 = [icona,icona,icona,icona,icona,icona,icona,icona,icona,icona]
iconligne2 = [icona,icona,icona,icona,icona,icona,icona,icona,icona,icona]
fond = pygame.image.load("Fond.png")
fond = pygame.transform.scale(fond, (800,800))
daydream20 = pygame.font.Font("Daydream.ttf",20)
daydream27 = pygame.font.Font("Daydream.ttf",27)
daydream50 = pygame.font.Font("Daydream.ttf",50)
ducka1 = pygame.image.load("duckA1.png")
ducka1 = pygame.transform.scale(ducka1, (100,100))
ducka2 = pygame.image.load("duckA2.png")
ducka2 = pygame.transform.scale(ducka2, (100,100))
ducka3 = pygame.image.load("duckA3.png")
ducka3 = pygame.transform.scale(ducka3, (100,100))
duckb1 = pygame.image.load("duckB1.png")
duckb1 = pygame.transform.scale(duckb1, (100,100))
duckb2 = pygame.image.load("duckB2.png")
duckb2 = pygame.transform.scale(duckb2, (100,100))
duckb3 = pygame.image.load("duckB3.png")
duckb3 = pygame.transform.scale(duckb3, (100,100))
duckaf1 = pygame.image.load("duckaf1.png")
duckaf1 = pygame.transform.scale(duckaf1, (100,100))
duckaf2 = pygame.image.load("duckaf2.png")
duckaf2 = pygame.transform.scale(duckaf2, (100,100))
duckaf3 = pygame.image.load("duckaf3.png")
duckaf3 = pygame.transform.scale(duckaf3, (100,100))
duckbf1 = pygame.image.load("duckbf1.png")
duckbf1 = pygame.transform.scale(duckbf1, (100,100))
duckbf2 = pygame.image.load("duckbf2.png")
duckbf2 = pygame.transform.scale(duckbf2, (100,100))
duckbf3 = pygame.image.load("duckbf3.png")
duckbf3 = pygame.transform.scale(duckbf3, (100,100))
duckad = pygame.image.load("duckAD.png")
duckad = pygame.transform.scale(duckad, (100,100))
duckbd = pygame.image.load("duckBD.png")
duckbd = pygame.transform.scale(duckbd, (100,100))
animducka = [ducka1,ducka2,ducka3]
animduckb = [duckb1,duckb2,duckb3]
animduckaf = [duckaf1,duckaf2,duckaf3]
animduckbf = [duckbf1,duckbf2,duckbf3]
frame = 0
ducks = []
directions = []
ducktypes = []
ducketat = []
duckrounds = [1, 2, 2, 3, 3, 4, 5]
vitesse = [10, 16, 20, 22, 24, 28, 32]
rounds = 0
totducks = 20
ducksmort = 0
duckspawn = 0
d = vitesse[rounds]
tempsdebut = pygame.time.get_ticks()

def dessins():
    global imagelunette, positionlunette, balles, bord1, totballes, directions, ducks,  tempsecoule
    fenetre.fill((125,125,200))
    fenetre.blit(fond,(0,0))
    pygame.draw.rect(fenetre, (30,30,150) , bord1, 8)
    pygame.draw.rect(fenetre, (30,30,150) , bord2, 8)
    pygame.draw.rect(fenetre, (30,30,150) , bord3, 8)
    pygame.draw.rect(fenetre, (30,30,150) , bord4, 8)
    pygame.draw.rect(fenetre, (30,30,150) , bord5, 8)
    pygame.draw.rect(fenetre, (20,20,20) , (-10,-10,142,42))
    pygame.draw.rect(fenetre, (20,20,20) , (55,630,114,104))
    pygame.draw.rect(fenetre, (20,20,20) , (218,630,364,104))
    pygame.draw.rect(fenetre, (20,20,20) , (631,630,114,104))
    pygame.draw.rect(fenetre, (20,20,20) , (640,0,250,34))
    surfaceballe = daydream20.render("Ammo left :" + str(totballes),True,pygame.Color(255,120,120))
    surfacescore1 = daydream20.render("score",True,pygame.Color(255,255,255))
    surfacescore2 = daydream27.render(str(score),True,pygame.Color(255,255,120))
    surfaceround = daydream20.render("Round: " + str(rounds), True, (255, 255, 255))
    fenetre.blit(surfaceround, (642, 2))
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
    for i in range(len(ducks)):
        if ducketat[i] == "alive":
            if tempsecoule<5:
                if ducktypes[i] == 'a':
                    if directions[i] == 1:
                        image = animducka[frame]
                    else:
                        image = pygame.transform.flip(animducka[frame], True, False)
                else:
                    if directions[i] == 1:
                        image = animduckb[frame]
                    else:
                        image = pygame.transform.flip(animduckb[frame], True, False)
            else:
                if ducktypes[i] == 'a':
                    image = animduckaf[frame]
                else:
                    image = animduckbf[frame]
        else:
            if ducktypes[i] == 'a':
                    image = duckad  
            else:
                    image = duckbd
            ducks[i] = (ducks[i][0], ducks[i][1] + 5)
        fenetre.blit(image, ducks[i])
    tempsecoule = (pygame.time.get_ticks() - tempsdebut) / 1000
    tempsrestant = max(0, (5 - tempsecoule))
    surfacechrono = daydream20.render("Time : " + str(int(tempsrestant)), True, (255, 255, 255))
    fenetre.blit(surfacechrono, (2, 2))
    fenetre.blit(imagelunette, positionlunette)
    pygame.display.flip()

def debut():
 pass
def transition(roundn):
    fenetre.blit(fond,(-1,-1))
    surfaceroundt = daydream50.render("Round " + str(roundn), True, (255, 150, 150))
    fenetre.blit(surfaceroundt, (240,350))
    pygame.display.flip()
    pygame.time.wait(1000)

def fin():
    pass
def controles():
    global positionlunette, check, balles, score, rounds, totballes, check1, icond, iconligne2, iconligne1, ducksmort
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           continuer = False
    if pygame.key.get_pressed()[pygame.K_r] == False:
       check1 = False
    if pygame.key.get_pressed()[pygame.K_r] == True and check1 == False:
       check1 = True
       if totballes>0:
           pygame.mixer.music.load("recharge.mp3")
           pygame.mixer.music.play()
           recharge = min(5 - balles, totballes)
           totballes -= recharge
           balles += recharge
    if pygame.mouse.get_pressed()[0] == False:
       check = False
    if pygame.mouse.get_pressed()[0] == True and check == False :
       check = True
       if balles>0:  
           pygame.mixer.music.load("tir.mp3")
           pygame.mixer.music.play()
           balles = balles - 1
           for i in range(len(ducks)):
              rectduck = pygame.Rect(ducks[i],(100,100))
              if rectduck.collidepoint(positionlunette) == True:
                 score = score + 100
                 ducketat[i] = "dead"
                 ducksmort = ducksmort+ 1                      
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
   tempsecoule = (pygame.time.get_ticks() - tempsdebut) / 1000
   tempsrestant = max(0, (5000 - tempsecoule*1000) // 1000)
   tic += 1
   if tic >= intervalle:
        tic = 0
        frame = (frame + 1) % 3
 
   positionsgrille = [(x, y) for x in range(50, 700, 100) for y in range(50, 423, 100)]
   while duckspawn < duckrounds[rounds] and len(ducks) < duckrounds[rounds]:
     if len(positionsgrille) > 0:
       pos = random.choice(positionsgrille)
       ducks.append(pos) 
       positionsgrille.remove(pos)
       directions.append(random.choice([-1, 1]))
       ducktypes.append(random.choice(['a', 'b']))
       ducketat.append("alive")
       duckspawn = duckspawn +1
       
   for i in range(len(ducks)-1, -1, -1):
    if ducketat[i] == "dead" and ducks[i][1] > 423 or tempsecoule >= 5 and ducks[i][1] < -100:
        del ducks[i]
        del directions[i]
        del ducketat[i]
        
        
   for i in range(len(ducks)):
      if ducketat[i] == "alive":
          if tempsecoule < 5:
               ducks[i] = (ducks[i][0] + d * directions[i], ducks[i][1])
          else:
               ducks[i] = (ducks[i][0] + 5 , ducks[i][1]-5)
      else:
          ducks[i] = (ducks[i][0], ducks[i][1]+10)
      if ducks[i][0] < 0 or ducks[i][0] > 700:
        directions[i] *= -1
        
   if len(ducks) == 0 and duckspawn == duckrounds[rounds] and ducksmort<=totducks:
      rounds = rounds + 1
      duckspawn = 0
      transition(rounds)
      tempsdebut = pygame.time.get_ticks()
    
   if 0 < ducksmort <= 10:
        for i in range(ducksmort):
            iconligne1[i] = icond
   elif 10 < ducksmort <= 20:
        for i in range(10):
            iconligne1[i] = icond
        for i in range(ducksmort - 10):
            iconligne2[i] = icond
    
   if iconligne2[-1] == "icond":
      pygame.mixer.music.load("win.mp3")
      pygame.mixer.music.play()
      score = score + (totballes*100)
   elif iconligne2[-1] == "icona" and totballes == 0:
      pygame.mixer.music.load("lose.mp3")
      pygame.mixer.music.play()
      
pygame.quit()      
