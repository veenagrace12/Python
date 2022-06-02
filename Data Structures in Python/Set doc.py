### SET practice 

#elements in the sets are cannot be duplicates, they can be unique
#the elemenys in the sets are mutable
#there is no indes attached to any element in the sets hence slicing is not possible
#we can add or remove items from it
#define with {}
# a set is created by placing all the elements inside the {}
#seperated by comma, or by using the built-in set() function

# type
# x={1,2,3,4,5,6}
# print(type(x))

#  add
# x={1,2,3,4,5,6}
# x.add('avi')  # it will add element at the last of the set
# print(x)

# remove
# x={1,2,3,4,5,6}
# x.remove(6)  # removes user given element and returns error if the element is not in the set
# print(x)

# discard
# x={1,2,3,4,5,6}
# x.discard(9)  # discard removes a specific item from set and returns the same set as it is if the element is not in the set
# print(x)

# clear
# x={1,2,3,4,5,6}
# x.clear()     # clears the set
# print(x)

# #copy
# x={1,2,3,4,5,6}
# x.copy()      # copy the set and it will be immutable
# print(x)

# update
# x={1,2,3,4,5,6}
# y={6,7,8,9}
# x.update(y)   # adds one set to another set and eleminates duplicates
# print(x)

## set operations

# union
#b1={1,2,3,4,5,6,7}
#b2={1,2,4,5,7,9,11}
#print(b1.union(b2))  # eliminates dublicate items

# intersection
#b1={1,2,3,4,5,6}
#b2={8,7,6,4,2,1}
#print(b1.intersection(b2)) # returns only common elements

# difference
#b1={1,2,3,4,5,6,7}
#b2={1,2,3,4}
#print(b1.difference(b2))  # removes common elements and returns remaining elements of set1

# symmetric difference
#b1={1,2,3,4,5,6,7}
#b2={1,3,6,8,15,30}
#print(b1.symmetric_difference(b2)) # removes common elements and returns remaining elements of both sets

# disjoint
#b1={1,2,3,4,5,6,7}
#b2={11,42,23,14,15,8,9}
#print(b1.isdisjoint(b2)) # elements in set1 should be different from set2 #true

# subset
#b1={1,2,8,4,9,6,7}
#b2={1,2,3,4,5,8,9}
#print(b1.issubset(b2)) # all s1 elements should be in s2 # true otherwise # false

# superset
#b1={1,2,3,4,5,6,7,8,9}
#b2={1,2,3,4,5,8,9}
#print(b1.issuperset(b2)) # all s2 elements shoulbe in s1 #true otherwise #false

# frozenset
# f={'name':'avi','age':28,'salary':25000}
# fset=frozenset(f)     # frozenset returns only key values of dictionary
# print(fset)






# user defined modules
def add(a,b):
    return a+b
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def modulus(a,b):
    return a%b