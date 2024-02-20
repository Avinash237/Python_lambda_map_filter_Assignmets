"""
#
"""

"""
 - lambda function/nameless/anonymous
 - syntax:
    
    lambda parameter:expresion

-----------------------------------------------
op = lambda x,y,z:x + z
print(op(10,20,30))

--------------------------------------------------
we can use if else in lambda
op = lambda x: x**2 if x > 2 else x
print(op(10))
--------------------------------------------------

op = lambda x:x**2 if x > 2 else x
print(op(-10))
------------------------------------------------

# expression is called as turnary operator
syntax:
process_1 if condition  == True else process_2

temp = 99
check = 'covid+ve' if temp > 90 else 'covid -ve'
print(check)
---------------------------------------------------------

cv = lambda temp:'covid+ve' if temp > 90 else 'covid-ve'
print(cv(97))
----------------------------------------------------

# higher order function 
1. filter 
 - filter (fucn,iterable)
 - used to filter the objects based on conditon
 - when true then select object else reject 

#ex.
h = [56,78,56,77,90,10,3,7,80]
#filter even numbers
print(filter(lambda num:num%2 ==0,h))
#filter return filter object
#to see actual value typecast the filter object
print(list(filter(lambda num:num%2 ==0,h)))
----------------------------------------------------------

ck = ['Virat','Rohit','Bumrah','Dinesh','Mahi']
# ps: fetch player who names ends with 't'
print(tuple(filter(lambda name:name.endswith('t'),ck)))
#   - there is no need if to give a condition just write condition
-----------------------------------------------------------

# select layer who names lenght >5
ck = ['Virat','Rohit','Bumrah','Dinesh','Mahi']
print(tuple(filter(lambda name:len(name)>5,ck)))
------------------------------------------------------------

- map 
- map(func,iterable)
- map is used to apply an expression/operation over each element form the iterable

ck = ['Virat','Rohit','Bumrah','Dinesh','Mahi']
# ps: conver each element in to upper case
print(list(map(lambda name:name.upper(),ck)))
-----------------------------------------------------------


salary = [20000,3500,6000,10000,5000]
# create a new list of 10% bonus of each salary
# give sal + 10% bonus to sal > 5000
# and sal +20% bonus to sal < 5000
def change(amt):
    if amt>5000:
        return amt+amt*10/100
    else:
        return amt+amt*20/100

print(tuple(map(change,salary)))
-------------------------------------------------------------

salary = [20000,3500,6000,10000,5000]
def change(amt):
    if amt>5000:
        return amt+amt*10/100
    else:
        return amt+amt*20/100
print(list(map(lambda num:change(salary),salary)))

-----------------------------------------------------------------

- reduce 
- this i s not a bulit it is present into functool module
- we need to import it
- purpose is to reduce a sequece into sinle number

from functools import reduce
d = [1,2,3,4,5]
print(reduce(lambda x,y:x+y,d))

#---------------------------------------------
# find out max number usin reduce
from functools import reduce
d = [1,2,3,4,5]

print(reduce(lambda x,y:max(x,y),d))
--------------------------------------------
"""
