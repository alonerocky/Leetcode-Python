'''
Created on Apr 18, 2014

@author: sli1
'''
import random
def swap(array, i, j):
    if i != j:
        temp = array[i]
        array[i] = array[j]
        array[j] = temp

def sort(colors):
    if colors is None:
        return
    low = -1
    high = len(colors)
    index = 0
    while index < high:
        if colors[index] == 1:
            index += 1
        elif colors[index] == 0:
            low += 1
            swap(colors,low,index)
            index += 1
        elif colors[index] == 2:
            high -= 1
            swap(colors, high,index)


def test():
    colors = [0] * 20
    for i in range(20):
        colors[i] = random.randint(0,2)
    print(colors)
    sort(colors)
    print(colors)

test()



