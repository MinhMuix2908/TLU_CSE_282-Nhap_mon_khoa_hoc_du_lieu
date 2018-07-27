'''
User1= [
        {"id" : "1"},
        {"birth" : "1/12/1998"},
        {"sex" : "male"},
        {"interest" : {
                "Pet": "1",
                "Art":"1",
                "Dance":"0"
                }
        },
        {"location" : {
                "lat" :"21.0070123",
                "long":"105.825709"
            }
        }                       
]

User2= [
        {"id" : "2"},
        {"birth" : "12/3/1998"},
        {"sex" : "female"},
        {"interest" : {
                "Pet": "1",
                "Art":"0",
                "Dance":"0"
                }
        },
        {"location" : {
                "lat" :"10.778359",
                "long":"106.752511"
            }
        }                       
]

User3= [
        {"id" : "3"},
        {"birth" : "1/1/1998"},
        {"sex" : "female"},
        {"interest" : {
                "Pet": "0",
                "Art":"0",
                "Dance":"1"
                }
        },
        {"location" : {
        "lat" :"10.121442",
        "long":"12.345345"
            }
        }                       
]
'''
import math
from operator import itemgetter
Data = [{"loc" : "hanoi", "lat": 21.0070123, "long": 105.825709},
        {"loc" : "hcm", "lat": 10.778359, "long": 106.752511},
        {"loc" : "hue", "lat": 16.467283, "long": 107.579685},
        {"loc" : "japan", "lat": 36.189022, "long": 138.044307},
        {"loc" : "kenya", "lat": -0.176227, "long": 37.434603},
]

Test  = {"lat": 16.267893, "long": 112.057949}

def dist(O1=[],O2=[]):
    return math.sqrt(math.pow(float(O1["lat"])-float(O2["lat"]),2)+
                     math.pow(float(O1["long"])-float(O2["long"]),2));


def NearestCity(NewTest={}):
    arr= [] #kieu dict trong list
    arr1= [] #kieu list trong list
    for i in Data:
        arr.append({i["loc"]:dist(i,NewTest)})
        arr1.append([i["loc"]] + [dist(i, NewTest)] )
    arr1.sort(key = itemgetter(1)) 
    return arr1              
if __name__ == '__main__':
    
    print(NearestCity(Test))

    
    
    
    
    
    
    
    
    
    
    
    
    