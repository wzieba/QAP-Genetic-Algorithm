import math
import turtle
from colorsys import hsv_to_rgb
import numpy as np
import sys


class CustomDrawer(turtle.Turtle):
    POINT_RADIUS = 20
    FONT_CONFIG = ["Arial", 14, "normal"]
    DRAWING_SPEED = "fastest"
    SHOW_TURTLE = False
    CAPTIONS_MARGIN = 50
    DISTANCE_BETWEEN_POINTS = 100

    coordinates_list = {}

    def __init__(self):
        turtle.Turtle.__init__(self, shape="classic")
        self.screen.tracer(0, 0)
        self.screen.colormode(255)
        self.speed(CustomDrawer.DRAWING_SPEED)
        if not CustomDrawer.SHOW_TURTLE:
            self.hideturtle()

    def draw_generation_frame(
            self,
            max_chromosome,
            generation_number,
            best_score,
            best_chromosome,
            flow_matrix,
            distance_matrix
    ):
        self.clear()
        self.reset()
        self.__draw_generation_info(generation_number, best_score, best_chromosome)
        self.draw_points(max_chromosome)
        self.__draw_connections_between_points(max_chromosome, flow_matrix, distance_matrix)
        self.screen.update()

    def move_to_circle_center(self, circle_radius, polygon_angle):
        self.penup()
        self.left(90)
        self.forward(circle_radius)
        self.right(90 - (polygon_angle / 2))
        self.pendown()

    def draw_points(self, best_chromosome):
        number_of_points = len(best_chromosome)
        circle_radius = CustomDrawer.DISTANCE_BETWEEN_POINTS / (2 * (math.sin(math.pi / number_of_points)))
        polygon_angle = 360 / number_of_points
        self.move_to_circle_center(circle_radius, polygon_angle)
        for draw_index in range(number_of_points):
            self.circle(CustomDrawer.POINT_RADIUS)
            self.coordinates_list[draw_index] = self.pos()
            self.penup()
            self.left(90)
            self.forward(20)
            self.write(best_chromosome[draw_index], font=CustomDrawer.FONT_CONFIG)
            self.backward(20)
            self.right(90)
            self.right((360 / number_of_points))
            self.forward(CustomDrawer.DISTANCE_BETWEEN_POINTS)
            self.pendown()

    def __draw_connections_between_points(self, max_chromosome, flow_matrix, distance_matrix):
        max_distance = np.max(distance_matrix)
        min_distance = np.min(distance_matrix[np.nonzero(distance_matrix)])
        for x in range(len(max_chromosome)):
            for y in range(len(max_chromosome)):
                flow_value = flow_matrix[max_chromosome[x] - 1, max_chromosome[y] - 1]
                distance_value = distance_matrix[x, y]
                if flow_value != 0:
                    self.__draw_line(x, y,
                                     pen_color=self.__get_color_for_value(distance_value, min_distance, max_distance),
                                     pen_size=flow_value)

    def __draw_line(self, object_from, object_to, pen_color=(0, 0, 0), pen_size=1):
        position_from = self.coordinates_list[object_from]
        position_to = self.coordinates_list[object_to]
        self.penup()
        self.goto(position_from[0], position_from[1])
        self.pendown()
        self.pensize(pen_size)
        self.pencolor(pen_color)
        self.goto(position_to[0], position_to[1])
        self.pensize(1)

    def __draw_generation_info(self, generation_number, best_score, best_chromosome):
        start_position = self.pos()
        self.penup()
        self.goto(-self.screen.window_width() / 2 + CustomDrawer.CAPTIONS_MARGIN,
                  self.screen.window_height() / 2 - CustomDrawer.CAPTIONS_MARGIN)
        self.write(f'Best chromosome: {best_chromosome}', font=CustomDrawer.FONT_CONFIG)
        self.right(90)
        self.forward(20)
        self.write(f'Generation number: {generation_number}', font=CustomDrawer.FONT_CONFIG)
        self.forward(20)
        self.write(f'Best score: {best_score}', font=CustomDrawer.FONT_CONFIG)

        self.left(90)
        self.goto(start_position[0], start_position[1])
        self.pendown()

    def __get_color_for_value(self, value, min_distance, max_distance):
        return self.convert_to_rgb(min_distance, max_distance, value)

    @staticmethod
    def convert_to_rgb(minval, maxval, val):
        colors = [(0, 255, 0), (255, 0, 0)]
        fi = float(val - minval) / float(maxval - minval) * (len(colors) - 1)
        i = int(fi)
        f = fi - i
        if f < sys.float_info.epsilon:
            return colors[i]
        else:
            (r1, g1, b1), (r2, g2, b2) = colors[i], colors[i + 1]
            return int(r1 + f * (r2 - r1)), int(g1 + f * (g2 - g1)), int(b1 + f * (b2 - b1))
