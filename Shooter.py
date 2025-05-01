import pygame

pygame.init()
pygame.display.set_caption("Shoot")
fenetre = pygame.display.set_mode((800,800))
imagelunette = pygame.image.load("Crosshair.png")
imagelunette = pygame.transform.scale(imagelunette, (20,20))
pygame.mouse.set_visible(False)
check = False
positionlunette = (-10,-10)

def dessins():
    global imagelunette, positionlunette
    fenetre.fill((200,200,200))
    fenetre.blit(imagelunette, positionlunette)
    pygame.display.flip()

def controles():
    global positionlunette, check
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           continuer = False
    if pygame.mouse.get_pressed(3)[0] == False:
       check = False
    if pygame.mouse.get_pressed(3)[0] == True and check == False :
       check = True
       pygame.mixer.music.load("tir.mp3")
       pygame.mixer.music.play()

clock = pygame.time.Clock()
Continuer = True
while Continuer == True:
   clock.tick(50)
   dessins()
   controles()
   positionlunette = pygame.mouse.get_pos()

pygame.quit()
