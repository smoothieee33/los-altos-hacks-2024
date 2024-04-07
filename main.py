from brython_graphics import *

pos = random.randint(1, 2)
answer = random.randint(1, 2)
import random
from browser import timer
def background():
    set_size(400,400)
    
    rect_b1 = Rectangle(400, 300)
    rect_b1.set_position(0, 50)
    rect_b1.set_color(Color.black)
    add(rect_b1)
    rect_white = Rectangle(396, 296)
    rect_white.set_position(2, 52)
    rect_white.set_color(Color.white)
    add(rect_white)
    rect_b2 = Rectangle(390, 290)
    rect_b2.set_position(6, 56)
    rect_b2.set_color(Color.black)
    add(rect_b2)
    rect_content = Rectangle(386, 286)
    rect_content.set_position(8, 58)
    rect_content.set_color(Color.gray)
    add(rect_content)
        
    count = 0
    for i in range(10):
        line = Line(200,58+count,200,73+count)
        line.set_color(Color.black)
        add(line)
        count += 30.23
def make_text(text, posx, posy, font, color):
    txt = Text(text)
    txt.set_position(posx, posy)
    txt.set_font(font)
    txt.set_color(color)
    add(txt)
def game_setup():
    if pos == 1:
        apple_green = Image("https://64.media.tumblr.com/3485ac9f205a7827c4c47e9b31018f01/be1212d3b065aaf4-d4/s540x810/977678391a68d6421031c1e5c8f3311a0299aa7a.pnj")
        apple_green.set_size(100, 100)
        apple_green.set_position(50, 150)
        add(apple_green) 

        apple_red = Image("https://64.media.tumblr.com/d0195dd9586fc9e8713392a05ed629de/be1212d3b065aaf4-3d/s540x810/a6fea9156ff1dac6a9f8d5a383e2fe040415040b.pnj")
        apple_red.set_size(100, 100)
        apple_red.set_position(250, 150)
        add(apple_red)
    if pos == 2:
        apple_green = Image("https://64.media.tumblr.com/3485ac9f205a7827c4c47e9b31018f01/be1212d3b065aaf4-d4/s540x810/977678391a68d6421031c1e5c8f3311a0299aa7a.pnj")
        apple_green.set_size(100, 100)
        apple_green.set_position(250, 150)
        add(apple_green) 

        apple_red = Image("https://64.media.tumblr.com/d0195dd9586fc9e8713392a05ed629de/be1212d3b065aaf4-3d/s540x810/a6fea9156ff1dac6a9f8d5a383e2fe040415040b.pnj")
        apple_red.set_size(100, 100)
        apple_red.set_position(50, 150)
        add(apple_red)
    if answer == 1:
        make_text("Choose the green apple!", 65, 35, "15pt Courier New", Color.black)
    if answer == 2:
        make_text("Choose the red apple!", 65, 35, "15pt Courier New", Color.black)
def choose_apples(x, y):
    if pos == 1:
        if 50 < x < 150:
            if answer == 1:
                correct()
            else:
                wrong()
        elif 250 < x < 350:
            if answer == 2:
                correct()
            else:
                wrong()
    elif pos == 2:
        if 250 < x < 350:
            if answer == 1:
                correct()
            else:
                wrong()
        elif 50 < x < 150:
            if answer == 2:
                correct()
            else:
                wrong()

def correct():
    make_text("Correct!", 150, 380, "15pt Courier New", Color.green)
    
def wrong():
    make_text("Sorry, your answer is wrong.", 40, 380, "15pt Courier New", Color.red)
background()
game_setup()
add_mouse_click_handler(choose_apples)
