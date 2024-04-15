import pygame
import math


background_colour = (0,0,0)
(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
pygame.display.flip()


camera = [[0,0,-200],[0,0]]
proj_plane = 500


def rotate(point, angle, origin=(0,0)):
    angle = math.radians(angle)
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

def drawline2d(p1,p2):
    global screen
    p1 = (p1[0]+width//2,-p1[1]+height//2)
    p2 = (p2[0]+width//2,-p2[1]+height//2)
    pygame.draw.line(screen,(200,200,200),p1,p2)


def drawline3d(p1,p2):
    global camera
    campos = camera[0]
    p1 = project(p1)    
    p2 = project(p2)    

    if p1 == 0 or p2 == 0:
        return

    drawline2d(p1,p2)

def project(p):
    global camera
    campos = camera[0]
    camrot = camera[1]
    x,y,z = (p[0]-campos[0],p[1]-campos[1],p[2]-campos[2])
    x,z = rotate((x,z),camrot[0])
    y,z = rotate((y,z),camrot[1])


    p = (x,y,z)
    

    if p[2] <= 0:
        return 0
    try:
        x= (proj_plane/p[2])*p[0]
    except(ZeroDivisionError):
        x=0
    try:
        y= (proj_plane/p[2])*p[1]
    except(ZeroDivisionError):
        y=0
    return (x,y)

def drawcube(p,s):
    c1 = (0,0,0)
    c2 = (p[0]+s[0],0,0)
    c3 = (0,p[1]+s[1],0)
    c4 = (p[0]+s[0],p[1]+s[1],0)
    c5 = (0,0,p[2]+s[2])
    c6 = (p[0]+s[0],0,p[2]+s[2])
    c7 = (0,p[1]+s[1],p[2]+s[2])
    c8 = (p[0]+s[0],p[1]+s[1],p[2]+s[2])
    drawline3d(c1,c2)
    drawline3d(c3,c4)
    drawline3d(c1,c3)
    drawline3d(c2,c4)
    drawline3d(c5,c6)
    drawline3d(c7,c8)
    drawline3d(c5,c7)
    drawline3d(c6,c8)
    drawline3d(c1,c5)
    drawline3d(c2,c6)
    drawline3d(c3,c7)
    drawline3d(c4,c8)





clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    cam_movespeed = 5
    cam_rotspeed = 5

    if keys[pygame.K_w]:
        camera[0][2]+=cam_movespeed*math.cos(math.radians(camera[1][0]))
        camera[0][0]+=cam_movespeed*math.sin(math.radians(camera[1][0]))
    if keys[pygame.K_s]:
        camera[0][2]-=cam_movespeed*math.cos(math.radians(camera[1][0]))
        camera[0][0]-=cam_movespeed*math.sin(math.radians(camera[1][0]))
    if keys[pygame.K_d]:
        camera[0][2]+=cam_movespeed*math.cos(math.radians(camera[1][0]+90))
        camera[0][0]+=cam_movespeed*math.sin(math.radians(camera[1][0]+90))
    if keys[pygame.K_a]:
        camera[0][2]-=cam_movespeed*math.cos(math.radians(camera[1][0]+90))
        camera[0][0]-=cam_movespeed*math.sin(math.radians(camera[1][0]+90))
    if keys[pygame.K_SPACE]:
        camera[0][1]+=cam_movespeed
    if keys[pygame.K_LSHIFT]:
        camera[0][1]-=cam_movespeed

    if keys[pygame.K_RIGHT]:
        camera[1][0] += cam_rotspeed
    if keys[pygame.K_LEFT]:
        camera[1][0] -= cam_rotspeed
    if keys[pygame.K_UP]:
        camera[1][1] -= cam_rotspeed
    if keys[pygame.K_DOWN]:
        camera[1][1] += cam_rotspeed

    print(camera)
    
    screen.fill(background_colour)
    drawcube((0,0,0),(100,100,100))
    pygame.display.flip()
    clock.tick(60)