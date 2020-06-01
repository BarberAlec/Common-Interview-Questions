'''Finds the closest fib number to a given input'''
import numpy as np


def fib(n):
    '''returns fib number at index n'''
    goldR = (1 + np.sqrt(5)) / 2
    result = int(round((goldR**n - (1-goldR)**n) / np.sqrt(5)))
    return result


def fibinv(f):
    '''returns index of fib number f, if f is not a fib number, 
    then return closet fib number index, Binet's formula'''
    if f < 2:
        return f

    goldR = (1 + np.sqrt(5)) / 2
    return int(round(np.log(f * np.sqrt(5)) / np.log(goldR)))

def ans_1():
    while True:
        k = input('Number: ')
        if k == '':
            continue
        k = int(k)
        indx = fibinv(k)
        print(fib(indx))


def fib_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    first_n = 0
    second_n = 1

    for i in range(1,n):
        temp = first_n+second_n
        first_n = second_n
        second_n = temp
    return second_n


def next_fib_num(prev,curr):
    return curr,prev+curr

def closest_fib_num(num):
    curr = 1
    prev = 0

    while curr<num:
        prev,curr = next_fib_num(prev,curr)
    
    if abs(curr-num) < abs(prev-num):
        return curr
    else:
        return prev

def ans_2():
    for i in range(-5,5):
        print(str(i)+' : '+str(closest_fib_num(i)))

ans_2()