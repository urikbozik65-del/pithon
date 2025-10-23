import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Noname game')

c_red = (255, 0, 0)
c_black = (0, 0, 0)
c_green = (0, 255, 0)

fps = pygame.time.Clock()
txt_fnt = pygame.font.Font(None, 36)

player = pygame.Rect(50, 50, 25, 25)
speed = 1

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    text_tutorial_btns = txt_fnt.render('W - up, S - down, A - left, D - right, \np - speed+, l - speed-', screen, c_black)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_p]:
        speed += 1
    if keys[pygame.K_l]:
        speed -= 1
        
    screen.fill(c_green)
    pygame.draw.rect(screen, c_red, player)
    
    fps.tick(60)
    
    pygame.display.flip()
    