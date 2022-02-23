# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle
from Food import Food

def setup():
    global vehicle
    global food
    contador = int(0)
    size(640, 360)
    velocity = PVector(0, 0)
    velFood = PVector(0,0)
    vehicle = Vehicle(width / 2, height / 2, velocity)
    food = Food(width / 3, height / 3, velFood)
    
    
def draw():
    background(255)
    textSize(30)
    fill(250,0, 0)
    text("Vida: " + str(food.contador),20,25)
    contador=0
    mouse = PVector(mouseX, mouseY)
    vehicle.update()
    vehicle.display()
    food.display()
    vel = PVector.sub(food.position, vehicle.position)
    vel.limit(5)
    vehicle.velocity = vel
    if vehicle.position == food.position:
        food.contador += 1
        newPos = PVector.random2D()
        if newPos.x < 0:
            newPos.x = -newPos.x
        if newPos.y < 0:
            newPos.y = -newPos.y
        newPos.x *= newPos.x* width
        newPos.y *= newPos.y* height
        #fit in the map
        if newPos.x <= 20:
            newPos.x +=20
        elif newPos.x >= width-20:
            newPos.x -= 20
        if newPos.y <= 20:
            newPos.y +=20
        elif newPos.y >= height-20:
            newPos.y -= 20
        
        food.position = newPos
