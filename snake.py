from turtle import Turtle
starting_position=[(0, 0), (-20, 0), (-40, 0)]

a=Turtle()
class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)

    def add_segment(self,position):
            a = Turtle("square")
            a.color("white")
            a.penup()
            a.goto(position)
            self.segments.append(a)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[i - 1].xcor()
            y_cor = self.segments[i - 1].ycor()
            self.segments[i].goto(x_cor, y_cor)
        self.segments[0].fd(20)
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

