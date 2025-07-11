# Databricks notebook source
# MAGIC %md
# MAGIC #### Exploratory Data Analysis: Understanding everything about data
# MAGIC
# MAGIC - Data Sanity Check: Everything is as it should be
# MAGIC - Univariate Analysis: Looking at individual columns and trying to understand properties of individual columns
# MAGIC - Bivariate Analysis: Look at relationship between different variables (eg: Price and size of company)
# MAGIC - Missing value treatment
# MAGIC - Outlier detection and treatment:
# MAGIC   - Outliers like SizeofHouse is not really a outlier as someone could have a very big house
# MAGIC   - Outliers like SquareFeetHouse could be a outlier as the km2 would be limited

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Importing necessary libraries

# COMMAND ----------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# To restrict the float value to 3 decimal places
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# COMMAND ----------

# let colab access my google drive
#from google.colab import drive
#drive.mount('/content/drive')

# COMMAND ----------

import os
file_path = os.path.abspath('Storage/Melbourne_Housing.csv')
data = pd.read_csv(file_path, on_bad_lines='skip')

# First 5 rows
data.head()

# Last 5 rows 
data.tail()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Sanity Check

# COMMAND ----------

#Understanding the shape of your data
print("There are", data.shape[0], 'rows and', data.shape[1], 'columns')

# COMMAND ----------

# Check data types of columns for the dataset
data.info()

# COMMAND ----------

# Date column is being read as object type column but it should be in date-time format
# BuildingArea is read as object type column but must be numerical column

data['Date'] = pd.to_datetime(data['Date'])
data['BuildingArea'].unique()

# COMMAND ----------

# Checking the counts of different data types in Building Area column
data['BuildingArea'].apply(type).value_counts()

# COMMAND ----------

# Replacing values with nan
data['BuildingArea'] = data['BuildingArea'].replace(['missing','inf'],np.nan)

# Changing data type to float
data['BuildingArea'] = data['BuildingArea'].astype(float)

# Building Area converted to float
data.info()

# COMMAND ----------

# alternative to load data
file_path = os.path.abspath('Storage/Melbourne_Housing.csv')
data = pd.read_csv(file_path, na_values=['missing','inf'])
data['BuildingArea'].dtype

# COMMAND ----------

# Checking missing values
data.isnull().sum()

# COMMAND ----------

# Check duplicates
data.duplicated().sum()

# COMMAND ----------

# Dropping duplicate entries from data
data.drop_duplicates(inplace=True)

# resetting index of data frame after dropping duplicates
data.reset_index(drop=True,inplace=True)

# COMMAND ----------

# Check statistical summary of data
data.describe().T

# COMMAND ----------

# Check total number of unique values in postcode column
data['Postcode'].nunique()

# COMMAND ----------

# Unique categorical levels in each column
cat_cols = ['Suburb', 'Type','SellerG', 'Regionname']

for column in cat_cols:
    print(data[column].value_counts())
    print('-'*50)

# COMMAND ----------

# Printing percentages of Unique categorical levels in each column
cat_cols = ['Suburb', 'Type','SellerG', 'Regionname']

for column in cat_cols:
    print(data[column].value_counts(normalize=True))
    print('-'*50)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Univariate Analysis 

# COMMAND ----------

import os
file_path = os.path.abspath('Storage/Automobile.csv')
data = pd.read_csv(file_path, on_bad_lines='skip')

# First 5 rows
data.head()

# COMMAND ----------

# Histrograms
sns.histplot(data=data, x='price')

# Q: What fundamenetal aspect of data does a histogram primarily represent
# A. Central Tendancy

# COMMAND ----------

# Customize Historgram
plt.title('Histogram:Price')
plt.xlim(3000,30000)
plt.ylim(0,70)
plt.xlabel('Price of cars')
plt.ylabel('Frequency')
sns.histplot(data=data, x='price', color='orange')

# COMMAND ----------

sns.histplot(data=data, x='price', bins = 20)

# COMMAND ----------

sns.histplot(data=data, x='price', binwidth = 200)

# COMMAND ----------

# MAGIC %md
# MAGIC %md
# MAGIC **How to find the optimal number of bins: Rule of thumb**
# MAGIC
# MAGIC - We calculate the bin-width first, using the following formula: $$ binwidth =\frac{(2 * IQR)}{\sqrt[3]{n}} $$ where n = number of rows the dataset
# MAGIC
# MAGIC - Then, we obtain bins using the calculated bin-width. $$ bins =\frac{Range}{binwidth} $$

# COMMAND ----------

# KDe :Kernel Density Estimation : visualizes distribution of data over a continuous interval
# Conversational scale for KDe is: Total frequency of each bin * probability

sns.histplot(data=data, x='price', kde=True, bins = 700)

# COMMAND ----------

# Compare distribution of several groups (complicated, we cant really tell whats going on)
sns.histplot(data=data, x='price', hue='body_style', kde=True)

# COMMAND ----------

# 
g = sns.FacetGrid(data, col='body_style')
g.map(sns.histplot, 'price')

# COMMAND ----------

