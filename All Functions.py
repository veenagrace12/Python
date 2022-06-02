#### FUNCTIONS practice

# syntax
# def funcname():
#    #statments
#      print("this is function declaration") #function body
# funcname() #function call

# parameter and argument
# def funcname(a): #parameter=a
#     print('this is function',a)
# funcname(500)  # argument=500 i.e a=500 -->here using argument we can assign value to the parameter

# multiple parameters and multiple arguments
# def funcname(a,b,c): #parameter=a,b,c
#     print('this is function',a,b,c)
# funcname(500,600,900)    # arguments=800,600,900 i.e a=500 b=600 c=900

# one parameter and multiple arguments
# def funcname(a):  # parameter=a; to pass more than one argument 
#         print('this is function',a)
# funcname(5,6,7)     # returns error

# one parameter and multiple arguments using orbitary argument(*)
# def funcname(*a,):  # parameter=a; to pass more than one argument "*"is used
#     print('this is function',a)
# funcname(5,6,7) # returns output as tuple -->(5,6,7)
 
# keyword arguments (**)
# def funcname(**a,):   # parameter=a; to pass dictionary "**" is used
#     print('this is function',a)
# funcname(name="kiran",age=28) # returns output in the form of dictionary


# default parameters
# def avi(a,b,c,d='jun'): # defalut element automatically replaces the not mentioned element
#     print('avi got his bonus salary',a,b,c,d)
# avi(212000,22100,22300,23200)
# avi('mar','apr','may')

# nested function
# def even(*a):
#     print('even:',a)
#     def odd(*d):
#          print('odd:',d)
#     odd(3,5,7)
# even(2,6,8)



#user defined modules are used to import and export to another programs to save time
# user defined modules
# def add(a,b):
#     return a+b
# def add(a,b):
#     return a+b


from task16 import *
x1=add(5,9)
x2=sub(12,9)
x3=mul(25,50)
x4=div(986,4)
x5=modulus(986,4)
print('sum:',x1, 'diff:',x2, 'mul:',x3, 'div:',x4, 'modulus:',x5)