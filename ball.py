import pgzrun
from random import randint

TITLE = "Flappy ball"
WIDTH =  700
HEIGHT = 600

gravity = 2000

R = randint(0,255)
G = randint(0,255)
B = randint(0,255)
CLR = R,G,B

class Ball:
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
        self.vx = 200
        self.vy = 0
        self.radius = 40
    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, CLR)


#creating instance "ball" for class "Ball"
ball = Ball(100,100)
ball2 = Ball(100,200)

def draw():
    screen.clear()
    ball.draw()
    ball2.draw()

def update(dt):
    uy = ball.vy
    ball.vy += gravity*dt
    ball.y += (uy+ball.vy)*0.5*dt
    uy = ball2.vy
    ball2.vy += gravity*dt
    ball2.y += (uy+ball.vy)*0.5*dt

    #detect and handle bounce
    if ball.y > HEIGHT-ball.radius: #we have bounced
        ball.y = HEIGHT -ball.radius #blocking the edges
        ball.vy = -ball.vy*0.5 #inelastic collision
    if ball2.y > HEIGHT-ball2.radius:
        ball2.y = HEIGHT -ball2.radius
        ball2.vy = -ball2.vy*0.5

    #x component does not have acceleration
    ball.x += ball.vx*dt
    if ball.x > WIDTH -ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx
    
    ball2.x += ball2.vx*dt
    if ball2.x > WIDTH -ball2.radius or ball2.x < ball2.radius:
        ball2.vx = -ball2.vx

def on_key_down(key):
    if key == keys.SPACE:
        ball.vy = -500
        ball2.vy = -750

pgzrun.go()
