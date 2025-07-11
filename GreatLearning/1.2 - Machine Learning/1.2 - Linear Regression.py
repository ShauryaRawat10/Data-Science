# Databricks notebook source
# MAGIC %md
# MAGIC <center><font size=8>Hands-on - Linear Regression</font></center>

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Problem Statement**

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Business Context**

# COMMAND ----------

# MAGIC %md
# MAGIC In the dynamic and competitive market of mobiles and tablets, retailers need to be aware of market trends and adapt to changing consumer preferences and technological advancements. They also need to efficiently manage inventory and marketing strategies to attract new customers and retain existing ones, ensuring sustained growth and profitability.
# MAGIC
# MAGIC A renowned online retailer faces the challenge of managing inventory and managing marketing expenditures. To address these challenges, the retailer aims to accurately forecast sales to make informed decisions regarding inventory management and resource allocation. In addition, they also want to identify key levers influencing sales to strategically focus on areas that can drive growth.  The end goal is to minimize stockouts and overstock situations and enhance sales performance to gain a competitive advantage.

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Objectives**

# COMMAND ----------

# MAGIC %md
# MAGIC As a data scientist, you are provided with sales data from the recent past along with other attributes like pricing strategies, promotional activities, and customer engagement. You are required to analyze the data, identify patterns, build a linear regression model to forecast sales, and identify factors contributing to changes in sales.

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Data Dictionary**

# COMMAND ----------

# MAGIC %md
# MAGIC 1. Advertising Expenditure: Amount spent on advertisements (in dollars) across different marketing channels
# MAGIC 2. Campaign Engagement Score: A score computed by the marketing team based on the engagement (likes, comments, shares) on social media campaigns
# MAGIC 3. Discount Percentage: Average discount offered for a given product
# MAGIC 4. Average Customer Rating: Average rating provided by customers for the product
# MAGIC 5. Product Price: The price of the product (in dollars)
# MAGIC 6. Return Rate: The average rate of return once the product has been delivered
# MAGIC 7. Length of Product Description: Number of words in the description of the product
# MAGIC 8. Region: Region where the product is sold (North, South, East, or West)
# MAGIC 9. Popularity: The level of popularity of the product (ranges from very low to very high)
# MAGIC 10. Sales: Amount of sales (in dollars)

# COMMAND ----------

# MAGIC %md
# MAGIC **Note**: Product here refers to a mobile or a tablet.

# COMMAND ----------

# MAGIC %md
# MAGIC # **Importing the necessary libraries**

# COMMAND ----------

# to load and manipulate data
import pandas as pd
import numpy as np

# to visualize data
import matplotlib.pyplot as plt
import seaborn as sns

# to split the data into train and test sets
from sklearn.model_selection import train_test_split

# to build a linear regression model
from sklearn.linear_model import LinearRegression

# to check a regression model's performance
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# COMMAND ----------

# MAGIC %md
# MAGIC # **Loading the data**

# COMMAND ----------

# uncomment and run the following line if using Google Colab
# from google.colab import drive
# drive.mount('/content/drive')

# COMMAND ----------

# loading data into a pandas dataframe
import os
file_path = os.path.abspath('Storage/Sales.csv')
sales = pd.read_csv(file_path, on_bad_lines='skip')


# COMMAND ----------

# creating a copy of the data
data = sales.copy()

# COMMAND ----------

# MAGIC %md
# MAGIC # **Data Overview**

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Checking the first 5 rows**

# COMMAND ----------

data.head(5)

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Checking the shape of the data**
# MAGIC
# MAGIC

# COMMAND ----------

data.shape

# COMMAND ----------

# MAGIC %md
# MAGIC * The dataset has 3000 rows and 10 columns.

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Checking the attribute types**

# COMMAND ----------

data.info()

# COMMAND ----------

# MAGIC %md
# MAGIC * There are 8 numerical and 2 categorical variables in the data.

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Checking the statistical summary**

# COMMAND ----------

data.describe()

# COMMAND ----------

# MAGIC %md
# MAGIC * On an average, the retailer has sold mobiles and tablets worth ~$24k.
# MAGIC * On an average, ~600 dollars have been spent on adversiting.
# MAGIC * The mobiles and tablets sold by the retailer are priced between 10 to 2000 dollars approx.

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Checking for missing values**

# COMMAND ----------

