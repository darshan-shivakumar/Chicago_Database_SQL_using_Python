#!/usr/bin/env python
# coding: utf-8

# ### Connect to the database
# 
# 
# 

# In[1]:


get_ipython().system('pip install sqlalchemy==1.3.9')
get_ipython().system('pip install ibm_db_sa')


# In[2]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[3]:


# Remember the connection string is of the format:
# %sql ibm_db_sa://my-username:my-password@my-hostname:my-port/my-db-name?security=SSL
# Enter the connection string for your Db2 on Cloud database instance below
get_ipython().run_line_magic('sql', 'ibm_db_sa://ktl54482:xxxxxxxxxx@dashdb-txn-sbox-yp-dal09-14.services.dal.bluemix.net:50000/BLUDB?security="SSL"')


# 
# ### Problem 1
# 
# ##### Find the total number of crimes recorded in the CRIME table.
# 

# In[20]:


get_ipython().run_line_magic('sql', 'select count(*) from CHICAGO_CRIME_DATA')


# ### Problem 2
# 
# ##### List community areas with per capita income less than 11000.
# 

# In[21]:


get_ipython().run_line_magic('sql', 'select COMMUNITY_AREA_NAME, PER_CAPITA_INCOME from CENSUS_DATA where PER_CAPITA_INCOME < 11000')


# ### Problem 3
# 
# ##### List all case numbers for crimes  involving minors?(children are not considered minors for the purposes of crime analysis)
# 

# In[30]:


get_ipython().run_line_magic('sql', 'select CASE_NUMBER from CHICAGO_CRIME_DATA where year(DATE)< 2003')


# ### Problem 4
# 
# ##### List all kidnapping crimes involving a child?
# 

# In[32]:


get_ipython().run_line_magic('sql', "select PRIMARY_TYPE from CHICAGO_CRIME_DATA where PRIMARY_TYPE ='KIDNAPPING'")


# ### Problem 5
# 
# ##### What kinds of crimes were recorded at schools?
# 

# In[39]:


get_ipython().run_line_magic('sql', "select PRIMARY_TYPE,LOCATION_DESCRIPTION from CHICAGO_CRIME_DATA where LOCATION_DESCRIPTION LIKE'SCHOOL%'")


# ### Problem 6
# 
# ##### List the average safety score for all types of schools.
# 

# In[40]:


get_ipython().run_line_magic('sql', 'select AVG(SAFETY_SCORE) as average_safety_score from CHICAGO_PUBLIC_SCHOOLS')


# ### Problem 7
# 
# ##### List 5 community areas with highest % of households below poverty line
# 

# In[41]:


get_ipython().run_line_magic('sql', 'select COMMUNITY_AREA_NAME from CENSUS_DATA order by PERCENT_HOUSEHOLDS_BELOW_POVERTY desc limit 5')


# ### Problem 8
# 
# ##### Which community area is most crime prone?
# 

# In[42]:


get_ipython().run_cell_magic('sql', 'select D.COMMUNITY_AREA_NAME from CENSUS_DATA D,CHICAGO_CRIME_DATA S where D.COMMUNITY_AREA_NUMBER=S.COMMUNITY_AREA_NUMBER', 'order by S.COMMUNITY_AREA_NUMBER desc limit 1')


# ### Problem 9
# 
# ##### Use a sub-query to find the name of the community area with highest hardship index
# 

# In[43]:


get_ipython().run_line_magic('sql', 'select COMMUNITY_AREA_NAME from CENSUS_DATA where HARDSHIP_INDEX= (select MAX(HARDSHIP_INDEX) from CENSUS_DATA )')


# ### Problem 10
# 
# ##### Use a sub-query to determine the Community Area Name with most number of crimes?
# 

# In[8]:


get_ipython().run_cell_magic('sql', 'select D.COMMUNITY_AREA_NAME,(select MAX(COMMUNITY_AREA_NUMBER) as most_prone_to_crime_city from CHICAGO_CRIME_DATA ) ', 'from CENSUS_DATA D,CHICAGO_CRIME_DATA S \nwhere D.COMMUNITY_AREA_NUMBER=S.COMMUNITY_AREA_NUMBER limit 1')

