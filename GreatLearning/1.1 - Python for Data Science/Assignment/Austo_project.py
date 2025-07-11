# Databricks notebook source
# MAGIC %md
# MAGIC # Python Foundations Project: Austo
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Problem Statement

# COMMAND ----------

# MAGIC %md
# MAGIC ### Context
# MAGIC
# MAGIC In the 21st century, cars are an important mode of transportation that provides us the opportunity for personal control and autonomy. In day-to-day life, people use cars for commuting to work, shopping, visiting family and friends, etc. Research shows that more than 76% of people prevent themselves from traveling somewhere if they don't have a car. Most people tend to buy different types of cars based on their day-to-day necessities and preferences. So, it is essential for automobile companies to analyze the preference of their customers before launching a car model into the market. Austo, a UK-based automobile company aspires to grow its business into the US market after successfully establishing its footprints in the European market.
# MAGIC
# MAGIC In order to be familiar with the types of cars preferred by the customers and factors influencing the car purchase behavior in the US market, Austo has contracted a consulting firm. Based on various market surveys, the consulting firm has created a dataset of 3 major types of cars that are extensively used across the US market. They have collected various details of the car owners which can be analyzed to understand the automobile market of the US.
# MAGIC
# MAGIC ### Objective
# MAGIC
# MAGIC Austo's management team wants to understand the demand of the buyers and trends in the US market. They want to build customer profiles based on the analysis to identify new purchase opportunities so that they can manipulate the business strategy and production to meet certain demand levels. Further, the analysis will be a good way for management to understand the dynamics of a new market. Suppose you are a Data Scientist working at the consulting firm that has been contracted by Austo. You are given the task to create buyer's profiles for different types of cars with the available data as well as a set of recommendations for Austo. Perform the data analysis to generate useful insights that will help the automobile company to grow its business.
# MAGIC
# MAGIC ### Data Description
# MAGIC
# MAGIC austo_automobile.csv: The dataset contains buyer's data corresponding to different types of products(cars).
# MAGIC
# MAGIC ### Data Dictionary
# MAGIC
# MAGIC * Age: Age of the customer
# MAGIC * Gender: Gender of the customer
# MAGIC * Profession: Indicates whether the customer is a salaried or business person
# MAGIC * Marital_status: Marital status of the customer
# MAGIC * Education: Refers to the highest level of education completed by the customer
# MAGIC * No_of_dependents: Number of dependents(partner/children/spouse) of the customer
# MAGIC * Personal_loan: Indicates whether the customer availed a personal loan or not
# MAGIC * House_loan: Indicates whether the customer availed house loan or not
# MAGIC * Partner_working: Indicates whether the customer's partner is working or not
# MAGIC * Salary: Annual Salary of the customer
# MAGIC * Partner_salary: Annual Salary of the customer's partner
# MAGIC * Total_salary: Annual household income (Salary + Partner_salary) of the customer's family
# MAGIC * Price: Price of the car
# MAGIC * Make: Car type (Hatchback/Sedan/SUV)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Importing necessary libraries

# COMMAND ----------

# Installing the libraries with the specified version.
!pip install numpy==1.25.2 pandas==1.5.3 matplotlib==3.7.1 seaborn==0.13.1 -q

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %md
# MAGIC **Note**: *After running the above cell, kindly restart the notebook kernel and run all cells sequentially from the start again.*

# COMMAND ----------

# import libraries for data manipulation
import numpy as np
import pandas as pd

# import libraries for data visualization
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# COMMAND ----------

# MAGIC %md
# MAGIC ## Importing the dataset

# COMMAND ----------

import os
file_path = os.path.abspath('Storage/austo_automobile.csv')
df = pd.read_csv(file_path, on_bad_lines='skip')

# COMMAND ----------

# return the first 5 rows
df.head()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Overview

# COMMAND ----------

# MAGIC %md
# MAGIC #### Question 1: How many rows and columns are present in the data? [0.5 mark]

# COMMAND ----------

# Check for number of rows and columns in dataset
print('There are' , df.shape[0] ,'rows and' , df.shape[1] ,'columns in the dataset') 

# COMMAND ----------

# MAGIC %md
# MAGIC #### Observations:
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #### Question 2: What are the datatypes of the different columns in the dataset? [0.5 mark]

# COMMAND ----------

# Check the dataset column datatype
df.info()

# COMMAND ----------

