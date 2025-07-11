# Databricks notebook source
# MAGIC %md
# MAGIC #### Numpy

# COMMAND ----------

# Numpy
# Numpy arrays are highly efficient multidimensional data structures in python that support a wide range of mathematical operations and functions. enabling fast and powerful computations
import numpy as np

arr_str = ['Mercedes', 'BMW', 'Audi']

np_arr_num = np.array(arr_str)
print(np_arr_num)
print(type(np_arr_num))


# COMMAND ----------

# Numy matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

# COMMAND ----------

# arange() has evenly spaced elements as per the interval.
arr2 = np.arange(start = 0, stop = 10, step = 3)
print(arr2)

# COMMAND ----------

# linspace() has evenly spaced elements as per the length.
arr3 = np.linspace(start = 0, stop = 10, num = 20)
print(arr3)

# COMMAND ----------

# zeros and ones for matrix
matrix4 = np.zeros([3, 3])
print(matrix4)

matrix5 = np.ones([3,5])
print(matrix5)

# COMMAND ----------

# eye - Ones on diagonal and zeros everywhere
matrix6 = np.eye(5)
print(matrix6)

# COMMAND ----------

# reshape: Converting one-d array to matrix
arr4 = np.arange(0,10)
print(arr4)

arr4_reshaped = arr4.reshape((2,5))
print(arr4_reshaped)

# COMMAND ----------

# Numpy Trignomatry
print('Sin Function', np.sin(4))
print('Cos Function', np.cos(4))
print('Tan Function', np.tan(4))

# Numpy Exponents
print(np.exp(2))

# Numpy Logarithm
print(np.log([2,3]))
print(np.log2(8))
print(np.log10(100))


# COMMAND ----------

# arithmatic operators
l1 = [1,2,3]
l2 = [4,5,6]

print(l1+l2)
print(np.add(l1,l2))

# COMMAND ----------

# arithmatic operators
arr7 = np.arange(1,6)
print('arr7:', arr7)
arr8 = arr7[::-1]
print('arr8:', arr8)

print('Addition:', arr7 + arr8)
print('Subtraction:', np.subtract(arr7, arr8))
print('Multiplication:', arr7 * arr8)
print('Division:', arr7 / arr8)
print('Power:', arr7 ** arr8)
print('Inverse:', 1/arr7)


# COMMAND ----------

# matrix multiplication based on rules of linear algebra 

matrix9 = np.arange(1,10).reshape(3,3)
print('First Matrix: \n', matrix9)

matrix10 = np.arange(11,20).reshape(3,3)
print('Second Matrix: \n', matrix10)

print('Normal Multiplcation    \n', matrix9 * matrix10)
print('Linear algebra multiplication \n', matrix9 @ matrix10)

# COMMAND ----------

# Function for min/max
print('Min: ', np.min(matrix9))
print('Max: ', np.max(matrix9))

# Random Numbers (0 - inclusive to 1 - exclusive)
rand_mat = np.random.rand(5)
print('Random Values :',rand_mat)

rand_mat = np.random.randint(1,25,10)
print('Random Numbers:', rand_mat)

rand_mat = np.random.randint(1,25,[5,5])
print('Random Matrix:', rand_mat)

# randn : returns random numpy array whose sample are drawn randomly from standard normal distribution (mean as 0 and standard deviation as 1)
rand_mat2 = np.random.randn(5,5)
print(rand_mat2)

# COMMAND ----------

# check mean and standard deviation
print('Mean: ', np.mean(rand_mat2))
print('Standard Deviation: ', np.std(rand_mat2))

# Accessing arrays
print(rand_mat2[rand_mat2>1])
print(rand_mat2[0:2, 1:3])

# COMMAND ----------

# Intersting question
vec1 = np.array([4,7,8,9,10,6,1])
vec1[vec1>6] = 2

print(vec1)

# COMMAND ----------

# Pointers in arrays

rand_mat = np.random.rand(5,5)
print(rand_mat)

# Correct way to avoid changes in original source variable
sub_mat = rand_mat[0:2,0:3].copy()
sub_mat[:] = 3
print(sub_mat)
print(rand_mat)

