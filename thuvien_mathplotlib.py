# -*- coding: utf-8 -*-
"""
Created on Sun May 27 15:11:42 2018

@author: minmin
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
csv1=pd.read_csv('k59.csv',index_col=0)
print(csv1)

print(csv1.head(),'\n',csv1.tail())


print('Diem lon hon 8: \n',csv1[csv1.Diem>8])
print(csv1.Ten[ (csv1.Diem >= 4)==False ])
a=list(csv1.Diem)
plt.hist(a)
plt.show()