# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 10:15:52 2021

@author: Deepak R
"""
  
#importing the libraries
import pandas as pd
import matplotlib.pyplot as plt








#Reading the data from files
data = pd.read_csv("advertising.csv")
print(data.head())
   



#TO visuaise data
fig , axs = plt.subplots(1,3,sharey = True)
data.plot(kind='scatter',x='TV',y='Sales',ax=axs[0],figsize=(16,8))
data.plot(kind='scatter',x='Radio',y='Sales',ax=axs[1])
data.plot(kind='scatter',x='Newspaper',y='Sales',ax=axs[2])




#Creating x&y for linear regression
feature_cols = ['TV']
X = data[feature_cols]
Y = data.Sales


#Importing linear regression

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,Y)

print(lr.intercept_)
print(lr.coef_)


result = 6.974+0.0554*33

print(result) 


#create a dataframe with min and max of the table


X_new = pd.DataFrame({'TV':[data.TV.min(),data.TV.max()]})

X_new.head()


preds = lr.predict(X_new)


print(preds)

data.plot(kind = 'scatter', x='TV',y='Sales')


plt.plot(X_new,preds,c='red',linewidth=4)

import statsmodels.formula.api as smf

lm = smf.ols(formula = 'Sales ~ TV',data = data).fit()
lm.conf_int()




#finding the probability valuse


lm.pvalues

#finding r-square values

lm.rsquared


#mulit line regression


feature_cols = ['TV','Radio','Newspaper']
X = data[feature_cols]
Y = data.Sales

lr = LinearRegression()
lr.fit(X,Y)


print(lr.intercept_)
print(lr.coef_)


#lm = snf.ols(formula='Sales ~ TV+Radio+Newspaper',data=data).fit()
#lm.conf_int()
#m.summary()


lm = smf.ols(formula='Sales ~ TV + Radio + Newspaper', data=data).fit()
lm.conf_int()
lm.summary()
