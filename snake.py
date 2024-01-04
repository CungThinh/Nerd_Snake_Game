import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


class Snake:
    snake_length = 100
    segments = []
    speed = 20

    def __init__(self):
        for i in range(0, -self.snake_length - 1, -20):
            new_segment = Turtle("square")
            new_segment.color("white")
            self.segments.append(new_segment)
            new_segment.penup()
            new_segment.goto(x=i, y=0)
            self.head = self.segments[0]
            self.tail = self.segments[-1]

    def move(self):
        # self.head.forward(self.speed)
        # Nếu để dòng này ở trên thì sẽ xảy ra lỗi
        # Nguyên nhân:
        # Những cái segment phía sau sẽ theo segement phía trước
        # Sau khi kết thúc move, phần tử head - 1 sẽ trùng với head
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(self.speed)
        # phần tử head sẽ dịch lên trước

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def extend(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        self.segments.append(new_segment)
        new_segment.penup()
        new_segment.goto(x=self.tail.xcor(), y=self.tail.ycor())

    def check_self_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False



