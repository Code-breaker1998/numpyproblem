import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r'C:\Users\Durgesh\Desktop\P14-Part1-Data-Preprocessing\Section 3 - Data Preprocessing in Python\Python\Salary_Data.csv')
da = dataset.iloc[:,:1].values
ta = dataset.iloc[:,1].values

from sklearn.model_selection import train_test_split
da_train,da_test,ta_train,ta_test = train_test_split(da,ta,test_size=1/3,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(da_train,ta_train)

y_pred=regressor.predict([[4]])
print(y_pred)

plt.scatter(da_train,ta_train,color='red')
plt.plot(da_train,regressor.predict(da_train),color='blue')
plt.title('Salary Vs Experience ')
plt.xlabel('Year Of Experience')
plt.ylabel('Salary')
plt.show()

