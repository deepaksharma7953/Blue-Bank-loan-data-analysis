# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 17:46:15 2023
"""
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
with open('loan_data_json.json') as jf:
    df=json.load(jf)
    print(df)
  
lndf=pd.DataFrame(df)
lndf['purpose'].unique()
lndf.describe()
lndf['int.rate'].describe()
lndf['fico'].describe()
lndf['dti'].describe()
income=np.exp(lndf['log.annual.inc'])
lndf['annualincome']=income
length=len(lndf)
ficocat=[]
for x in range(0,length):
    category=lndf['fico'][x]
    
    try:
        if category >= 300 and category < 400: 
            cat='Very Poor'
        elif category >= 400 and category < 600: 
           cat='Poor'
        elif category >= 601 and category < 660: 
            cat='Fair'
        elif category >= 660 and category < 700: 
            cat='Good'
        elif category >=700: 
            cat='Excellent'
        else:
            cat='Unknown'
    except:
        cat='error-unknown'
    ficocat.append(cat)
ficocat=pd.Series(ficocat)
lndf['fico.category']=ficocat
#df.loc as conditional statement
lndf.loc[ lndf['int.rate']>0.12,'int.rate type']='high'
lndf.loc[ lndf['int.rate']<0.12,'int.rate type']='low'

#no. of loans or rows by fico category
catplot=lndf.groupby(['fico.category']).size()
pplot=lndf.groupby(['purpose']).size()
catplot.plot.bar(color='grey',width=0.1)
plt.show()
pplot.plot.bar(color='grey',width=0.2)
plt.show()

#scatterplot
xpoint=lndf['annualincome']
ypoint=lndf['dti']
plt.scatter(ypoint, xpoint,color='#4CAF50')
plt.show()
#high income less debt less dti

#writing lndf to csv
lndf.to_csv('loanddatacleaned.csv',index=True)
