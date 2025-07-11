# Databricks notebook source
# MAGIC %md
# MAGIC ## Data Preprocessing
# MAGIC
# MAGIC ##### Missing value treatment
# MAGIC - Imputation 
# MAGIC   - Replacing with mean: outliers impact erroneous imputations
# MAGIC   - Replacing with median: appropriate for outliers
# MAGIC   - Replacing with mode: Preferred with categorical data
# MAGIC - Drop the column: Loss of information
# MAGIC
# MAGIC ```
# MAGIC Limitations of imputing missing values with central tendencies
# MAGIC - When we impute missing values with central tendencies the original distribution of feature can get distorted
# MAGIC - After imputation with central value the variance and standard deviation of feature can get drastically impacted
# MAGIC - The impact of distortion is higher with higher percentage of missing value
# MAGIC So, before directly imputing missing values with central values of column, we should investigate the missing data closely to observe the pattern of missing values and then take a decision to impute missing value with appropriate measure
# MAGIC ```

# COMMAND ----------

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = os.path.abspath('Storage/Melbourne_Housing.csv')
data = pd.read_csv(file_path, on_bad_lines='skip')

# COMMAND ----------

pd.DataFrame(
    {
        'Count':data.isnull().sum()[data.isnull().sum()>0],
        'Percentage':( data.isnull().sum()[data.isnull().sum()>0]/data.shape[0] ) * 100
    }
)

# COMMAND ----------

# extracting all information of other variables where distance is null
data.loc[ data['Distance'].isnull()==True ]

# COMMAND ----------

# MAGIC %md
# MAGIC It has everything missing

# COMMAND ----------

data.loc[ data['Suburb'] == 'Fawkner Lot' ]

# COMMAND ----------

# MAGIC %md
# MAGIC It is only one value for Fawkner lot, removing one value would not make difference, as it has everthing missing

# COMMAND ----------

data = data.drop(9594).reset_index(drop=True)

# COMMAND ----------

pd.DataFrame(
    {
        'Count':data.isnull().sum()[data.isnull().sum()>0],
        'Percentage':( data.isnull().sum()[data.isnull().sum()>0]/data.shape[0] ) * 100
    }
)

# COMMAND ----------

# Extracting all information of other variables where Bedroom is null
data.loc[ data['Bedroom'].isnull()==True ]

# COMMAND ----------

data.loc[data['Bedroom'].isnull()==True, 'Bathroom'].value_counts(dropna=False)

# COMMAND ----------

data.loc[data['Bedroom'].isnull()==True, 'Car'].value_counts(dropna=False)

# COMMAND ----------

data.loc[data['Bedroom'].isnull()==True, 'Landsize'].value_counts(dropna=False)

# COMMAND ----------

data.loc[data['Bedroom'].isnull()==True, 'BuildingArea'].value_counts(dropna=False)

# COMMAND ----------

data.loc[data['Bedroom'].isnull()==True, 'YearBuilt'].value_counts(dropna=False)

# COMMAND ----------

# MAGIC %md
# MAGIC There seems to be strong pattern in missing values. When Bedroom column has missing data, other columns like Bathroom, car, Landsize, BuildingArea, YearBuilt also have missing value
# MAGIC

# COMMAND ----------

# Check if missing data has some pattern in suburbs and regions od properties
data.loc[data['Bedroom'].isnull()==True, 'Suburb'].value_counts(dropna=False)

# COMMAND ----------

data['Suburb'].nunique()

# COMMAND ----------

data.loc[data['Bedroom'].isnull()==True, 'Regionname'].value_counts(dropna=False)

# COMMAND ----------

# MAGIC %md
# MAGIC No notable pattern in Suburb and Region

# COMMAND ----------

# MAGIC %md
# MAGIC #### Missing Value treatment - Part 2
# MAGIC
# MAGIC - Missing value treatment for Bedroom, Bathroom, and Car column
# MAGIC   - Group the data on basis of Categorical variable - Region, Type of property. This will get better idea of average number of bedrooms, bathrooms, and car parking spaces
# MAGIC   - It is more likely that property of certain type in given region would have similar number of bedrooms, bathrooms, and car parking spaces

# COMMAND ----------

data.groupby(['Regionname', 'Type'])[['Bedroom', 'Bathroom', 'Car']].mean()

# COMMAND ----------

# MAGIC %md
# MAGIC #### fillna()
# MAGIC - Transform method of pandas to impute missing values
# MAGIC - Used to fill NaN values using input value
# MAGIC - Syntax: data['column'].fillna(value=x)
# MAGIC
# MAGIC #### transform()
# MAGIC - Tranform function works on each value of DataFrame and allows to execute specified function on each value
# MAGIC - data.tranform(func=function_name)

# COMMAND ----------

data['Bedroom'] = data['Bedroom'].fillna( value = data.groupby(['Regionname', 'Type'])['Bedroom'].transform('mean') )

# COMMAND ----------

data['Bathroom'] = data['Bathroom'].fillna( value = data.groupby(['Regionname', 'Type'])['Bathroom'].transform('mean') )

# COMMAND ----------

data['Car'] = data['Car'].fillna( value = data.groupby(['Regionname', 'Type'])['Car'].transform('mean') )

# COMMAND ----------

pd.DataFrame(
    {
        'Count': data.isnull().sum()[data.isnull().sum()>0],
        'Percentage': ( data.isnull().sum()[data.isnull().sum()>0] / data.shape[0] ) * 100
    }
)

# COMMAND ----------

# bedroom, bathroom, car is of type int
data['Bathroom'] = data['Bathroom'].astype(int)
data['Bedroom'] = data['Bedroom'].astype(int)
data['Car'] = data['Car'].astype(int)

# COMMAND ----------

data['Total Space'] = data['Rooms'] + data['Bedroom'] + data['Bathroom'] + data['Car']
data['Total Space'] = data['Total Space'].astype(int)

# COMMAND ----------

sns.scatterplot(data=data, x='Total Space', y='Price')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC We see that relationship between total space and price has not changed. and positive correlation between these variables is still maintained which is good thing

# COMMAND ----------

sns.displot(data=data, x='Landsize', kind='kde')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC - As landsize is highly skewed, using average value for imputation might not be correct method as mean gets impacted by outliers
# MAGIC - So, we will use median value to impute missing values of this column as median is not affected by outliers

# COMMAND ----------

data.groupby(['Regionname', 'Type'])[['Landsize']].median()

# COMMAND ----------

data['Landsize'] = data['Landsize'].fillna( value = data.groupby(['Regionname', 'Type'])['Landsize'].transform('median'))

# COMMAND ----------

pd.DataFrame(
    {
        'Count': data.isnull().sum()[data.isnull().sum()>0],
        'Percentage': ( data.isnull().sum()[data.isnull().sum()>0] / data.shape[0] ) * 100
    }
)

# COMMAND ----------

# MAGIC %md
# MAGIC Missing value treatment of BuildingArea and Yearbuilt
# MAGIC - We will not do imputation for these columns as it has more than 50% missing data. 

# COMMAND ----------

data = data.drop(['BuildingArea', 'YearBuilt'], axis=1)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Outliers detection and Treatment

# COMMAND ----------