data.isnull().sum()

# COMMAND ----------

# MAGIC %md
# MAGIC * There are no missing values in the data

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Checking for duplicate values**

# COMMAND ----------

# checking for duplicate values
data.duplicated().sum()

# COMMAND ----------

# MAGIC %md
# MAGIC * There are no duplicate values in the data

# COMMAND ----------

# MAGIC %md
# MAGIC # **Exploratory Data Analysis**

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Univariate Analysis**

# COMMAND ----------

# defining the figure size
plt.figure(figsize=(15, 10))

# defining the list of numerical features to plot
features = data.select_dtypes(include=['number']).columns.tolist()

# creating the histograms
for i, feature in enumerate(features):
    plt.subplot(3, 3, i+1)    # assign a subplot in the main plot
    sns.histplot(data=data, x=feature)    # plot the histogram

plt.tight_layout()    # to add spacing between plots
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * Sales, Advertising Expenditure, Discount Percentage, and Product Price exhibit left-skewed distributions.
# MAGIC * Return Rate exhibits a right-skewed distribution.
# MAGIC * Campaign Engagement Score and Length of Product Description are approx. normally distributed.

# COMMAND ----------

# defining the figure size
plt.figure(figsize=(15, 10))

# defining the list of numerical features to plot
features = data.select_dtypes(include=['number']).columns.tolist()

# creating the histograms
for i, feature in enumerate(features):
    plt.subplot(3, 3, i+1)    # assign a subplot in the main plot
    sns.boxplot(data=data, x=feature)    # plot the histogram

plt.tight_layout()    # to add spacing between plots
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * There are outliers in all the attributes in the data.

# COMMAND ----------

# defining the figure size
plt.figure(figsize=(10, 5))

# defining the list of categorical features to plot
features = data.select_dtypes(exclude=['number']).columns.tolist()

# creating the histograms
for i, feature in enumerate(features):
    plt.subplot(1, 2, i+1)    # assign a subplot in the main plot
    sns.countplot(data=data, x=feature)    # plot the histogram

plt.tight_layout()    # to add spacing between plots
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC * The North region has slightly fewer data points than the others.
# MAGIC * Most of the mobiles and tablets sold are very popular, and only a negligible amount of them are very unpopular.

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Bivariate Analysis**

# COMMAND ----------

sns.pairplot(data);

# COMMAND ----------

# MAGIC %md
# MAGIC - Sales seem to be positively correlated with Advertising Expenditure, Campaign Engagement Score, and Average Customer Rating.
# MAGIC - Sales seem to be negatively correlated with Product Price and Return Rate.

# COMMAND ----------

# defining the figure size
plt.figure(figsize=(10, 7))

# plotting the correlation heatmap
sns.heatmap(data.corr(numeric_only = True), annot=True, fmt='0.2f', cmap='coolwarm');

# COMMAND ----------

# MAGIC %md
# MAGIC - Sales is indeed highly positively correlated with Advertising Expenditure.
# MAGIC - Sales are indeed negatively correlated with Product Price and Return Rate, but the strength of the correlation is low.
# MAGIC - Advertising Expenditure and Campaign Engagement Score are positively correlated.
# MAGIC - Return Rate and Average Customer Rating are negatively correlated.

# COMMAND ----------

# MAGIC %md
# MAGIC for categrical, we cant have correlation, so use box plot maybe

# COMMAND ----------

sns.boxplot(data=data, y='Sales', x='Popularity');

# COMMAND ----------

# MAGIC %md
# MAGIC * We observe lower sales for unpopular products.

# COMMAND ----------

sns.boxplot(data=data, y='Sales', x='Region');

# COMMAND ----------

# MAGIC %md
# MAGIC * Sales seem to be uniform across different regions.

# COMMAND ----------

# MAGIC %md
# MAGIC # **Data Preparation for Modeling**

# COMMAND ----------

# defining the explanatory (independent) and response (dependent) variables
X = data.drop('Sales', axis=1)
y = data['Sales']

# COMMAND ----------

# splitting the data in 80:20 ratio for train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X,    # specifying the independent variables
    y,    # specifying the dependent variable
    test_size=0.20,    # specifying the size of the test set as a fraction of the whole data
    random_state=42    # specifying a seed value to enable reproducible results
)

# COMMAND ----------

