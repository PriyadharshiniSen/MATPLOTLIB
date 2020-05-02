#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 19:33:39 2020

@author: priya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

#%matplotlib inline


start_date=dt.datetime(2020,3,21)
end_date=dt.datetime(2020,5,20)

date_range=pd.date_range(start_date,end_date)
covid_cases=(np.random.rand(len(date_range))*50).astype(int)
df=pd.DataFrame(covid_cases,index=date_range,columns=['Lockdown'])

lr_coef=np.polyfit(range(0,len(df)),df['Lockdown'],1)
lr_fun=np.poly1d(lr_coef)
trend=lr_fun(range(0,len(df)))
df['Trend']=trend


df.loc['Apr 2 2020':'May 2 2020'].plot()

plt.xlabel('Lockdown Date')
plt.ylabel('covid_cases ')
plt.title('covid Plot')
plt.legend('Covid','Trend')
plt.show()
