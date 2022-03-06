#!/usr/bin/env python
# coding: utf-8

# In[175]:


get_ipython().system('pip install selenium')


# In[176]:


url= 'https://www.serialupdates.me/shark-tank-india-investors-names-sony-tv-new-show-entrepreneurs-list/'


# In[177]:


import os


# In[178]:


os.chdir('E:/Scripting')


# In[179]:


from selenium import webdriver
from bs4 import BeautifulSoup


# In[180]:


browser = webdriver.Firefox()
browser.get(url)


# In[181]:


html = browser.page_source
html


# In[182]:


soup = BeautifulSoup(html,'html.parser')
soup


# In[183]:


type(soup)


# In[184]:


soup.select('table')


# In[185]:


soup.select('table')[2]


# In[186]:


soup.select('table')[2].find_all('thead')[0].find_all('th')[0].text.strip()


# In[187]:


table2 = soup.select('table')[2]


# In[188]:


table2.find_all('th')


# In[189]:


thead = [i.text.strip() for i in table2.find_all('th')]
thead


# In[190]:


table2.find_all('tbody')[0].text


# In[191]:


soup.select('table')[2].tbody.find_all('tr')


# In[192]:


data=[]
for r in soup.select('table')[2].tbody.find_all('tr'):
    data.append([i.text.strip() for i in r.find_all('td')])


# In[193]:


data


# In[194]:


import pandas as pd
df = pd.DataFrame(data)
df.columns = thead
df


# In[195]:


def sharktank_table():
    thead = [i.text.strip() for i in table2.find_all('th')]
    data=[]
    for r in soup.select('table')[2].tbody.find_all('tr'):
        data.append([i.text.strip() for i in r.find_all('td')])
    df = pd.DataFrame(data)
    df.columns = thead
    return df


# In[196]:


sharktank_table()


# In[197]:


df.info()


# In[198]:


df.to_csv("Shark_Tank_Season1_data.csv")


# In[199]:


df.to_csv()


# In[200]:


df.head()


# In[ ]:




