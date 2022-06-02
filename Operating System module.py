'''
1)Python OS module is a collection of functions and provides the facility to establish the interaction between the user and the operating system
2)It offers many useful OS functions that are used to perform OS-based tasks and get related information about operating system.
3)module is collections of python language code, which consists of python functions, variables and classes.
4)The Python OS module lets us work with the files and directories.
'''

# list of functions in OS module:-

# os.name:- This function provides the name of the operating system module that it imports.
# import os   
# print(os.name)

# getcwd():-It returns the current working directory(CWD) of the file.
# import os     
# cwd=os.getcwd()
# print("current working directory is:",cwd)      # C:\Users\John Wesley\Desktop\codingrad


# os.mkdir():-used to create new directory (or) folder.
# import os
# os.mkdir("d:\\newdirectory") 
 
# makedirs():-creating group of directories
# import os
# os.makedirs("d:\\newdirectory\sub\sub1\sub2") 

# os.chdir():-used to change the current working directory.
# import os  
# os.chdir("d:\\")  

# os.rmdir():-remove the specific directory
# import os
# os.rmdir("d:\\newdirectory\sub\sub1\sub2") 
# print("sub2 is deleted")

# os.removedirs():-remove group of directories in single shot
# import os
# os.removedirs("d:\\newdirectory\sub\sub1") 
# print("all directories are deleted")

# os.listdir():-it will print all the list of files and directories which are exist in the current directory in the form of list
# import os
# lst=os.listdir()
# print(lst)

# print all files in one by one and total n.o of files and directories
# import os
# lst=os.listdir()
# import time
# for i in lst:
#     time.sleep(0.5)
#     print(i)
# ni=len(lst)    
# print("-"*20)
# print("count files and directories:",ni)

# os.system():if we want to execute other than the python commanda i.e, executing operating sysytem commands
#import os
# os.system("date")   # returns the current date
# os.system("calc")   # open the calculator

# os.rename():- used to change the name of existing file or directory
import os
os.rename("tasks","daily_tasks")



