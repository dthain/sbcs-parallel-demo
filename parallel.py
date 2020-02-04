# A brief introduction to parallelism using Python and multiprocessing

from multiprocessing import Pool
import time
import random

# Change the values of these variables to play around with parallel performance.
# there are initially 20 tasks (ntasks) to complete using 2 workers (nworkers).

# Each task takes (on average) 2 seconds to complete, so how long will it take
# to finish with 2 workers and 20 tasks?

# Now vary the number of workers up and down.  Predict the total runtime before
# running the experiment; some answers are easy and some are a little unpredictable.

# Q: Do the tasks always finish in the same order?  Why or why not?

nworkers = 2
ntasks = 20

# Define a function f that computes the factorial of x and returns it.
# Along the way, print out when the function starts and ends.
# (Also, add a little sleep so the function takes a few seconds.)

def f(x):
    print("task for ", x, " starting")
    total = 1
    i=x
    while i>1:
        total = total * i
        i=i-1
    time.sleep(random.randrange(1,4))
    print("task for ", x, " stopping")
    return total

# The main program creates a pool of nworkers, sets up ntasks,
# and then lets them all run.

print("main: starting all tasks")

p = Pool(nworkers)
inputs = range(1,ntasks)
starttime = time.time()
outputs = p.map(f, inputs)
stoptime = time.time()

print("main: all tasks done")
print("results: ", outputs)
print("elapsed time: ",stoptime-starttime, " seconds")
