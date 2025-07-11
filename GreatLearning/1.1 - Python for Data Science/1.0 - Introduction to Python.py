# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC ```
# MAGIC Introduction to Google Colab
# MAGIC Variables
# MAGIC Data Structures - List, Tuple, and Dictionary
# MAGIC Conditional Statements
# MAGIC Looping Statements
# MAGIC List Comprehension
# MAGIC Functions
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC - ipnby file: Interactive Python Notebook
# MAGIC - Google Collaboratory: 
# MAGIC   - Cloud based tool for running Jupyter notebooks
# MAGIC   - Free access to GCPs/TPUs

# COMMAND ----------

# Automatic separator added in comma 
print('hello world',2+2,'this is python')

# print('hello world',2+2,'this is python', sep='')

# COMMAND ----------

# Error in concatenating 2 different datatypes in Plus Operator
print('hello'+'world')
print('hello'+5)


# COMMAND ----------

# Variables
price = 900
print('The price of the mobile is $',price,sep='')

# COMMAND ----------

# Zero division error
result = 10/0

# COMMAND ----------

# Output in Integer vs Non-Integer

# forces variable to be integer
print('Cost of the mobile phone is',150/4)
print('Cost of the mobile phone is',150//4)

# typecasting
print('The discounted price is '+str(4609/4))
print('The variable type is '+str(type(4609/4)))

# COMMAND ----------

# MAGIC %md
# MAGIC #### Data Structures
# MAGIC
# MAGIC - List
# MAGIC - Tuples
# MAGIC - Dictionary

# COMMAND ----------

# List
price_list = [900,800,600,1000,4500]
#            [ 0,  1,  2,   3,  4  ]
#            [-5, -4, -3,  -2, -1  ]

print('The max price in list is',max(price_list))
print('The min price in list is',min(price_list))
print('The sum of all prices in list is',sum(price_list))
print('The length of the list is',len(price_list))

print('Ranges', price_list[0:3]) #Right one is exclusive
print('Last index of the list', price_list[-1])

# List pop
price_list.pop()
price_list.append(56700)
price_list[0] = 100000
print(price_list)

# COMMAND ----------

'''
Tuple
- immutable
- faster than list
- can be used as key in dictionary
'''

price_tuple = (900,800,600,1000,4500)
price_tuple[0] = 100000
print(price_tuple)

# COMMAND ----------

# Dictionary
# Key-Value pairs

dictionary = {1:"USA", 2:"India", 3:"China"}
dictionary.update({3:"Japan"})
print(dictionary)

dictionary.pop(2) #key is used to pop
print(dictionary)

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

# COMMAND ----------

# Conditional Statements
budget = int(input('Enter your budget(in dollars)'))

if price <= budget:
  print('Congrats! You can buy the Iphone')
elif price > budget:
  print('Sorry! You cannot buy the Iphone')
else:
  print('Invalid input')

# COMMAND ----------

# Error , True must be samll
a = b = TRUE

# COMMAND ----------

# For Loop

price = 100
for i in range(5,21,5):       # End range is exclusive
    discount = price * (i/100)
    discounted_price = price - discount
    print('Discounted price for product',i,'% is',discounted_price)

print(range(5))

# COMMAND ----------

# While loop
i = 5
while i <=20:
    print(i)
    i += 5

# COMMAND ----------

# Functions
def display_iphone_attributes(brand, ram, storage):
    print('The apple iphone has ', ram, 'GB RAM and' , storage, 'GB storage')

display_iphone_attributes('samsung', 12, 128)

# COMMAND ----------

# Lambda Function: Creating anonymous, simple and small functions
# function_name (optional) = lambda arguments : expression
dis_price_lambda = lambda discount : 900 - (900 * discount/100)

print(dis_price_lambda(10))

# COMMAND ----------

'''
The expression (lambda x: (x+2)*5/2)(4) does not need a function name because it's an anonymous function that is defined and called in a single line. The 4 is indeed passed as the parameter x to this anonymous function. The 15.0 is the result of the float division in the function's expression.
'''
(lambda x: (x+2)*5/2)(4)

# COMMAND ----------

# DBTITLE 1,args vs kwars
# args vs kwargs

# *args

def total_amount(*args):
    total = 0
    for arg in args:
        total += arg 
    return total

print(total_amount(700,900,700,500))


# COMMAND ----------

# MAGIC %md
# MAGIC ```
# MAGIC def test(a, b=5, *args, **kwargs):
# MAGIC
# MAGIC a: Positional argument(can also be keyword if not ambiguous).
# MAGIC b=5: Keyword argument (with a default value).
# MAGIC *args: Collects extra Positional arguments into a tuple.
# MAGIC **kwargs: Collects extra Keyword arguments into a dictionary.
# MAGIC ```

# COMMAND ----------

# kwargs: Keyword argument
#kwargs must be after args

def order_summary(*prices, **additionals):
    total = 0
    print(type(prices))
    for price in prices:
        total += price
    
    net_spend = total - additionals['discount'] * total - additionals['cashback'] 

    if total >= 10000:
        rewards_points = 300
    elif total >= 5000:
        rewards_points = 200
    elif total >= 2000:
        rewards_points = 100
    else:
        rewards_points = 0
    
    return total, net_spend, rewards_points


additionals = {'discount':0.05, 'cashback':5}
to, ns, rp = order_summary(700,900,700,500, **additionals)
print(to, ns, rp)

# COMMAND ----------

def my_function(a,b,*args, **kwargs):
    return a+b
my_function(5,6)

# COMMAND ----------

# OOP : Class - User Defined data type
# Class has attributes and methods, not variables/functions
class my_data_type:
    def init_some_vals(self,val2):
        self.first_var = 1.7
        self.second_var = val2
    def multiple_vals(self):
        return self.first_var * self.second_var

my_obj = my_data_type()  # Object creation
my_obj.init_some_vals(2)
print(my_obj.multiple_vals())

# COMMAND ----------

number = input().split()
print(number)
print(type(number[0]))

# COMMAND ----------

# Operating System
import os

print('Current Directory Path', os.getcwd())
print('Current Directory name', os.listdir('.'))
print('List directory', os.listdir('/Workspace/Users/shaurya.rawat@ukg.com/'))

# os.mkdir('/Workspace/Users/shaurya.rawat@ukg.com/GreatLearning/Introduction to Python - Data Science/test')

file = open('/Workspace/Users/shaurya.rawat@ukg.com/GreatLearning/Introduction to Python - Data Science/test/test.txt','w')
file.write('hello\n')
file.write('world!')
file.close()

# COMMAND ----------

# DBTITLE 1,Interesting Question part 01
# Interesting question: quotient must always be greater than dividend , which in this case is 2 * -3 = -6,   -5- (-6) = 1
-5%2

# COMMAND ----------

# DBTITLE 1,Interesting Question part 02
(0.1+0.2)==0.3

# COMMAND ----------

# DBTITLE 1,Interesting Question part 03
# Python int range in memory -5 to 256

x=-6
y=-6
print(x is y)

x=257
y=257
print(x is y)

# COMMAND ----------

input1 = int(input())
input2 = int(input())

class Calculator:
    def add(self, a, b):
        # Write your code below
        return a + b
        

    def subtract(self, a, b):
        # Write your code below
        return a - b

# Create an object of the class
calculator1 = Calculator()

# Call the add and subtract functions using the object
print(calculator1.add(input1,input2))
print(calculator1.subtract(input1,input2))