# Incorrect
sub_mat = rand_mat[0:2,0:3]
sub_mat[:] = 3
print(sub_mat)
print(rand_mat)

# COMMAND ----------

# Saving and loading Numpy arrays 
from google.colab import drive
drive.mount('/content/drive')

np.save('/content/drive/MyDrive/Python', randint_matrix1)
np.savez('/content/drive/MyDrive/Python', randint_matrix1 = randint_matrix1, randint_matrix2 = randint_matrix2)

loaded_arr = np.load('/content/drive/MyDrive/Python/multiple_files.npz')
new_matrix = loaded_arr['randint_matrix1']

# COMMAND ----------

a="hello"
b="hello"
print(a is b)
x="".join(["he", "llo"])
print(type(a))
print(x is a)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Pandas
# MAGIC
# MAGIC ```
# MAGIC Pandas Series: 1-D labeled array/list capable of holding data of any type (int,str,float,python obj,etc)
# MAGIC                Single column in Excel
# MAGIC Pandas Dataframe: 
# MAGIC ```

# COMMAND ----------

import pandas as pd
import numpy as np

med_price_list = [55,25,75,40,80]

med_price_arr = np.array(med_price_list)

series_list = pd.Series(med_price_list)
series_arr = pd.Series(med_price_arr, index = ['a','b','c','d','e'])
print(series_list)
print(series_arr)

# COMMAND ----------

# MAGIC %md
# MAGIC ```
# MAGIC In pandas which method is used to capitalize first letter of each string to Series
# MAGIC - str.capitalize()
# MAGIC ```

# COMMAND ----------

price_list = [77,45.5,100,50,80]
new_price_list_labeled = pd.Series(price_list, index = ['Omeprazole', 'Azithromycin', 'Ibuprofen', 'Paracetamol', 'Cetirizine'])

print(new_price_list_labeled - price_list)

# COMMAND ----------

# DataFRame - Single column
student = ['Mary', 'Peter', 'Susan', 'Toby', 'Vishal']
df1 = pd.DataFrame(student, columns=['Student'])
df1

# COMMAND ----------

# DataFrame using Dictionary
grades = ['B-', 'A+', 'A-', 'B+', 'C']

df2 = pd.DataFrame({'Student': student, 'Grade': grades})
df2

# COMMAND ----------

# DataFrame using Distionary of Series

year = pd.Series([2019, 2020, 2021, 2022, 2023])
energy_consumption = pd.Series([1000, 1200, 1500, 1800, 2000])

df3 = pd.DataFrame({'Year': year, 'Energy Consumption': energy_consumption})
df3

# COMMAND ----------

# DataFrame using Random Values
df4 = pd.DataFrame(np.random.randn(5,2), columns = ['Trial 1', 'Trial 2'])
df4

# COMMAND ----------

# Accessing and Modifying Series

Operations = ['At&T', 'Verizon', 'T-Mobile US', 'US Cellular']
revenue = [171.76, 128.29, 68.4, 4.04]

telecom = pd.Series(revenue, index = Operations)

display(telecom)
print('0th element',telecom[0])
print('Last 2 elements',telecom[-2:])
print('\nRevenue of T Mobile',telecom['T-Mobile US'])
print('\nRevenue upto T Mobile',telecom[:'T-Mobile US'])

# COMMAND ----------

# Accessing DataFrames
store_data = pd.DataFrame(
    {
        'CustomerID': ['CustID00', 'CusID001', 'CustID002', 'CustID003', 'CustID004'],
        'location': ['NY', 'LA', 'NY', 'LA', 'LA'],
        'gender': ['Female', 'Male', 'Female', 'Male', 'Female'],
        'type': ['Premium', 'Basic', 'Premium', 'Basic', 'Basic'],
        'quantity':[1,3,2,1,2],
        'total_bill': [100,75,120,50,60]
    }
)
display(store_data) 

#Accessing first row
print('\n',store_data[:1])

# Accessing first column of DataFrame
print('\n',store_data['location'])

# Accessing rows with step size 2
print('\n', store_data[::2])