# MAGIC %md
# MAGIC - 6 columns are integer type (Age, No-Of_Dependents, Salary, Partner_Salary, Total_Salary, Price)
# MAGIC - 7 columns are object type (Gender, Profession, Marital_Status, Education, Personal_Loan, House_Loan, Partner_Working, Make)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Observations:
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #### Question 3: Check the statistical summary of the data. What is the minimum, average, and maximum Price of the cars? [2 marks]

# COMMAND ----------

# Check statistical summary of data
df.describe().T

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC - The minimum price of the cars is 18000$
# MAGIC - The average price of the cars is 35597.7$
# MAGIC - The maximum price of the cars is 70000$

# COMMAND ----------

# MAGIC %md
# MAGIC #### Observations:
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #### Question 4: Are there any missing values in the data? If yes, treat them using an appropriate method.  [1 Mark]

# COMMAND ----------

# Checking missing values
df.isnull().sum()

# COMMAND ----------

# Check duplicates
df.duplicated().sum()

# COMMAND ----------

# MAGIC %md
# MAGIC - There are no missing values in the datset as all values across columns are populated

# COMMAND ----------

# MAGIC %md
# MAGIC #### Observations:
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #### Question 5: How many cars are there of type SUV? [1 mark]

# COMMAND ----------

(df['Make'] == 'SUV').sum()

# COMMAND ----------

# MAGIC %md
# MAGIC - We have 237 SUV Type cars in datset

# COMMAND ----------

# MAGIC %md
# MAGIC #### Observations:
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exploratory Data Analysis (EDA)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Univariate Analysis

# COMMAND ----------

# MAGIC %md
# MAGIC #### **Question 6:** Explore all the variables and provide observations on their distributions. (Generally, histograms, boxplots, countplots, etc. are used for univariate exploration.) [10 marks]

# COMMAND ----------

# Exploring Age of target market
plt.figure(figsize=(15,5))
plt.title('Histogram - Age')
plt.xlabel('Age')
plt.ylabel('Total')
sns.histplot(data=df, x='Age', color='green', kde = 'True')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC - Majority of car owners are in age group 22 to 30, having strong interest in personal cars
# MAGIC - As age increases after 30, there is steap decline in owning personal cars  

# COMMAND ----------

# Exploring Age of target market
plt.figure(figsize=(10,4))
plt.title('Boxplot - Age')
plt.xlabel('Age')
plt.ylabel('Total')
sns.boxplot(data=df, x='Age', color='green')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC - Age is right skewed, with median age of 29 years
# MAGIC - Few customers aged above 57 are outliers

# COMMAND ----------

# Exploring Gender of target market
plt.figure(figsize=(8,4))
plt.title('Histogram - Gender')
plt.xlabel('Gender')
plt.ylabel('Total')
sns.countplot(data=df, x='Gender', color='blue')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC - More than 1200 cars are owned by males, compared to females with only ~350 cars

# COMMAND ----------

# Exploring Gender Perecentage of target market
df['Gender'].value_counts(normalize=True) * 100 

# COMMAND ----------

# MAGIC %md
# MAGIC - 80% car owners are male, 20% are females

# COMMAND ----------

# Exploring Profession of target market
plt.figure(figsize=(8,4))
plt.title('Histogram - Profession')
plt.xlabel('Profession')
plt.ylabel('Total')
sns.countplot(data=df, x='Profession', color='cyan')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC - Salaried people owns more cars than Business people

# COMMAND ----------

# Exploring Profession Perecentage of target market
df['Profession'].value_counts(normalize=True) * 100 

# COMMAND ----------

# MAGIC %md
# MAGIC - 56% salaried people owns the car over 43% business people

# COMMAND ----------

# Exploring Profession of target market
plt.figure(figsize=(8,4))
plt.title('Histogram - Marital_status')
plt.xlabel('Marital_status')
plt.ylabel('Total')
sns.countplot(data=df, x='Marital_status', color='cyan')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC - Family plays crucial role in ownership of cars. There is a strong interest of cars in married customers

# COMMAND ----------

# Exploring Profession Perecentage of target market
df['Marital_status'].value_counts(normalize=True) * 100 

# COMMAND ----------

# MAGIC %md
# MAGIC - 91% married customers owns the car, only 8% non-married customers have cars

# COMMAND ----------

# Exploring Education of target market
plt.figure(figsize=(8,4))
plt.title('Histogram - Education')
plt.xlabel('Education')
plt.ylabel('Total')
sns.countplot(data=df, x='Education', color='orange')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC - Education of customers influence owning cars. Higher the education, more changes of need to have personal car

