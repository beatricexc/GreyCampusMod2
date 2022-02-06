
#Simple Liner Regression

#Y = ax + b (y- dep variable, x- indep variable, a - coeffcicient/slope of the line, b- constant)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the datset
dataset = pd.read_csv("Salary_Data.csv")
X = dataset.iloc[:, :-1].values #independent variable
y = dataset.iloc[:, 1].values #dependent variable (salary)


# task1
# Splitting the datset into the Training set and the test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 1/3, random_state= 0)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#ytest is the real salaries, ypred is predicted salaries

# Predicting the Test set results
y_pred = regressor.predict(X_test)

#testing
from sklearn.metrics import mean_squared_error
RMSE = mean_squared_error(y_test, y_pred) 
#root mean squared error
#RMSE is a comparative value
RMSE 
np.sqrt(21026037)


#Visualising the Training set results
#here the red points are actual data points
#blue line-regr line is predicted values
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
         
#Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')

#Not to replace X_train with X_test as our model is trained on X_train
plt.plot(X_train, regressor.predict(X_train), color ='blue')
plt.title('Salary Vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
