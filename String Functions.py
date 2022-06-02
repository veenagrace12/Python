# ## DOCUMENTATION
# #strings
# '''
# 1.string is a collection of character enclosed either with single or double or triple quotes
# 2.the computer doesnt understand the characters,internally it stores the manipulated character as the 
# combination of 0's and 1's.
# 3.Each characters is encoded in ASCII or unicode character.So we can say the string as collection
# '''
# a='veena'
# b="string's"
# c='''veena
# grace
# '''
# print(type(a))
# print(type(b))
# print(type(c))
# print(a,b,c)

# String functions

# 1.capitalize
# '''In Python, the capitalize() function converts first character of a string to uppercase letter
# and remaining all characters are lowercase'''
#  example
# av="this is python class"
# print(av.capitalize())

# output=This is python class

# 2.upper
# '''The upper() function converts all lowercase characters in a string into uppercase characters and returns it'''
#  example
#  av="this is python class"
# print(av.upper())

# output=THIS IS PYTHON CLASS

# 3.lower
# '''The lower() function converts all uppercase characters in a string into lowercase characters and returns it'''
# example
# av="THIS IS PYTHON CLASS"
# print(av.lower())

# output=this is python class

# 4.center
# '''The center() function returns a string which is padded with the specified character'''
#  example
# av="THIS IS PYTHON CLASS"
# print(av.center(24,"$"))

# output=$$THIS IS PYTHON CLASS$$

# 5.count
# '''The count() function returns the number of occurrences of a substring in the given string'''
# example
# av="this is book"
# print(av.count(' is')) # is
# print(av.count('is'))  # is and this

# output= 1
#         2

# 6.startswith
# '''The startswith() function returns True if a string starts with the specified string
#    If not, it returns False.'''
#  example
# av="gold is more precious than any other metals"
# print(av.startswith("gold"))  
# print(av.startswith("any"))

# output=True
#        False 

# 7.endswith
# '''The endswith() function returns True if a string starts with the specified string
# If not, it returns False.'''       
#  example
# av="gold is more precious than any other metals"
# print(av.endswith("metals"))  
# print(av.endswith("any"))

# output=True
#        False 

#  8.format
# '''The format() function reads the type of arguments passed to it and formats it according to the format codes defined in the string'''      
# example
# x="my name is {}".format("veena")
# print(x)
# y="my name is {b} {a}".format(a="kiran",b="grace")
# print(y)
#  output= my name is veena
#          my name is grace kiran

# 9.find
# '''The find() function returns the index of first occurrence of the substring (if found)
#    If not found, it returns -1'''
# example
# av="python is easy to learn"
# print(av.find(to))  
# print(av.find('that'))  # word which is not in the string returns -1

# output= 15
#         -1

# 10.index
# '''The index() function returns the index of a substring inside the string (if found)
#    If the substring is not found, it raises an exception.'''
#    example
# av="python is easy to learn"
# print(av.index(to))  
# print(av.index('that'))

# output= 15
#         error-substring not found

# 11.split
# '''The split() function breaks up a string at the specified separator and returns a list of strings'''
# text="windows 10 is better than windows 11'''
# example
# av="python is easy to learn"
# print(av.split())          

# output=['python', 'is', 'easy', 'to', 'learn']

# 12.isalnum
# '''The isalnum() function returns True if all characters in the string are alphanumeric
# (either alphabets or numbers).If not, it returns False'''
# example
# a="1261768hkjdv"      #true
# b="279528723"       #true
# c="jhdghef"       #true 
# d="hgfjhf htrewf"   #false (space)
# print(a.isalnum())
# print(b.isalnum())
# print(c.isalnum())
# print(d.isalnum())

# 13.isdecimal
# '''The isdecimal() function returns True if all characters in a string are decimal characters
#    If not, it returns False'''
# example
# a="9875"                    #true
# b="25906.831"                #false
# c="mnbcx"                 #false
# d="2324.793iute"            #false
# e="3.14 54 qeiou"           #false
# print(a.isdecimal())
# print(b.isdecimal())
# print(c.isdecimal())
# print(d.isdecimal())
# print(e.isdecimal())

# 13.isdigit
# '''The isdigit() function returns True if all characters in a string are digits
#    If not, it returns False.'''
#  example  
#  x='43'
# y="9395avee"
# print(x.isdigit())   # True
# print(y.isdigit())   # False

# 15.join
# '''The join() function returns a string by joining all the elements of an iterable (list, string, tuple), separated by a string separator.'''
# example
# av="this is my pc"
# x=av.split()
# v="*".join(av)
# print(v)

# output=this*is*my*pc

# 16.lstrip
# '''The lstrip() removes characters from the left based on the argument a string specifying the set of characters to be removed'''
# example
# av="      this book is mine"
# print(av.lstrip())

# output=this book is mine

# 17.rstrip
# '''The lstrip() removes characters from the left based on the argument a string specifying the set of characters to be removed'''
# example
# av="this book is mine          "
# print(len(av))
# x=av.rstrip()
# print(len(x))
# print(x)

# output=27
#        17
#        this book is mine

# 18.strip
# '''The lstrip() removes characters from the left based on the argument a string specifying the set of characters to be removed'''
# example
# av="      this book is mine        "
# print(len(av))
# x=av.strip()
# print(len(x))
# print(x)

# output=31
#        17
#        this book is mine


# 19.title
# '''The title() function returns a string with first letter of each word capitalized; a title cased string'''
# example
# av="nothing succeeds like success"
# print(av.title())
# output= Nothing Succeds Like Success


# 20.removeprefix
# '''The removeprefix removes the prefix (starting) word in the string'''
# example
# av="do good and good will come to you"
# print(av.removeprefix("do"))

# output= good and good will come to you

# 21.removesuffix
# '''The removesuffix remove the suffix (ending) word in the string'''
# example
# av="the pen is mightier than the sword"
# print(av.removesuffix("sword"))

# output=the pen is mightier than the 


# 22.replace
# '''The replace() function replaces each matching occurrence of the old character/text in the string with the new character/text'''
# example
# av="man learns little from success,but much from failure"
# print(av.replace("much","more"))

# output=man learns little from success,but more from failure
