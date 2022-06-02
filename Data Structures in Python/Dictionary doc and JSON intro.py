# fruit={}
# print(fruit) 
# print(type(fruit))
fruits={"apple":10,"orange":20,"banana":30,"kiwi":40,"cost":[25,50,100,150]}
# extracting keys and values
# print(fruits['orange'])    # 20

# print(fruits["cost"])     # [25,50,100,150]
# print(fruits["cost"][2])    # 100

# adding new element
# fruits["mango"]=50
# print(fruits)

'''output:
{'apple': 10, 'orange': 20, 'banana': 30, 'kiwi': 40, 'cost': [25, 50, 100, 150], 'mango': 50}
'''
# changing an existed element
# fruits["orange"]=250
# print(fruits)
'''output= 
{'apple': 10, 'orange': 250, 'banana': 30, 'kiwi': 40, 'cost': [25, 50, 100, 150]}
'''
# dictionary functions

#1. clear
# print(fruits.clear())
#2. copy
#print(fruits.copy())     
#3.get
# print(fruits["kiwi"]) # 40
# 4.items
# print(fruits.items())    #seperated as tuples in one list

'''output: 
dict_items([('apple', 10), ('orange', 20), ('banana', 30), ('kiwi', 40), ('cost', [25, 50, 100, 150])])
'''
# 5. keys
# print(fruits.keys())

'''output=
dict_keys(['apple', 'orange', 'banana', 'kiwi', 'cost'])
'''
# 6. values
# print(fruits.values())

'''output=
dict_values([10, 20, 30, 40, [25, 50, 100, 150]])
'''
# 7. update
# fruits.update({"quantity":"dozen"})
# print(fruits)

'''output=
{'apple': 10, 'orange': 20, 'banana': 30, 'kiwi': 40, 'cost': [25, 50, 100, 150], 'quantity': 'dozen'}
'''
# 8. pop
#fruits.pop("cost")
#print(fruits)
'''output:
{'apple': 10, 'orange': 20, 'banana': 30, 'kiwi': 40}
'''
# del
# del fruits
# print(fruits)    NameError: name 'fruits' is not defined

# for i in fruits:
#     print(i)

'''output :apple
        orange
        banana
        kiwi  
        cost
        '''
#for i in fruits.keys():
# print(i)        
'''output :apple
        orange
        banana
        kiwi  
        cost
        '''
#for i in fruits.values():
#      print(i)        
'''output:
10
20
30
40
[25, 50, 100, 150]'''


#for k,v in fruits.items():
 #   print(k,v)

'''output:
apple 10
orange 20
banana 30
kiwi 40  
cost [25, 50, 100, 150]
'''
# nested dictionary
fruits={
    "apple":{"green_apple":35},
    "cost":[25,50,100,150]
}

# print(fruits)

'''output=
{'apple': {'green_apple': 35}, 'cost': [25, 50, 100, 150]}
'''
#print(fruits["apple"]) ## output= {'green_apple': 35}

print(fruits["apple"]["green_apple"])   # 35


## DOCUMENTATION
'''
Python Dictionary
1.Python Dictionary is used to store the data in a key-value pair format. 
2.The dictionary is the data type in Python.
3.It is the mutable data-type. The dictionary is defined into element
 Keys and values.
4.Keys must be a single element
5.Value can be any type such as list, tuple, integer, string etc.
we can say that a dictionary is the collection of key-value pairs where the 
value can be any Python object.
the keys are the immutable Python object, i.e., Numbers, string, or tuple.
it wii be unordered
'''

#fruit={}
# print(fruit)   # empty dictionary
# print(type(fruit)) # dict
# fruit={"apple":10,"orange":20,"banana":30,"guava":40}

# dictionary functions
# 1.clear: it will clear the dict
     #fruits.clear()
# 2. copy: it will copy the dict 
#     fruits.copy()     
# 3. get: we can get the values for a particular key
# when compared to manual by using the functions operation will be speed
#    fruite.get["key"]
# 4. items: it will print both keys and values as different tuples in a list
#     fruits.items()   # [(" ", ),(" ", ).....]
# 5. keys: it will extract only keys
#     fruits.keys()
# 6. values: it will extract only values
#     fruits.values()
# 7. update: it will add new element in the last, only one key will be updated at a time,we can't update in a particular key
#     fruits.update("key":"value")
# 8. pop: it will remove the particular key-value pair
#    fruits.pop("key")
# del: built in function, it will delete the variable

#nested dictionary: 
        #var={'key1':"value1","key2":"value2", {"key":"value"}}

'''
#about  python JSON

'''
#JSON JavaScript Object Notation is a format for structuring data.
#It is mainly used for storing and transferring data between the browser and the server.
#Python too supports JSON with a built in package called json.
#This package provides all the necessary tools for working with JSON objects including parsing,serializing,deserializing and many more.'''
'''
#syntax
{"name":"anjali"} #data is separated by commas
#example to convert the JSON objects to Python objects

from contextlib import nullcontext
import json
import numbers
import string
from xmlrpc.client import boolean
#JSON  string

employee='{"id":"09","name":"anjali","development":"finance"}'

#convert string to python dict
employee_dict=json.loads(employee)
print(employee_dict)
print(type(employee_dict))
print("\n")

#convert python dict to JSON 
json_object = json.dumps(employee_dict,indent=4)
print(json_object)
print(type(json_object))

#JSON data types
# it supports mainly 6 data types
1.string
2.numbers
3.boolean
4.null
5.object
6.array
'''