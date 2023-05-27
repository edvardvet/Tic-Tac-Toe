import time

import pygame as pg
from pygame import *
import sys


pg.init()
size_block = 150
margin = 20
width = height = size_block * 3 + margin * 4
size_windows = (width, height)
screen = pg.display.set_mode(size_windows)
pg.display.set_caption("Кресты и Нули")
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
arr = [[0]*3 for i in range(3)]
query = 0

gameover = False
start_menu = True


def screen_text(text: str, text_size: int) -> None:
    """
    :param text:
    :param text_size:
    :return:
    """
    font = pg.font.SysFont('stxingkai', text_size)
    text1 = font.render(text, True, white)
    text_rect = text1.get_rect()
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_width() / 2 - text_rect.height / 2
    screen.blit(text1, [text_x, text_y])

def check_win(arr: list, sign: str) -> str:
    """
    :param arr:
    :param sign:
    :return:
    """
    zeroes = 0
    for row in arr:
        zeroes+= row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if arr[0][col] == sign and arr[1][col] == sign and arr[2][col] == sign:
            return sig
        if arr[0][0] == sign and arr[1][1] == sign and arr[2][2] == sign:
            return sign
        if arr[0][2] == sign and arr[1][1] == sign and arr[2][0] == sign:
            return sign
        if zeroes == 0:
            return "Peace"
        return False


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit(0)
        elif event.type == pg.KEYDOWN and start_menu:
            start_menu = False
        elif event.type == pg.MOUSEBUTTONDOWN and not gameover and not start_menu:
            x_mouse, y_mouse = pg.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if arr[row][col] == 0:
                if query % 2 == 0:
                    arr[row][col] = 'x'
                else:
                    arr[row][col] = 'o'
                query += 1
        elif (event.type == pg.KEYDOWN and event.key == pg.K_SPACE) or (event.type == pg.KEYDOWN and gameover):
            gameover = False
            arr = [[0]*3 for i in range(3)]
            query = 0
            screen.fill(black)

    if start_menu:
        screen.fill(black)
        screen_text("Press any key to start the game", 40)

    if not gameover and not start_menu:
        screen.fill(black)
        for row in range(3):
            for col in range(3):
                if arr[row][col] == 'x':
                    color = red
                elif arr[row][col] == 'o':
                    color = green
                else:
                    color = white
                x =  col * size_block + (col +1) * margin
                y = row * size_block + (row +1) * margin
                pg.draw.rect(screen, white, (x,y, size_block, size_block))
                if color == red:
                    pg.draw.line(screen, red, (x+10, y+10), (x+size_block-10, y + size_block-10), 15)
                    pg.draw.line(screen, red, (x +size_block- 10, y + 10), (x + 10, y + size_block - 10), 15)
                elif color == green:
                    pg.draw.circle(screen, blue, (x+ size_block//2, y + size_block//2), size_block//2-3, 15)
    if(query - 1) % 2 == 0:
        gameover = check_win(arr, 'x')
    else:
        gameover = check_win(arr, 'o')


    if gameover:
        if gameover == 'x':
            screen.fill(red)
        elif gameover == 'o':
            screen.fill(blue)
        else:
            screen.fill(green)
        screen_text(gameover.upper() + " wins\n" + "Press any button to restart game", 30)
    pg.display.update()
