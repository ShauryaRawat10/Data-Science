# Statistics

## Statistics Fundamentals
- **Distributions**
  - Normal Distribution
  - Standard Deviation
  - Mean, Median, Mode
  - Types of Distributions
- Central limit Theorem
- Hypothesis Testing
  - Z-Score
  - T-test
- **Stat Significance (P-Value)**
- Confidence Interval
- **A/B Testing**
- Pareto Principle (80/20)
- Law of Large Numbers

## Data Science Process
- Lifecycle of Data Science Project
  - 10% - Identify the Question
  - 70% - Prepare the data (Clean, resolve anomalies, perform QA)
  - 10% - Analyze the data (Build models, perform data mining, run text analytics)
  - 10% - Visualize the data
  - 80% - Present your findings (show insights to stakeholders)

## Visualization
- Visualization for Data Mining
- Visualization for Presentation

**Visual cinnamon**

**Bussed out - Article on population : Has Visualization**

## Curriculum
- Data Preprocessing
  - Get the dataset
  - Import the Libraries
  - Import the dataset
  - Missing data
  - Categorical data
  - Splitting dataset into training and testing data
  - Feature Scaling
  - Data Preprocessing template
- Regression
  - Simple Linear Regression
  - Multiple Linear Regression
  - Polynomial Regression
  - SVR Regression
  - Decision Tree Regression
  - Random Forest Regression
  - Evaluate Model Performance
    - Mean Squared Error (MSE)
    - R-Squared
    - Adjusted R-Squared
  - Regularization Methods
    - Ridge Regression
    - Lasso
    - Elastic Net
    - LARS
- Classification
  - Logistic Regression
  - KNN
  - SVM
  - Kernel SVM -> For Non Linear problem
  - Naive Bayes
  - Decision Tree Classification
  - Random Forest Classification
  - Evaluate Performance of Classification model
    - TP, FP, TN, FN
    - Precision and Recall
    - Cumulative Accuracy Profile (CAP)
    - Receiver Operating Characteristics (ROC)
    - Comparing training and test performance
- Clustering
  - K-Means Clustering
  - Hierarchical Clustering
- Association Rule Learning
  - Apriori
  - Eclat
- Reinforcement Learning
  - Upper Confidence Bound (UCB)
  - Thompson Sampling
- Natural Language Processing
- Deep Learning
  - ANN
  - CNN
- Dimensionality Reduction
  - Reducing dataset size, beacuse we are dealing with TB of data
  - PCA (Principle Component Analysis)
  - LDA (Linear Discriminant Analysis)
  - Kernel PCA
- Model Selection and Boosting
  - XGBoost Model: Gradient Boosting
  - Regularization for Hyperparameters:
    - Hyperparameters
      - K-Fold Cross Validation
      - Grid Search

## Deep Learning
| Type         | Model                     | Use Case                     |
|--------------|---------------------------|------------------------------|
| **Supervised**   | ANN                       | Used for regression and classification |
|              | CNN                       | Used for Computer Vision     |
|              | RNN                       | Used for Time Series Analysis |
| **Unsupervised** | Self Organizing Maps      | Used for Feature Detection    |
|              | Deep Boltzmann Machines   | Used for Recommendation Systems |
|              | AutoEncoders              | Used for Recommendation Systems |



## Deep Learning and Computer Vision
- Computer Vision Library (Not real Deep Learning model):
  - Open CV
    - Smile Detector
- SSD: Single Shot MultiBox Detector
- YOLO v2
  - Real time detection
- GANs
  - Generating Images
- Cycle GANs

## Deep Learning and NLP
- Sentiment Analysis
- Machine Translation
  - Seq2Seq
    - Use Pytorch
  - Bag of Words

- Artificial Intelligence (Deep Reinforcement Learning)
  - Reinforcement Learning and 
  - Open AI Gym
    - Toolkit for developing and comparing reinforcement learning algorithm
    - It is a environment where can just focus on building AI
  - Q-Learning
    - AI without brain
  - Deep Q-Learning: Brain to AI
  - Deep Convolutional Q-Learning: Eyes to AI
  - Deep Convolutional LSTM Q-Learning: Memory to AI
  - A3C (Asynchronous Advantage Actor-Critic): Critic Sense to AI


# EDA
- Statistical Significance (Something like P_Value less than 0.05 for all features)
- Correlation between I/P and O/P variable (or across independent variables)


# Python

**Note**: Download dataset of choice from **uci ml repository**
https://archive.ics.uci.edu/

## Machine Learning

```
# Regression

import pandas as pd 
dataset = pd.read_excel('sample_data/Folds5x2_pp.xlsx')

X = dataset.iloc[:, 0:-1].values
y = dataset.iloc[:, -1].values

# Splitting dataset into training and testing set
# sklearn is library, model_selection is module with models
from sklearn.model_selection import train_test_split 

# random_state = 0 means that everytime we run experiment, it will have same combination set in test-train data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Gradient Boosting model to training set (Has multiple week learners, choose loss function -> GD find params such that decision tree minimize loss function)
# GBR is actually a class that defines GD model
from sklearn.ensemble import GradientBoostingRegressor 

# create object of a gradient boosting regressor class
regressor = GradientBoostingRegressor()

# train regressor with data
regressor.fit(X_train, y_train)

# Predict test set results
y_pred = regressor.predict(X_test)



# Classification

columns = [
    'Sample code', 'Clump Thickness', 'Uniformity of Cell Size',
    'Uniformity of Cell Shape', 'Marginal Adhesion',
    'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
    'Normal Nucleoli', 'Mitoses', 'Class'
]

dataset = pd.read_csv('sample_data/breast-cancer-wisconsin.data', header=None, names=columns)

dataset = dataset.replace('?', 0)

X = dataset.iloc[:, 0:-1].values
y = dataset.iloc[:, -1].values

# Splitting dataset into training and testing set
# sklearn is library, model_selection is module with models
from sklearn.model_selection import train_test_split 

# random_state = 0 means that everytime we run experiment, it will have same combination set in test-train data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Gradient Boosting model to training set (Has multiple week learners, choose loss function -> GD find params such that decision tree minimize loss function)
# GBR is actually a class that defines GD model
from sklearn.ensemble import GradientBoostingClassifier

# create object of a gradient boosting classifier class
classifier = GradientBoostingClassifier()

# train classifier with data
classifier.fit(X_train, y_train)

# Predict test set results
y_pred = classifier.predict(X_test)

# Confusion matrix
# CM is a function, metrics is module, sklearn is library
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
```




