# COMMAND ----------

# Exploring No_of_Dependent of target market

plt.figure(figsize=(8,4))
plt.title('BarGraph - No_of_Dependent')
plt.xlabel('No_of_Dependent')
plt.ylabel('Total')
sns.countplot(data=df, x='No_of_Dependents', color='orange')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC - Having 1 to 3 dependents, increases chances of owning cars

# COMMAND ----------

# Exploring Personal_loan of target market

plt.figure(figsize=(8,4))
plt.title('BarGraph - Personal_loan')
plt.xlabel('Personal_loan')
plt.ylabel('Total')
sns.countplot(data=df, x='Personal_loan', color='yellow')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC - Personal loan does not influence having the cars directly

# COMMAND ----------

# Exploring House_loan of target market

plt.figure(figsize=(8,4))
plt.title('BarGraph - House_loan')
plt.xlabel('House_loan')
plt.ylabel('Total')
sns.countplot(data=df, x='House_loan', color='yellow')
plt.show()

# COMMAND ----------

# Exploring House_loan percentage of target market
df['House_loan'].value_counts(normalize=True) * 100 

# COMMAND ----------

# MAGIC %md
# MAGIC - Customers with no House loan have 50% more chances of owning the car

# COMMAND ----------

# Exploring Partner_working of target market

plt.figure(figsize=(8,4))
plt.title('BarGraph - Partner_working')
plt.xlabel('Partner_working')
plt.ylabel('Total')
sns.countplot(data=df, x='Partner_working', color='yellow')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC - Working partner creates more chances of owning car

# COMMAND ----------

# Exploring Salary of target market

plt.figure(figsize=(15,5))
plt.title('Histogram - Salary')
plt.xlabel('Salary')
plt.ylabel('Total')
sns.histplot(data=df, x='Salary', color='blue', kde='True')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC - Some cutsomers earns significantly more than others
# MAGIC - Most commom salary band is around 50000 to 60000 dollars

# COMMAND ----------

# Exploring Partner_salary of target market

plt.figure(figsize=(15,5))
plt.title('Histogram - Partner_salary')
plt.xlabel('Partner Salary')
plt.ylabel('Total')
sns.histplot(data=df, x='Partner_salary', color='blue', kde='True')
plt.show()

plt.figure(figsize=(5,3))
plt.title('Boxplot - Partner_salary')
sns.boxplot(data=df, x='Partner_salary', color='blue');
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC - Partner_salary data is highly right skewed, indicating strong concentration near 0$ salary and very rare cases of high earners
# MAGIC - Many customers have non-working partners, as most of the partners have 0$ salary or income not declared
# MAGIC - Partner_Salary has 2 groups of income holders
# MAGIC   - One with 25000 to 30000
# MAGIC   - second with 35000 to 45000
# MAGIC - There are no outliers in data
# MAGIC

# COMMAND ----------

# Exploring Total_salary of target market

plt.figure(figsize=(15,5))
plt.title('Histogram - Total_salary')
plt.xlabel('Total_salary')
plt.ylabel('Total')
sns.histplot(data=df, x='Total_salary', color='blue', kde='True')
plt.show()

plt.figure(figsize=(5,3))
plt.title('Boxplot - Total_salary')
sns.boxplot(data=df, x='Total_salary', color='blue');
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC - Total_salary data is right skewed
# MAGIC - Many outliers detected with salary more than 160,000 dollars indicating very high income customers
# MAGIC - Most of the customers holds income ranges between 60,000 to 95,000
# MAGIC

# COMMAND ----------

# Exploring Price of target market

plt.figure(figsize=(15,5))
plt.title('Histogram - Price of car')
plt.xlabel('Price')
plt.ylabel('Price')
sns.histplot(data=df, x='Price', color='blue', kde='True')
plt.show()

plt.figure(figsize=(5,3))
plt.title('Boxplot - Price')
sns.boxplot(data=df, x='Price', color='blue')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC - Price of car data is again right skewed. No outliers in Price of cars
# MAGIC   - Most of the cars with range 25000 to 45000, reflecting demand for affordability and mid-range vehicle
# MAGIC   - Permium and luxury cars are less common due to high price

# COMMAND ----------

# Exploring Make of target market

