#this is a comment
print("hello world")

str = "hello"

#Slicing
print(str)
print(str[0:1])
print(str[0:-2])
print(str[3:5])
print(str[4])

#Line Indentation
#Press Tab
print("Hi")

'''
    #Quotation


#Multiplication
a = 2
b = "Hello"
c = a*b
print(c)

#Addition
a = "to"
b = "gether"
c = a+b
print(c)

#Divide
a = 54
b = 3
c = a/b
print(c)

#Subtraction
a = 5
b = 1
c = a - b
print(c)

#
a = 8
b = 7
c = a % b
print(c)

#Equal to: ==
#Not Equal to: !=

#Declare of variables, Expression, Displaying
#Declare of variables
a_side = 2
b_side = 50
base = 25
height = 2.5

#Expression
area = (base*height)/2
perimeter = a_side + b_side + base

#Displaying
print(area)
print (perimeter)

#If & Else Statements
var1 = 100
if var1 == 2000:
    print("1 - Got a true expression value")
    print(var1)
else:
    print("1 - Got a false expression value")
    print(var1)

var2 = 0
if var2 == 300:
    print("2 - Got a true expression value")
    print(var2)
else:
    print("2 - Got a false expression value")
    print(var2)

print("Goodbye")

#IF & Else Ladder
var = 100
if var == 200:
    print("1 - Got a true expression value")
    #to be continued

#while loop
count = 0
while (count<9):
    count+=1
    print("number",count)


#for loop
for i in range (11):
    print()
print("================== loop with start and end")

for i in range (4,11):
    print(i)
print("================== loop within range")

for i in range (1,11,2):
    print(i)
print("================== loop within range with condition")

for letters in "python":
    print(letters)
print("================== loop within the word")
'''

#Function
#Define Function

#local variable
#global variable
x = 50
def func():
    global x
    print ("x is",x)
    x = 2
    print("changed global x to",x)

func()
print("Value of x is",x)

#default parameters
def times(x,y):
    print(x*y)

times(2,6)

def maximum(x, y):
    if x > y:
        return(x)
    elif x == y:
        return('The numbers are equal')
    else:
        return(y)
print(maximum(2, 3))

# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), 'items to purchase.')
print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')
print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)
print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)
print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)
