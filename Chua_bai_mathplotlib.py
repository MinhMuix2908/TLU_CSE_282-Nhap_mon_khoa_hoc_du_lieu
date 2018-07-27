# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

def Bai1():
    x=(1,2,3)
    y=(2,4,1)
    plt.plot(x,y)
    plt.title("Sample graph!")
    plt.xlabel('x-axis')
    plt.ylabel('y-axis') 
    plt.show()
    
def Bai2():
    x1=(10,20,30)
    y1=(20,40,10)
    x2=x1
    y2=(40,10,30)
    plt.plot(x1,y1,'g-',x2,y2,'b-')
    plt.title('Two or more lines on same plot with suitable legends')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')    
    plt.legend(["line 1","line 2"])
    plt.axis([1,3,1,4]) # lệnh này dùng trong spyder sẽ gây ra mất đường biểu đồ
    plt.show()
    
    
def Bai3():
    x=(1,4,5,6,7)
    y=(2,6,3,6,3)
    plt.plot(x,y,'b-.',color='r',linestyle='-.',lw='2',marker='o',markerfacecolor='b',markersize='12')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis') 
    plt.title("Display marker")
    plt.axis([1,8,1,8])

def Bai4():
    Languages=("Java", "Python", "PHP", "JavaScript", "C#", "C++")    
    Popularity= (22.2, 17.6, 8.8, 8, 7.7, 6.7)
    plt.bar(range(len(Popularity)),Popularity)    
    plt.ylabel("Popularity")
    plt.xticks(range(len(Popularity)),Languages)
    
def Bai5():
    Languages=("Java", "Python", "PHP", "JavaScript", "C#", "C++")    
    Popularity= (22.2, 17.6, 8.8, 8, 7.7, 6.7)
    plt.pie(Popularity,labels=Languages)
    
    
    
    
    
    
Bai1()
Bai5()