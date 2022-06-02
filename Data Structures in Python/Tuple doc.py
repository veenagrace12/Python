# x=()
# print(x)   # empty tuple
#tup=(1,'a','True',2,'b','False')
#print(tup[2])   # True

# slicing
x=(2,6,8,9,31,15,9,2,6,9,8,6,12,3,10)
#print(x[3:9])    # (9, 31, 15, 9, 2, 6)
#print(x[1:12:2])  # (6, 9, 15, 2, 9, 6)

# built in functions
# 1. min
#print(min(x))  # 2

# 2. max
#print(max(x))   # 31

# 3. len
#print(len(x))    # 15

# 4. sum
#print(sum(x))     # 136

# 5. count
# y=x.count(6)
# print(y)            # 3

# 6. index
# y=x.index(8)        # 2
# print(y)

# 7. sort
#print(sorted(x))     # [2, 2, 3, 6, 6, 6, 8, 8, 9, 9, 9, 10, 12, 15, 31]

#print(sorted(x,reverse=True))  # [31, 15, 12, 10, 9, 9, 9, 8, 8, 6, 6, 6, 3, 2, 2]

# in and not in
#v=[2,4,6,8,10,12,14]
#print(6 in v)     # True

#print(9 in v)      # False

#print(9 not in v)   # True
# identity operator
# t=9
# t1=9
# print(id(t))        # 1240967545328
# print(id(t1))       # 1240967545328

#t=[8,8]
#t1=[8,8]
# print(id(t))      ## 2393003136768
# print(id(t1))     ## 2393003274560

# is and is not
#print(t is t1)      # False
#print(t is not t1)  # True

t=(4,5,6,7)
t1=(2,9,8,1)
print(t+t1)          ## (4, 5, 6, 7, 2, 9, 8, 1)


## Tuple Documentation
'''
1.Tuple is used to store the sequence of different data types.
2.The tuple is similar to lists since the value of the items stored 
in the list can be changed, whereas the tuple is immutable,
and the value of the items stored in the tuple cannot be changed.
3.A tuple can be written as the collection of comma-separated (,) 
4.values enclosed with the small () brackets.'''

tup=()

## built in functions
# 1. min: it will print the minimum of all values
#     min(x)
# 2. max: it will print the maximum of all values
#     max(x)
# 3. len: it will print the length of the tuple
#     len(x)
# 4. sum: it will add the all values in the tuple
#     sum(x)
# 5. count: it will count the repeted elements in the tuple
#    x.count(value)
# 6. index: it will print the index value 
#    x.index(value)
# 7. sorted: it will sort the values in a specific order
#    sorted(x)   # small to large
#    sorted(x,reverse=True)  # large to small
