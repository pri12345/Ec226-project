#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.tsa.stattools as ts
import numpy as np
import openpyxl



# In[2]:


oil_excel = pd.read_excel("Ignore/WTI.xlsx", sheet_name='Monthly', engine="openpyxl")  # Specify engine for .xlsx files
oil_excel
print(plt)

plt.figure(figsize= (15,6))
plt.plot(oil_excel['observation_date'], oil_excel['WTISPLC'])
oil_excel


# In[3]:


oil_excel[oil_excel['observation_date'] == '1969-01-01']


# In[4]:


oil_from_1969 = oil_excel.iloc[276:]
oil_from_1969

plt.figure()
plt.plot(oil_from_1969['observation_date'], oil_from_1969['WTISPLC'], color = 'green')
plt.title('WTI crude oil prices from 1969 (us$ / bbl)\n Not seasonally adjusted, source: Fed St.Louis')
plt.ylabel('$ per barrel')
plt.xlabel ('year')
plt.legend()
plt.show()


# In[5]:


alldata_excel = pd.read_excel("Ignore/Alldata.xlsx", engine="openpyxl")  # Specify engine for .xlsx files
alldata_workingdata = alldata_excel.iloc[264:]
cpi = alldata_workingdata[['observation_date', 'CPI']]
cpi
plt.figure()
plt.plot(cpi['observation_date'], cpi['CPI'], color = 'purple')
plt.title('CPI seasonally adjusted, monthly. Source: Fed St.Louis')


# In[6]:


air_fares = alldata_workingdata[['observation_date', 'Air Fares']]
air_fares
plt.figure()
plt.plot(air_fares['observation_date'], air_fares['Air Fares'], color = 'silver')
plt.title('Air fares CPI city average (index), not seasonally adjusted \n source: Fed St.Louis')
plt.xlabel ('year')
plt.ylabel('index value')


# In[7]:


plt.figure()
plt.plot(air_fares['observation_date'], air_fares['Air Fares']/air_fares['Air Fares'].iloc[0] * 100, color = 'silver', label = 'Air Fares')
plt.plot(air_fares['observation_date'], oil_from_1969['WTISPLC']/oil_from_1969['WTISPLC'].iloc[0]* 100, color = 'green', label = 'WTI Crude Oil')
plt.plot(air_fares['observation_date'], cpi['CPI']/cpi['CPI'].iloc[0]* 100, color = 'purple', label = 'CPI')
plt.title('Raw data, relative change \n (All variables starting from 100)')
plt.xlabel ('year')
plt.ylabel('relative change')
plt.legend()


# In[8]:


plt.figure()
plt.plot(air_fares['observation_date'], air_fares['Air Fares']/air_fares['Air Fares'].iloc[0] * 100, color = 'silver', label = 'Air Fares')
plt.plot(air_fares['observation_date'], oil_from_1969['WTISPLC']/oil_from_1969['WTISPLC'].iloc[0]* 100, color = 'green', label = 'WTI Crude Oil')

plt.title('Oil vs Air Fares Raw data, relative change \n (All variables starting from 100)')
plt.xlabel ('year')
plt.ylabel('relative change')
plt.legend()


# In[9]:


real_fares = alldata_workingdata[['observation_date', 'real_AirFares']]
real_fares
plt.figure()
plt.plot(air_fares['observation_date'], alldata_workingdata['real_AirFares'], color = 'blue')
plt.title('REAL air fares (CPI adjusted), not seasonally adjusted')
plt.xlabel ('year')
plt.ylabel('index value (CPI adjusted)')
plt.show()

plt.figure()
plt.plot(air_fares['observation_date'], alldata_workingdata['real_AirFares'], color = 'blue', label = 'Real')
plt.plot(air_fares['observation_date'], air_fares['Air Fares'], color = 'silver', label = 'Nominal')
plt.title('REAL air fares vs nominal air fares')
plt.xlabel ('year')
plt.ylabel('index value')
plt.legend()

plt.show()


# In[10]:


alldata_workingdata


# In[11]:


real_oil = alldata_workingdata[['observation_date', 'real_WTI']]

plt.figure()
plt.plot(air_fares['observation_date'], alldata_workingdata['real_WTI'], color = 'orange')
plt.title('REAL WTI crude (us$/bbl), not seasonally adjusted')
plt.xlabel ('year')
plt.ylabel('us$/bbl')
plt.show()

plt.figure()
plt.plot(air_fares['observation_date'], oil_from_1969['WTISPLC'], color = 'green', label = 'Nominal')
plt.plot(air_fares['observation_date'], alldata_workingdata['real_WTI'], color = 'orange', label = 'Real')
plt.title('Real vs nominal WTI crude oil (us$/bbl)')
plt.xlabel ('year')
plt.ylabel('us$/bbl')
plt.legend()

