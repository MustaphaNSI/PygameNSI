import pygame
import random

pygame.init()
pygame.display.set_caption("Shoot")
fenetre = pygame.display.set_mode((800,800))
imagelunette = pygame.image.load("Crosshair.png")
imagelunette = pygame.transform.scale(imagelunette, (20,20))
check = False
check1 = False
check3 = False
check4 = False
positionlunette = (-10,-10)
bord0 = pygame.Rect(0,0,800,800)
bord1 = pygame.Rect(47,622,130,120)
bord3 = pygame.Rect(623,622,130,120)
bord4 = pygame.Rect(610,-10,250,50)
bord5 = pygame.Rect(-10,-10,150,50)
rectstart = pygame.Rect(250,500,287,87)
rectquitter = pygame.Rect(300, 380, 200, 60)
balle0 = pygame.image.load("Ammo0.png")
balle1 = pygame.image.load("Ammo1.png")
balle2 = pygame.image.load("Ammo2.png")
balle3 = pygame.image.load("Ammo3.png")
balle4 = pygame.image.load("Ammo4.png")
balle5 = pygame.image.load("Ammo5.png")
balle = [balle0,balle1,balle2,balle3,balle4,balle5]
balles = 5
score = 0
fond = pygame.image.load("Fond.png")
fond = pygame.transform.scale(fond, (800,800))
logo = pygame.image.load("logo.png")
logo = pygame.transform.scale(logo, (760,300))
daydream20 = pygame.font.Font("Daydream.ttf",20)
daydream27 = pygame.font.Font("Daydream.ttf",27)
daydream50 = pygame.font.Font("Daydream.ttf",50)
daydream65 = pygame.font.Font("Daydream.ttf",65)
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
verticaldirection = []
ducktypes = []
ducketat = []
duckrounds = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6 ]
vitesse = [10, 13, 10, 13, 16,10, 13, 16, 19, 22,10, 13, 16, 19, 22, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37,10, 13, 16, 19, 22, 25, 28, 31, 34, 37]
rounds = 0
totducks = 148
ducksmort = 0
duckspawn = 0
ducksuivit = 0
d = vitesse[rounds]
tempsdebut = pygame.time.get_ticks()

def dessins():
    global imagelunette, positionlunette, balles, directions, ducks,  tempsecoule, ducksmort, duckspawn
    fenetre.fill((125,125,200))
    fenetre.blit(fond,(0,0))
    pygame.draw.rect(fenetre, (30,30,150) , bord1, 8)
    pygame.draw.rect(fenetre, (30,30,150) , bord3, 8)
    pygame.draw.rect(fenetre, (30,30,150) , bord4, 8)
    pygame.draw.rect(fenetre, (30,30,150) , bord5, 8)
    pygame.draw.rect(fenetre, (20,20,20) , (-10,-10,142,42))
    pygame.draw.rect(fenetre, (20,20,20) , (55,630,114,104))
    pygame.draw.rect(fenetre, (20,20,20) , (631,630,114,104))
    pygame.draw.rect(fenetre, (20,20,20) , (618,0,250,34))
    surfacescore1 = daydream20.render("score",True,pygame.Color(255,255,255))
    surfacescore2 = daydream27.render(str(score),True,pygame.Color(255,255,120))
    surfaceround = daydream20.render("Round: " + str(rounds), True, (255, 255, 255))
    fenetre.blit(surfaceround, (622, 2))
    scorect = surfacescore2.get_rect(topright = (740,675))
    fenetre.blit(balle[balles],(57,629))
    fenetre.blit(surfacescore1,(633,635))
    fenetre.blit(surfacescore2, scorect)
    
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
    global rectstart, logo
    start = True
    pygame.mouse.set_visible(True)
    while start == True:
        fenetre.fill((20,20,20))
        pygame.draw.rect(fenetre, (30,30,150) , bord0, 8)
        fenetre.blit(logo,(20,50))
        pygame.draw.rect(fenetre, (30,30,150), rectstart, 8)
        surfacestart = daydream50.render("START", True, (255, 255, 255))
        fenetre.blit(surfacestart, (rectstart[0] + 10, rectstart[1] + 10))
        pygame.display.flip()
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                continuer = False
        if pygame.mouse.get_pressed()[0] == False:
           check3 = False
        if pygame.mouse.get_pressed()[0] == True and check3 == False :
           check3 = True
           if rectstart.collidepoint(event.pos):
              start = False               
    
def transition(roundn):
    fenetre.blit(fond,(-1,-1))
    surfaceroundt = daydream50.render("Round " + str(roundn), True, (30, 30, 150))
    fenetre.blit(surfaceroundt, (220,350))
    pygame.mixer.music.load("round.mp3")
    pygame.mixer.music.play()
    pygame.display.flip()
    pygame.time.wait(2000)

