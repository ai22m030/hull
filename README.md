# APRG_ConvexHull

## General operation jarvis march

The programm has 2 modes:
- mode 0: The speed mode
  calculates the convex hull using the Jarvis' March algorithm and prints out a list of all points located on the boundaries of the hull. A measure of the performance in seconds is shown in the console.
- mode 1: The graphics mode
  shows an graphical animation of how the algorithm determines the points which form the convex hull

In both modes you can define for how many points a hull shall be determined. The points are then derived at random.

### Libraries used

- pandas
- numpy
- pygame
- random
- time
- timeit

## General operation divide and conquer

The programm has 2 modes:
- mode 0: The speed mode
  calculates the convex hull using the divide and conquer algorithm and prints out a list of all points located on the boundaries of the hull. A measure of the performance in seconds is shown in the console.
- mode 1: The graphics mode
  shows an graphical animation of how the algorithm determines the points which form the convex hull. A measure of the performance in seconds is shown in the console.

In both modes you can define for how many points a hull shall be determined. The points are then derived at random.

### Libraries used

- numpy
- timeit
- math
- matplotlib
- imageio

### O-notation performance

- For showing the performance of 'Divide & Conquer', run the file 'show_performance_dc.py'
- For showing the performance of 'Jarvis' March', run the file 'show_performance_j.py'

After testing it shows that there is no best and worst case for both algorithms.
