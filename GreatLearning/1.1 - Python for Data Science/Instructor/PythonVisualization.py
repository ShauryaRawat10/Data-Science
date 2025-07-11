# Databricks notebook source
# MAGIC %md
# MAGIC # Data Visualization with Python

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Loading and Overview

# COMMAND ----------

# from google.colab import drive
# drive.mount('/content/drive')

# COMMAND ----------

# Libraries to help with reading and manipulating data
import numpy as np
import pandas as pd

# Libraries to help with data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Command to tell Python to actually display the graphs
%matplotlib inline

# COMMAND ----------

df = pd.read_csv('Automobile.csv')
# df = pd.read_csv('/location on your computer/Automobile (1).csv')

# COMMAND ----------

df.head()

# COMMAND ----------

df.shape

# COMMAND ----------

# MAGIC %md
# MAGIC - The data has 201 rows and 26 columns.

# COMMAND ----------

df.info()

# COMMAND ----------

# MAGIC %md
# MAGIC - There are attributes of different types (*int*, *float*, *object*) in the data.

# COMMAND ----------

df.describe(include='all').T

# COMMAND ----------

# MAGIC %md
# MAGIC - The car price ranges from 5118 to 45400 units.
# MAGIC - The car weight ranges from 1488 to 4066 units.
# MAGIC - The most common car make in the data is of Toyota.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Histogram
# MAGIC
# MAGIC - A **histogram** is a univariate plot which helps us understand the distribution of a continuous numerical variable.
# MAGIC - It breaks the range of the continuous variables into a intervals of equal length and then counts the number of observations in each interval.
# MAGIC - We will use the *histplot()* function of seaborn to create histograms.

# COMMAND ----------

sns.histplot(data=df, x='price')

# COMMAND ----------

# MAGIC %md
# MAGIC **Let's see how we can customize a histogram.**

# COMMAND ----------

plt.title('Histogram:Price')
plt.xlim(3000,50000)
plt.ylim(0,70)
plt.xlabel('Price of cars')
plt.ylabel('Frequency')
sns.histplot(data=df, x='price',color='orange');

# COMMAND ----------

# MAGIC %md
# MAGIC **We can specify the number of intervals (or groups or bins) to create by setting the *bins* parameter.**
# MAGIC
# MAGIC - If not specified it is passed to [numpy.histogram_bin_edges()](https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html#numpy.histogram_bin_edges)

# COMMAND ----------

sns.histplot(data=df, x='price', bins=5)

# COMMAND ----------

sns.histplot(data=df, x='price', bins=20)

# COMMAND ----------

# MAGIC %md
# MAGIC **If we want to specify the width of the intervals (or groups or bins), we can use *binwidth* parameter.**

# COMMAND ----------

sns.histplot(data=df, x='price', binwidth=20)

# COMMAND ----------

sns.histplot(data=df, x='price', binwidth=200)

# COMMAND ----------

# MAGIC %md
# MAGIC **How to find the optimal number of bins: Rule of thumb**
# MAGIC
# MAGIC - We calculate the bin-width first, using the following formula: $$ binwidth =\frac{(2 * IQR)}{\sqrt[3]{n}} $$ where n = number of rows the dataset
# MAGIC
# MAGIC - Then, we obtain bins using the calculated bin-width. $$ bins =\frac{Range}{binwidth} $$

# COMMAND ----------

# MAGIC %md
# MAGIC **In addition to the bars, we can also add a density estimate by setting the *kde* parameter to *True*.**
# MAGIC
# MAGIC - **Kernel Density Estimation**, or **KDE**, visualizes the distribution of data over a continuous interval.
# MAGIC - The conventional scale for KDE is: **Total frequency of each bin × Probability**

# COMMAND ----------

sns.histplot(data=df, x='price', kde=True);

# COMMAND ----------

sns.histplot(data=df, x='price', bins=700, kde=True);

# COMMAND ----------

# MAGIC %md
# MAGIC Clearly, if we increase the number of bins, it reduces the frequency count in each group (bin). Since the scale of KDE depends on the total frequency of each bin (group), the above code gives us a flattened KDE plot.

# COMMAND ----------

# MAGIC %md
# MAGIC **Let's check out the histograms for a few more attributes in the data.**

# COMMAND ----------

sns.histplot(data=df, x='curb_weight', kde=True);

# COMMAND ----------

# MAGIC %md
# MAGIC - A histogram is said to be **symmetric** if the left-hand and right-hand sides resemble mirror images of each other when the histogram is cut down the middle.

# COMMAND ----------

sns.histplot(data=df, x='horsepower', kde=True);

# COMMAND ----------

# MAGIC %md
# MAGIC - The tallest clusters of bars, i.e., peaks, in a histogram represent the **modes** of the data.
# MAGIC - A histogram **skewed to the right** has a large number of occurrences on the left side of the plot and a few on the right side of the plot.
# MAGIC - Similarly, a histogram **skewed to the left** has a large number of occurrences on the right side of the plot and few on the left side of the plot.

