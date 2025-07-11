# Databricks notebook source
# MAGIC %md
# MAGIC ## Context
# MAGIC The dataset provided is from the city of Melbourne and contains the different attributes of the properties there and the locations in which they are located. The aim is to perform a detailed analysis of this dataset and provide useful insights to facilitate the process of buying and selling real estate.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Description:
# MAGIC
# MAGIC The detailed data dictionary is given below:
# MAGIC
# MAGIC * Suburb - Suburb in which the property is located
# MAGIC * Rooms - Number of rooms in the property
# MAGIC * Type - Type of the property like 
# MAGIC     * h - house,cottage,villa, semi,terrace, 
# MAGIC     * t - townhouse,
# MAGIC     * u - unit, duplex
# MAGIC * SellerG - Name of the real estate agent who sold the property
# MAGIC * Date - Date on which the property was sold
# MAGIC * Distance - Distance of the property from CBD in kilometres. CBD is the central business district of the city.
# MAGIC * Postcode - Postcode of the area
# MAGIC * Bedroom - Number of bedrooms in the property
# MAGIC * Bathroom - Number of bathrooms in the property
# MAGIC * Car - Number of car parking spaces in the property
# MAGIC * Landsize - Size of the land in square metres
# MAGIC * BuildingArea - Size of the building in square metres (Generally, building size is smaller than land size since someone can have personal gardens and other things in the property.) 
# MAGIC * YearBuilt - Year in which the building was built
# MAGIC * Regionname - Name of the region in which the property is located like Eastern Metropolitan, Western Metropolitan, Northern Victoria etc.
# MAGIC * Propertycount - Number of properties that are present in the suburb
# MAGIC * Price - price (in AUD) at which the property was sold

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4.1 Sanity Checks

# COMMAND ----------

# MAGIC %md
# MAGIC **Importing necessary libraries**

# COMMAND ----------

# Libraries to help with reading and manipulating data
import numpy as np
import pandas as pd

# Libraries to help with data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# to restrict the float value to 3 decimal places
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# COMMAND ----------

# let colab access my google drive
from google.colab import drive
drive.mount('/content/drive')

# COMMAND ----------

# MAGIC %md
# MAGIC **Importing the dataset**

# COMMAND ----------

data = pd.read_csv('/content/drive/MyDrive/Python Course/Melbourne_Housing.csv')

# COMMAND ----------

# MAGIC %md
# MAGIC **View the first and last 5 rows of the dataset**

# COMMAND ----------

data.head()

# COMMAND ----------

data.tail()

# COMMAND ----------

# MAGIC %md
# MAGIC **Understand the shape of the dataset**

# COMMAND ----------

# checking shape of the data
print("There are", data.shape[0], 'rows and', data.shape[1], "columns.")

# COMMAND ----------

# MAGIC %md
# MAGIC **Check the data types of the columns for the dataset**

# COMMAND ----------

data.info()

# COMMAND ----------

# MAGIC %md
# MAGIC * There are 10 numerical columns in the data and 6 object type columns.
# MAGIC * Date column is being read as object type column but it should be in date-time format.
# MAGIC * BuildingArea is read as object type column but it should be a numerical column.

# COMMAND ----------

# changing the data type of Date column
data['Date'] = pd.to_datetime(data['Date'])

# COMMAND ----------

# let's see why BuildingArea column has object data type
data['BuildingArea'].unique()

# COMMAND ----------

# MAGIC %md
# MAGIC * It will be difficult to analyze each data point to find the categorical values in this column. Let's find the count of non-numeric values and see what are these values.

# COMMAND ----------

# checking the count of different data types in BuildingArea column
data['BuildingArea'].apply(type).value_counts()

# COMMAND ----------

# MAGIC %md
# MAGIC * We can see that there are mixed data type values in the column like - 'missing', 'inf' which should actually be read as missing values (NaN). Let's replace such data points with null values.
# MAGIC

# COMMAND ----------

# replacing values with nan
data['BuildingArea'] = data['BuildingArea'].replace(['missing','inf'],np.nan)

# changing the data type to float
data['BuildingArea'] = data['BuildingArea'].astype(float)

# COMMAND ----------

# let's check the data type of columns again
data.info()

# COMMAND ----------

# MAGIC %md
# MAGIC * We see that the data types of Date and BuildingArea columns have been fixed.
# MAGIC * There are 11 numerical columns, 4 object type columns, and 1 date time column in the data.
# MAGIC * We observe that some columns have less entries that other columns (less than 27114 rows) which indicates the presence of missing values in the data.

# COMMAND ----------

# MAGIC %md
# MAGIC **We could have also done this replacement of missing and inf to NaN while loading the data. Let's see how -**

# COMMAND ----------

# using na_values to tell python which values it should consider as NaN
data_new = pd.read_csv('/content/drive/MyDrive/Python Course/Melbourne_Housing.csv',na_values=['missing','inf'])

# COMMAND ----------

# MAGIC %md
# MAGIC * This method is useful when we know what kind of values to consider as anomalies in the data. 

# COMMAND ----------

data_new['BuildingArea'].dtype

# COMMAND ----------

# MAGIC %md
# MAGIC * We observe that now building area is being considered as float after the 'missing' and 'inf' were read as NaN.

# COMMAND ----------

# MAGIC %md
# MAGIC **What are missing values?**
# MAGIC
# MAGIC Missing values occur when no data value is stored for the variable in an observation. Missing data are a common occurrence and can have a significant effect on the conclusions that can be drawn from the data.

