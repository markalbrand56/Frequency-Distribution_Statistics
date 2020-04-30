#!/usr/bin/env python3.8
#_*_ coding: utf8 _*_

import collections

import Myapp.interval
from Myapp.interval import range_iterval

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
    print (data)
    print("Amount of data: ", counter)
    cuentarep = collections.Counter(data) #this will sort data by how many times it appears in the data collection
    print (cuentarep)
    range_iterval(data)
    print("-------")

if __name__ == "__main__":
    frecuencias()