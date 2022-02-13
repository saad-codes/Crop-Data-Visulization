# Importing Libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import cufflinks as cf
from plotly.offline import init_notebook_mode,iplot,download_plotlyjs
cf.go_offline()
init_notebook_mode(connected=True)

#Importind Data and showing first 5 elements

df = pd.read_excel('bhawalnagar.xlsx',sheet_name=0)
df = df.fillna(df.mean())
df1  = pd.DataFrame()
df1= df[["MIN_T","MAX_T","Rainfall","fertilizer_consumption","Wheat_Yield"]]
df1.head(5) 

#MAking independent(x) and dependent(y) variables
x = df1.iloc[:30,0:4]
y = df1.iloc[:30,4]
# Independent variable that are choosen
x.head()

#importing regression library and fitting it to x, y

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=500, random_state=101)
regressor.fit(x,y)

#Checking how much Accurate predictions we have made
regressor.score(x,y)

# Making predictions
rfc_pred= regressor.predict(x)
df1['Predictions of Yield'] = rfc_pred
df1.head()
g = sns.PairGrid(df1,y_vars=['Predictions of Yield'],x_vars=["Rainfall","MIN_T","MAX_T","fertilizer_consumption"],height=4)
g.map(sns.regplot,color=".1")
g.set();