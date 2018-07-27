# -*- coding: utf-8 -*-
"""
Created on Mon May 28 20:36:49 2018

@author: minmin
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model, metrics

df= pd.read_csv('winequality-red.csv')
print(df)

#qlt = df.loc[:, ['quality']].values
X = df.loc[:, ['']].values