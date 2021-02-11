import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv(r'C:\Users\Durgesh\Desktop\P14-Part1-Data-Preprocessing\Section 3 - Data Preprocessing in Python\Python\50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
label = LabelEncoder()
X[:,3] = label.fit_transform(X[:,3])
one = OneHotEncoder(categorical_features= [3])
X = one.fit_transform(X).toarray()

x = X[:,1:]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)

# import statsmodels.api as sm
# x = np.append(arr = np.ones((50,1)).astype(int), values= x , axis = 1)
# x_opt = x[:,[0,3]]
# regressor_opt = sm.OLS(y,x_opt).fit()
# print(regressor_opt.summary())

from sklearn.metrics import r2_score
score = r2_score(x_train,y_train)
print(score)