# MAGIC %md
# MAGIC #### Boxplot
# MAGIC - Minimum Q1 Median Q3 Maximum
# MAGIC - Whiskers
# MAGIC - IQR = Q3 - Q1
# MAGIC - Outliers
# MAGIC   - Q1 - 1/2 (IQR) -> Anything smaller than that is outlier
# MAGIC   - Q3 + 1/2 (IQR) -> Anything bigger than that is outlier
# MAGIC - Left skewed
# MAGIC   - When the median is close to right side of whisker, left side whisker is bigger tahn right
# MAGIC - Right skewed

# COMMAND ----------

sns.boxplot(data=data, x='curb_weight')

# COMMAND ----------

# data is right skewed
plt.title('Boxplot:Horsepower')
plt.xlim(30,300)
plt.xlabel('Horsepower')
sns.axes_style('whitegrid')
sns.boxplot(data=data, x='horsepower', color='green')

# COMMAND ----------

# comparing groups with boxplots
plt.figure(figsize=(8,4))
sns.boxplot(data=data, x='body_style', y = 'price')

# COMMAND ----------

# compare boxplot vs histogram
# Boxplot visually summarizes variation in large datasets but is unable to show multimodality and clusters
sns.boxplot(data=data, x='bore')

# COMMAND ----------

sns.histplot(data=data, x='bore', kde=True)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Bar Graph

# COMMAND ----------

sns.countplot(data=data, x='body_style', hue='fuel_type')

# COMMAND ----------

# avoid messy plots
plt.figure(figsize=(20,7))
sns.countplot(data=data, x='make')
plt.xticks(rotation=30) # or end with ; to avoid text data
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Line plot
# MAGIC - For each x value, you will have multiple y value
# MAGIC - How data evolve with Time 

# COMMAND ----------

flights = sns.load_dataset("flights")

sns.lineplot(data=flights, x = 'month', y='passengers')

# Bluw line is confidence interval, is a range of values that estimate that are believed to contain true value of that estimate with certain probability

# COMMAND ----------

plt.figure(figsize = (15,7))
sns.lineplot(data=flights, x='month', y='passengers', ci = False, hue='year')
plt.legend(bbox_to_anchor=[1,1]); # move legend to right of graph

# COMMAND ----------

fmri = sns.load_dataset("fmri")
sns.lineplot(data=fmri, x='timepoint', y='signal', hue='event', style='region', ci=False); 
# style is for different types of lines

# COMMAND ----------

# MAGIC %md
# MAGIC ## Univariate Analysis
# MAGIC - Individual analysis on each column
# MAGIC
# MAGIC Applications:
# MAGIC - Understanding distribution of variable
# MAGIC - Identifying outliers and anomalies
# MAGIC - Assessing variability and central tendency of data

# COMMAND ----------

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
file_path = os.path.abspath('Storage/Melbourne_Housing.csv')
data = pd.read_csv(file_path, on_bad_lines='skip')

# COMMAND ----------

sns.histplot(data=data, x='Distance', stat='density') # density will show density of data
plt.show()
sns.boxplot(data=data, x='Distance')
plt.show()

# The distribution is skewed towards right
# Many outliers in column, values above 25 kms are represented as outliers

# COMMAND ----------

sns.displot(data=data, x='Landsize', kind='kde')
plt.show()
sns.boxplot(data=data, x='Landsize')
plt.show()

# Distribution is skewed towards right
# some values in landsize of more than 60000 sq meters, very high, possibly data entry error

# COMMAND ----------

data.loc[data['Landsize']>60000]

# COMMAND ----------

# MAGIC %md
# MAGIC Observations on building area

# COMMAND ----------

# Replacing values with nan
data['BuildingArea'] = data['BuildingArea'].replace(['missing','inf'],np.nan)
# Changing data type to float
data['BuildingArea'] = data['BuildingArea'].astype(float)

sns.displot(data=data, x='BuildingArea', kind='kde')
plt.show()
sns.boxplot(data=data, x ='BuildingArea')
plt.show()

# COMMAND ----------

data['BuildingArea']

# COMMAND ----------

sns.boxplot(data=data, x='Rooms')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC - Properties with more than 7 rooms are being represented as outliers by boxplot
# MAGIC - To find such properties which have more than 7 rooms 

# COMMAND ----------

data.loc[ data['Rooms']>7 ].shape
# 23 such properties with more than 7 rooms

# COMMAND ----------

data.loc[ data['Rooms']>7, 'Type' ].value_counts()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Bivariate data analysis
# MAGIC - Two perpendicular axes of coordinates , one for x, one for y
# MAGIC - Plot each pair of values as point on 2D space

# COMMAND ----------

# Scatterplot
file_path = os.path.abspath('Storage/Automobile.csv')
data = pd.read_csv(file_path, on_bad_lines='skip')

sns.scatterplot(data=data , x = 'engine_size', y = 'horsepower', hue= 'fuel_type', style='fuel_type') # hue for color, style for marker/shape

# COMMAND ----------

