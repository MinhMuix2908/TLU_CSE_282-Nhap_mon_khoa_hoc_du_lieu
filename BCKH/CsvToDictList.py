# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 23:25:50 2018

@author: Minh
"""

testIn=[ #this is the goal
    {"id" : "5"},
    {"birth" : "1/19/1994"},
    {"sex" : "male"},
    {"interest" : {
            "Pet": "0",
            "Art":"0",
            "Dance":"0"
            }},
    {"location" : {
            "lat" :"21.0070123",
            "long":"105.825709"
            }},
    ]

DataInterest=["Pet","Art","Dance"] 

A=[5,"1/19/1994","male",0,1,1,21.222,106.2222]

"""----------------------------------------------"""
def ChangeIN(listIN,DataBaseInterest):
    Out=[] #list kết quả cuối
    
    _id={"id": listIN[0]}
    Out.append(_id) # nhập đc id
    
    _bday={"birth":listIN[1]}
    Out.append(_bday)
    
    _gender={"sex":listIN[2]}
    Out.append(_gender)
    
    _insideInterest={}
    for i in DataBaseInterest:
        _insideInterest[i]=listIN[DataBaseInterest.index(i)+3]
    _interest={"interest":_insideInterest}
    Out.append(_interest)
    
    _location={"location":{"lat":listIN[3+len(DataBaseInterest)], "long": listIN[4+len(DataBaseInterest)]}}
    Out.append(_location)
    print(Out)
    pass


if __name__ == "__main__": 
    ChangeIN(A,DataInterest)


    