plt.figure(figsize=(8,4))
plt.title('BarGraph - Car Type')
plt.xlabel('Make')
plt.ylabel('Total')
sns.countplot(data=df, x='Make', color='yellow', order=df['Make'].value_counts().index)
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC - Hatchback cars are most popular choice (around 850 customers), followed by Sedan (~450 customers) and SUV being least prefered (only ~250 customers)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Observations:
# MAGIC
# MAGIC **Summary of univariate analysis**
# MAGIC - Strong Preference of personal cars among youngsters aged 22 to 30 years
# MAGIC - Gender plays crucial role in interest in cars with male being dominating group for car ownership
# MAGIC - Customers who are married, have very high chances of owning personal car
# MAGIC   - Most of the customers have non-working partners
# MAGIC   - Working partner increases the chances of buying a car
# MAGIC   - Customers with more dependent have more chances of buying a car
# MAGIC - Highly educated people have more demand for cars
# MAGIC - House loan decreases the chances of having cars by 50%, Personal loan does not impact sales of car
# MAGIC - Customers earning mid-range between 50K to 60K have strong desire for car
# MAGIC   - Working partner have little influence in car ownership as most of the partners are non-working or with no declaration of salary
# MAGIC - Affordable cars with price ranges between 25000 to 45000 are highly demanding, premium cars are owned by less people
# MAGIC - Most comman car is hatchback, followed by Sedan and SUV is least preferred choice
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #### Question 7: How many cars are of make Hatchback and priced above 25000. State your observations? [2 marks]

# COMMAND ----------

df.loc[(df['Price'] > 25000) & (df['Make'] == 'Hatchback'), 'Make'].value_counts()

# COMMAND ----------

df2 = df[(df['Make'] == 'Hatchback') & (df['Price'] > 25000)]
df2.describe().T

# COMMAND ----------

cols = ['Age', 'Gender', 'Profession', 'Education', 'Marital_status', 'Salary', 'House_loan', 'Personal_loan', 'No_of_Dependents', 'Price']

# Grid setup
fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(18, 8))
axes = axes.flatten()

# Loop through and plot
for i, col in enumerate(cols):
    ax = axes[i]
    if df2[col].dtype == 'object' or df2[col].nunique() < 10:
        sns.countplot(x=col, data=df2, ax=ax)
    else:
        sns.histplot(df2[col], bins=20, kde=True, ax=ax)
    ax.set_title(col)
    ax.tick_params(axis='x', rotation=30)

# Hide extra axes if any
for j in range(len(cols), len(axes)):
    axes[j].set_visible(False)

plt.tight_layout()
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Observations:
# MAGIC
# MAGIC **Cars with Type Hashback and Price more than 25000**
# MAGIC - Age of the customers is between 22 to 30, indicating 
# MAGIC - Males are the main target group of potential buyers
# MAGIC - Married male have strong chances to buy cars
# MAGIC - More dependents (usually 2 to 4) influence more potential buyers
# MAGIC - House loan decreases the chances of owming the cars
# MAGIC - Salary of customers are in range 50,000 to 60,000

# COMMAND ----------

# MAGIC %md
# MAGIC #### Question 8: How many owners have bought cars that were priced higher than their salary. How many of them have taken personal loan? [3 marks]

# COMMAND ----------

df3 = df[df['Price'] > df['Salary']]

print('Total owners who bought cars that were priced higher than their salary', df3.shape[0])

print('Customer who have taken personal loans', df3['Personal_loan'].value_counts()['Yes'])


# COMMAND ----------

# How much percentage of customers have car cost higher than their salary
( df3.shape[0] / df.shape[0] ) * 100

# COMMAND ----------

# Calculating percentage of personal loans taken
df3['Personal_loan'].value_counts(normalize=True) * 100

# COMMAND ----------

# MAGIC %md
# MAGIC #### Observations:
# MAGIC
# MAGIC - Only 96 customers (6%) have cars priced higher than their salary
# MAGIC - Only 44 customers out of 96 have personal loans
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Multivariate Analysis

# COMMAND ----------

# MAGIC %md
# MAGIC #### Question 9: Perform a multivariate analysis to explore relationships between the important variables in the dataset. (It is a good idea to explore relations between numerical variables as well as relations between numerical and categorical variables) [15 marks]

# COMMAND ----------

# Find correlation between all the columns which are continuous
plt.figure(figsize=(15,8))
sns.heatmap(data = df[df.columns].corr(), annot=True, cmap='YlGnBu', vmin=-1, vmax=1)
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC - Older customers tend to buy more expensive cars
# MAGIC - Both individual and household income only moderately influence car price decisions
# MAGIC - Household income is heavily influenced by partner's earnings
# MAGIC - Older customers often contribute to higher household income, possibly due to experience or addition of partner income
# MAGIC - Number of dependents doesn’t significantly affect salary or car buying decision in this data

