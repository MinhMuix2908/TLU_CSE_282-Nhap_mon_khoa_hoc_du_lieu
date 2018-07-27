# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 19:24:01 2017

@author: Minh
"""

import random
import csv




def exportCSV(filename,L1=[]):
    with open('IrisNewTest.csv', 'w', newline='') as csvfile:
        fwriter = csv.writer(csvfile, delimiter=',')
        for i in range (0,len(L1),4):
            fwriter.writerow([L1[i]]+[L1[i+1]]+[L1[i+2]]+[L1[i+3]])


def RandList(n):
    L1 = []
    for i in range(0,n,1):
        L1.append(round(random.uniform(0.0,9.9),1))
    return L1


if __name__ == '__main__':
    k=int(input("Nhập số lượng test:"))
    testList = RandList(k*4)
    
    exportCSV('IrisNewTest.csv',testList)
    