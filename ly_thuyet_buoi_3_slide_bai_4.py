# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 10:47:33 2018

@author: Minh
"""

"""
1.Người dùng nhập từ bàn phím liên tiếp các từ tiếng Anh viết tách nhau bởi dấu cách.
Hãy nhập chuỗi đầu vào và tách thành các từ sau đó in ra màn hình các từ đó theo thứ tự từ điển.

2.Người dùng nhập từ bàn phím chuỗi các số nhị phân viết liên tiếp được nối nhau bởi dấu phẩy.
Hãy nhập chuỗi đầu vào sau đó in ra những giá trị được nhập.

3.Nhập số n, in ra màn hình các số nguyên dương nhỏ hơn n có tổng các ước số lớn hơn chính nó.

4.Hãy nhập số nguyên n, tạo một list gồm các số fibonacci nhỏ hơn n và in ra
Dãy fibonacci là dãy số nguyên được định nghĩa một cách đệ quy như sau: 
    f(0)=0, f(1) = 1, f(1<n) = f(n-1) + f(n-2)
    
5.Hãy tạo ra một tuple gồm các số nguyên tố nhỏ hơn 1 triệu.
Số nguyên tố là số tự nhiên có 2 ước số là 1 và chính nó.

6.Nhập vào một chuỗi từ người dùng, kiểm tra xem đó có phải địa chỉ email hợp lệ hay không?

7.Nhập n, in n dòng đầu tiên của tam giác pascal.
"""

def bai1():
    inputLine = input("Mời nhập các từ tiếng anh tách nhau bởi dấu cách: ").split(" ");
    print(sorted(inputLine))

def bai2():
    inputLine = input("Mời nhập chuỗi nhị phân cách nhau bởi dấu phẩy: ").split(",");
    for digi in inputLine:
        for char in digi:
            if (char !='0' and char !='1'):
                print("Có chuỗi không phải nhị phân hoặc chứa dấu cách")
                bai2()
                return
    print(inputLine)
def sumOfCommonFactor(n):
    s=0;
    for i in range(1,n,1):
        if(n%i==0):
            s+=i;
    return s;       
        
   
def bai3():
    n= int(input("Nhập n: "));
    for i in range(1,n,1):
        if(sumOfCommonFactor(i)>i):
            print(i);

def Fibo(n):
    if(n==0):
        return 0;
    elif(n==1):
        return 1;
    else:
        return Fibo(n-1)+Fibo(n-2);

def bai4():
    n= int(input("Nhập n: "));
    for i in range(1,n,1):
        print("Fibonacci(",i,"):",Fibo(i))

def isPrime(a):
    if(a==1):
        return False;
    for i in range(2,a,1):
        if(a%i==0):
            return False;
    return True;   
 
def bai5():
    for i in range(1,1000,1):
        if(isPrime(i)):
            print(i)
            

if __name__=="__main__":
    bai5()
    pass