# COMMAND ----------

# MAGIC %md
# MAGIC **Checking for missing values in the data**

# COMMAND ----------

data.isnull().sum()

# COMMAND ----------

# MAGIC %md
# MAGIC * There are missing values in 8 columns of the data.
# MAGIC * We will treat these missing values after understanding the distributions of features in the data, the relationships that exist in the data. This will help us impute these values more effectively.

# COMMAND ----------

# MAGIC %md
# MAGIC **Checking for duplicate entries in the data**

# COMMAND ----------

data.duplicated().sum()

# COMMAND ----------

# MAGIC %md
# MAGIC * There are 11 duplicate entries in the data. Let's remove them.

# COMMAND ----------

# dropping duplicate entries from the data
data.drop_duplicates(inplace=True)

# resetting the index of data frame since some rows will be removed
data.reset_index(drop=True,inplace=True)

# COMMAND ----------

# MAGIC %md
# MAGIC **Let's check the statistical summary of the data.**

# COMMAND ----------

data.describe().T

# COMMAND ----------

# MAGIC %md
# MAGIC * `Rooms:` On average there are 3 rooms in a property. 75% of the properties have less than or equal to 4 rooms. There are some properties which have 16 rooms.
# MAGIC * `Distance`: On average the properties are located within 11.28 Kms of central business district, while the median is 10.5 Kms. There is a huge difference between the maximum value and the 75% percentile of the data which indicates there might be outliers present in this column.
# MAGIC * The distribution of the number of bedrooms, bathrooms, and car parking spaces is fine. The maximum values of these columns might require a quick check.
# MAGIC * `Landsize`: The Landsize column has a huge standard deviation with a mean and median land size of 560.53 and 513 metres respectively. Also, there is a huge difference between the maximum value and the 75% percentile of the data which indicates there might be outliers present in this column.
# MAGIC * `YearBuilt`: The latest property was built in 2019 while the earliest property was built in 1850.
# MAGIC * `Propertycount`: On average a suburb has around 7564 properties. The column has a large standard deviation of 4494.02 units.
# MAGIC * `Price`: On average the house prices are AUD 1050664. The median prices are AUD 871000. There is a huge difference between the maximum value and the 75% percentile of the data which indicates there might be outliers present in this column.

# COMMAND ----------

# let's check the total number of unique values in the Postcode column
data['Postcode'].nunique()

# COMMAND ----------

# MAGIC %md
# MAGIC * There are a total of 209 different postcodes in the data.

# COMMAND ----------

# MAGIC %md
# MAGIC **Let's check the count and percentage of categorical levels in each column**

# COMMAND ----------

# Making a list of all categorical variables
cat_cols =  ['Suburb', 'Type', 'SellerG', 'Regionname']

# Printing the count of unique categorical levels in each column
for column in cat_cols:
    print(data[column].value_counts())
    print("-" * 50)

# COMMAND ----------

# Printing the percentage of unique categorical levels in each column
for column in cat_cols:
    print(data[column].value_counts(normalize=True))
    print("-" * 50)

# COMMAND ----------

# MAGIC %md
# MAGIC **Observations**
# MAGIC * Highest number (724) of the properties are in Reservoir suburb followed by 493 properties in Bentleigh East suburb.
# MAGIC * Most of the properties (18394 or 67%) are of type 'h' that is houses/cottages/villas, etc followed by 5882 or 21% properties of type 'u' that is unit/duplex. The least number (2827 or 10%) is of type 't' that is townhouses.
# MAGIC * Top 5 sellers of properties are  - Nelson, Jellis, Barry, hockingstuart, and Ray.
# MAGIC * 31% of the properties are in Southern Metropolitan followed by 28% in Northern Metropolitan, and 21% in Western Metropolitan. This shows that our analysis will be biased towards Metropolitan regions than Victoria regions as around 98% of the data points are from Metropolitan region.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4.2 Univariate Analysis

# COMMAND ----------

# MAGIC %md
# MAGIC **Let's check the distribution for numerical columns.**

# COMMAND ----------

# MAGIC %md
# MAGIC **Observations on Distance**

# COMMAND ----------

sns.histplot(data=data,x='Distance',stat='density')
plt.show()
sns.boxplot(data=data,x='Distance')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * The distribution is skewed towards right.
# MAGIC * There are many outliers present in this column. 
# MAGIC * Values above 25 Kms are being represented as outliers in the boxplot, indicating there there are many properties that are atleast 25 Kms away from CBD.

# COMMAND ----------

# MAGIC %md
# MAGIC **Observations on Landsize**

# COMMAND ----------

sns.displot(data=data,x='Landsize',kind='kde')
plt.show()
sns.boxplot(data=data,x='Landsize')
plt.show()

# COMMAND ----------

# converting Landsize to sq. kilometres from sq. metres 
sns.displot(data=data,x=data['Landsize']/1000000,kind='kde')
plt.show()
sns.boxplot(data=data,x=data['Landsize']/1000000)
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * The distribution is skewed towards the right, even after conversion to Kilometres.  
# MAGIC * There are many outliers present in this column. Some properties have a landsize of more than 60000 sq meters. These value seems to be very high and can possibly be a data entry error. We should check it further.

# COMMAND ----------

data.loc[data['Landsize']>60000]

# COMMAND ----------

