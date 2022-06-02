# open,close and read of txt file

#f=open('file_handling.txt','r')   # file will be open in read mode
# c=f.read()                
# print(c)
#f.close()        # file will be closed

# readline of txt file
# f=open('file_handling.txt','r')   # file will be open in read mode
# c=f.readline()            # return as it is in the file,if it is multi line then only print the first line    
# print(c)
# f.close()

# reading of txt file upto specified characters

# f=open('file_handling.txt','r')   # file will be open in read mode
# c=f.readline(15)            # it will print the first 15(0-14) characters   
# print(c)
# f.close()

# readlinse of txt file

# f=open('file_handling.txt','r')   # file will be open in read mode
# c=f.readlines()            #     returns the data in list format,every single line is taken as an element
# print(c)
# f.close()

# writing of file
# f=open('file_handling.txt','w')   # file will be open in read mode
# c=f.write("many operations")            # return as it is in the file,if it is multi line then only print the first line    
# f.close()

# writelines of a file

# f=open('file_handling.txt','w')   # file will be open in read mode
# c=f.writelines('''1.many operations\n2.handling of files such as opening,closing,reading,writing and
# 3.many other operations\n4.r means open in read mode\n5.w means open in write mode''')            # return as it is in the file,if it is multi line then only print the first line    
# f.close()

# f=open('file_handling.txt', 'w')
# d=['this is insert','kiran function', 'kiran']
# for i in d:
#     f.writelines([i])


# tell-- used to get the position of file handle

# f=open('file_handling.txt','r')
# print(f.tell())    # cursor is at 0th position
# f.close()

# f=open('file_handling.txt','r')
# f.read(15)         # read upto 15th index
# print(f.tell())    # cursor is at 15th position
# f.close()


## seek-- used to change the position of file handle to given specific position

# f=open('file_handling.txt','r')
# f.read(15)         # read upto 15th index
# print(f.tell())    # cursor is at 15th position
# f.seek(0)
# print(f.tell())
# f.close()


# f=open('file_handling.txt','r')
# f.read(15)         # read upto 15th index
# print(f.tell())    # cursor is at 15th position
# f.seek(20)
# print(f.tell())    # cursor is changed from 15th to 20th position
# f.close()


f=open('file_handling.txt',mode='r+')
content=f.read()
v=str(content)
print(v)
x=v.split()
print(x)
x.insert(3,'kiran')
print(f.tell())
f.close

f=open('file_handling.txt',mode='w')
for i in x:
    f.writelines([i])
f.close()    

