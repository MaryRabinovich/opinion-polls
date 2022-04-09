from turtle import Screen, done 
from painter import Painter
from config import screenWidth, screenHeight

screen = Screen()
screen.colormode(255)
screen.setup(
    startx = 0,
    starty = 0,
    width = screenWidth,
    height = screenHeight
)

painter = Painter()

painter.year([5, 2, 4, 3])

painter.year([3, 5, 7, 2])

done()