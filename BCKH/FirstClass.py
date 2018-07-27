# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:49:02 2018

@author: Minh
"""

import math
import operator

"""Mã chuyển đổi input từ CSV sang List sang dictList"""
def ChangeIN(listIN,DataBaseInterest): #input:List from CSV -----output dict in list for calculator
    Out=[] #list kết quả cuối
    
    _id={"id": listIN[0]}
    Out.append(_id) # nhập đc id
    
    _bday={"birth":listIN[1]}
    Out.append(_bday) # nhập đc ngày sinh birth
    
    _gender={"sex":listIN[2]}
    Out.append(_gender) #nhập đc gender
    
    _insideInterest={} #tạo 1 dict chứa các phần tử key lấy trong DataBaseInterest
    for i in DataBaseInterest:
        _insideInterest[i]=listIN[DataBaseInterest.index(i)+3]
        #lấy đc giá trị cho dict vừa tạo
    _interest={"interest":_insideInterest}
    Out.append(_interest) #nhập đc interest
    
    _location={"location":{"lat":listIN[3+len(DataBaseInterest)], "long": listIN[4+len(DataBaseInterest)]}}
    Out.append(_location) #nhập đc location
    return Out
"""-------------------------------------------------"""


"""Mã tính toán khoảng cách và tìm người giống nhất"""
def EuclidDistance(test, sample2): #used in def Result
    x1=float(test[4]["location"]["lat"])
    y1=float(test[4]["location"]["long"])
    x2=float(sample2[2])
    y2=float(sample2[3])
    return math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))
  
    
def HammingDistances(sample1, sample2): #used in def Result
    s1= sample1[3]["interest"]
    s2= sample2[3]["interest"]
    count=0
    for i in DataInterest:
        if not (s1[i]== s2[i]):
            count+=1
    return count
    

def Result(test,database, defaultLeftOfFirstEliminated =10): #calculator for final answer
    hamresult=[]
    listID=[]
    listLat=[]
    listLong = []
    for record in database:
        hamresult.append(HammingDistances(record,test)) # được 1 list chứa kết quả hamming
        listID.append(record[0]["id"])
        listLat.append(record[4]["location"]["lat"])
        listLong.append(record[4]["location"]["long"])
    
    result1= list(zip(listID, hamresult,listLat,listLong)) #list chứa zip của id và hamming
    #print(result1)
    result1.sort(key=operator.itemgetter(1))
    #print("After:")
    #print(result1)
    
    result2=[]
    if(defaultLeftOfFirstEliminated>len(database)): 
        defaultLeftOfFirstEliminated=len(database)  
    #số người giống nhau cần tìm lớn hơn số người trong database ta cho số người cần tìm bằng cả database
    #trường hợp rất khó xảy ra vì không thể tìm số lượng người quá lớn
    #đoạn mã này sẽ hữu dụng khi sau này chúng ta có thêm chức năng cho người dùng tự yêu cầu số người cần tìm
    
    for i in range(0, defaultLeftOfFirstEliminated,1):
        result2.append(result1[i])   # được list chứa 10 phần tử có sở thích giống nhau nhất
    #print(result2)
    euresult=[]
    listID2=[]
    for record in result2:
        euresult.append(EuclidDistance(test,record)) #đc kc Euclid của các phần tử
        listID2.append(record[0])
    #print(listID2)
    result3= list(zip(listID2,euresult))
    #print(result3)
    result3.sort(key=operator.itemgetter(1))
    finalResult=[]
    for result in result3:
        #print(result[0])
        finalResult.append(result[0])
    return finalResult
"""----------------------------------------------------------------------------------"""


"""This is the Built-in DataBase of this module"""
DataInterest=["Pet","Art","Dance",]
def AddMoreInterest(newInterest): # tăng thêm tùy chọn sở thích
    DataInterest.append(newInterest)
"""-------------------------------------------"""


"""Get thông tin newUser và DatabaseCity của newUser"""
newUser=[5,"1/19/1994","male",0,0,0,21.0070123,105.8257092] #người dùng vừa đăng ký

#danh sách bản khi thành phố rời rạc và bộ đếm
CityRecord1=[1651160863,"1/12/1998","male",1,1,0,21.0070123,105.8257092]
CityRecord2=[1651160931,"1/1/1988","female",0,0,1,20.999585,105.854268]
CityRecord3=[1651160910,"1/1/1948","female",1,1,1,20.111111,104.854268]

"""-----------------------------------------------"""


DataBaseCity = [ChangeIN(CityRecord1,DataInterest),ChangeIN(CityRecord2,DataInterest),ChangeIN(CityRecord3,DataInterest)]



"""Run from here"""


if __name__ == "__main__": 
    #print(DataBaseCity)
    print(Result(ChangeIN(newUser,DataInterest) ,DataBaseCity,5))


    
    