# MAGIC %md
# MAGIC * Just by looking at these observation it is difficult to say whether these are data entry errors or not. Although the land size does look very high.

# COMMAND ----------

# MAGIC %md
# MAGIC **Observations on BuildingArea**

# COMMAND ----------

sns.displot(data=data,x='BuildingArea',kind='kde')
plt.show()
sns.boxplot(data=data,x='BuildingArea')
plt.show()

# COMMAND ----------


sns.displot(data=data,x=data['BuildingArea'],kind='kde')
plt.show()
sns.boxplot(data=data,x=data['BuildingArea'])
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * The distribution of BuildingArea is similar to Landsize that is right skewed.
# MAGIC * It has many outliers. There are values above 4000 sq meters which seems high.

# COMMAND ----------

# MAGIC %md
# MAGIC **Observations on Price**

# COMMAND ----------

sns.histplot(data=data,x='Price')
plt.show()
sns.boxplot(data=data,x='Price')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * The distribution of the Price is skewed towards the right.
# MAGIC * There are many outliers in this variable and the values above 2000000 are being represented as outliers by the boxplot. 
# MAGIC * The values seem fine as the selling price of the properties varies and depends upon various factors. For example, distance, if the properties are closer to CBD they might have a higher selling price.

# COMMAND ----------

# MAGIC %md
# MAGIC **Observations on Rooms**
# MAGIC

# COMMAND ----------

sns.boxplot(data=data,x='Rooms')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * Properties with more than 7 rooms are being represented as outliers by the boxplot.
# MAGIC * Let's find out how many such properties are there which have more than 7 rooms and what are the types of such properties.

# COMMAND ----------

data.loc[data['Rooms']>7].shape

# COMMAND ----------

# MAGIC %md
# MAGIC * There are only 23 such properties which have more than 7 rooms.

# COMMAND ----------

# findig the type of such properties
data.loc[data['Rooms']>7,'Type'].value_counts()

# COMMAND ----------

# MAGIC %md
# MAGIC * There are no townhouses in these.
# MAGIC * Most of these properties are houses/villas,etc
# MAGIC * Only 2 of such properties are units/duplexes.
# MAGIC * This indicates that 'h' type properties are a more likely choice for customers who are looking for bigger properties.

# COMMAND ----------

# MAGIC %md
# MAGIC **Observations on Region Name**

# COMMAND ----------

sns.countplot(data=data,x='Regionname')
plt.xticks(rotation=90)
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * Eastern, Northern, and Western Victoria have very less number of properties.
# MAGIC * Southern and Northern Metropolitan have the most number of properties.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4.3 Bivariate Analysis

# COMMAND ----------

plt.figure(figsize=(10,5))
sns.heatmap(data.corr(),annot=True,cmap='Spectral',vmin=-1,vmax=1)
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC **Observations**
# MAGIC * Price column shows a high correlation with number of rooms, bedrooms, bathrooms and car parking spaces. This indicates that more the number of rooms, bedrooms, etc more will be the selling price of a property. 
# MAGIC * Price has a negative correlation with Distance column. This indicates as the distance increases the selling price of a property will decrease.
# MAGIC * Price has a negative correlation with YearBuilt column. This indicates that vintage properties have higher selling price as compared to properties built recently.
# MAGIC * Rooms, Bedrooms, and Bathrooms show a high correlation with each other which is expected.
# MAGIC * BuildingArea and Landsize shows a positive correlation which makes sense as if the land size is more the building area will also be more.
# MAGIC * We should not consider the correlation value with Postcode because this column is a unique identifier for an area, and an increase or decrease in postcode can not impact any other feature.

# COMMAND ----------

# MAGIC %md
# MAGIC **Properties which have more space for living or more number of rooms, bedrooms and bathrooms generally tend to have higher selling prices. Let's analyze the relationship between the price and total number of rooms in a property**

# COMMAND ----------

# let's create a column with a sum of number of rooms, bedrooms, bathrooms, and car parking spaces 
data['Total Space'] = data['Rooms'] + data['Bedroom'] + data['Bathroom'] + data['Car']
data.head()


# COMMAND ----------

# MAGIC %md
# MAGIC * The column has been successfully added in the data frame.

# COMMAND ----------

plt.figure(figsize=(10,5))
sns.scatterplot(data=data,x='Total Space',y='Price')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * We can see an increasing trend of selling price with total space. Let's visualize the trend using lmplot().

# COMMAND ----------

sns.lmplot(data=data,x='Total Space',y='Price',height=5,aspect=2)
plt.xlim(0,55)
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * A positive correlation or an increasing trend can be clearly observed between the total number of rooms and the selling price of the property, although the line plotted by lmlot() doesn't show a high correlation. Let's check the correlation value further.
# MAGIC * The positive correlation indicates that more living space implies a higher selling price.

# COMMAND ----------

# lets check the correlation between Total space and Price
data[['Total Space','Price']].corr()

# COMMAND ----------

# MAGIC %md
# MAGIC * As expected, there is a positive correlation between Total Space and Price but it is not very high.

# COMMAND ----------

# MAGIC %md
# MAGIC **The distance of the property from the key facilities play a cruicial role in deciding the selling price of a property. The properties located closer to key facilities tend to be priced higher and vice versa. Let's find out if the same relationship exists in our data**

# COMMAND ----------

plt.figure(figsize=(15,7))
sns.scatterplot(data=data, x='Distance', y ='Price')
plt.show()

# COMMAND ----------

