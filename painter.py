from turtle import Turtle 
from random import randint
from config import *

class Painter:

    def __init__(self):
        self.__pen = Turtle()
        self.__pen.speed(0)
        self.__pen.penup()
        self.__pen.goto(0, screenHeight // 2)

    def writeNum(self, num):
        self.__pen.color(textColor)

        self.__pen.right(90)
        self.__pen.forward(textMargin)
        
        self.__pen.write(num, font = ('arial', fontSize, 'bold'))
        
        self.__pen.backward(textMargin)
        self.__pen.left(90)

    def person(self):
        self.__pen.down()

        self.__pen.width(
            randint(2, 4)
        )

        red = randint(0, colorMax)
        green = randint(0, colorMax)
        blue = randint(0, colorMax)
        self.__pen.color((red, green, blue))

        corps = randint(20, 30)
        hand = randint(20, 25)
        leg = randint(25, 35)
        head = randint(5, 10)

        self.__pen.left(90)
        self.__pen.forward(corps)
        self.__pen.right(90)

        self.__pen.circle(head)

        self.__pen.right(45)
        self.__pen.forward(hand)
        self.__pen.backward(hand)
        self.__pen.right(90)
        self.__pen.forward(hand)
        self.__pen.backward(hand)

        self.__pen.left(45)
        self.__pen.forward(corps)

        self.__pen.left(20)
        self.__pen.forward(leg)
        self.__pen.backward(leg)
        self.__pen.right(40)
        self.__pen.forward(leg)
        self.__pen.backward(leg)
        self.__pen.left(110)

        self.__pen.up()

    def group(self, number = 1):
        self.writeNum(number)

        for i in range(number):
            self.person()
            self.stepIntragroup()

    def year(self, groups = [1, 2, 3]):
        self.newLine()

        for number in groups:
            self.group(number)
            self.stepIntergroup()



    def newLine(self):
        x = -screenWidth // 2 + personWidth

        y = self.__pen.ycor()
        y = y - interYearVertical

        self.__pen.goto(x, y)

    def stepIntergroup(self, distance = 50):
        self.__pen.forward(distance)

    def stepIntragroup(self):
        self.__pen.forward(
            randint(30, 40)
        )
        
        self.__pen.left(90)
        self.__pen.forward(
            randint(-intragroupVerticalMax, intragroupVerticalMax)
        )
        self.__pen.right(90)
