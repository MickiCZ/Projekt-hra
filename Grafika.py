import turtle
#import Hra
import Obchod
import Funkce
import Inventář
import random

score = 0
player_speed = 10

money = 10000
invetory = []

#definice obrazovky
wn = turtle.Screen()
wn.title("Test hry")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#definice panáčka
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("red")
player.penup()
player.goto(-350,0)

#definice obchodu
shop = turtle.Turtle()
shop.speed(0)
shop.shape("triangle")
shop.color("blue")
shop.penup()
shop.goto(0,player_speed)


def kolize():
    if (player.xcor() == shop.xcor()) and (player.ycor() == shop.ycor()):
        Obchod.buy_in_shop(money, invetory)

#ovladani
def player_up():
    y = player.ycor()
    y += player_speed
    player.sety(y)

def player_down():
    y = player.ycor()
    y -= player_speed
    player.sety(y)

def player_left():
    x = player.xcor()
    x -= player_speed
    player.setx(x)

def player_right():
    x = player.xcor()
    x += player_speed
    player.setx(x)

#ovládání klávesnice
def ovladani():
    wn.listen()
    wn.onkeypress(player_up, "w")
    wn.onkeypress(player_down, "s")
    wn.onkeypress(player_left, "a")
    wn.onkeypress(player_right, "d")

while True:
    wn.update()
    ovladani()
    kolize()