plt.figure(figsize=(15,7))
sns.lineplot(data=data, x='Distance', y ='Price',ci=None)
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * We observe that after 20-25 Kms the selling price of the properties starts decreasing which indicates that distance plays a key role in deciding the selling price of a property.
# MAGIC * Let's create bins/buckets for the Distance column to get better visualization of the relationship between Price and Distance.

# COMMAND ----------

# MAGIC %md
# MAGIC **Creating bins for distance column**
# MAGIC * 0 - 15  KMs  - The property will be said to be in **`Nearby`** location.
# MAGIC * 15 - 30 KMs - The property will be said to be in **`Moderately Close`** location.
# MAGIC * 30 - 50 KMs - The property will be said to be in **`Far`** away location.
# MAGIC
# MAGIC We will use **pd.cut() function** to create the bins in Distance column.
# MAGIC
# MAGIC     Syntax: pd.cut(x, bins, labels=None, right=False)
# MAGIC     
# MAGIC     x - column/array to binned
# MAGIC     bins - number of bins to create or an input of list for the range of bins
# MAGIC     labels - specifies the labels for the bins
# MAGIC     right - If set to False, it excludes the rightmost edge of the interval

# COMMAND ----------

# using pd.cut() function to create bins
data['Distance_bins'] = pd.cut(data['Distance'],bins=[0,15,30,50],labels=['Nearby','Moderately Close','Far'], right = False)

# COMMAND ----------

data.head()

# COMMAND ----------

# MAGIC %md
# MAGIC **Let's check the price with the distance bins**

# COMMAND ----------

sns.boxplot(data=data,x='Distance_bins',y='Price')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * It is a little difficult to make observations from here with so many outliers present in the data. Let's turn off these outliers (not removing from data) and see if we can observe any noticeable difference.

# COMMAND ----------

sns.boxplot(data=data,x='Distance_bins',y='Price',showfliers=False) # showfliers parameter controls the representation of outliers in the boxplot
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * We can see that as the distance increases the selling price of the property decreases.
# MAGIC * The properties closer to CBD have a high variance in the selling price. This variance in price decreases with the increase in distance.
# MAGIC * Considering that a customer has planned the budget for buying a property as the 'median' selling price for nearby, moderately close, and far away properties.
# MAGIC
# MAGIC   This variation in the selling price of a property might impact the planned budget of the customer who is looking to buy a property near CBD (as the variance is high). The customer might be able to get the property within the planned budget for properties that are far from CBD.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **As we observed in the correlation plot there is a negative correlation between the selling price of a property and the year it was built. Let's analyze it further**

# COMMAND ----------

# let's first calculate the age of a property from the year it was built in to see how the prices vary with it
year_at_sale = data['Date'].dt.year
year_at_sale

# COMMAND ----------

np.max(year_at_sale)

# COMMAND ----------

data['AgeofProp'] = year_at_sale - data['YearBuilt']
data.head()

# COMMAND ----------

# MAGIC %md
# MAGIC * The column was added in the data frame.

# COMMAND ----------

data[data['AgeofProp']==-2]

# COMMAND ----------

plt.figure(figsize=(15,5))
sns.lineplot(data=data,x='AgeofProp',y='Price',ci=None)
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * We observe an increasing trend indicating the properties which are older (vintage properties) have higher selling prices.
# MAGIC * The customers who wish to live in vintage properties might have to spend more money.
# MAGIC * Let's see this trend for all the regions

# COMMAND ----------

# MAGIC %md
# MAGIC * sns.relplot() is used to visualize any statistical relationships between quantitative variables.
# MAGIC * Why use relplot() instead of scatterplot() ?
# MAGIC     * relplot() lets you create multiple plots on a single axis.
# MAGIC         - kind - specifies the kind of plot to draw (scatter or line)
# MAGIC         - ci - specifies the confidence interval
# MAGIC         - col_wrap - specifies the number of columns in the grid

# COMMAND ----------

sns.relplot(data=data,x='AgeofProp',y='Price',col='Regionname',kind='line', ci=None, col_wrap=4)
plt.show()
# double click on the plot to zoom in

# COMMAND ----------

# MAGIC %md
# MAGIC * The trend of selling price increasing with the increase in age of the property is evident from the plot for Metropolitan regions.
# MAGIC * The trend of Victoria regions is slightly unclear, but this was expected as the number of data points for these regions is very low.

# COMMAND ----------

# MAGIC %md
# MAGIC **The price of properties vary based on the type of the property. For example, a villa may be priced higher than a duplex because of more amenities. Let's see which type of property is priced higher.**

# COMMAND ----------

plt.figure(figsize=(10,5))
sns.boxplot(data=data,x='Type',y='Price',showfliers=False) # turning off outliers
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * The properties like villa, cottage, etc have a higher median price as compared to a townhouse and a duplex.
# MAGIC * The townhouses have a higher median price than unit, duplex properties.
# MAGIC * Customers planning to buy 'h' type property might have to invest more.

# COMMAND ----------

# MAGIC %md
# MAGIC **Similarly the region of the property will play an integral role in deciding the selling price. Let' do a similar analysis with regions as well**

# COMMAND ----------

plt.figure(figsize=(10,5))
sns.boxplot(data=data,x='Regionname',y='Price',showfliers=False) # turning off outliers
plt.xticks(rotation=90)
plt.show()

# COMMAND ----------

