import numpy as np
import pandas as pd
import random as rd


def create_big_array(lenght):
    print('Building array')

    arr = np.zeros(lenght)
    compt = 0

    for i in arr:
        print("Loading: " + str(round(compt / lenght * 100)) + "%", end='\r', flush=True)
        i = rd.expovariate(3)
        compt+=1
    
    return arr