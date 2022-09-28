import pygame as pg
from sys import exit

pg.init()
screen = pg.display.set_mode((1280,720))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    pg.display.update()