# Dispersion of price in every region
sns.catplot(x='Price',
            col='Regionname', 
            data=data,
            col_wrap=4,
            kind="violin")
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * In Metropolitan, the southern and eastern regions have the costliest properties while the northern and western properties are priced similarly.
# MAGIC
# MAGIC * In Victoria, there is an increasing trend of prices, western having the lowest priced properties while northern has moderately priced properties, and eastern region having high priced properties.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4.4 Missing value treatment

# COMMAND ----------

# MAGIC %md
# MAGIC * There is no universally accepted method of dealing with missing values. 
# MAGIC * It is often left to the discretion of the data scientist to take a decision on missing values that is whether to impute them or drop them. 
# MAGIC * However, it is sometimes a good practice to impute the missing values rather than dropping them, because it can lead to loss of information in other features where values are present.

# COMMAND ----------

# MAGIC %md
# MAGIC **How to treat missing values?**
# MAGIC
# MAGIC One of the commonly used method to deal with the missing values is to impute them with the central tendencies - mean, median, and mode of a column.
# MAGIC
# MAGIC * `Replacing with mean`: In this method the missing values are imputed with the mean of the column. Mean gets impacted by the presence of outliers, and in such cases where the column has outliers using this method may lead to erroneous imputations. 
# MAGIC
# MAGIC * `Replacing with median`: In this method the missing values are imputed with the median of the column. In cases where the column has outliers, median is an appropriate measure of central tendency to deal with the missing values over mean.
# MAGIC
# MAGIC * `Replacing with mode`: In this method the missing values are imputed with the mode of the column. This method is generally preferred with categorical data.
# MAGIC
# MAGIC * Other methods include k-NN, MICE, SMOTE, deep learning, ...

# COMMAND ----------

# MAGIC %md
# MAGIC **Limitations of imputing missing values with central tendencies**
# MAGIC
# MAGIC * When we impute the missing values with central tendencies the original distribution of the feature can get distorted. 
# MAGIC * After imputation with the central value the variance and standard deviation of a feature can get drastically impacted.
# MAGIC * The impact of distortion is higher with higher percentage of missing values.
# MAGIC
# MAGIC So, before directly imputing the missing values with central values of column we should investigate the missing data closely to observe the pattern of missing values, and then take a decision to impute the missing value with appropriate measure.

# COMMAND ----------

# MAGIC %md
# MAGIC **Lets see the count and the percentage of missing values in each column**

# COMMAND ----------

# data.shape[0] will give us the number of rows in the dataset
# selecting the instances where missing value is greater than 0
pd.DataFrame({'Count':data.isnull().sum()[data.isnull().sum()>0],'Percentage':(data.isnull().sum()[data.isnull().sum()>0]/data.shape[0])*100})

# COMMAND ----------

# MAGIC %md
# MAGIC * BuildingArea and YearBuilt columns have the highest percentage of missing values.
# MAGIC * Distance and Postcode have the least number of missing values.
# MAGIC * Bedroom, Bathroom, and Car have almost equal percentage of missing values.
# MAGIC * AgeofProp and Total Space has equal percentage of missing values as YearBuilt and Bedroom, Bathroom, and Car because the information here were extracted using these columns.
# MAGIC * Landsize has around 34% missing values.

# COMMAND ----------

# MAGIC %md
# MAGIC **Missing value treatment for Distance column**

# COMMAND ----------

# extracting all the information of other variables where Distance is null
data.loc[data['Distance'].isnull()==True]

# COMMAND ----------

# MAGIC %md
# MAGIC * We observe that the data is missing for other attributes as well. This is a common problem with data collection where sometimes the data is not missing randomly and has a pattern in missingness. 
# MAGIC * Let's see if we can find more information using the name of the Suburb.

# COMMAND ----------

data.loc[data['Suburb']=='Fawkner Lot']

# COMMAND ----------

# MAGIC %md
# MAGIC * We see that there is only one data entry for the Fawkner Lot suburb and in this case it is possible that data for this suburb was not collected. This shows that data is not missing randomly rather has pattern in missingness.
# MAGIC * Imputing the Distance as well other information will not be a suitable approach as the imputed values will not be reliable. Hence, we will drop this row.

# COMMAND ----------

# adding the index value of the row in data.drop() function
data = data.drop(9590).reset_index(drop=True)

# COMMAND ----------

pd.DataFrame({'Count':data.isnull().sum()[data.isnull().sum()>0],'Percentage':(data.isnull().sum()[data.isnull().sum()>0]/data.shape[0])*100})

# COMMAND ----------

# extracting all the information of other variable where Bedroom is null
data.loc[data['Bedroom'].isnull()==True]

# COMMAND ----------

# MAGIC %md
# MAGIC * It looks like wherever Bedroom is null the data points in other columns are also missing. Let's check this.

# COMMAND ----------

data.loc[data['Bedroom'].isnull()==True,'Bathroom'].value_counts(dropna=False)

# COMMAND ----------

data.loc[data['Bedroom'].isnull()==True,'Car'].value_counts(dropna=False)

# COMMAND ----------

data.loc[data['Bedroom'].isnull()==True,'Landsize'].value_counts(dropna=False)

# COMMAND ----------

data.loc[data['Bedroom'].isnull()==True,'BuildingArea'].value_counts(dropna=False)

# COMMAND ----------

data.loc[data['Bedroom'].isnull()==True,'YearBuilt'].value_counts(dropna=False)

# COMMAND ----------

