# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 20:34:24 2018

@author: Minh
"""
import math
def isPrime(a): #câu 1: kiểm tra 1 số có phải số nguyên tố k
    if(a==1):
        return False;
    for i in range(2,a,1):
        if(a%i==0):
            return False;
    return True;


def printPrimeBetween(a,b): #câu 2: tìm các số nguyên tố [a,b]
    result=[];
    for i in range(a,b+1,1):
        if(isPrime(i)):
            result.append(i);
    return result

def GCD(a,b): #câu 3: tìm ước chung lớn nhất
    while(a!=b):
        if(a>b):
            a=a-b;
        else:
            b=b-a;
    return a;


def LCM(a,b): #tìm bội chung nhỏ nhất
    return int(abs(a*b)/GCD(a,b));


def lengthCal(xA,yA,xB,yB,xC,yC): #chuyển các tọa độ về độ dài các cạnh
    xAB=xB-xA;
    yAB=yB-yA;
    dAB=math.sqrt(math.pow(xAB,2)+math.pow(yAB,2));
    xBC=xC-xB;
    yBC=yC-yB;
    dBC=math.sqrt(math.pow(xBC,2)+math.pow(yBC,2));
    xCA=xA-xC;
    yCA=yA-yC;
    dCA=math.sqrt(math.pow(xCA,2)+math.pow(yCA,2));
    return dAB, dBC, dCA;
    
    
def isRightTriangle(dAB,dBC,dCA): #tam giác vuông
    if(dAB>dBC and dAB>dCA and round(math.pow(dAB,2),4)==round(math.pow(dBC,2)+math.pow(dCA,2),4)):
        return "C";
    elif(dBC>dAB and dBC>dCA and round(math.pow(dBC,2),4)==round(math.pow(dAB,2)+math.pow(dCA,2),4)):
        return "A";
    elif(dCA>dAB and dCA>dBC and round(math.pow(dCA,2),4)==round(math.pow(dAB,2)+math.pow(dBC,2),4)):
        return "B";
    else:
        return None;
       
def isIsoscelesTriangle(dAB,dBC,dCA): #tam giác đều
    if(dAB==dBC):
        return "B";
    elif(dBC==dCA):
        return "C";
    elif(dCA==dAB):
        return "A";
    else:
        return None;
    
def isEquilateralTriangle(dAB,dBC,dCA): #tam giác cân
    if(dAB==dBC==dCA):
        return True;
    else:
        return False;
    
    
def triangleClassification(xA,yA,xB,yB,xC,yC):
    dAB, dBC, dCA = lengthCal(xA,yA,xB,yB,xC,yC);
    rightTriangle = isRightTriangle(dAB, dBC, dCA);
    isoscelesTriangle = isIsoscelesTriangle(dAB, dBC, dCA);
    equilateralTriangle = isEquilateralTriangle(dAB,dBC,dCA);

  
    
#đây là phần main chương trình
if __name__ == "__main__":
    
    pass    