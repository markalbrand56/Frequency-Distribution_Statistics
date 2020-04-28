#!/usr/bin/env python3.8
#_*_ coding: utf8 _*_

import collections

def range_iterval(list):
    i_range = max(list) - min(list)
    print (i_range)
    def interval(num):
        poss_inter = []
        inter_lst = []
        for i in range(1,(int(i_range))): #NEEDS REVISION    
             for x in range (8,19):
                poss_inter.append(x)

             if i_range / i in poss_inter:
                 i_interval = i_range / i 
                 inter_lst.append(i_interval)


        print (inter_lst)
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
    range_iterval(data)
    print("-------")

if __name__ == "__main__":
    frecuencias()