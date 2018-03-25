import string

import math
import turtle


class CustomDrawer(turtle.Turtle):
    POINT_RADIUS = 20
    FONT_CONFIG = ["Arial", 14, "normal"]
    DRAWING_SPEED = "fastest"
    SHOW_TURTLE = False
    CAPTIONS_MARGIN = 50
    DISTANCE_BETWEEN_POINTS = 100

    coordinates_list = {}

    def __init__(self):
        """Turtle Constructor"""
        turtle.Turtle.__init__(self, shape="classic")
        # self.screen.delay(0)
        self.screen.tracer(0, 0)
        self.screen.colormode(255)
        self.speed(CustomDrawer.DRAWING_SPEED)
        if not CustomDrawer.SHOW_TURTLE:
            self.hideturtle()

    def move_to_circle_start_position(self, circle_radius, polygon_angle):
        self.penup()
        self.left(90)
        self.forward(circle_radius)
        self.right(90 - (polygon_angle / 2))
        self.pendown()

    def draw_points(self, best_chromosome):
        number_of_points = len(best_chromosome)
        circle_radius = CustomDrawer.DISTANCE_BETWEEN_POINTS / (2 * (math.sin(math.pi / number_of_points)))
        polygon_angle = 360 / number_of_points
        self.move_to_circle_start_position(circle_radius, polygon_angle)
        for draw_index in range(number_of_points):
            self.circle(CustomDrawer.POINT_RADIUS)
            self.coordinates_list[draw_index] = self.pos()
            self.write(best_chromosome[draw_index], font=CustomDrawer.FONT_CONFIG)
            self.penup()
            self.right((360 / number_of_points))
            self.forward(CustomDrawer.DISTANCE_BETWEEN_POINTS)
            self.pendown()

    def draw_line(self, object_from, object_to, pen_color=(0, 0, 0), pen_size=1):
        position_from = self.coordinates_list[object_from]
        position_to = self.coordinates_list[object_to]
        self.penup()
        self.goto(position_from[0], position_from[1])
        self.pendown()
        self.pensize(pen_size)
        self.pencolor(pen_color)
        self.goto(position_to[0], position_to[1])
        self.pensize(1)

    def draw_generation_info(self, generation_number, best_score):
        start_position = self.pos()
        self.penup()
        self.goto(-self.screen.window_width() / 2 + CustomDrawer.CAPTIONS_MARGIN,
                  self.screen.window_height() / 2 - CustomDrawer.CAPTIONS_MARGIN)
        self.write(f'Generation number: {generation_number}', font=CustomDrawer.FONT_CONFIG)
        self.right(90)
        self.forward(20)
        self.write(f'Best score: {best_score}', font=CustomDrawer.FONT_CONFIG)

        self.left(90)
        self.goto(start_position[0], start_position[1])
        self.pendown()

    def draw_generation(self, objects, generation_number, best_score):
        self.clear()
        self.reset()
        self.draw_generation_info(generation_number, best_score)
        self.draw_points(objects)