# COMMAND ----------

# MAGIC %md
# MAGIC **Histograms are intuitive but it is hardly a good choice when we want to compare the distributions of several groups. For example,**

# COMMAND ----------

sns.histplot(data=df, x='price', hue='body_style', kde=True);

# COMMAND ----------

# MAGIC %md
# MAGIC It might be better to use subplots!

# COMMAND ----------

g = sns.FacetGrid(df, col="body_style")
g.map(sns.histplot, "price");

# COMMAND ----------

# MAGIC %md
# MAGIC In such cases, we can use **boxplots**. Boxplots, or box-and-whiskers plots, are an excellent way to visualize differences among groups.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Boxplot
# MAGIC
# MAGIC - A **boxplot**, or a **box-and-whisker plot**, shows the distribution of numerical data and skewness through displaying the data quartiles
# MAGIC - It is also called a **five-number summary plot**, where the five-number summary includes the minimum value, first quartile, median, third quartile, and the maximum value.
# MAGIC - The *boxplot()* function of seaborn can be used to create a boxplot.

# COMMAND ----------

from IPython.display import Image
Image('/content/drive/MyDrive/Python Course/boxplot.png')
#Image('/location on your computer/boxplot.png')

# COMMAND ----------

# creating a boxplot with seaborn
sns.boxplot(data=df, x='curb_weight');

# COMMAND ----------

# MAGIC %md
# MAGIC **Let's see how we can customize a boxplot.**

# COMMAND ----------

plt.title('Boxplot:Horsepower')
plt.xlim(30,300)
plt.xlabel('Horsepower')
sns.axes_style('whitegrid')
sns.boxplot(data=df, x='horsepower',color='green');

# COMMAND ----------

# MAGIC %md
# MAGIC - In a boxplot, when the median is closer to the left of the box and the whisker is shorter on the left end of the box, we say that the distribution is **positively skewed (skewed right)**.
# MAGIC - Similarly, when the median is closer to the right of the box and the whisker is shorter on the right end of the box, we say that the distribution is **negatively skewed (skewed left)**.

# COMMAND ----------

from IPython.display import Image
Image('/content/drive/MyDrive/skew_box.png')
#Image('/location on your computer/skew_box.png')

# COMMAND ----------

# MAGIC %md
# MAGIC **For example,**

# COMMAND ----------

sns.boxplot(data=df, x='price');

# COMMAND ----------

# MAGIC %md
# MAGIC From the above plot, we can see that the distribution of `price` is positively skewed.

# COMMAND ----------

# MAGIC %md
# MAGIC **Let's see how we can compare groups with boxplots.**

# COMMAND ----------

sns.boxplot(data=df, x='body_style', y='price') ;

# COMMAND ----------

# MAGIC %md
# MAGIC **Though boxplot visually summarizes variation in large datasets, it is unable to show multimodality and clusters.**

# COMMAND ----------

sns.boxplot(data=df, x='bore');

# COMMAND ----------

# MAGIC %md
# MAGIC - From the above boxplot we can not tell if the data is bimodal or not, but it is clearly visible in the following histogram.

# COMMAND ----------

sns.histplot(data=df, x='bore',kde = True);

# COMMAND ----------

# MAGIC %md
# MAGIC ## Bar Graph
# MAGIC
# MAGIC - A bar graph is generally used to show the counts of observations in each bin (or level or group) of categorical variable using bars.
# MAGIC - We can use the *countplot()* function of seaborn to plot a bar graph.

# COMMAND ----------

sns.countplot(data=df, x='body_style');

# COMMAND ----------

# MAGIC %md
# MAGIC **We can also make the plot more granular by specifying the *hue* parameter to display counts for subgroups.**

# COMMAND ----------

sns.countplot(data=df, x='body_style', hue='fuel_type');

# COMMAND ----------

# MAGIC %md
# MAGIC **Let's check out the bar graphs for a few more attributes in the data.**

# COMMAND ----------

sns.countplot(data=df, x='make');

# COMMAND ----------

# MAGIC %md
# MAGIC - This plot looks a little messy and congested.
# MAGIC - Let's increase the size of the plot to make it look better.

# COMMAND ----------

plt.figure(figsize=(20,7))
sns.countplot(data=df, x='make');

# COMMAND ----------

# MAGIC %md
# MAGIC - Some of the tick marks on the x-axis are overlapping with each other.
# MAGIC - Let's rotate the tick marks to make it look better.

# COMMAND ----------

plt.figure(figsize=(20,7))
sns.countplot(data=df, x='make')
plt.xticks(rotation=90)

# COMMAND ----------

