#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x = float(input("please enter your first number: "))
print ('you have entered: ' + str(x) +  '  x = '+ str(x))
y = float(input("please enter your first number: "))
print ('you have entered: ' + str(y) +  '  y = '+ str(y))
z = int(input('Please Select the operation you want to perform\n\tFor addition please enter 1\n\tFor subtraction , please enter 2\n\tFor Multiplication, please enter 3,\n\tFor division, please enter 4,\n\tFor Modulus, please enter 5'))
if z == 1:
    print ('x + y = ' + str(x + y))
if z == 2:
    print ('x - y = ' + str(x - y))
if z == 3:
    print ('x * y = ' + str(x * y))
if z == 4:
    print ('x / y = ' + str(x / y))
if z == 5:
    print ('modulus = ' + str(x % y))
if z > 5:
    print ('You have entered a wrong selection')
if x > y:
    a = x / y
    print('The first number is bigger than the second number\nand the result when you divide the bigger number by the smaller number \nis: '   + str(a))
else:
    b = y / x
    print('The second number is bigger than the first number\nand the result when you divide the bigger number by the smaller number \nis:  '    + str(b))

