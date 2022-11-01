import pandas
from timeit import Timer
# import helper
from divide_conquer import convex_hull
from jarvis import runJarvisAlgo
from numpy import genfromtxt

files = ['t100.csv','t10000.csv','t100000.csv','r100.csv','r10000.csv','r100000.csv','p100.csv','p10000.csv','p100000.csv','pCycle.csv']



for file in files:
    #Extract the xy coordinates
    xy = genfromtxt(file, delimiter=';')[1:]
    #Divide and Conquer
    print('Divide and Conquer')
    average_time = 0
    for i in range(5):
        t = Timer(lambda: convex_hull(xy, 0))
        average_time += t.timeit(number=1)
    print('Divide_conquer | File: '+str(file)+' | Time: '+str(average_time/5))

    #Jarvis March
    print('Jarvis March')
    average_time = 0
    for i in range(5):
        df_file = pandas.read_csv(file,delimiter=";")
        t = Timer(lambda: runJarvisAlgo(1, 0, df_file))
        average_time += t.timeit(number=1)
    print('Jarvis | File: '+str(file)+' | Time: '+str(average_time/5))