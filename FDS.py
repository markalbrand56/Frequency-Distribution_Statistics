#!/usr/bin/env python3.8
#_*_ coding: utf8 _*_

import collections
from s_package.interval import finterval

def frecuencias():
    data = []
    counter = 0
    while True:
        var = float(input("Enter a number: "))
        if var == 0.0:
            break #0 is for finishing the input process
        else:
            counter += 1
            data.append(var)
    data = sorted(data)
    countrep = collections.Counter(data) #this will sort data by how many times it appears in the data collection
    i_range = max(data) - min(data)
    min_inter = int(input("How many intervals do you at least need? "))
    max_inter = int(input("How many intervals is your max? "))
    max_inter += 1
    intervals = finterval(i_range,min_inter,max_inter)
    print("\n-------")
    print ("Sorted data: ", data)
    print("Amount of data: ", counter)
    print ("Data, and how many times they repeat: ",countrep)
    if intervals == 0:
        print("An error ocurred while calculating intervals...")
    else:
        print("Possible intervals: ",intervals)
    print("-------")

if __name__ == "__main__":
    frecuencias()