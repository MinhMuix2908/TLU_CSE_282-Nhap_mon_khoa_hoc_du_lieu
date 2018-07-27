# -*- coding: utf-8 -*-
"""
Created on Mon May 28 20:36:49 2018

@author: minmin
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model, metrics
# đọc dữ liệu từ file csv
df = pd.read_csv("winequality-red.csv", index_col = 0)
print(df)
# vẽ biểu đồ minh họa dataset
#plt.plot(df.Cao, df.Nang, 'ro')
plt.xlabel('Chiều cao (cm)')
plt.ylabel('Cân nặng (kg)')
plt.show()

# sử dụng hồi quy tuyến tính
X = df.loc[:, ['alcohol']].values # X là dữ liệu đầu vào
y = df.Nang.values # y là dữ liệu đầu ra
model = linear_model.LinearRegression() # loại mô hình
model.fit(X, y) # tập huấn trên dữ liệu
# in một số thông tin về mô hình
mse = metrics.mean_squared_error(model.predict(X), y)
print("Tổng bình phương sai số trên tập mẫu:", mse)
print("Hệ số hồi quy:", model.coef_)
print("Sai số:", model.intercept_)
#print(f"Công thức: [Nặng] = {model.coef_} x [Cao] + {model.intercept_}")
print("Công thức : [Nặng] =",model.coef_,"x [Cao] +",model.intercept_)

plt.scatter(X, y, c='b')
plt.plot(X, model.predict(X))
plt.show()