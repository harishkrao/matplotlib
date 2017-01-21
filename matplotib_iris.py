# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 11:03:55 2017

@author: harish k rao
"""

import pandas as pd
import warnings
warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
iris = pd.read_csv(r'C:\Users\priyu\Documents\matplotlib\Iris.csv')

iris.head()

iris.plot(kind="scatter",x="SepalLengthCm",y="SepalWidthCm")

iris.plot(kind="scatter", x="PetalLengthCm", y="PetalWidthCm")