# GreyCampusMod2
Supervised Learning-Linear Regression

The process of finding out the relationship between 2 variables is called linear regression.

Residuals = actual-predicted
*actual* = data points
*predicted* = line of regression (line of best fit)
-residuals are independent 
-there is no correlation between the consecutive residuals in a time series data 

**Homoscedasticity** : The residuals have constant variance at every level of x (error distribution)
- the simples wasy to detect heteroscedasticity is by creating a fitted value vs a residual plot.

**Multivariate Normality** : assumes that residuals are normally distributed

**No Multicolliniarity** : assumes that the independent variables are not highly correlated with each other. The assumption is tested using VIF (**V**ariance **I**nflation **F**actor)

**Homoscedasticity**: states that the variance of error terms are similar across the values of the independed variables. A plot of standardized residuals vs predicted values can show whether points are equally distributed across all values of the indepdent variables. 
