#!/usr/bin/env python

import sys
import pygame
from pygame.locals import *
from rrt import *

from environment import Environment

#constants
XDIM = 640
YDIM = 480
WINSIZE = [XDIM, YDIM]

def plot_points(screen, color, point_list):
    for i in range(len(point_list) - 1):
        p1 = point_list[i]
        p2 = point_list[i+1]

        pygame.draw.line(screen, color, p1, p2)

    pygame.display.update()

def plot_robots(screen, color, workspace):
    for robot in workspace.robots:
        x = int(round(robot.centroid.x))
        y = int(round(robot.centroid.y))

        pygame.draw.circle(screen, color, [x, y], 10)

    pygame.display.update()

def main():
    #initialize and prepare screen
    workspace = Environment(XDIM, YDIM)

    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption('RRT')
    white = 255, 240, 200
    black = 20, 20, 40
    color = 0, 255, 100
    robot_color = 200, 0, 0

    screen.fill(black)
    pygame.display.update()

    init_point = None;
    end_point = None;

    # workspace.addRobot(10, 20)
    # workspace.addRobot(50, 50)
    # workspace.addRobot(XDIM / 2, YDIM / 2)

    while True:
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                sys.exit("Leaving because you requested it.")

            if e.type == KEYUP and e.key == K_c:
                print("clear screen")
                screen.fill(black)
                pygame.display.update()

            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                if init_point == None:
                    init_point = e.pos
                elif end_point == None:
                    end_point = e.pos

        if init_point and end_point:
            print(init_point)
            print(end_point)

            plan = normal_plan([XDIM, YDIM], init_point, end_point, workspace)

            plot_points(screen, color, plan)

            init_point = None
            end_point = None

        plot_robots(screen, robot_color, workspace)

# if python says run, then we should run
if __name__ == '__main__':
    main()


