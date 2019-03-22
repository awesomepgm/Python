import pygame
from PIL import Image
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

backgroundName='bg.jpg'
bgimg=Image.open(backgroundName)
bheight= bgimg.height
bwidth= bgimg.width
dispSize=(bwidth,bheight)
win= pygame.display.set_mode(dispSize)

pygame.display.set_caption('the worst game')

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load(backgroundName)
char = pygame.image.load('standing.png')

clock= pygame.time.Clock()

#player
debugMode=True
width = 64
height = 64
x = dispSize[0]/2
y= dispSize[1]-height
vel= 6
left=False
right=False
walkCount=0

#platform
platX=255
platY=dispSize[1]-100
platWidth=30
platHeight=5
onPlatform=False

#gravity
onGround=False
f=0
isFall=False
isJump=False
jumpVel=25
gravity=2

#redraw
def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))

    pygame.draw.rect(win,(255,0,0), (platX,platY,platWidth,platHeight))
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount +=1
    else:
        win.blit(char, (x, y))
    if debugMode:
        win.blit(debug,(0,0))
    pygame.display.update()

#mainloop
run= True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    keys= pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x-vel > 0:
            x -= vel
        else:
            x=0
        left=True
        right=False
    elif keys[pygame.K_RIGHT]:
        if x+vel+width < dispSize[0]:
            x += vel
        else:
            x=dispSize[0]-width
        right=True
        left=False
    else:
        right=False
        left=False
        walkCount=0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump=True
            jumpY=y
            t=0
            walkCount=0
    else:
        t+=1
        beforey =int(jumpY - jumpVel*t + 0.5*gravity*t**2)
        if beforey <=dispSize[1]-height:
            y=beforey
        else:
            y=dispSize[1]-height
            isJump=False
        if x+width/2 in range(platX,platX+platWidth+1) and dispSize[1]-110 <= y+height <= dispSize[1]-100:
            if t >= (jumpY-(0.5*jumpVel**2/gravity))/jumpVel:
                y= dispSize[1]-99-height
                isJump=False
                onPlatform= True
    if not(x+width/2 in range(platX,platX+platWidth+1)) and onPlatform:
        if not(isJump):
            if isFall:
                f+=1
                fallY =int(platY-height  + 0.5*gravity*f**2)
                if fallY <=dispSize[1]-height:
                    y=fallY
                else:
                    y=dispSize[1]-height
                    f=0
                    isFall=False
                    onPlatform=False
                print(f)
            else:
                isFall=True
    if debugMode:
        debug=myfont.render(f'({int(x)},{int(y)})', False, (0,0,0))
    redrawGameWindow()
pygame.quit()
#realistic gravity:
# while y+100*x + 1/2*-9.8*x**2>=0:
#    x=x+1
#    y+= 100*x + 1/2*-9.8*x**2
#    print(str(y))
#else:
#    y=0
#    x=0