Random state parameter: In sklearn, it controls the randomness of certain functions and methods. It ensures the reproductibility of the results by ensuring that the same random numbers are generated each time the code has same same split of data

# COMMAND ----------

# MAGIC %md
# MAGIC # **Model Building**

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Simple Linear Regression - `Sales` vs `Advertising Expenditure`**

# COMMAND ----------

# defining the independent variable
ind_vars1 = ['Advertising Expenditure']

# COMMAND ----------

# creating an instance of the linear regression model
lin_reg1 = LinearRegression()

# fitting the model to the training data
lin_reg1.fit(X_train[ind_vars1], y_train)

# COMMAND ----------

# MAGIC %md
# MAGIC In above, the lin_reg1 has been fitted, in other worlds it has coefficient. this is called method chaining

# COMMAND ----------

# printing the linear regression coefficients
print(
    "Slope:", lin_reg1.coef_,
    "Intercept:", lin_reg1.intercept_,
)

# COMMAND ----------

# printing the linear regression equation
print(
    "Sales =",
     "(", lin_reg1.coef_[0], ")", "*", ind_vars1[0],
    "+", lin_reg1.intercept_,
)

# COMMAND ----------

# MAGIC %md
# MAGIC One unit increase in Advertizing expenditure, will result in 28.7 unit increase in sales

# COMMAND ----------

# plotting the best-fit line
fitted_values1 = lin_reg1.predict(X_train[ind_vars1])

# Plot the scatterplot and regression line
plt.scatter(X_train[ind_vars1], y_train)
plt.plot(X_train[ind_vars1], fitted_values1, color='blue')
plt.xlabel(ind_vars1[0])
plt.ylabel('Sales')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Simple Linear Regression - `Sales` vs `Discount Percentage`**

# COMMAND ----------

# defining the independent variable
ind_vars2 = ['Discount Percentage']

# COMMAND ----------

# creating an instance of the linear regression model
lin_reg2 = LinearRegression()

# fitting the model to the training data
lin_reg2.fit(X_train[ind_vars2], y_train)

# COMMAND ----------

# printing the linear regression coefficients
print(
    "Slope:", lin_reg2.coef_,
    "Intercept:", lin_reg2.intercept_,
)

# COMMAND ----------

# printing the linear regression equation
print(
    "Sales =",
    "(", lin_reg2.coef_[0], ")", "*", ind_vars2[0],
    "+", lin_reg2.intercept_,
)

# COMMAND ----------

# plotting the best-fit line
fitted_values2 = lin_reg2.predict(X_train[ind_vars2])

# Plot the scatterplot and regression line
plt.scatter(X_train[ind_vars2], y_train)
plt.plot(X_train[ind_vars2], fitted_values2, color='blue')
plt.xlabel(ind_vars2[0])
plt.ylabel('Sales')
plt.show()

# COMMAND ----------

Does not look as good. We need to deep dive on statistical equation on how much sense it makes. 

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Simple Linear Regression - `Sales` vs `Product Price`**

# COMMAND ----------

# defining the independent variable
ind_vars3 = ['Product Price']

# COMMAND ----------

# creating an instance of the linear regression model
lin_reg3 = LinearRegression()

# fitting the model to the training data
lin_reg3.fit(X_train[ind_vars3], y_train)

# COMMAND ----------

# printing the linear regression coefficients
print(
    "Slope:", lin_reg3.coef_,
    "Intercept:", lin_reg3.intercept_,
)

# COMMAND ----------

# printing the linear regression equation
print(
    "Sales =",
    "(", lin_reg3.coef_[0], ")", "*", ind_vars3[0],
    "+", lin_reg3.intercept_,
)

# COMMAND ----------

# plotting the best-fit line
fitted_values3 = lin_reg3.predict(X_train[ind_vars3])

# Plot the scatterplot and regression line
plt.scatter(X_train[ind_vars3], y_train)
plt.plot(X_train[ind_vars3], fitted_values3, color='blue')
plt.xlabel(ind_vars3[0])
plt.ylabel('Sales')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Multiple Linear Regression - `Sales` vs `Advertising Expenditure`, `Discount Percentage`**

# COMMAND ----------

# defining the independent variables
ind_vars4 = ['Advertising Expenditure', 'Discount Percentage']

# COMMAND ----------

