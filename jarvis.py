# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:22:26 2022

@author: Gerald Kloimstein

references:
https://algorithmtutor.com/Computational-Geometry/Convex-Hull-Algorithms-Jarvis-s-March/
https://www.tutorialspoint.com/Jarvis-March-Algorithm
https://www.youtube.com/watch?v=3-jxPY-mnhQ
https://www.youtube.com/watch?v=cf0FyCRuzq8
https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
"""

import pygame
import random
import time
from timeit import Timer
import pandas as pd
import numpy as np


def direction(a, b, c):
    # cross product of vectors to determine the direction

    # We select the vertex following l and call it q. We check if q is turning right from the line joining l and every other point one at a time. If q is turning right, we move q to the point from where it was turning right. This way we move q towards left in each iteration and finally stop when q is in the leftmost position from l. We add q to the list of convex hull vertices.

    # a = hull_point
    # b = candidate_point
    # c = current_point

    # if cross product = positive the point is clockwise

    return (((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])) > 0)


def showText(string, font, size, color, screen_height, screen_width, screen):
    pygame.font.init()
    font = pygame.font.SysFont(font, size)

    # create a text surface object, on which text is drawn
    text = font.render(string, True, color, )

    # create a rectangular object for the text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (screen_width // 2, screen_height // 2)

    # copy the text surface object to the screen object
    screen.blit(text, textRect)

    pygame.font.quit()


def restartJarvis():
    print("test")


def quitJarvis():
    pygame.display.quit
    pygame.quit


def runJarvisAlgo(points_to_create):
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # General Configuration Settings
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # variables
    screen_width = 1080
    screen_height = 800
    screen_offset = 50
    hull = []

    x = np.random.randint(screen_offset, screen_width - screen_offset,
                          size=points_to_create)
    y = np.random.randint(screen_offset, screen_height - screen_offset,
                          size=points_to_create)

    df = pd.DataFrame({"x": x, "y": y})

    # test for rectangle
    # df = pd.DataFrame({"x": [60,500,60,500], "y": [60,60,500,500]})

    # test speed mode vs graphics mode
    # df = pd.DataFrame({"x": [60,500,60,500,200,60,80,70,400,800,600,300,200],
    #                   "y": [60,60,500,500,70,200,600,50,300,500,200,150,620]})

    data_points = list(map(tuple, df.values))  # make a list
    count_points = len(data_points)

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Jarvis March algorithm
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # start timeer here

    # get left_most point
    leftmost_point_idx = df.index[df.x == df.x.min()].tolist()[0]  # index
    leftmost_point = data_points[leftmost_point_idx]  # point

    # find the hull via Jarvis March alogrithm
    hull_point = leftmost_point

    while (True):
        hull.append(hull_point)
        candidate_point = data_points[(data_points.index(hull_point) + 1)
                                      % count_points]
        # get the next data point (could be randomly anyone,
        # we just take the next in the list)
        # hull_point is our last found point in the hull
        # candidate_point is our current candidate for a hull_point
        # current_point is any other point where we check if it is left of
        #     candidate_point

        for current_point in data_points:
            if (direction(hull_point, candidate_point, current_point)):
                candidate_point = current_point

        hull_point = candidate_point

        if (hull_point == hull[0]):
            break

    # end timer here

    df_hull = pd.DataFrame(hull, columns=["x", "y"])
    df_hull.sort_values(by=["x", "y"], inplace=True)
    print(df_hull)


def runJarvisGraph(points_to_create):
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # General Configuration Settings
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # variables
    hull = []
    velocity = 20
    acceleration = 1.005

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # Visualisation Configuration Settings
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # screen
    screen_width = 1080
    screen_height = 800
    screen_offset = 50

    # colors
    start_point_color = (255, 100, 100)  # light red
    # point_color = (180, 180, 180)  # grey
    point_color = (255, 255, 66)  # yellow
    hull_color = (128, 255, 255)  # light blue
    line_color = (255, 255, 255)  # white
    background_color = (0, 0, 0)  # black
    font_color = (255, 100, 100)  # light red

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Convex Hull (Jarvis' March)")
    screen = pygame.display.set_mode((screen_width, screen_height))

    # background color
    screen.fill(background_color)

    # build dataframe with x and y coordinates
    x = np.random.randint(screen_offset, screen_width - screen_offset,
                          size=points_to_create)
    y = np.random.randint(screen_offset, screen_height - screen_offset,
                          size=points_to_create)

    df = pd.DataFrame({"x": x, "y": y})

    # test rectangle
    # df = pd.DataFrame({"x": [60,500,60,500],"y": [60,60,500,500]})

    # test speed mode vs graphics mode
    # df = pd.DataFrame({"x": [60,500,60,500,200,60,80,70,400,800,600,300,200],
    #                   "y": [60,60,500,500,70,200,600,50,300,500,200,150,620]})

    df["y"] = screen_height - df["y"]  # necessary as y-axis origin in Python is on top left

    data_points = list(map(tuple, df.values))  # make a list
    count_points = len(data_points)

    # display points on screen
    for i in range(0, count_points):
        pygame.draw.circle(screen, point_color, data_points[i], 4)
    pygame.display.update()

    # get left_most point
    leftmost_point_idx = df.index[df.x == df.x.min()].tolist()[0]  # index
    leftmost_point = data_points[leftmost_point_idx]  # point
    pygame.draw.circle(screen, start_point_color, leftmost_point, 4)
    pygame.display.update()

    # find the hull via Jarvis March alogrithm
    hull_point = leftmost_point

    while (True):

        hull.append(hull_point)
        candidate_point = data_points[(data_points.index(hull_point) + 1)
                                      % count_points]
        # get the next data point (could be randomly anyone,
        # we just take the next in the list)

        for current_point in data_points:

            # get the next data point (could be randomly anyone,
            # we just take the next in the list)
            # hull_point is our last found point in the hull
            # candidate_point is our current candidate for a hull_point
            # current_point is any other point where we check if it is left of
            #     candidate_point
            pygame.draw.line(screen, line_color, hull_point, current_point, 1)
            clock.tick(velocity)
            pygame.display.update()
            if (direction(hull_point, candidate_point, current_point)):
                candidate_point = current_point
            velocity *= acceleration

        pygame.draw.line(screen, hull_color, hull_point, candidate_point, 4)

        pygame.display.update()
        hull_point = candidate_point

        if (hull_point == hull[0]):
            break

    while True:
        time.sleep(1)
        showText("Press r to restart or q to quit",
                 "Arial Black", 45, font_color,
                 screen_height, screen_width, screen)
        pygame.display.update()

        for event in pygame.event.get():
            # if event.type == pygame.QUIT:
            #     #pygame.display.quit()
            #     #pygame.quit()
            #     return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.display.quit()
                    pygame.quit()
                    return False

                elif event.key == pygame.K_r:
                    return True

    pygame.display.quit()
    pygame.quit()
    return False


# # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # Measure performance
# # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# #Create the performance data (comment out later)
# for k in range(9416,10001):

#     t = Timer(lambda: runJarvisAlgo(k))
#     #Save the timerequired to the file "o_notationdata.txt"
#     matrix = np.loadtxt('o_notation_data_j.txt')
#     #Find the current time value for a specific k (note that k is stored in the first column)
#     k_index = np.where(matrix[:,0] == k)[0]
#     if k_index.size == 0:
#         matrix = np.vstack((matrix,[k,t.timeit(number=1)]))
#     else:
#         #Get average value between current and previous
#         matrix[k_index[0]][1] = (matrix[k_index[0]][1] + t.timeit(number=1))/2
#     with open('o_notation_data_j.txt', 'wb') as f:
#         np.savetxt(f, matrix, delimiter=' ')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Starter program
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++ General Config Setting ++++

app_mode = 99
points_to_create = 0

while not (app_mode == 0 or app_mode == 1):
    print("\nChose the algorithm mode:\n")
    try:
        app_mode = int(input("0 - speed mode, 1 - graphics mode: "))
    except:
        print("wrong input")

if app_mode == 0:
    try:
        points_to_create = int(input("How many data points shall be created (default 100 000) : ") or 100000)
    except:
        print("wrong input, proceeding with default")
        points_to_create = 100000
    runJarvisAlgo(points_to_create)

elif app_mode == 1:
    while not (points_to_create >= 3 and points_to_create <= 2000):
        try:
            points_to_create = int(input("How many data points shall be created (max 2000, default 100): ") or 100)
        except:
            print("wrong input")
    run = True
    while run:
        run = runJarvisGraph(points_to_create)