# COMMAND ----------

# Exploring Age of target market
plt.figure(figsize=(15,5))
plt.title('Histogram:Age')
plt.xlabel('Age')
plt.ylabel('Total')
sns.histplot(data=df, x='Age', color='orange', hue='Make')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC - Impact of Age wrt personal cars:
# MAGIC   - We observe that Customer's aged below 30 have more interest in personal cars
# MAGIC   - Hatchback is the popular choice amongst yongsters aged below 30
# MAGIC   - Customers aged between 30 to 45 have comparitively low craze for cars with preference of Sedan, SUV's prefered by customer aged between 45 to 60
# MAGIC - Age is a key driver for Personal cars and choice of cars

# COMMAND ----------

plt.figure(figsize=(10,4))
plt.title('Boxplot:Salary and Profession')
plt.xlabel('Profession')
plt.ylabel('Salary')
sns.boxplot(x='Profession', y='Salary', data=df);

# COMMAND ----------

# MAGIC %md
# MAGIC - No outlier detected
# MAGIC - Salaried people have little edge over business class to own car. There is not much difference across profession though

# COMMAND ----------

plt.figure(figsize=(10,4))
plt.title('BarGraph:Car prefrence')
plt.xlabel('Make')
plt.ylabel('Total Customers');
sns.countplot(x='Make', hue='Profession', data=df, order=['Hatchback', 'Sedan', 'SUV']);

# COMMAND ----------

# MAGIC %md
# MAGIC - In every car model type, salaried customers owns more cars than Business person 

# COMMAND ----------

plt.figure(figsize=(10,4))
plt.title('Boxplot: TotalSalary vs Make')
plt.xlabel('Make of Car')
plt.ylabel('Total Salary')
sns.boxplot(x='Make', y='Total_salary', data=df, hue='Make', order=['Hatchback', 'Sedan', 'SUV']);

# COMMAND ----------

# MAGIC %md
# MAGIC - Mean of SUV is higher than Sedan and Hatchback and the IQR width is also widder.
# MAGIC   - Higher the Family income, drives higher chances of owning luxury cars
# MAGIC   - Hashback is most affordable choice for low income households

# COMMAND ----------

plt.figure(figsize=(10,4))
plt.title('Car Price by Number of Dependents')
plt.xlabel('No of Dependents')
plt.ylabel('Price');
sns.boxplot(x='No_of_Dependents', y='Price', data=df);

# COMMAND ----------

# MAGIC %md
# MAGIC - Mean of Price based on No_Of_Dependents is higher in case no of depedents are 1 or 2
# MAGIC   - Wider IQR, they buy both entry and premium models
# MAGIC   - Fewer dependents may mean early career individuals with budget constraints
# MAGIC   - Even people with 0 or 4 dependents sometimes buy high-end cars (50k+), but they are exceptions

# COMMAND ----------

# ViolinPlot: House_loan and Salary distribution wrt no_of_dependents in family
sns.catplot(x='House_loan', y='Salary', col='No_of_Dependents',
            data=df, col_wrap=2, kind='violin',
            height=4, aspect=1);

# COMMAND ----------

# MAGIC %md
# MAGIC - Salary distribution remains stable across both loan status and number of dependents, so these features may not independently drive income level or loan decisions that much

# COMMAND ----------

plt.figure(figsize=(10,5))
plt.title('ScatterPlot: Salary vs Price wrt Age')
plt.xlabel('Salary')
plt.ylabel('Price of car')
sns.scatterplot(x='Salary', y='Price', data=df, hue='Age');
plt.legend(title='Age', bbox_to_anchor=(1.02, 1));

# COMMAND ----------

# MAGIC %md
# MAGIC - Higher the age, higher the chnaces of owning luxury car
# MAGIC - More experienced the customer, more chances of having higher salary and luxury car

# COMMAND ----------

plt.figure(figsize=(10,5))
plt.title('ScatterPlot: Salary vs Price wrt Make')
plt.xlabel('Salary')
plt.ylabel('Price of car')
sns.scatterplot(x='Salary', y='Price', data=df, hue='Make');
plt.legend(title='Make', bbox_to_anchor=(1.02, 1));

# COMMAND ----------

