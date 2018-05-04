# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 10:08:47 2018

@author: Minh
"""
"""
giải phương trình bậc 1,2
"""
import math;
def ptbac1(a,b):
    print("Giải phương trình bậc 1: ",a,"x + ",b," = 0",sep='');
    if(a==0):
        if(b==0): #a=0, b=0
            print("Phương trình có vô số nghiệm");
            return
        else: #a=0, b!=0
            print("Phương trình vô nghiệm");
    else: #a !=0
        print("Phương trinh có nghiệm duy nhất:", -b/a);
        return -b/a;


def ptbac2(a,b,c): #hàm giải phương trình bậc 2 ax^2+bx+c=0
    if(a==0): # a=0
        print("Đây là phương trình bậc 1 vì a = 0");
        return ptbac1(b,c),None; 
        ''' gọi hàm giải phương trình bậc 1 và trả ra 1 kết quả none thay vì chỉ
            return mỗi hàm ptbac1 vì:
                giả sử ở main ta dùng x1,x2=ptbac2(0,1,1)
                nếu chỉ có return 1 số thì x2 sẽ có lỗi vì ko có giá trị đc truyền vào x2
            
        '''
    else:
        print("Giải phương trình bậc 2: ",a,"x^2 + ",b,"x + ",c," = 0",sep='');
        delta=b*b-4*a*c; # tính delta
        if(delta>0): 
            print("Phương trình có 2 nghiệm riêng biệt x1 =",(-b+math.sqrt(delta))/2*a,"và x2 =",(-b-math.sqrt(delta))/2*a);
            return(-b+math.sqrt(delta))/2*a,(-b-math.sqrt(delta))/2*a
        elif(delta==0):
            print("Phương trình có nghiệm duy nhất x =",-b/2*a);
            return -b/2*a,None
        else:
            print("Phương trình vô nghiệm");


def inputNumber(): #hàm nhập a,b,c
    try: # nếu có lỗi ở block này thì sẽ được đi xuống phần bắt lỗi ở dưới
        a=float(input("Mời nhập a: "));
        b=float(input("Mời nhập b: "));
        c=float(input("Mời nhập c: ")); 
        #nhập 3 số a,b,c
    except ValueError: #lỗi kiểu
        print("Bạn vừa nhập chữ hoặc nhập rỗng! Mời nhập số!"); #in lỗi
        return inputNumber(); # đệ quy lại hàm
    except Exception as ex: #các lỗi còn lại đặt tên là ex
        print("Lỗi: ",ex); #in ra tên lỗi ex để sửa lại
        return inputNumber(); # đệ quy lại hàm
    return a,b,c; # trả ra a,b,c đã đúng kiểu để tính toán


#đây là phần main chương trình
if __name__ == "__main__":
    a,b,c=inputNumber();# gọi hàm nhập a,b,c
    x1,x2= ptbac2(a,b,c); #gọi hàm giải phương trình bậc 2
    
    
    
