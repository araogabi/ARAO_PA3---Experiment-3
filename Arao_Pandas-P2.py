#!/usr/bin/env python
# coding: utf-8

# ### EXPERIMENT 3: PYTHON DATA ANALYSIS (PANDAS)

# ##### ---------------------------------------------------------------------------------------------------------------------------
# 
# ##### Name: ARAO, Angeline Jeannah E.
# ##### Year & Section: 2ECE-A
# 
# ##### ---------------------------------------------------------------------------------------------------------------------------

# #### PROBLEM 2

# In[9]:


# Access the Pandas library

import pandas as pd


# ##### A. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.

# In[27]:


# Selects columns at positions 0, 2, 4, 6, 8, and 10 from the cars DataFrame and displays the first 5 rows of these columns.

cars.iloc[:,[0,2,4,6,8,10]].head(5)


# ##### B. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

# In[30]:


# .loc syntax searches for the 'Model' column where the value is 'Mazda RX4'. Once found, it displays all the data corresponding to that row.

cars.loc[(cars['Model']=='Mazda RX4')]


# ##### C. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

# In[33]:


# After the comma in the second part, it only displays the specified columns, 'cyl' and 'gear', as instructed

cars.loc[(cars['Model']=='Camaro Z28'), ['cyl'] ]


# ##### D. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# In[36]:


# .loc uses multiple OR conditions to filter specific car models, displaying their corresponding cylinder and gear values

cars.loc[(cars['Model']=='Mazda RX4 Wag') | (cars['Model']== 'Ford Pantera L') | (cars['Model'] == 'Honda Civic'), ['cyl', 'gear']]

