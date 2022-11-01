# -*- coding: utf-8 -*-
"""
Helper program to generate csv Files for data import

"""

import matplotlib.pyplot as plt
import math
import random
import pandas as pd


# %% functions

def points_in_triangle(pt1, pt2, pt3):
    """
    Random point in the triangle with vertices pt1, pt2 and pt3.
    """
    x, y = random.random(), random.random()
    q = abs(x - y)
    s, t, u = q, 0.5 * (x + y - q), 1 - 0.5 * (q + x + y)
    return (
        s * pt1[0] + t * pt2[0] + u * pt3[0],
        s * pt1[1] + t * pt2[1] + u * pt3[1],
    )


def points_on_rectangle(pt1, pt2, pt3, pt4):
    """
    Random point on the rectangle with vertices pt1, pt2, pt3 and pt4.
    """

    list = [pt1, pt2, pt3, pt4]
    min_x = min(list, key=lambda p: p[0])[0]
    max_x = max(list, key=lambda p: p[0])[0]
    min_y = min(list, key=lambda p: p[1])[1]
    max_y = max(list, key=lambda p: p[1])[1]

    line = random.randint(0, 3)

    if line == 0:  # point on lower line
        return min_x + (max_x - min_x) * random.random(), min_y
    elif line == 1:  # point on upper line
        return min_x + (max_x - min_x) * random.random(), max_y
    elif line == 2:  # point on left line
        return min_x, min_y + (max_y - min_y) * random.random()
    elif line == 3:  # point on right line
        return max_x, min_y + (max_y - min_y) * random.random()


def points_within_polygone(pt1, pt2, pt3, pt4):
    """
    Random point on the rectangle with vertices pt1, pt2, pt3 and pt4.
    """

    list = [pt1, pt2, pt3, pt4]
    min_x = min(list, key=lambda p: p[0])[0]
    max_x = max(list, key=lambda p: p[0])[0]
    min_y = min(list, key=lambda p: p[1])[1]
    max_y = max(list, key=lambda p: p[1])[1]

    line = random.randint(0, 3)

    if line == 0:  # point on lower line
        return min_x + (max_x - min_x) * random.random(), min_y + (max_y - min_y) * random.random()
    elif line == 1:  # point on upper line
        return min_x + (max_x - min_x) * random.random(), min_y + (max_y - min_y) * random.random()
    elif line == 2:  # point on left line
        return min_x + (max_x - min_x) * random.random(), min_y + (max_y - min_y) * random.random()
    elif line == 3:  # point on right line
        return min_x + (max_x - min_x) * random.random(), min_y + (max_y - min_y) * random.random()


def points_on_cycle():
    p = list()
    i = 0.0
    while i <= 2 * math.pi:
        p.append((math.cos(i) * 10, math.sin(i) * 10))
        i += 0.01
    return p


# %% triangle 100 points within

# triangle with 100 points
random.seed()

pt1 = (50, 50)
pt2 = (1000, 80)
pt3 = (300, 770)
points = [points_in_triangle(pt1, pt2, pt3) for _ in range(97)]

x, y = zip(*points)
plt.scatter(x, y, s=0.1)
plt.show()

df = pd.DataFrame({"x": [pt1[0], pt2[0], pt3[0]],
                   "y": [pt1[1], pt2[1], pt3[1]]})
df2 = pd.DataFrame({"x": x, "y": y})
df = pd.concat([df, df2], ignore_index=True)
df.to_csv("t100.csv", sep=";", index=False, mode="w+")

# %% triangle 10 000 points within

# triangle with 10 000 points
random.seed()

pt1 = (50, 50)
pt2 = (1000, 80)
pt3 = (300, 770)
points = [points_in_triangle(pt1, pt2, pt3) for _ in range(9997)]

x, y = zip(*points)
plt.scatter(x, y, s=0.1)
plt.show()

df = pd.DataFrame({"x": [pt1[0], pt2[0], pt3[0]],
                   "y": [pt1[1], pt2[1], pt3[1]]})
df2 = pd.DataFrame({"x": x, "y": y})
df = pd.concat([df, df2], ignore_index=True)
df.to_csv("t10000.csv", sep=";", index=False, mode="w+")

# %% triangle 100 000 points within

# triangle with 100 000 points
random.seed()

pt1 = (50, 50)
pt2 = (1000, 80)
pt3 = (300, 770)
points = [points_in_triangle(pt1, pt2, pt3) for _ in range(99997)]

x, y = zip(*points)
plt.scatter(x, y, s=0.1)
plt.show()

df = pd.DataFrame({"x": [pt1[0], pt2[0], pt3[0]],
                   "y": [pt1[1], pt2[1], pt3[1]]})
df2 = pd.DataFrame({"x": x, "y": y})
df = pd.concat([df, df2], ignore_index=True)
df.to_csv("t100000.csv", sep=";", index=False, mode="w+")

# %% rectangle with 100 points on it (near best case)

# rectangle with 100 points on rectangle
random.seed()

pt1 = (50, 50)
pt3 = (1000, 770)

pt2 = (pt3[0], pt1[1])
pt4 = (pt1[0], pt3[1])

points = [points_on_rectangle(pt1, pt2, pt3, pt4) for _ in range(96)]

x, y = zip(*points)
plt.scatter(x, y, s=0.1)
plt.show()

df = pd.DataFrame({"x": [pt1[0], pt2[0], pt3[0], pt4[0]],
                   "y": [pt1[1], pt2[1], pt3[1], pt4[1]]})
df2 = pd.DataFrame({"x": x, "y": y})
df = pd.concat([df, df2], ignore_index=True)
df.to_csv("r100.csv", sep=";", index=False, mode="w+")

# %% rectangle with 10 000 points on it (near best case)

# rectangle with 10 000 points on rectangle
random.seed()

pt1 = (50, 50)
pt3 = (1000, 770)

pt2 = (pt3[0], pt1[1])
pt4 = (pt1[0], pt3[1])

points = [points_on_rectangle(pt1, pt2, pt3, pt4) for _ in range(9996)]

x, y = zip(*points)
plt.scatter(x, y, s=0.1)
plt.show()

df = pd.DataFrame({"x": [pt1[0], pt2[0], pt3[0], pt4[0]],
                   "y": [pt1[1], pt2[1], pt3[1], pt4[1]]})
df2 = pd.DataFrame({"x": x, "y": y})
df = pd.concat([df, df2], ignore_index=True)
df.to_csv("r10000.csv", sep=";", index=False, mode="w+")

# %% rectangle with 100 000 points on it (near best case)

# rectangle with 100 000 points on rectangle
random.seed()

pt1 = (50, 50)
pt3 = (1000, 770)

pt2 = (pt3[0], pt1[1])
pt4 = (pt1[0], pt3[1])

points = [points_on_rectangle(pt1, pt2, pt3, pt4) for _ in range(99996)]

x, y = zip(*points)
plt.scatter(x, y, s=0.1)
plt.show()

df = pd.DataFrame({"x": [pt1[0], pt2[0], pt3[0], pt4[0]],
                   "y": [pt1[1], pt2[1], pt3[1], pt4[1]]})
df2 = pd.DataFrame({"x": x, "y": y})
df = pd.concat([df, df2], ignore_index=True)
df.to_csv("r100000.csv", sep=";", index=False, mode="w+")

# %% polygone with 100 points within

# polygone with 100 points within it
random.seed()

pt1 = (10, 10)  # limits of coordinates
pt3 = (1000, 790)  # limits of coordinates

pt2 = (pt3[0], pt1[1])
pt4 = (pt1[0], pt3[1])

points = [points_within_polygone(pt1, pt2, pt3, pt4) for _ in range(100)]

x, y = zip(*points)
plt.scatter(x, y, s=0.1)
plt.show()

df = pd.DataFrame({"x": x, "y": y})
df.to_csv("p100.csv", sep=";", index=False, mode="w+")

# %% polygone with 10 000 points within

# polygone with 10 000 points within it
random.seed()

pt1 = (50, 50)
pt3 = (1000, 770)

pt2 = (pt3[0], pt1[1])
pt4 = (pt1[0], pt3[1])

points = [points_within_polygone(pt1, pt2, pt3, pt4) for _ in range(10000)]

x, y = zip(*points)
plt.scatter(x, y, s=0.1)
plt.show()

df = pd.DataFrame({"x": x, "y": y})
df.to_csv("p10000.csv", sep=";", index=False, mode="w+")

# %% polygone with 100 000 points within

# polygone with 100 000 points within it
random.seed()

pt1 = (50, 50)
pt3 = (1000, 770)

pt2 = (pt3[0], pt1[1])
pt4 = (pt1[0], pt3[1])


points = [points_within_polygone(pt1, pt2, pt3, pt4) for _ in range(100000)]

x, y = zip(*points)
plt.scatter(x, y, s=0.1)
plt.show()

df = pd.DataFrame({"x":x, "y":y})
df.to_csv("p100000.csv",sep=";",index=False,mode="w+")


# points on cycle
points = points_on_cycle()

x, y = zip(*points)
plt.scatter(x, y, s=0.1)
plt.show()

df = pd.DataFrame({"x":x, "y":y})
df.to_csv("pCycle.csv",sep=";",index=False,mode="w+")
