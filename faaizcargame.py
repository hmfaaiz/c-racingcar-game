# https://github.com/hmfaaiz
import pygame
from pygame.locals import *
pygame.init()
(width, height) = (690, 633)
CarWindow = pygame.display.set_mode((width, height))
bk_Colour = (255,255,255)
pygame.display.set_caption("Faaiz Car Game")



leftimg=pygame.image.load("a.png").convert_alpha()
leftimg=pygame.transform.scale(leftimg,(200,633))

rightimg=pygame.image.load("b.png").convert_alpha()
rightimg=pygame.transform.scale(rightimg,(200,633))

myc=pygame.image.load("mycar.png").convert_alpha()
myc=pygame.transform.scale(myc,(90,130))

lcar=pygame.image.load("leftcar.png").convert_alpha()
lcar=pygame.transform.scale(lcar,(90,130))

rcar=pygame.image.load("rightcar.png").convert_alpha()
rcar=pygame.transform.scale(rcar,(90,130))

ccar=pygame.image.load("centcar.png").convert_alpha()
ccar=pygame.transform.scale(ccar,(90,130))

cl=pygame.image.load("line.png").convert_alpha()
cl=pygame.transform.scale(cl,(45,150))

cl2=pygame.image.load("line.png").convert_alpha()
cl2=pygame.transform.scale(cl2,(45,150))

font_color=(0,150,250)
myfont=pygame.font.Font('Wowsers Italic.ttf',30)


def left(x,y):
    CarWindow.blit(leftimg, (x,y))



def right(x,y):
    CarWindow.blit(rightimg, (x,y))


def carline(x,y):
    CarWindow.blit(cl, (x,y))

def carline2(x, y):
    CarWindow.blit(cl2, (x, y))
carline2(315,  1.5)



                                            #(0,0)    (800,0)

                                            #(0,600)  (800,600)
def mycar(x,y):
    CarWindow.blit(myc, (x,y))

def leftcar(x,y):
    CarWindow.blit(lcar, (x,y))


def rightcar(x,y):
    CarWindow.blit(rcar, (x,y))


def centcar(x,y):
    CarWindow.blit(ccar, (x,y))

def totalscore(x,y):
    CarWindow.blit(mytext, (x,y))






cl_x=325
cl_y=0

mc_x=304
mc_y=450
lc_y=-200
lc_x=204

rc_y=-150
rc_x=400

cc_y=-120
cc_x=304

score=0


running = True
while running:

    CarWindow.fill(bk_Colour)

    mytext = myfont.render(("Score :" + str(score)), True, font_color)

    ##Call function
    left(0, 0)  #left pic
    right(490, 0)  #right pic
    totalscore(8, 40)  #position of score display

    leftcar(lc_x,lc_y)
    rightcar(rc_x, rc_y)
    #road line

    cl_y = cl_y + 1.5   #lines
    if cl_y>600:
        cl_y=0

    carline(cl_x, cl_y)


    #left car increment
    lc_y = lc_y + 0.5
    if lc_y > 1000:
        lc_y = -200
    leftcar(lc_x, lc_y)

    #right car increment
    rc_y = rc_y + 0.4
    if rc_y > 1160:
        rc_y = -120
    rightcar(400, rc_y)

    # center car increment
    cc_y = cc_y +0.2

    if cc_y > 1190:
        cc_y =-150
    centcar(300, cc_y)

    # call main car
    mycar(mc_x,mc_y)

    #crashed


    if mc_x == 204 and lc_y >= 340 and lc_y <= 560:
        print("Crashed")
        running = False

    elif mc_x == 404 and rc_y >= 340 and rc_y <= 560:
        print("Crashed in Right hand side")
        running = False

    elif mc_x == 304 and cc_y >= 340 and cc_y <= 560:
        print("Crashed in center")
        running = False


    elif mc_x < 204 :
        print("Crashed in Left")
        running = False

    elif mc_x > 404 :
        print("Crashed in Right")
        running = False

    else:
        if int(lc_y) == 560:
            score += 1
            lc_y += 1


        if int(cc_y) == (560):
            score += 1
            cc_y += 1

        if int(rc_y) == (560):
            score += 1
            rc_y += 1


    # for instructions
    for i in pygame.event.get():

        if i.type == KEYDOWN:
            if i.key==K_RIGHT:
                mc_x=mc_x+100
                mycar(mc_x, 450)

            if i.key==K_LEFT:
                mc_x=mc_x-100
                mycar(mc_x,450)



        if i.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    