# creating an instance of the linear regression model
lin_reg4 = LinearRegression()

# fitting the model to the training data
lin_reg4.fit(X_train[ind_vars4], y_train)

# COMMAND ----------

# printing the linear regression coefficients
print(
    "Coefficients:", lin_reg4.coef_, lin_reg4.intercept_
)

# COMMAND ----------

# printing the linear regression equation
print(
    "Sales =",
    "(", lin_reg4.coef_[0], ")", "*", ind_vars4[0],
    "+ (", lin_reg4.coef_[1], ")", "*", ind_vars4[1],
    "+", lin_reg4.intercept_,
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Multiple Linear Regression - `Sales` vs `Advertising Expenditure`, `Discount Percentage`, `Product Price`**

# COMMAND ----------

# defining the independent variables
ind_vars5 = ['Advertising Expenditure', 'Discount Percentage', 'Product Price']

# COMMAND ----------

# creating an instance of the linear regression model
lin_reg5 = LinearRegression()

# fitting the model to the training data
lin_reg5.fit(X_train[ind_vars5], y_train)

# COMMAND ----------

# printing the linear regression coefficients
print(
    "Coefficients:", lin_reg5.coef_, lin_reg5.intercept_
)

# COMMAND ----------

# printing the linear regression equation
print(
    "Sales =",
    "(", lin_reg5.coef_[0], ")", "*", ind_vars5[0],
    "+ (", lin_reg5.coef_[1], ")", "*", ind_vars5[1],
    "+ (", lin_reg5.coef_[2], ")", "*", ind_vars5[2],
    "+", lin_reg5.intercept_,
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Multiple Linear Regression - `Sales` vs `Advertising Expenditure`, `Discount Percentage`, `Product Price`, `Popularity`**

# COMMAND ----------

# MAGIC %md
# MAGIC We first need to label encode the `Popularity` column.

# COMMAND ----------

# defining the label encoding
lab_enc = {
    'Very Low': 1,
    'Low': 2,
    'Moderate': 3,
    'High': 4,
    'Very High': 5,
}

# COMMAND ----------

# encoding the Popularity column
X['Popularity'] = X['Popularity'].map(
    lambda x: lab_enc[x]
)

X.head()

# COMMAND ----------

# splitting the data in 80:20 ratio for train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X,    # specifying the independent variables
    y,    # specifying the dependent variable
    test_size=0.20,    # specifying the size of the test set as a fraction of the whole data
    random_state=42    # specifying a seed value to enable reproducible results
)

# COMMAND ----------

# defining the independent variables
ind_vars6 = ['Advertising Expenditure', 'Discount Percentage', 'Product Price', 'Popularity']

# COMMAND ----------

# creating an instance of the linear regression model
lin_reg6 = LinearRegression()

# fitting the model to the training data
lin_reg6.fit(X_train[ind_vars6], y_train)

# COMMAND ----------

# printing the linear regression coefficients
print(
    "Coefficients:", lin_reg6.coef_, lin_reg6.intercept_
)

# COMMAND ----------

# printing the linear regression equation
print(
    "Sales =",
    "(", lin_reg6.coef_[0], ")", "*", ind_vars6[0],
    "+ (", lin_reg6.coef_[1], ")", "*", ind_vars6[1],
    "+ (", lin_reg6.coef_[2], ")", "*", ind_vars6[2],
    "+ (", lin_reg6.coef_[3], ")", "*", ind_vars6[3],
    "+", lin_reg6.intercept_,
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Multiple Linear Regression - `Sales` vs All independent variables**

# COMMAND ----------

# MAGIC %md
# MAGIC We first need to one-hot encode the `Region` column.

# COMMAND ----------

# creating one-hot encoded (also called dummy) variables
X = pd.get_dummies(
    X,    # defining the dataframe from where to fetch the data
    columns=X.select_dtypes(include=["object", "category"]).columns.tolist(),    # defining the type of columns for which dummies will be made
    drop_first=True,    # dropping the first dummy column
)

# specifying the datatype of the independent variables dataframe
X = X.astype(float)

X.head()

# COMMAND ----------

# MAGIC %md
# MAGIC * Note that the dummy variable corresponding to the '*East*' category has been dropped.

# COMMAND ----------

# splitting the data in 80:20 ratio for train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X,    # specifying the independent variables
    y,    # specifying the dependent variable
    test_size=0.20,    # specifying the size of the test set as a fraction of the whole data
    random_state=42    # specifying a seed value to enable reproducible results
)

# COMMAND ----------

# creating an instance of the linear regression model
lin_reg7 = LinearRegression()

# fitting the model to the training data
lin_reg7.fit(X_train, y_train)

# COMMAND ----------

# printing the linear regression coefficients
print(
    "Coefficients:", lin_reg7.coef_, lin_reg7.intercept_
)

# COMMAND ----------

# printing the linear regression equation
equation = "Sales = ( " + str(lin_reg7.coef_[0]) + " ) * " + X_train.columns.tolist()[0]

for i in range(1, lin_reg7.coef_.shape[0]):
    equation += " + ( " + str(lin_reg7.coef_[i]) + " ) * " + X_train.columns.tolist()[i]

equation +=  " + " + str(lin_reg7.intercept_)

print(equation)

# COMMAND ----------

# MAGIC %md
# MAGIC # **Model Performance Evaluation**

# COMMAND ----------

# MAGIC %md
# MAGIC We first define a set of utility functions to compute MAPE and Adjusted $R^2$, and another one to collate all the metrics into a single dataframe.

# COMMAND ----------

# function to compute MAPE
def mape_score(targets, predictions):
    return np.mean(np.abs(targets - predictions) / targets) * 100

# function to compute adjusted R-squared
def adj_r2_score(predictors, targets, predictions):
    r2 = r2_score(targets, predictions)
    n = predictors.shape[0]
    k = predictors.shape[1]
    return 1 - ((1 - r2) * (n - 1) / (n - k - 1))

# function to compute different metrics to check performance of a regression model
def model_performance_regression(model, predictors, target):
    """
    Function to compute different metrics to check regression model performance

    model: regression model
    predictors: independent variables
    target: dependent variable
    """

    # predicting using the independent variables
    pred = model.predict(predictors)

    rmse = np.sqrt(mean_squared_error(target, pred))  # to compute RMSE
    mae = mean_absolute_error(target, pred)  # to compute MAE
    mape = mape_score(target, pred)  # to compute MAPE
    r2 = r2_score(target, pred)  # to compute R-squared
    adj_r2 = adj_r2_score(predictors, target, pred)  # to compute Adjusted R-squared

    # creating a dataframe of metrics
    df_perf = pd.DataFrame(
        {
            "RMSE": rmse,
            "MAE": mae,
            "MAPE": mape,
            "R-squared": r2,
            "Adj R-squared": adj_r2,
        },
        index=[0],
    )

    return df_perf

# COMMAND ----------

# MAGIC %md
# MAGIC We'll now check the performance of all the models we've built so far.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Simple Linear Regression - `Sales` vs `Advertising Expenditure`**

# COMMAND ----------

lin_reg1_train_perf = model_performance_regression(lin_reg1, X_train[ind_vars1], y_train)
lin_reg1_train_perf

# COMMAND ----------

lin_reg1_test_perf = model_performance_regression(lin_reg1, X_test[ind_vars1], y_test)
lin_reg1_test_perf

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Simple Linear Regression - `Sales` vs `Discount Percentage`**

# COMMAND ----------

lin_reg2_train_perf = model_performance_regression(lin_reg2, X_train[ind_vars2], y_train)
lin_reg2_train_perf

# COMMAND ----------

lin_reg2_test_perf = model_performance_regression(lin_reg2, X_test[ind_vars2], y_test)
lin_reg2_test_perf

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Simple Linear Regression - `Sales` vs `Product Price`**

# COMMAND ----------

lin_reg3_train_perf = model_performance_regression(lin_reg3, X_train[ind_vars3], y_train)
lin_reg3_train_perf

# COMMAND ----------

lin_reg3_test_perf = model_performance_regression(lin_reg3, X_test[ind_vars3], y_test)
lin_reg3_test_perf

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Multiple Linear Regression - `Sales` vs `Advertising Expenditure`, `Discount Percentage`**

# COMMAND ----------

lin_reg4_train_perf = model_performance_regression(lin_reg4, X_train[ind_vars4], y_train)
lin_reg4_train_perf

# COMMAND ----------

lin_reg4_test_perf = model_performance_regression(lin_reg4, X_test[ind_vars4], y_test)
lin_reg4_test_perf

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Multiple Linear Regression - `Sales` vs `Advertising Expenditure`, `Discount Percentage`, `Product Price`**

# COMMAND ----------

lin_reg5_train_perf = model_performance_regression(lin_reg5, X_train[ind_vars5], y_train)
lin_reg5_train_perf

# COMMAND ----------

lin_reg5_test_perf = model_performance_regression(lin_reg5, X_test[ind_vars5], y_test)
lin_reg5_test_perf

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Multiple Linear Regression - `Sales` vs `Advertising Expenditure`, `Discount Percentage`, `Product Price`, `Popularity`**

# COMMAND ----------

lin_reg6_train_perf = model_performance_regression(lin_reg6, X_train[ind_vars6], y_train)
lin_reg6_train_perf

# COMMAND ----------

lin_reg6_test_perf = model_performance_regression(lin_reg6, X_test[ind_vars6], y_test)
lin_reg6_test_perf

# COMMAND ----------

# MAGIC %md
# MAGIC ## **Multiple Linear Regression - `Sales` vs All independent variables**

# COMMAND ----------

lin_reg7_train_perf = model_performance_regression(lin_reg7, X_train, y_train)
lin_reg7_train_perf

# COMMAND ----------

lin_reg7_test_perf = model_performance_regression(lin_reg7, X_test, y_test)
lin_reg7_test_perf

# COMMAND ----------

# MAGIC %md
# MAGIC # **Model Performance Comparison**

# COMMAND ----------

# MAGIC %md
# MAGIC We'll now compare the performances of all the models we built.

# COMMAND ----------

# training performance comparison

# concatenating all the training performance dataframes
models_train_comp_df = pd.concat(
    [
        lin_reg1_train_perf.T,
        lin_reg2_train_perf.T,
        lin_reg3_train_perf.T,
        lin_reg4_train_perf.T,
        lin_reg5_train_perf.T,
        lin_reg6_train_perf.T,
        lin_reg7_train_perf.T,
    ],
    axis=1,
)

# defining the list of models built
models_train_comp_df.columns = [
    "Simple Linear Regression - Sales vs Advertising Expenditure",
    "Simple Linear Regression - Sales vs Discount Percentage",
    "Simple Linear Regression - Sales vs Product Price",
    "Multiple Linear Regression - Sales vs Advertising Expenditure, Discount Percentage",
    "Multiple Linear Regression - Sales vs Advertising Expenditure, Discount Percentage, Product Price",
    "Multiple Linear Regression - Sales vs Advertising Expenditure, Discount Percentage, Product Price, Popularity",
    "Multiple Linear Regression - Sales vs All independent variables",
]

print("Training performance comparison:")
models_train_comp_df.T

# COMMAND ----------

# test performance comparison

# concatenating all the test performance dataframes
models_test_comp_df = pd.concat(
    [
        lin_reg1_test_perf.T,
        lin_reg2_test_perf.T,
        lin_reg3_test_perf.T,
        lin_reg4_test_perf.T,
        lin_reg5_test_perf.T,
        lin_reg6_test_perf.T,
        lin_reg7_test_perf.T,
    ],
    axis=1,
)

# defining the list of models built
models_test_comp_df.columns = [
    "Simple Linear Regression - Sales vs Advertising Expenditure",
    "Simple Linear Regression - Sales vs Discount Percentage",
    "Simple Linear Regression - Sales vs Product Price",
    "Multiple Linear Regression - Sales vs Advertising Expenditure, Discount Percentage",
    "Multiple Linear Regression - Sales vs Advertising Expenditure, Discount Percentage, Product Price",
    "Multiple Linear Regression - Sales vs Advertising Expenditure, Discount Percentage, Product Price, Popularity",
    "Multiple Linear Regression - Sales vs All independent variables",
]

print("Test performance comparison:")
models_test_comp_df.T

# COMMAND ----------

# MAGIC %md
# MAGIC * Advertising Expenditure seems to be a good predictor of Sales.
# MAGIC * Discount Percentage and Product Price are individually poor predictors of Sales. But when combined with Advertising Expenditure, they together provide good predictive power.
# MAGIC * The final model with all independent variables exhibits the best performance.

# COMMAND ----------

# MAGIC %md
# MAGIC <font size=6 color='blue'>Power Ahead</font>
# MAGIC ___