def fin():
    global score, ducksmort, duckspawn
    finjeu = True
    appreciation = ""
    if score >= 5000:
        appreciation = "INCROYABLE !"
    elif score >= 2500:
        appreciation = "Très bien joué !"
    elif score >= 500:
        appreciation = "Pas mal du tout !"
    else:
        appreciation = "Tu peux mieux faire !"
    while finjeu == True:
        fenetre.fill((20, 20, 20))
        pygame.draw.rect(fenetre, (30,30,150) , bord0, 8)
        surfacefin = daydream50.render("FIN DE PARTIE", True, (255, 255, 255))
        fenetre.blit(surfacefin, (240, 150))
        surfacescore = daydream50.render("Score : "+str(score), True, (255, 255, 0))
        fenetre.blit(surfacescore, (290, 220))
        surfaceapp = daydream30.render(appreciation, True, (0, 200, 0))
        fenetre.blit(surfaceapp, (200, 300))
        pygame.draw.rect(fenetre, (30, 30, 150), rectquitter, 8)
        surfacequit = daydream50.render("QUITTER", True, (255, 255, 255))
        fenetre.blit(surfacequit, (rectquitter[0] + 35, rectquitter[1] + 10))
        surfaceratio = daydream30.render(str(ducksmort)+ "/" + str(totducks) + "canards abattus", True, (255, 255, 255))
        fenetre.blit(surfaceratio, (250, 260))
        pygame.mixer.music.load("win.mp3")
        pygame.mixer.music.play()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               continuer = False
        if pygame.mouse.get_pressed()[0] == False:
           check4 = False
        if pygame.mouse.get_pressed()[0] == True and check4 == False :
           check4 = True
           if rectquitter.collidepoint(event.pos):
              finjeu = False
              continuer = False
              
def controles():
    global positionlunette, check, balles, score, rounds, check1, iconligne2, iconligne1, ducksmort
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           continuer = False
           
    if pygame.key.get_pressed()[pygame.K_r] == False:
       check1 = False
    if pygame.key.get_pressed()[pygame.K_r] == True and check1 == False:
        check1 = True
        pygame.mixer.music.load("recharge.mp3")
        pygame.mixer.music.play()
        balles = 5
        
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
                 score = score + 50
                 ducketat[i] = "dead"
                 ducksmort = ducksmort+ 1
       else:
          pygame.mixer.music.load("outofammo.wav")
          pygame.mixer.music.play()
         
tic = 0
intervalle = 10
clock = pygame.time.Clock()
debut()
transition(0)
Continuer = True
while Continuer == True:
   clock.tick(50)
   dessins()
   controles()
   pygame.mouse.set_visible(False)
   positionlunette = pygame.mouse.get_pos()
   
   tempsecoule = (pygame.time.get_ticks() - tempsdebut) / 1000
   tempsrestant = max(0, (5000 - tempsecoule*1000) // 1000)
   tic += 1
   if tic >= intervalle:
        tic = 0
        frame = (frame + 1) % 3
   if rounds < len(duckrounds):
     while duckspawn < duckrounds[rounds]:
       ducks.append((random.randint(50, 600), random.randint(50, 423)))
       directions.append(random.choice([-1, 1]))
       ducktypes.append(random.choice(['a', 'b']))
       ducketat.append("alive")
       verticaldirection.append(random.choice([0, 1])) 
       duckspawn = duckspawn +1
   else:
    fin()
       
   for i in range(len(ducks)-1, -1, -1):
    if ducketat[i] == "dead" and ducks[i][1] > 423 or tempsecoule >= 5 and ducks[i][1] < -100:
        del ducks[i]
        del directions[i]
        del ducktypes[i]
        del ducketat[i]
        del verticaldirection[i]

   for i in range(len(ducks)):
      if ducketat[i] == "alive":
          if tempsecoule < 5:
             ducks[i] = (ducks[i][0] + d * directions[i], ducks[i][1])
             if verticaldirection[i] == 1:  
                ducks[i] = (ducks[i][0], ducks[i][1] - 5)
                if ducks[i][1] <= 50:  
                    verticaldirection[i] = 0
             elif verticaldirection[i] == 0:  
                  ducks[i] = (ducks[i][0], ducks[i][1] + 5)
                  if ducks[i][1] >= 423:  
                     verticaldirection[i] = 1
          else:
               ducks[i] = (ducks[i][0] + 5 , ducks[i][1]-5)
      else:
          ducks[i] = (ducks[i][0], ducks[i][1]+10)
      if ducks[i][0] < 0 or ducks[i][0] > 700:
        directions[i] *= -1
        
   if len(ducks) == 0 and ducksmort<=totducks:
      pygame.time.wait(500)
      rounds = rounds + 1
      duckspawn = 0
      transition(rounds)
      tempsdebut = pygame.time.get_ticks()
     
pygame.quit()      
