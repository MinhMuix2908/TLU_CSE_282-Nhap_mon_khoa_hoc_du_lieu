import unicodecsv
import random
import operator
import math
def get_data():
    with open('IRIS.csv', 'rb') as f:
        reader = unicodecsv.reader(f)
        i_data = list(reader)
    return i_data


def shuffle(i_data):
    random.shuffle(i_data)
    train_data = i_data[:int(0.7*30)]
    test_data = i_data[int(0.7*30):]
    return train_data, test_data


def euclideanDist(x, xi):
    d = 0.0
    for i in range(len(x)-1):
        d += pow((float(x[i]) - float(xi[i])), 2)
        d = math.sqrt(d)
        return d
  
    
    
    
def knn_predict(test_data, train_data, k_value=15):
   for i in test_data:
       
       for ele in train_data:
           
           #print(euclideanDist(i, ele))    
            
        #sap xep tang dan
        
            
            
            
        
            
            
CSV_data=get_data()
train_data, test_data = shuffle(CSV_data)
knn_predict(test_data, train_data)