# MAGIC %md
# MAGIC - Hatchback is affordable and preferred choice irrepective of salary
# MAGIC - SUV's are premimum and expensive choice with target consumer belonging to higher income class
# MAGIC - Sedan is again a 2nd popular choice with all salary class people with a higher price range

# COMMAND ----------

plt.figure(figsize=(10,5))
plt.title('ScatterPlot: TotalSalary vs Price wrt PartnerSalary')
plt.xlabel('Total Salary')
plt.ylabel('Price of car')
sns.scatterplot(x='Total_salary', y='Price', data=df, hue='Partner_salary');
plt.legend(title='Partner_salary', bbox_to_anchor=(1.02, 1));

# COMMAND ----------

# MAGIC %md
# MAGIC - Partner_Salary influences the total salary of household and more chances of owning luxury cars

# COMMAND ----------

plt.figure(figsize=(10,5))
plt.title('ScatterPlot: TotalSalary vs PartnerSalary')
plt.ylabel('Total Salary')
plt.xlabel('Partner Salary')
sns.scatterplot( x='Partner_salary', y='Total_salary', data=df);

# COMMAND ----------

# MAGIC %md
# MAGIC - As partner salary increases, total salary increases indicating high income household and probably higher chances of affording car

# COMMAND ----------

# MAGIC %md
# MAGIC #### Question 10:For customers who have 3 or fewer dependents, how does the average car price vary by profession ? [2 marks]

# COMMAND ----------

filtered_df = df[df['No_of_Dependents'] <= 3]
avg_price_df = filtered_df.groupby('Profession')['Price'].mean().reset_index()

plt.figure(figsize=(10,5))
plt.title('Average Price of Car by Profession for Customers with 3 or less dependents')
sns.barplot(x='Profession', y='Price', data=avg_price_df, order=['Salaried', 'Business']);

# COMMAND ----------

# MAGIC %md
# MAGIC #### Observations:
# MAGIC
# MAGIC - Salaried customers spend more on average than business customers when they have 3 or fewer dependents
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #### Question 11: For customers who have availed a home loan and a personal loan, how does the price vary by profession? [3 marks]

# COMMAND ----------

filtered_df2 = df [ (df['House_loan'] == 'Yes') & (df['Personal_loan'] == 'Yes') ]
avg_price_df2 = filtered_df2.groupby('Profession')['Price'].mean().reset_index()

plt.figure(figsize=(10,5))
plt.title('Price of Car by Profession for Customers with Home loan and personal loan')
sns.barplot(x='Profession', y = 'Price', data=avg_price_df2, order=['Salaried', 'Business'])

# COMMAND ----------

# MAGIC %md
# MAGIC #### Observations:
# MAGIC
# MAGIC - Salaried professionals spend more, as they have cars priced higher than Business professionals on average
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Conclusion and Recommendations

# COMMAND ----------

# MAGIC %md
# MAGIC #### **Question 12:** Write the conclusions and business recommendations derived from the analysis. (6 marks)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Conclusion**
# MAGIC - The majority of car buyers are young (22–30 years old), married, and predominantly male
# MAGIC - Hatchbacks are the most preferred car type, followed by Sedans and then SUVs
# MAGIC - Customers with 1 to 3 dependents are more likely to purchase higher-priced cars
# MAGIC - Salaried professionals own more cars and spend more on average compared to business owners, same for more educated people the chances of owning car is high
# MAGIC - Partner income is often zero, but when present, it contributes to higher total income and increases the chance of owning higher-priced vehicles like SUVs
# MAGIC - House loans slightly reduce the likelihood of car ownership; personal loans have almost no effect
# MAGIC - Cars are most commonly priced between ₹25,000 to ₹45,000, indicating strong demand for mid-range, affordable vehicles
# MAGIC
# MAGIC **Business Recommendation**
# MAGIC - Austo should target young, salaried, married customers with 1 to 3 dependents, as they represent the most active car-buying segment
# MAGIC - The company should prioritize production and promotion of hatchbacks and mid-range sedans to meet current demand trends
# MAGIC - Car models should be priced and financed to fall within the ₹25,000–₹45,000 range to maximize sales conversion in the mass market
# MAGIC - Marketing efforts should be segmented based on household income and education levels, focusing on aspirational value for postgraduate, mid-income families
# MAGIC - Austo should not heavily rely on personal loan tie-ins, but rather offer flexible pricing and bundled offers that appeal regardless of loan status

# COMMAND ----------

# MAGIC %md
# MAGIC ___