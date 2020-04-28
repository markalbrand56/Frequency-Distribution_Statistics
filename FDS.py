#!/usr/bin/env python3.8
#_*_ coding: utf8 _*_

import collections

def range(list):
    i_range = max(list) - min(list)
    print (i_range)
    def interval(num):
        i_interval = i_range // 2
        print (i_interval)
    interval(i_range)
    

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
    range(data)
    

if __name__ == "__main__":
    frecuencias()