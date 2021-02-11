import pandas as pd
import numpy as np

df=pd.read_csv(r'C:\Users\Durgesh\Downloads\pandas-master\pandas-master\pokemon_data.csv')
x=[df.iloc[:,5]]
x=np.reshape(x,(1,-1))

y=[df.iloc[:,6]]
y=np.reshape(y,(1,-1))

from sklearn.model_selection import train_test_split
x_train,x,test,y_train,y_test = train_test_split(x,y,test_size=0.3)