# MAGIC %md
# MAGIC * There seems to be a strong pattern in missing values, as wherever the Bedroom column has missing data the other columns like Bathroom, Car, Landsize, BuildingArea, and YearBuilt also have missing values.
# MAGIC * Let's see if the missing data has some pattern in suburbs, and regions of properties.

# COMMAND ----------

data.loc[data['Bedroom'].isnull()==True,'Suburb'].value_counts(dropna=False)

# COMMAND ----------

# to find the total number of unique values in a suburb
data['Suburb'].nunique()

# COMMAND ----------

# MAGIC %md
# MAGIC * Across 344 suburbs the missing values are present in 307 suburbs, indicating that the most suburbs have missing values.
# MAGIC * There seems to be no pattern of missing values with respect to suburb column.

# COMMAND ----------

data.loc[data['Bedroom'].isnull()==True,'Regionname'].value_counts(dropna=False)

# COMMAND ----------

# MAGIC %md
# MAGIC * Similar to suburbs there seems to be no notable pattern across different regions.

# COMMAND ----------

# MAGIC %md
# MAGIC **Missing value treatment for Bedroom, Bathroom, and Car columns**

# COMMAND ----------

# MAGIC %md
# MAGIC * One of the approaches to treat the missing values of these columns would be to group the data on the basis of Region and Type of the property to get a better idea of the average number of bedrooms, bathrooms, and car parking spaces.
# MAGIC * It is more likely that a property of certain type in a given region would have similar number of bedrooms, bathrooms, and car parking spaces.

# COMMAND ----------

# checking the average number of bedrooms, bathrooms, and car parking spaces in a region
data.groupby(['Regionname','Type'])[['Bedroom','Bathroom','Car']].mean()

# COMMAND ----------

# MAGIC %md
# MAGIC * We have received the mean number of Bedrooms, Bathrooms, and Car parking spaces for each type of property in a specific region.

# COMMAND ----------

# MAGIC %md
# MAGIC We will use fillna() function and transform method of pandas to impute the missing values.
# MAGIC
# MAGIC **fillna() Function -** The fillna() function is used to fill NaN values using the provide input value.
# MAGIC
# MAGIC        Syntax of fillna():  data['column'].fillna(value = x)
# MAGIC  
# MAGIC -----
# MAGIC
# MAGIC **transform function -** The transform() function works on each value of  a DataFrame and allows to execute a specified function on each value.
# MAGIC
# MAGIC     Sytanx of transform function: data.transform(func = function name)
# MAGIC
# MAGIC     * func - A function to be executed on the values of the DataFrame.
# MAGIC

# COMMAND ----------

# imputing missing values in Bedroom column
data['Bedroom'] = data['Bedroom'].fillna(value = data.groupby(['Regionname','Type'])['Bedroom'].transform('mean'))

# COMMAND ----------

# imputing missing values in Bathroom column
data['Bathroom'] = data['Bathroom'].fillna(value = data.groupby(['Regionname','Type'])['Bathroom'].transform('mean'))

# COMMAND ----------

# imputing missing values in Car column
data['Car'] = data['Car'].fillna(value = data.groupby(['Regionname','Type'])['Car'].transform('mean'))

# COMMAND ----------

# checking if all the missing values were imputed in Bedroom, Bathroom, and Car columns
pd.DataFrame({'Count':data.isnull().sum()[data.isnull().sum()>0],'Percentage':(data.isnull().sum()[data.isnull().sum()>0]/data.shape[0])*100})

# COMMAND ----------

# MAGIC %md
# MAGIC * We see that the missing values have been imputed.
# MAGIC * Let's convert all the values of Bedroom, Bathroom, and Car to integer type as these columns have discrete values.

# COMMAND ----------

data['Bedroom'] = data['Bedroom'].astype(int)
data['Bathroom'] = data['Bathroom'].astype(int)
data['Car'] = data['Car'].astype(int)

# COMMAND ----------

# MAGIC %md
# MAGIC **Missing values of Total Space column**
# MAGIC
# MAGIC We can create this feature again from the combination of Rooms, Bedroom, Bathroom, and Car as the missing values have now been imputed.

# COMMAND ----------

# removing Total Space column
data.drop('Total Space',axis=1,inplace=True)

# creating new Total Space column
data['Total_Space_New'] = data['Rooms'] + data['Bedroom'] + data['Bathroom'] + data['Car']
data['Total_Space_New'] = data['Total_Space_New'].astype(int)

# COMMAND ----------

# MAGIC %md
# MAGIC **Note:**
# MAGIC
# MAGIC It is a good idea to check the distributions of the column again after missing value imputation

# COMMAND ----------

# MAGIC %md
# MAGIC **Let's check the relationship of Total Space column with Price once again**

# COMMAND ----------

sns.scatterplot(data=data,x='Total_Space_New',y='Price')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * We observe that the relationship between Total Space and Price has not changed and the positive relation between these variables is still maintained, which is a good thing.

# COMMAND ----------

# MAGIC %md
# MAGIC **Missing value Treatment for Landsize**

# COMMAND ----------

# MAGIC %md
# MAGIC * We will use similar approach we took for imputing missing values in Bedroom, Bathroom, and Car columns. Using region and type of property will be a good way to find the size of land.
# MAGIC * Let's plot the distribution of Landsize.

# COMMAND ----------