# MAGIC %md
# MAGIC Correlation means association. It expresses the extent to which two variables change together at a constant rate
# MAGIC - In scatter plot, when y variable tends to increase as x variable increases, it is positively correlated
# MAGIC - When y tend to decrease as x increases, negatively correlated
# MAGIC - points scattered randomly, no correlation

# COMMAND ----------

# Positively correlated
sns.scatterplot(data=data, x='curb_weight', y = 'engine_size')

# COMMAND ----------

# No correlation
sns.scatterplot(data=data, x='bore', y = 'stroke')

# COMMAND ----------

# MAGIC %md
# MAGIC #### Pairplot
# MAGIC - shows relationship between two numerical variable for each pair of columns in dataset
# MAGIC - It creates grid of axes such that variable in data will be shared in y-axis across a single row and x-axis across single column
# MAGIC   - Scatterplot for numerical variables, histograms for individual variables

# COMMAND ----------

sns.pairplot(data = data[['normalized_losses', 'wheel_base', 'curb_weight', 'engine_size', 'price', 'peak_rpm']] )

# COMMAND ----------

sns.pairplot(data = data, vars= ['wheel_base', 'curb_weight', 'engine_size', 'price'], hue='number_of_doors', corner=True ); # corner shows diagonal

# COMMAND ----------

# MAGIC %md
# MAGIC ## Heatmap
# MAGIC - Graph of correlation

# COMMAND ----------

sns.heatmap(data = data[[ 'wheel_base', 'curb_weight', 'engine_size', 'price']].corr()); 
# black represent highly correlated

# COMMAND ----------

sns.heatmap(data = data[[ 'wheel_base', 'curb_weight', 'engine_size', 'price']].corr(), annot=True, cbar=False, cmap='YlGnBu'); 
# annot : To show numbers on each box
# cbar: To remove color bar
# cmap: To set the color

# COMMAND ----------

# MAGIC %md
# MAGIC ## Bivariate Analysis

# COMMAND ----------

plt.figure(figsize=(10,5))
sns.heatmap(data.corr(), annot=True, cmap='Spectral', vmin=-1, vmax=1)
plt.show();

# COMMAND ----------

# create a column
data['Total Space'] = data['Rooms'] + data['Bedroom'] + data['Bathroom'] + data['Car']
data.head()

# COMMAND ----------

plt.figure(figsize=(10,5))
sns.scatterplot(data=data, x='Total Space', y='Price')
plt.show()

# COMMAND ----------

# we can see increasing trend of selling price with total space. Visualize with lmplot
sns.lmplot(data=data, x='Total Space', y='Price', height=5, aspect=2)
plt.xlim(0,55)
plt.show()

# COMMAND ----------

# check correlation between Total space and Price
data[['Total Space', 'Price']].corr()

# COMMAND ----------


plt.figure(figsize=(15,7))
sns.scatterplot(data=data, x='Distance', y='Price')
plt.show()

# COMMAND ----------

# average out scatter plot
plt.figure(figsize=(15,7))
sns.lineplot(data=data, x='Distance', y='Price', ci=None)
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC #### pd.cut()
# MAGIC Creating bins for distance columns
# MAGIC - 0 -15 kms - The property will be said to be in Nearby location
# MAGIC - 15 -30 kms - The property will be said to be in Moderately Close location
# MAGIC - 30 -50 kms - The property will be said to be in Far location
# MAGIC
# MAGIC ```
# MAGIC Syntax: pd.cut( x, bins, labels= None, right=False )
# MAGIC
# MAGIC Right -> excludes rightmost edge of interval if set to false
# MAGIC ```

# COMMAND ----------

data['Distance bins'] = pd.cut( data['Distance'], bins=[1,15,30,50], labels=['Nearby', 'Moderately Close', 'Far'], right=False)

# COMMAND ----------

# showfliers will disable the outlier from display
sns.boxplot(data=data, x='Distance bins', y='Price', showfliers=False)

# COMMAND ----------

data['Date'] = pd.to_datetime(data['Date'])

year_at_sale = data['Date'].dt.year
year_at_sale

# COMMAND ----------

data['AgeofProp'] = year_at_sale - data['YearBuilt']
data.head()

# COMMAND ----------

data[data['AgeofProp'] < 0]

# COMMAND ----------

plt.figure(figsize=(15,7))
sns.lineplot(data=data, x='AgeofProp', y='Price', ci=None)
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC - We observe increasing trend indicating properties which are older (vintage properties) have higher selling prices
# MAGIC - Customers who wish to live in vintage properties might have to spend more

# COMMAND ----------

# MAGIC %md
# MAGIC **Relplot()**
# MAGIC - Visualizes any relationship between quantitative variables
# MAGIC - Lets you create mutiple plots in single axis
# MAGIC
# MAGIC plots both line and scatter plots

# COMMAND ----------

import warnings
warnings.filterwarnings('ignore')

sns.relplot(data = data, x='AgeofProp', y='Price', col='Regionname', kind='line', ci=None, col_wrap=4)
plt.show();

# COMMAND ----------

# dispersion of price in every region
sns.catplot(x='Price',
            col='Regionname',
            data=data,
            col_wrap=4,
            kind='violin'
            )
plt.show()