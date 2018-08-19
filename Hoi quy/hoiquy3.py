import pandas as pd
import numpy as np
 
wine = pd.read_csv("winequality-red.csv", sep=";")
wine.head


# Phan tich hoi quy
from sklearn import linear_model
clf = linear_model.LinearRegression()
 
# chuẩn hoá dữ liệu các cột
wine2 = wine.apply(lambda x: (x - np.mean(x)) / (np.max(x) - np.min(x)))
wine2.head()
print(wine2)
# Tạo dataframe không chứa quality làm biến giải thích
X = wine2.drop("quality", axis=1)
 
# Sử dụng quality làm biến mục tiêu
Y = wine2['quality']

clf.fit(X, Y)
 
print(pd.DataFrame({"Name":X.columns, "Coefficients":np.abs(clf.coef_)}).sort_values(by='Coefficients') )
 
print(clf.intercept_)