sns.displot(data=data,x='Landsize',kind='kde')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * As Landsize column is skewed, using average value for imputation might not be the correct method as mean gets impacted by outliers. So we will use median value to impute the missing values of this column as median is not affected by the outliers.

# COMMAND ----------

data.groupby(['Regionname','Type'])[['Landsize']].median()

# COMMAND ----------

# MAGIC %md
# MAGIC * We have received the median value of Landsize for each type of property in a specific region.

# COMMAND ----------

# grouping data on region and type of property
# finding the median of landsize for each group and imputing the missing data with it
data['Landsize'] = data['Landsize'].fillna(value = data.groupby(['Regionname','Type'])['Landsize'].transform('median'))

# COMMAND ----------

# checking if all the missing values were imputed in Landsize column
pd.DataFrame({'Count':data.isnull().sum()[data.isnull().sum()>0],'Percentage':(data.isnull().sum()[data.isnull().sum()>0]/data.shape[0])*100})

# COMMAND ----------

# MAGIC %md
# MAGIC **Missing value treatment for BuildingArea, YearBuilt, and AgeofProp**

# COMMAND ----------

# MAGIC %md
# MAGIC * We will not do any imputation for Building Area and Year Built as these columns have more than 50% of missing data. As AgeofProp was extracted from YearBuilt column we can not do imputations in it as well.
# MAGIC * Any imputation in these columns will result in creation of new data points which will not be reliable to extract insights from.
# MAGIC * We have two options here - 
# MAGIC     * Option 1 - We can use the data which is not null to proceed with the analysis which will allow us to preserve the data which is not missing
# MAGIC     * Option 2- We can drop these columns from the data but it will lead to loss of data points from the data frame.
# MAGIC     

# COMMAND ----------

# Taking option 1 to remove the 61% null values from the building area column  
new_data = data[data['BuildingArea'].notnull()]
new_data.head()

# COMMAND ----------

# MAGIC %md
# MAGIC * We observe that the index of data frame has changed and the rows which had missing values in BuildingArea column have been removed.
# MAGIC * Similarly the above steps can be repeated for YearBuilt and AgeofProp column.

# COMMAND ----------

# Option 2 -  dropping columns BuildingArea, YearBuilt, and AgeofProp from the data frame
data = data.drop(['BuildingArea','YearBuilt','AgeofProp'],axis=1)

# COMMAND ----------

# saving the dataset with all the missing values treated
data.to_csv('/content/drive/MyDrive/Python Course/Melbourne_Housing_NoMissing.csv',index=False)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4.5 Outlier Detection and Treatment

# COMMAND ----------

from IPython.display import Image
Image("/content/drive/MyDrive/Python Course/boxplot.png")

# COMMAND ----------

# MAGIC %md
# MAGIC * An outlier is a data point that are abnormally/unrealistically distant from other points in the data. 
# MAGIC
# MAGIC * The challenge with outlier detection is determining if a point is truly a problem or simply a large value. If a point is genuine then it is very important to keep it in the data as otherwise we're removing the most interesting data points. 
# MAGIC
# MAGIC * It is left to the best judgement of the investigator to decide whether treating outliers is necessary and how to go about it. Domain Knowledge and impact of the business problem tend to drive this decision.

# COMMAND ----------

# MAGIC %md
# MAGIC **Handling outliers**
# MAGIC
# MAGIC Some of the commonly methods to deal with the data points that we actually flag as outliers are:
# MAGIC
# MAGIC * Replacement with null values - We can consider these data points as missing data and replace the abnormal values with NaNs.
# MAGIC * IQR method - Replace the data points with the lower whisker (Q1 - 1.5 * IQR) or upper whisker (Q3 + 1.5 * IQR) value.
# MAGIC * We can also drop these observations, but we might end up with losing other relevant observations as well.
# MAGIC
# MAGIC So, it is often a good idea to examine the results by  running an analysis with and without outliers.

# COMMAND ----------

# reading the dataset 
data = pd.read_csv('Melbourne_Housing_NoMissing.csv')
data.head()

# COMMAND ----------

# MAGIC %md
# MAGIC **Let's visualize all the outliers present in data together**

# COMMAND ----------

# outlier detection using boxplot
# selecting the numerical columns of data and adding their names in a list 
numeric_columns = ['Rooms', 'Distance', 'Postcode', 'Bedroom', 'Bathroom', 'Car','Landsize',
                   'Propertycount', 'Price']
plt.figure(figsize=(15, 12))

for i, variable in enumerate(numeric_columns):
    plt.subplot(4, 4, i + 1)
    plt.boxplot(data[variable], whis=1.5)
    plt.tight_layout()
    plt.title(variable)

plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC We can see that all the numerical features in the data set have outliers present in them.
# MAGIC
# MAGIC
# MAGIC **Let's analyze each column to see if the values in them can be considered as outliers or not.**
# MAGIC   
# MAGIC   
# MAGIC  * Rooms, Bedroom, Bathroom, Car - The values which are being represented as outliers in the above boxplot may not seem realistic in some cases. For example- It is not common to have more than 15 rooms, 15 bedrooms, and more than 10 car parking spaces in a general scenario. 
# MAGIC
# MAGIC Although these values can not be considered to be unrealistic but we will rarely see such high number of rooms, bedrooms, bathrooms and car parking in a property. So, we will treat the outliers in this column.
# MAGIC   
# MAGIC   
# MAGIC  * Distance - The outliers in this column can be considered as genuine values because a property can be at varying distances from the C.B.D. In the context of this problem we will not consider these values as outliers.
# MAGIC  
# MAGIC  
# MAGIC  * Postcode - Postcodes are a combination of several numerical values based on region, sub-region, etc and these cannot be considered as outliers. 
# MAGIC  
# MAGIC  
# MAGIC  
# MAGIC  * Landsize - The values in this column seem unrealistic as some of the properties have a Land size greater than 0.1 Sq Kms. So, we will treat the outliers in this column.
# MAGIC  
# MAGIC  
# MAGIC  
# MAGIC  * Propertycount- Each suburb can have varying number of properties depending upon the region and the area of a suburb. Hence, the count of properties in a suburb can be considered as genuine values and not outliers.
# MAGIC  
# MAGIC  
# MAGIC  
# MAGIC  * Price - The selling price of properties depends upon various factors (for example location of a property) and the prices can change from time to time. Hence, the selling price of properties can be considered as genuine values and not outliers.

# COMMAND ----------

# MAGIC %md
# MAGIC **Let's find the percentage of outliers, in each column of the data, using IQR.**

# COMMAND ----------

# to find the 25th percentile and 75th percentile for the numerical columns.
Q1 = data[numeric_columns].quantile(0.25)
Q3 = data[numeric_columns].quantile(0.75)

IQR = Q3 - Q1                   #Inter Quantile Range (75th percentile - 25th percentile)

lower_whisker = Q1 - 1.5*IQR    #Finding lower and upper bounds for all values. All values outside these bounds are outliers
upper_whisker = Q3 + 1.5*IQR

# COMMAND ----------

# Percentage of outliers in each column
((data[numeric_columns] < lower_whisker) | (data[numeric_columns] > upper_whisker)).sum()/data.shape[0]*100

# COMMAND ----------

# MAGIC %md
# MAGIC **Treating outliers**
# MAGIC
# MAGIC We will cap/clip the minimum and maximum value of these columns to the lower and upper whisker value of the boxplot found using  **Q1 - 1.5*IQR** and **Q3 + 1.5*IQR**, respectively.
# MAGIC
# MAGIC **Note**: Generally, a value of 1.5 * IQR is taken to cap the values of outliers to upper and lower whiskers but any number (example 0.5, 2, 3, etc) other than 1.5 can be chosen. The value depends upon the business problem statement.

# COMMAND ----------

# MAGIC %md
# MAGIC **Creating a function to floor and cap/clip outliers in a column**

# COMMAND ----------

def treat_outliers(df, col):
    """
    treats outliers in a variable
    col: str, name of the numerical variable
    df: dataframe
    col: name of the column
    """
    Q1 = df[col].quantile(0.25)  # 25th quantile
    Q3 = df[col].quantile(0.75)  # 75th quantile
    IQR = Q3 - Q1                # Inter Quantile Range (75th perentile - 25th percentile)
    lower_whisker = Q1 - 1.5 * IQR
    upper_whisker = Q3 + 1.5 * IQR

    # all the values smaller than lower_whisker will be assigned the value of lower_whisker
    # all the values greater than upper_whisker will be assigned the value of upper_whisker
    # the assignment will be done by using the clip function of NumPy
    df[col] = np.clip(df[col], lower_whisker, upper_whisker)

    return df

# COMMAND ----------

# MAGIC %md
# MAGIC **Treating outliers in Rooms column**

# COMMAND ----------

data = treat_outliers(data,'Rooms')

# visualizing the column after outlier treatment
sns.boxplot(data=data,x='Rooms')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * The maximum number of rooms in a property have been capped to 7. All the values greater than 7 (whisker value) have been treated.

# COMMAND ----------

# MAGIC %md
# MAGIC **Similarly we will treat the outliers in other columns using the same approach**

# COMMAND ----------

# treating outliers of Bedroom column
data = treat_outliers(data,'Bedroom')

# treating outliers of Car column
data = treat_outliers(data,'Car')

# treating outliers of Bathroom column
data = treat_outliers(data,'Bathroom')

# treating outliers of Landsize column
data = treat_outliers(data,'Landsize')

# COMMAND ----------

# MAGIC %md
# MAGIC **Let's visualize numerical columns where outliers were treated**

# COMMAND ----------

# outlier detection using boxplot
# selecting the numerical columns where outliers were treated 
numeric_columns = ['Rooms', 'Bedroom', 'Bathroom', 'Car','Landsize']
plt.figure(figsize=(15, 12))

for i, variable in enumerate(numeric_columns):
    plt.subplot(4, 4, i + 1)
    plt.boxplot(data[variable], whis=1.5)
    plt.tight_layout()
    plt.title(variable)

plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * All the outliers have been treated.
# MAGIC * We observe that the data type of Bedroom, Bathroom, and Car has changed to float which we should change to the integer type.
# MAGIC * We can also see that the distribution of Landsize column doesn't look heavily right-skewed now.

# COMMAND ----------

# MAGIC %md
# MAGIC **Setting the data type to integer for Bedroom, Bathroom, and Car columns**

# COMMAND ----------

data['Bedroom'] = data['Bedroom'].astype(int)
data['Bathroom'] = data['Bathroom'].astype(int)
data['Car'] = data['Car'].astype(int)

# COMMAND ----------

# saving the dataset with all the outlier values treated
data.to_csv('/content/drive/MyDrive/Python Course/Melbourne_Housing_NoOutliers.csv',index=False)