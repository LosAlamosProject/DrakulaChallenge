import pygame as pg
import sys, math, random, winsound
pg.init()
clock = pg.time.Clock()

window = pg.display.set_mode((800,800))

pg.mouse.set_visible(False)
rect = pg.Rect(250,310,300,180)
nothitler = pg.image.load("nothitler.png")
nothitler = pg.transform.scale(nothitler,(300,180))
r = 69

def distance(pos1 : pg.Vector2,pos2 : pg.Vector2) -> float:
    return math.sqrt((pos2.x - pos1.x) ** 2 + (pos2.y - pos1.y) ** 2)

pg.display.set_caption("Drakula čelendž frfr")
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    window.fill((0,0,0))
    
    pg.draw.rect(window,(255,0,0),rect)
    window.blit(nothitler,rect)
    pg.draw.circle(window,(0,0,128),pg.mouse.get_pos(),r)
    mousepos = pg.Vector2(pg.mouse.get_pos())
    if mousepos.x > rect.right:
        # pg.draw.line(window,(0,255,0),mousepos,(rect.right,mousepos.y))
        # if abs(mousepos.x - rect.right) < r:
            # print("\a",random.randint(1,100))
        if rect.top < mousepos.y < rect.bottom:
            if distance(pg.Vector2(mousepos),pg.Vector2(rect.right,mousepos.y)) < r: 
                pg.draw.line(window,(0,255,0),mousepos,(rect.right,mousepos.y))
                pg.draw.circle(window,(0,0,255),pg.mouse.get_pos(),r)
                winsound.Beep(1000, 1)
        else:
            if abs(rect.top - mousepos.y) < abs(rect.bottom - mousepos.y) and distance(pg.Vector2(mousepos),pg.Vector2(rect.right,rect.top)) < r: 
                pg.draw.line(window,(0,0,255),mousepos,(rect.right,rect.top))
                pg.draw.circle(window,(0,0,255),pg.mouse.get_pos(),r)
                winsound.Beep(1000, 1)
            elif abs(rect.top - mousepos.y) > abs(rect.bottom - mousepos.y) and distance(pg.Vector2(mousepos),pg.Vector2(rect.right,rect.bottom)) < r: 
                pg.draw.line(window,(0,0,255),mousepos,(rect.right,rect.bottom))
                pg.draw.circle(window,(0,0,255),pg.mouse.get_pos(),r)
                winsound.Beep(1000, 1)
    elif mousepos.x < rect.left and rect.top < mousepos.y < rect.bottom:
        # pg.draw.line(window,(0,255,0),mousepos,(rect.left,mousepos.y))
        # if abs(mousepos.x - rect.left) < r:
            # print("\a",random.randint(1,100))
        if rect.top < mousepos.y < rect.bottom:
            if distance(pg.Vector2(mousepos),pg.Vector2(rect.left,mousepos.y)) < r: 
                pg.draw.line(window,(0,255,0),mousepos,(rect.left,mousepos.y))
                pg.draw.circle(window,(0,0,255),pg.mouse.get_pos(),r)
                winsound.Beep(1000, 1)
        else:
            if abs(rect.top - mousepos.y) < abs(rect.bottom - mousepos.y) and distance(pg.Vector2(mousepos),pg.Vector2(rect.left,rect.top)) < r: 
                pg.draw.line(window,(0,0,255),mousepos,(rect.left,rect.top))
                pg.draw.circle(window,(0,0,255),pg.mouse.get_pos(),r)
                winsound.Beep(1000, 1)
            elif abs(rect.top - mousepos.y) > abs(rect.bottom - mousepos.y) and distance(pg.Vector2(mousepos),pg.Vector2(rect.left,rect.bottom)) < r: 
                pg.draw.line(window,(0,0,255),mousepos,(rect.left,rect.bottom))
                pg.draw.circle(window,(0,0,255),pg.mouse.get_pos(),r)
                winsound.Beep(1000, 1)
    elif mousepos.y < rect.top:
        # pg.draw.line(window,(0,255,0),mousepos,(mousepos.x,rect.top))
        # if abs(mousepos.y - rect.top) < r:
            # print("\a",random.randint(1,100))
        if rect.left < mousepos.x < rect.right:
            if distance(pg.Vector2(mousepos),pg.Vector2(mousepos.x,rect.top)) < r: 
                pg.draw.line(window,(0,255,0),mousepos,(mousepos.x,rect.top))
                pg.draw.circle(window,(0,0,255),pg.mouse.get_pos(),r)
                winsound.Beep(1000, 1)
        else:
            if abs(rect.left - mousepos.x) < abs(rect.right - mousepos.x) and distance(pg.Vector2(mousepos),pg.Vector2(rect.left,rect.top)) < r: 
                pg.draw.line(window,(0,0,255),mousepos,(rect.left,rect.top))
                pg.draw.circle(window,(0,0,255),pg.mouse.get_pos(),r)
                winsound.Beep(1000, 1)
            elif abs(rect.left - mousepos.x) > abs(rect.right - mousepos.x) and distance(pg.Vector2(mousepos),pg.Vector2(rect.right,rect.top)) < r: 
                pg.draw.line(window,(0,0,255),mousepos,(rect.right,rect.top))
                pg.draw.circle(window,(0,0,255),pg.mouse.get_pos(),r)
                winsound.Beep(1000, 1)
    elif mousepos.y > rect.bottom:
        # pg.draw.line(window,(0,255,0),mousepos,(mousepos.x,rect.bottom))
        if rect.left < mousepos.x < rect.right:
            if distance(pg.Vector2(mousepos),pg.Vector2(mousepos.x,rect.bottom)) < r: 
                pg.draw.line(window,(0,255,0),mousepos,(mousepos.x,rect.bottom))
                pg.draw.circle(window,(0,0,255),pg.mouse.get_pos(),r)
                winsound.Beep(1000, 1)
        else:
            if abs(rect.left - mousepos.x) < abs(rect.right - mousepos.x) and distance(pg.Vector2(mousepos),pg.Vector2(rect.left,rect.bottom)) < r: 
                pg.draw.line(window,(0,0,255),mousepos,(rect.left,rect.bottom))
                pg.draw.circle(window,(0,0,255),pg.mouse.get_pos(),r)
                winsound.Beep(1000, 1)
            elif abs(rect.left - mousepos.x) > abs(rect.right - mousepos.x) and distance(pg.Vector2(mousepos),pg.Vector2(rect.right,rect.bottom)) < r: 
                pg.draw.line(window,(0,0,255),mousepos,(rect.right,rect.bottom))
                pg.draw.circle(window,(0,0,255),pg.mouse.get_pos(),r)
                winsound.Beep(1000, 1)

    elif (mousepos.x - r > rect.left or mousepos.x + r < rect.right) and (mousepos.y - r > rect.top or mousepos.y + r < rect.bottom):
        pg.draw.circle(window,(0,0,255),pg.mouse.get_pos(),r)
        winsound.Beep(1000, 1)


    pg.display.flip()
    clock.tick(40)