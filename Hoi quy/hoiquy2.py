import pandas as pd
import numpy as np
 
wine = pd.read_csv("winequality-red.csv", sep=";")
wine.head
print(wine)

# Phan tich hoi quy
from sklearn import linear_model
clf = linear_model.LinearRegression()
#X=wine[1:10]
# Tạo dataframe chỉ chứa data làm biến giải thích
wine_except_quality = wine.drop("quality", axis=1)
X = wine_except_quality

# Sử dụng quality làm biến mục tiêu
Y = wine['quality']
 
# Tạo model
clf.fit(X, Y)
 
# Hệ số hồi quy
print(pd.DataFrame({"Name":wine_except_quality.columns,
                    "Coefficients":clf.coef_}).sort_values(by='Coefficients') )
 
# Sai số
print(clf.intercept_)

