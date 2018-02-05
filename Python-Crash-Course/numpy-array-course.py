# -*- coding: utf-8 -*-

import numpy as np

np.arange(0,10,2)

np.zeros((5,5))

np.linspace(0,5,10)

np.eye(4)

np.random.rand()

arr = np.arange(25)

ranarr = np.random.randint(0,50,10)

arr = arr.reshape(5,5)

print(ranarr.min())

from numpy.random import randint 

randint(2,10)

#Begin numpy indexing and selection

arr = np.arange(0,11)

arr

arr[8]

arr[0:5]

arr_2d = np.array([[5,10,15], [20,25,30], [35,40,45]])

arr_2d[:2,1:]

bool_arr = arr_2d > 5 

bool_arr

arr_2d[bool_arr]

