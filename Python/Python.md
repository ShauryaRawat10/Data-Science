## Python
- Dynamically typed language
  - Number = 50
  - Number = 'UNKNOWN' # Data Type changed
 
"{} - {}".format(A,B) 

# Variables
```
# First, create a variable called start, and set it equal to "I am ".
# Remember the space after the word "am" !
start = "I am "

# Next, create a variable called age and set it equal to your age in years.
# This must be a number
age = 27

# Next, create a variable called end, and set it equal to " years old".
# Remember the space before the word "years"
end = " years old"

# Next, create a variable called output and use {} symbols and the format() function to stick the start, age and end variables
# together to make a string.
output = "{}{}{}".format(start, age, end)
```

# String
```
"hello".count('e') 

"hello".lower()

"hello".capitalizer()

y = "happybirthday!123"
y.isalnum()
y.isdigit()
y.isalpha()

y.index('day')
```

# Functions
```
a = [1,2,3]

def f1():
  global a 
  a[0] = 5 
  print(a) # Global a will be changed
  
## Unpacking and Packing Positional args 
def add(*numbers):
  total = 0 
  for number in numbers:
    total = total + number 
  return total 
  
add(1,2,3,4,5,6)  
```

## Keyword arguments
```
def about(name, age, likes):
  sentence = 'Meet {} They are {} years old and they like {}'.format(name, age, likes)
  return sentence 

dictionary = {'name': 'Ziyad', 'age': 23, 'likes': 'Python'}  
about(**dictionary)
  
def foo(**kwargs):
  for key,value in kwargs.items():
    print("{}:{}".format(key, value))
  
foo(huda = 'female', ziyad = 'male')  
```  
  
# Classes and Objects

Classes -> Templates
        -> Has States and Methods
Objects -> Instances of class

```
Class Pound:

  # Constructor
  def __init__(self, rare=False):
    self.rare = rare 
	if self.rare:
	  self.rare = 1.25 
	else:
	  self.rare = 1.00 
	  
	self.colour = 'gold'
	self.num_edges = 1
	self.diameter = 22.5
	self.thickness = 3.15
	self.heads = True
  
  # Destructor
  def __del__(self):
    print('Coin Spent')

  def rust(self):
    self.colour = "greenish"
	
  
  
coin1 = Pound()
print(coin1.value)
def coin1
```




  
  
  
  
  
  
  
  






