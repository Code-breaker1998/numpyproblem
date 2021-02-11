import numpy as np
# n = np.array([0,1, 2, 3, 4, 5, 6, 7, 8, 9])
# n[1:10:2] = -1
# print(n)
# n1=np.arange(3,10,2)
# print(n1)
# n2 = np.array([11,12,13,14,15,16,17,15,11,12,14,15,16,17])
# result = np.where(n2 < 12,[1,2,4],[7,8,9])
# print(result)

# a = np.arange(10).reshape(2,-1)
# b = np.repeat(1,10).reshape(2,-1)
# print(a)
# print(b)

# n=np.arange(10)
# print(n.reshape(2,5))
#
# a = np.arange(10).reshape(2,-1)
# b = np.repeat(1,10).reshape(2,-1)
#
# v=np.hstack((a,b))
# print(v)

# b=np.array([1,2,3])
# print(np.r_[np.repeat(b,3),np.tile(b,3)])
#
# a=np.array([1,2,3,2,3,4,3,4,5,6])
# b=np.array([7,2,10,2,7,4,9,4,9,8])
# print(np.intersect1d(a,b))

# a=np.array([1,2,3,4,5])
# b=np.array([5,6,7,8,9])
# print(np.setdiff1d(a,b))

# a = np.array([2,6,1,9,10,3,27])
# in1 = np.where((a>=5) & (a<=10))
# print(a[in1])

# import random
# n=np.random.randint(5,10,size=(5,3)) + np.random.random((5,3))
# print(n)

# a = np.arange(15)
# np.set_printoptions(threshold=1)
# print(a)

# from numpy import genfromtxt
# my=genfromtxt(r'C:\Users\Durgesh\Downloads\iris.csv',delimiter=',',dtype='float',usecols=[0])
# # names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
# print(np.mean(my),np.median(my),np.std(my))

# from numpy import genfromtxt
# my=genfromtxt(r'C:\Users\Durgesh\Downloads\iris.csv',delimiter=',',dtype='float',usecols=[0])
# print(np.where((my >= 0.0) & (my <= 1.0)))


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# dataset = pd.read_csv(r'C:\Users\Durgesh\Desktop\P14-Part1-Data-Preprocessing\Section 3 - Data Preprocessing in Python\Python\Data.csv')
# da = dataset.iloc[:,:-1].values
# print(da)
# ta = dataset.iloc[:,3].values
# from sklearn.preprocessing import Imputer
# imputer = Imputer(missing_values="NaN",strategy="mean",axis=0)
# imputer = imputer.fit(da[:,1:3])
# da[:,1:3] = imputer.transform(da[:,1:3])
# print(da)
#
# from sklearn.preprocessing import LabelEncoder,OneHotEncoder
# labelencoder = LabelEncoder()
# da[:,0] = labelencoder.fit_transform(da[:,0])
# print(da)

def ultimate_answer(a):
    result=np.zeros_like(a)
    result.flat=42
    return result

ufunc=np.frompyfunc(ultimate_answer,1,1)
print('the answer',ufunc(np.arange(4)))