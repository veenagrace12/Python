# lambda function

'''

A lambda function is a small anonymous function.

A lambda function can take any number of arguments,
 but can only have one expression.

lambda arguments : expression

'''

# x = lambda a,b,c : a*b*c
# print(x(5,2,9))
# print(x(5,7,6))              

# y = lambda a,b,c,d,e : a-b*c+d/e
# print(y(8,49,3,14,56))        # -138.75

# n=lambda a,b: a**2+b**2+2*a*b
# print(n(256,125))

# m=lambda a,b,c : (a+b+c)**3
# print(m(8,7,9))

# filter function

'''
The filter() method filters the given sequence with the help 
of a function that tests each element in the sequence 
to be true or not.


syntax:

filter(function, sequence)
Parameters:
function: function that tests if each element of a 
sequence true or not.
sequence: sequence which needs to be filtered, it can 
be sets, lists, tuples, or containers of any iterators.
Returns:
returns an iterator that is already filtered.

'''

# ages = [5, 8, 10, 12, 17, 18, 24, 32,45,67]

# def myFunc(x):
#   if x <= 18:
#     return False
#   else:
#     return True
# adults = filter(myFunc, ages)
# print(tuple(adults))                # (24, 32, 45, 67)
 

# nums = [5, 8, 10, 12, 15, 17, 18, 24, 27, 32, 45, 67, 73]

# def Func(x):
#   if x%2==0:
#     return False
#   else:
#     return True
# odd = filter(Func, nums)
# print(tuple(odd))              # (5, 15, 17, 27, 45, 67, 73)

# Genarator function

'''
Generator-Function : A generator-function is defined like a normal function,
but whenever it needs to generate a value, 
it does so with the yield keyword rather than return.
If the body of a def contains yield, the function automatically
becomes a generator function.
'''
'''
The yield statement is responsible for controlling the flow of the generator function.
It pauses the function execution by saving all states and yielded to the caller. 
Later it resumes execution when a successive function is called. We can use the multiple yield statement in the generator function.

The return statement returns a value and terminates the whole function and only one return statement can be used in the function.
'''
# generator object with next()


# def simpleGeneratorFun():
# 	yield ((7*5)+(17*15)+(27*25))
# 	yield ((26**2)-(28**2)+(29**3))
# 	yield (288**4)
# 	yield(4783942+6938290-9893025*56935/985%2)

# # x is a generator object
# x = simpleGeneratorFun()

# #Iterating over the generator object using next
# print(x.__next__()) # In Python 3, __next__()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

'''
965
24281
6879707136
11722231.639593959

'''

 
# def table(m):
# 	for i in range(1,11):
# 		yield m*i
# 		i = i+1
  
# for i in table(19):
# 	print(i)


# def simpleGeneratorFun():
# 	yield [45,67,34,89]+[76,55,28,90]
# 	yield len({'Apples':35,'Oranges':60,'Grapes':20,'Guava':32,'Banana':12,'Mango':100,'Cherries':500,'Berries':50})
# 	yield ({9,4,29,54,69}.symmetric_difference({54,78,432,9,890,29}))

# # x is a generator object
# x = simpleGeneratorFun()

# #Iterating over the generator object using next
# print(x.__next__()) # In Python 3, __next__()
# print(x.__next__())
# print(x.__next__())

'''
[45, 67, 34, 89, 76, 55, 28, 90]
8
{432, 4, 69, 890, 78}
'''

# def generate_numbers(n):
#      num = 0
#      while num < n:
#          yield num
#          num += 1
# total = sum(generate_numbers(1000))
# print(total)

# map function

'''
The python map() function is used to return a list of results
after applying a given function to each item of an iterable(list, tuple etc.)

map(function, iterables)  
'''

# def squares(n):  
#   return n**n   
# numbers = (5, 7, 9, 11)  
# result = map(squares, numbers)  
# print(list(result))                     # [3125, 823543, 387420489, 285311670611]


# def difference(x,y):  
#   return x-y  
# num=(98,54,76,23)  
# num1= (43,56,14,19)  
# result = map(difference, num,num1)  
# print(set(result))                    # {62, 4, -2, 55}


# def tmul(a,b):  
#   return a*b    
# result = map(tmul, (17,42,51),(37,58,99))   # [629, 2436, 5049]
# print(list(result)) 


# reduce function
'''
The reduce() function, as the name describes,
applies a given function to the iterables and returns a single value.
'''


# from functools import reduce
# d=reduce(lambda a,b: a-b,[23,21,45,98,2])      # reduce(function,sequence)
# print(d)


# from functools import reduce
# x=reduce(lambda a, b: a if a > b else b, (45,67,34,86,98,59))
# y=reduce(lambda a, b: a if a < b else b, (45,67,34,86,98,59))
# print('maximum value of tuple',x)
# print('minimum value of tuple',y)



def even(x):
    if x%2==0:
        print(x)
#diff bw filter and map
nums = [11, 22, 33, 44, 55]
map = list(map(lambda x: x%2==0, nums))       # [False, True, False, True, False]
print(list(map))
filter = list(filter(lambda x: x%2==0, nums))  # [22, 44]
print(filter)

