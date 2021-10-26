# Author CCG AMDG 10/25/21

import time
import math

t1start = time.perf_counter()

calc = math.pow(2,2)

t1end = time.perf_counter()

t2start = time.perf_counter()

brain = 2 ** 2

t2end = time.perf_counter()

speed1 = t1end - t2start
speed2 = t2end - t2start

print(speed1)
print(speed2)

