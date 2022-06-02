# Exception handling or Error handling
# exception-- interrupt occured during the program running

# try:
#     print(q)
# except:
#     print('error occured')  
# else:
#     print('done')
# finally:
#     print('friend')          
        
# a=10
# try:
#     print(a+b)
# except:
#     print('b is not defined')
# else:
#     print('done')
# finally:
#     print('friend')                   


# a=10
# b=50
# try:
#     print(a+b)
# except:
#     print('b is not defined')
# else:
#     print('done')
# finally:
#     print('friend')      

### using more than one exception

# a=10
# try:
#     print(a+b)
# except NameError:
#     print('name error occured')
# except ValueError:
#         print('value error occured')

### return the error but the program is not terminated

# try:
#     print(a)         # name 'a' is not defined
# except Exception as x:
#     print(x)


# try:
#     print(1/0)         # division by zero
# except Exception as x:
#      print(x)


## raise-user defined exception

y='kiran'
try:
    dec=float(y)
except ValueError:
    raise ValueError('string cannot be converted in to float')   










