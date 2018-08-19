import pandas as pd
import numpy as np
 
wine = pd.read_csv("winequality-red.csv", sep=";") 
wine.head
print(wine)
# Phan tich hoi quy
# import thư viện sklearn.linear_model.LinearRegression 
from sklearn import linear_model
clf = linear_model.LinearRegression()
 
# Sử dụng "density (mật độ)" làm biến giải thích
X = wine.loc[:, ['density']].as_matrix()
 
# Sử dụng "alcohol (Số độ cồn)" làm biến mục đích
Y = wine['alcohol'].as_matrix()
# Tạo model suy đoán
clf.fit(X, Y)
# Hệ số hồi quy
print(clf.coef_)
# Sai số
print(clf.intercept_)
# Score
print(clf.score(X, Y))
#Bieu dien tren do thi
# sử dụng package matplotlib
import matplotlib.pyplot as plt
 
# Biểu diễn sự phân bố tập dữ liệu input
# c: color
plt.scatter(X, Y, c='b')
 
# Đường thẳng hồi quy
plt.plot(X, clf.predict(X),'r')
plt.show()