# MAGIC %md
# MAGIC - A lot of plot-specific text has shown up in the output.
# MAGIC - Let's see how we can get rid of those.

# COMMAND ----------

plt.figure(figsize=(20,7))
sns.countplot(data=df, x='make')
plt.xticks(rotation=90)
plt.show() # this will ensure that the plot is displayed without the text

# COMMAND ----------

# MAGIC %md
# MAGIC **Here are some common ways to customize a barplot.**

# COMMAND ----------

plt.figure(figsize=(10,7))
plt.title('Barplot:Engine-type')
plt.ylim(0,180)
sns.countplot(data=df, x='engine_type',hue='fuel_type')
plt.xlabel('Engine-type');

# COMMAND ----------

# MAGIC %md
# MAGIC ## Lineplot
# MAGIC
# MAGIC Suppose, your dataset has multiple y values for each x value.  A lineplot is a great way to visualize this.  This type of data often shows up when we have data that evolves over time, for example, when we have monthly data over several years.  If we want to compare the individual months, then a line plot is a great option.  This is sometimes called seasonality analysis.
# MAGIC
# MAGIC

# COMMAND ----------

from IPython.display import Image
Image('/content/drive/MyDrive/Python Course/Line_plot.png')
#Image('/location on your computer/Line_plot.png')

# COMMAND ----------

# MAGIC %md
# MAGIC - A **line plot** uses straight lines to connect individual data points to display a trend or pattern in the data.
# MAGIC     - For example, seasonal effects and large changes over time.
# MAGIC
# MAGIC - The *lineplot()* function of seaborn, by default, aggregates over multiple y values at each value of x and uses an estimate of the central tendency for the plot.
# MAGIC
# MAGIC - *lineplot()* assumes that you are most often trying to draw y as a function of x. So, by default, it sorts the data by the x values before plotting.

# COMMAND ----------

# loading one of the example datasets available in seaborn
flights = sns.load_dataset("flights")

# creating a line plot
sns.lineplot(data = flights , x = 'month' , y = 'passengers');

# COMMAND ----------

# MAGIC %md
# MAGIC - The light blue shaded area is actually the '**confidence interval**' of the y-value estimates for each x-axis value.
# MAGIC
# MAGIC - The **confidence interval** is a range of values around that estimate that are believed to contain the true value of that estimate with a certain probability.

# COMMAND ----------

# MAGIC %md
# MAGIC **We can switch off the confidence intervals by setting the *ci* parameter to *'False'*.**

# COMMAND ----------

sns.lineplot(data = flights , x = 'month' , y = 'passengers', ci = False);

# COMMAND ----------

# MAGIC %md
# MAGIC **We can also check the relationship between two variables for different categories by specifying the *hue* parameter.**

# COMMAND ----------

sns.lineplot(data=flights,x = 'month' , y = 'passengers', ci = False ,hue='year');

# COMMAND ----------

# MAGIC %md
# MAGIC **We can change the style of the lines by adding 'style' parameter to the function.**

# COMMAND ----------

# loading one of the example datasets available in seaborn
fmri = sns.load_dataset("fmri")

# creating the line plot
sns.lineplot(data = fmri, x="timepoint", y="signal", hue="region", style="region", ci = False);

# COMMAND ----------

# MAGIC %md
# MAGIC **We can also add markers at each observation to identify groups in a better way.**

# COMMAND ----------

sns.lineplot(data = fmri, x="timepoint", y="signal", hue="region", style="region", ci = False, markers = True);

# COMMAND ----------

# MAGIC %md
# MAGIC **Let's customize the lineplot for a better visualization.**

# COMMAND ----------

plt.figure(figsize = (15,7))
sns.lineplot(data = flights , x = 'month' , y = 'passengers', hue = 'year')
plt.ylabel('Number of Passengers')
plt.legend(bbox_to_anchor=[1, 1]); #another way to change the legend's location in the plot

# COMMAND ----------

# MAGIC %md
# MAGIC - Note that, unlike barplots and histograms, line plots may not include a zero baseline.
# MAGIC - We create a line chart is to emphasize changes in value, rather than the magnitude of the values themselves, and hence, a zero line is not meaningful.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Scatterplot
# MAGIC
# MAGIC Sometimes we want to know if two variables mean something when put together, whether a small change in one variable affects the other variable. In such cases, plotting a **scatterplot**, or **scatter-diagram**, with our data points can help us to check whether there is a potential relationship between them.

# COMMAND ----------

# MAGIC %md
# MAGIC - A **scatterplot** is the simplest mode of a diagrammatic representation of two variables.
# MAGIC - It takes two perpendicular axes of coordinates, one for x and one for y.
# MAGIC - Unlike the lineplot, it directly plots each pair of values as a point on the 2D space.
# MAGIC - The *scatterplot()* function of seaborn can be used to make a scatterplot.

# COMMAND ----------

