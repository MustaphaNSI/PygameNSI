
import pygame

pygame.init()
pygame.display.set_caption("Shoot")
fenetre = pygame.display.set_mode((800,800))
imagelunette = pygame.image.load("Crosshair.png")
imagelunette = pygame.transform.scale(imagelunette, (20,20))
pygame.mouse.set_visible(False)
check = False
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
balles = 5
sol = pygame.image.load("Sol.png")
sol = pygame.transform.scale(sol, (800,301))

def dessins():
    global imagelunette, positionlunette, balles, bord1
    fenetre.fill((125,125,200))
    fenetre.blit(imagelunette, positionlunette)
    fenetre.blit(sol,(0,500))
    pygame.draw.rect(fenetre, (0,0,150) , bord1, 8)
    pygame.draw.rect(fenetre, (0,0,150) , bord2, 8)
    pygame.draw.rect(fenetre, (0,0,150) , bord3, 8)
    pygame.draw.rect(fenetre, (0,0,0) , (55,630,114,104))
    pygame.draw.rect(fenetre, (0,0,0) , (218,630,364,104))
    pygame.draw.rect(fenetre, (0,0,0) , (631,630,114,104))
    fenetre.blit(balle[balles],(57,630))
    pygame.display.flip()

def controles():
    global positionlunette, check, balles
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           continuer = False
    if pygame.mouse.get_pressed(3)[0] == False:
       check = False
    if pygame.mouse.get_pressed(3)[0] == True and check == False :
       check = True
       pygame.mixer.music.load("tir.mp3")
       pygame.mixer.music.play()
       balles = balles - 1

clock = pygame.time.Clock()
Continuer = True
while Continuer == True:
   clock.tick(50)
   dessins()
   controles()
   positionlunette = pygame.mouse.get_pos()

pygame.quit()    
