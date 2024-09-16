#!/usr/bin/env python
# coding: utf-8

# ### EXPERIMENT 3: PYTHON DATA ANALYSIS (PANDAS)

# ##### ---------------------------------------------------------------------------------------------------------------------------
# 
# ##### Name: ARAO, Angeline Jeannah E.
# ##### Year & Section: 2ECE-A
# 
# ##### ---------------------------------------------------------------------------------------------------------------------------

# #### PROBLEM 1

# In[2]:


# Access the Pandas library

import pandas as pd


# ##### A. Load the corresponding .csv file into a data frame named cars using pandas

# In[5]:


# Reads the csv file into a DataFrame

cars = pd.read_csv('cars.csv')
cars


# ##### B. Display the first five and last five rows of the resulting cars.

# In[21]:


# Display the first five rows (head)

cars.head()


# In[23]:


# Display the last five rows (tail)

cars.tail()