sns.scatterplot(data=df, x='engine_size', y='horsepower');

# COMMAND ----------

# MAGIC %md
# MAGIC **We can also check the relationship between two variables for different categories by specifying the *hue* parameter.**

# COMMAND ----------

sns.scatterplot(data=df, x='engine_size', y='horsepower', hue='fuel_type');

# COMMAND ----------

# MAGIC %md
# MAGIC **We can assign the same variable as *hue* to another parameter *style* which will vary the markers and create a more readable plot.**

# COMMAND ----------

sns.scatterplot(data=df, x='engine_size', y='horsepower', hue='fuel_type', style='fuel_type');

# COMMAND ----------

# MAGIC %md
# MAGIC **Correlation**
# MAGIC
# MAGIC Correlation means association. More precisely, it expresses the extent to which two variables change together at a constant rate.
# MAGIC
# MAGIC - In a scatter plot when the y variable tends to increase as the x variable increases, we say there is a **positive correlation** between the variables.
# MAGIC - Again, when the y variable tends to decrease as the x variable increases, we say there is a **negative correlation** between the variables.
# MAGIC - If the points on the scatter plot seem to be scattered randomly, we say that there is **no correlation** between the variables.
# MAGIC
# MAGIC **Let's check out the relationship between a few more variables using scatter plots.**

# COMMAND ----------

sns.scatterplot(data=df, x='curb_weight', y='engine_size');

# COMMAND ----------

# MAGIC %md
# MAGIC From the above plot, we can say that these variables are *positively correlated.*

# COMMAND ----------

sns.scatterplot(data=df, x='bore', y='stroke');

# COMMAND ----------

# MAGIC %md
# MAGIC - From the above plot, it is clear that the variables have no correlation.
# MAGIC
# MAGIC **Note:**
# MAGIC 1. A strong correlation will have data points close together, while a weak correlation will have data points that are further apart.
# MAGIC 2. We can not measure the relationship quantitatively using a scatter plot. It just gives an expression for the relative change between the variables.

# COMMAND ----------

# MAGIC %md
# MAGIC We can see from the scatterplot of `engine_size` vs `horsepower` that there is a positive correlation between the two variables. Now, we want to measure the relationship between these two variables quantitatively and try to predict the '**horsepower**' based on '**engine size**'. This can be easily done by fitting a linear model. Here comes the seaborn ***lmplot()*** function to help us with that.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Pair Plot
# MAGIC
# MAGIC * A **pairplot** shows the relationship between two numeric variables for each pair of columns in the dataset.
# MAGIC * It creates a grid of axes such that each variable in data will be shared in the y-axis across a single row and in the x-axis across a single column.
# MAGIC * The *pairplot()* function of seaborn can be used to create such a plot.

# COMMAND ----------

sns.pairplot(data=df[['normalized_losses','wheel_base','curb_weight','engine_size','price','peak_rpm']])

# COMMAND ----------

# MAGIC %md
# MAGIC **We can add the *hue* parameter in pairplot to create a semantic mapping.**
# MAGIC
# MAGIC - It changes the default marginal plot to a layered kde plot.
# MAGIC
# MAGIC **Also, we can add *vars* parameter to assign a list of variables from the dataset for which we want to create the pairplot.**

# COMMAND ----------

sns.pairplot(data=df, vars=['wheel_base', 'curb_weight', 'engine_size', 'price'], hue='number_of_doors');

# COMMAND ----------

# MAGIC %md
# MAGIC **We can set *corner=True* to plot only the lower triangle of a pairplot.**

# COMMAND ----------

sns.pairplot(data=df, vars=['wheel_base', 'curb_weight', 'engine_size', 'price'], corner=True);

# COMMAND ----------

# MAGIC %md
# MAGIC ## Heatmap
# MAGIC
# MAGIC * A **heatmap** is a graphical representation of data as a color-encoded matrix.
# MAGIC * It is a great way of representing  the correlation for each pair of columns in the data.
# MAGIC * The *heatmap()* function of seaborn helps us to create such a plot.

# COMMAND ----------

sns.heatmap(data=df[['wheel_base','curb_weight','engine_size','price']].corr());

# COMMAND ----------

# MAGIC %md
# MAGIC **We can set the *annot* parameter to *True* for displaying the numeric value in each cell.**
# MAGIC
# MAGIC - To remove the color bar, the *cbar* parameter can be set to *False*.

# COMMAND ----------

sns.heatmap(data=df[['wheel_base','curb_weight','engine_size','price']].corr(), annot=True, cbar=False);

# COMMAND ----------

# MAGIC %md
# MAGIC **We can apply a different colormap with the *cmap* parameter for better visual appeal.**

# COMMAND ----------

sns.heatmap(data=df[['wheel_base','curb_weight','engine_size','price']].corr(), annot=True, cmap='YlGnBu');