# Accessing rows with reverse order
print('\n', store_data[::-1])

# COMMAND ----------

# Accessing and Modefying DataFrame
# loc vs iloc
# loc is label-based indexing, while iloc is positional integer-based indexing

print('\nFirst element', store_data.loc[1])
print('\nFirst and Fourth index values with location & type columns', store_data.loc[[1,4],['location', 'type']])
print('\nFirst and Fourth index values with location & type columns', store_data.iloc[[1,4],[1,3]])

store_data.loc[4,'type'] = 'Electronics'
print(store_data)

# COMMAND ----------

print('\nAccessing Store data with quantity greater than 1')
store_data.loc[ store_data['quantity']>1 ]

# To avoid modifying original DataFrame, use copy method
new_store_data = store_data.copy()

# 0 axis is row and 1 axis is column
print('\nDroping column')
new_store_data.drop('CustomerID', axis=1, inplace=True)
print(new_store_data)


# COMMAND ----------

# Combinning DataFrame
# Concat vs join vs merge
import pandas as pd

data_cust = pd.DataFrame({
    'customerID': ['101', '102','103', '104'],
    'category': ['Medium', 'Medium', 'High', 'Low'],
    'first_visit': ['yes', 'no', 'yes','yes'],
    'sales': [123,52,214,663]
}, index = [0,1,2,3])

data_cust_new = pd.DataFrame(
    {
        'customerID': ['101','103','104','105'],
        'distance': [12,9,44,21],
        'sales': [123,214,663,331]
    }, index = [4,5,6,7]
)

print('\nConcatenating rows:\n', pd.concat([data_cust, data_cust_new], axis = 0) )

print('\nConcatenating columns:\n', pd.concat([data_cust, data_cust_new], axis = 1) )

# COMMAND ----------

# Merging DataFrame
print('\nMerging using outer merge\n', pd.merge(data_cust, data_cust_new, how='outer', on='customerID') )

print('\nMerging using inner merge\n', pd.merge(data_cust, data_cust_new, how='inner', on='customerID') )

print('\nMerging using right join\n', pd.merge(data_cust, data_cust_new, how='inner', on='customerID'))




# COMMAND ----------

# Saving and Loading datasets

from google.colab import drive
drive.mount('/content/drive')

path = 'content/drive/MyDrive/Python Course/StockData.csv'
data = pd.read_csv(path)

data.head()

#saving as csv
data.to_csv('content/drive/MyDrive/Python Course/StockData.csv', index=False)
data.to_excel('content/drive/MyDrive/Python Course/StockData.xlsx', index=False)

# COMMAND ----------

# Pandas Function
# top 5 rows
data.head()

#last 5 rows
data.tail()

#check number of rows and columns in dataset
data.shape

# to check datatype of column
data.info()

data['price'].min()

data['price'].max()

# To check the number of unique values that are present in column
data['stock'].unique()

# To check the number of values that each unique quantity has in column
data['stock'].value_counts()

# Using the normalize parameter and initializing it to True will return reklative frequencies of unique value
data['stock'].value_counts()

# To check mean averge value of column
data['price'].mean()

# To check median value of column
data['price'].median()

# To check mode value of column
data['price'].mode()



# COMMAND ----------

# Pandas Functions (groupby)
data.groupby(['stock'])['price'].median()

data.groupby(['stock'])['price'].mean()

# Custom function apply

def profit(s):
    return s+ s*0.10

data['price'].apply(profit)

data['new_price'] = data['price'].apply(profit)
data.head()


# sort_values() function sorts a dataframe in ascending or descending order of passed column
data.sort_values(by='new_price', ascending=False)

# COMMAND ----------

# Converting data column to datetime format
data['date'] = pd.to_datetime(data['date'], dayfirst=True)
data.info()

data['date'].dt.strftime('%Y-%m-%d')

data['month'] = data['date'].dt.month
data['year'] = data['date'].dt.year
data['day'] = data['date'].dt.day

# Comparing dates on different rows
data['date'][1] - data['date'][0]
data['date'][1] > data['date'][0]

# COMMAND ----------

import datetime
date = datetime.date(2022,1,29)
print(date)