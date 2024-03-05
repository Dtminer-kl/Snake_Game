from turtle import Turtle
STARTING_POS= [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.snake_seg = []
        self.create_snake()
        self.head = self.snake_seg[0]


    def create_snake(self):
        for position in STARTING_POS:
            self.add_seg(position)

    def move(self):
        for seg_num in range(len(self.snake_seg)-1, 0, -1):
            new_x = self.snake_seg[seg_num -1].xcor()
            new_y = self.snake_seg[seg_num -1].ycor()
            self.snake_seg[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_seg(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_seg.append(snake)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_seg(self.snake_seg[-1].position())

    def reset(self):
        for seg in self.snake_seg:
            seg.goto(1000,1000)
        self.snake_seg.clear()
        self.create_snake()
        self.head = self.snake_seg[0]