plt.show()


# In[12]:


plt.figure()
plt.plot(air_fares['observation_date'], alldata_workingdata['real_WTI']/alldata_workingdata['real_WTI'].iloc[0]* 100, color = 'orange', label = 'Real WTI crude oil')
plt.plot(air_fares['observation_date'], alldata_workingdata['real_AirFares']/alldata_workingdata['real_AirFares'].iloc[0]* 100, color = 'blue', label = 'Real airfares')

plt.title('Oil vs Air Fares CPI Adjusted relative change \n (All variables starting from 100) --> real relative change')
plt.xlabel ('year')
plt.ylabel('relative change')
plt.legend()


# In[13]:


results = ts.coint(alldata_workingdata['real_WTI']/alldata_workingdata['real_WTI'].iloc[0]* 100, alldata_workingdata['real_AirFares']/alldata_workingdata['real_AirFares'].iloc[0]* 100)
results


# In[14]:


spread_relative_changes = alldata_workingdata['real_WTI']/alldata_workingdata['real_WTI'].iloc[0]* 100 - alldata_workingdata['real_AirFares']/alldata_workingdata['real_AirFares'].iloc[0]* 100

spread_relative_changes.index = alldata_workingdata['observation_date']

#plt.plot(spread_relative_changes)


# In[15]:


spread_relative_changes


# In[24]:


log_oil_price = np.log(alldata_workingdata['WTI'])
log_WTI_returns = log_oil_price.diff().dropna()
log_WTI_returns.index = alldata_workingdata['observation_date'].iloc[1:]

plt.figure()
plt.plot(log_WTI_returns)
plt.ylabel('log returns')
plt.title('log returns of WTI (nominal)')
plt.show()



# In[25]:


log_real_oil_price = np.log(alldata_workingdata['real_WTI'])
log_real_oil_returns = log_real_oil_price.diff().dropna()
log_real_oil_returns.index = alldata_workingdata['observation_date'].iloc[1:]

plt.figure()
plt.plot(log_real_oil_returns, color = 'purple')
plt.ylabel('log returns')
plt.title('log returns of REAL WTI')
plt.show()

log_real_airfares_price = np.log(alldata_workingdata['real_AirFares'])
log_real_airfares_returns = log_real_airfares_price.diff().dropna()
log_real_airfares_returns.index = alldata_workingdata['observation_date'].iloc[1:]

plt.figure()
plt.plot(log_real_airfares_returns, color = 'gold')
plt.ylabel('log returns')
plt.title('log returns of REAL Airfares')
plt.show()



# In[ ]:


adf_realairfares = ts.adfuller(log_real_airfares_returns)


print(adf_realairfares[0:2])
# %%


# %%
alldata_workingdata = alldata_workingdata.copy()
alldata_workingdata.reset_index()
GDP_excel = pd.read_excel("Ignore/GDP.xlsx", sheet_name='Quarterly', engine="openpyxl")  # Specify engine for .xlsx files
quarter_GDP = GDP_excel['GDP'].iloc[88:]
quarter_GDP.index = GDP_excel['observation_date'].iloc[88:]
monthly_GDP = quarter_GDP.resample('MS').ffill()
cleangdp = monthly_GDP.reset_index()
new_row_1 = pd.DataFrame({'observation_date': ['2024-11-01'], 'GDP': [29719.647]})  # Replace with actual column names and values
new_row_2 = pd.DataFrame({'observation_date': ['2024-12-01'], 'GDP': [29719.647]})  # Replace with actual column names and values
completegdp = pd.concat([cleangdp, new_row_1, new_row_2], ignore_index=True)
alldata_workingdata['GDP'] = completegdp['GDP']
alldata_workingdata.dropna()












# %%

plt.figure()
plt.plot(alldata_workingdata['observation_date'], alldata_workingdata['GDP'], color = 'red')
plt.plot(alldata_workingdata['observation_date'], alldata_workingdata['real_AirFares'], color = 'orange')


# %%


log_gdp = np.log(alldata_workingdata['GDP'])
# %%
log_gdp_returns = log_gdp.diff().dropna()
# %%
log_gdp_returns.head(50)
# %%

plt.figure()
plt.plot(log_real_airfares_price/log_real_airfares_price.iloc[0])
plt.plot(log_real_oil_price/log_real_oil_price.iloc[0])
# %%
log_real_airfares_price
# %%
plt.scatter(real_fares, real_oil)
# %%
