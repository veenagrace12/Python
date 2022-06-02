# #pattern-1
# n= int(input("Enter the number of rows: "))  

# for i in range(n):

#     for j in range(n):

#             print('*', end=' ')

#     print()

''' output

* * * * * 
* * * * *
* * * * *
* * * * *
* * * * *
'''

# # pattern-2
# rows = int(input("Enter the number of rows: "))  

# for i in range(rows):
    
#     for j in range(rows):
        
#         print(i+1,end=" ")
        
#     print()     

''' output

1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
'''
# # Pattern-3
# rows = int(input("Enter the number of rows: "))  
# for i in range(rows+1):  
#     for j in range(1,i+1):  
#         print(i, end=" ")   
#     print(" ")  

''' output
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

'''

# # Pattern-4
# no_rows=int(input("Enter the number of rows:"))
# for row in range(no_rows,0,-1):

#     for column in range(1,row+1):
#             print('*', end=' ')

#     print()

''' output

* * * * * 
* * * *
* * *
* *
*

'''
# Pattern-5
# n=int(input("Enter the number of rows:"))
# for i in range(n):
#     for space in range(-1,n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()    

'''
            * 
          * *
        * * *
      * * * *
    * * * * *
'''
#Pattern-6
n=int(input("Enter the number of rows:"))
for i in range(n):
    for space in range(-1,n-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()  

'''
            * 
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
    '''