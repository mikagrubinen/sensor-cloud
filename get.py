# get.py
import random

def temperature():
    ret = random.uniform(50, 75)
    return round(ret, 2)

def pressure():
    ret = random.uniform(950, 1015)
    return round(ret, 2)

def humidity():
    ret = random.uniform(40, 53)
    return round(ret, 2)

def light():
    ret = random.uniform(1000, 2000)
    return round(ret, 2)