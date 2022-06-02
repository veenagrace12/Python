## date and time module
# for retreving current date
# import datetime
# current_date=datetime.datetime.now()
# print(current_date)        # 2022-02-14 12:15:04.161011


# import datetime
# current_date=datetime.datetime.today()
# print(current_date)         # 2022-02-14 12:16:15.167793

# creating date and time

# import datetime
# x=datetime.datetime(2022,2,15,1,30,25,444298)
# print(x)                      # 2022-02-15 01:30:25.444298

# # creating date
# import datetime
# x=datetime.datetime(2022,2,15)
# print(x)                      # 2022-02-15 00:00:00 time fields automatically set to 0


# parameters in strftime()

# import datetime
# cd=datetime.datetime.now()
# result=cd.strftime("%y")                  # %y-Short version of year
# print("Short version of year:",result)   # Short version of year: 22


# import datetime
# cd=datetime.datetime.now()
# result=cd.strftime("%Y")                  # %Y-Full version of year
# print("Full version of year:",result) # Full version of year: 2022


# import datetime
# cd=datetime.datetime.now()
# result=cd.strftime("%b")                  # %b-Short version of month
# print("Short version of month:",result)   # Short version of month:Feb


# import datetime
# cd=datetime.datetime.now()
# result=cd.strftime("%B")                  # %B-Full version of month
# print("Full version of year:",result)     # Full version of month: February


# import datetime
# cd=datetime.datetime.now()
# result=cd.strftime("%w")                  # %B-number of weekday (sunday=0)
# print("number of weekday is:",result)     # number of weekday is : 1


# import datetime
# cd=datetime.datetime.now()
# result=cd.strftime("%a")                  # %a-Short version of day
# print("Short version of day:",result)     # Short version of day: Mon


# import datetime
# cd=datetime.datetime.now()
# result=cd.strftime("%A")                  # %A-Full version of day
# print("Full version of day:",result)     # Full version of day: Monday


# import datetime
# cd=datetime.datetime.now()
# result=cd.strftime("%H")                  # %H-24hrs format
# print("24hrs format:",result)     # 24hrs format: 12


# import datetime
# cd=datetime.datetime.now()
# result=cd.strftime("%I")                  # %I-12hrs format
# print("12hrs format:",result)     # 12hrs format: 12

# import datetime
# cd=datetime.datetime.now()
# result=cd.strftime("%M")                  # %M-Minutes format
# print("Minutes :",result)                 # Minutes : 42

# import datetime
# cd=datetime.datetime.now()
# result=cd.strftime("%S")                  # %S-Seconds format (capital-s)
# print("Seconds :",result)                 #Seconds : 15

# import datetime
# cd=datetime.datetime.now()
# result=cd.strftime("%f")                  # %f-Micro Seconds format
# print("Micro Seconds :",result)           #Micro Seconds : 986559



# import datetime
# cd=datetime.datetime.now()
# result=cd.strftime("%p")                  # %p-AM/PM  small(p)
# print("AM/PM :",result)                   # AM/PM : PM


# import datetime
# cd=datetime.datetime.now()
# result=cd.strftime("%d")                  # %d-day number small(p)
# print("day number :",result)                   # day number: 14


# import datetime
# cd=datetime.datetime.now()
# result=cd.strftime("%x")                  # %x-local version of date small(x)
# print("local version of date :",result)    # local version of date :02/14/22


# import datetime
# cd=datetime.datetime.now()
# result=cd.strftime("%X")                  # %X-local version of time capital(X)
# print("local version of time :",result)    # local version of time :12:50:37


## time delta function

# incriment of days
# from datetime import datetime,timedelta

# cd=datetime.now()                     # current date is: 2022-02-14 12:57:59.778596
# print("current date is:",cd)
# New_date=cd+timedelta(days=3)         # new date is: 2022-02-17 12:57:59.778596
# print("new date is:",New_date)


# decriment of days
# from datetime import datetime,timedelta

# cd=datetime.now()                     # current date is: current date is: 2022-02-14 12:59:44.765007
# print("current date is:",cd)
# New_date=cd-timedelta(days=3)         # new date is:new date is: 2022-02-11 12:59:44.765007 
# print("new date is:",New_date)


# incriment of year
# from datetime import datetime,timedelta

# cd=datetime.now()                     # current date is: current date is: 2022-02-14 13:05:39.580325
# print("current date is:",cd)
# New_date=cd+timedelta(days=365)         # new date is:new date is: 2023-02-14 13:05:39.580325
# print("new date is:",New_date)

# n.o of days difference between new date and current date 

from datetime import datetime,timedelta

cd=datetime.now()                     # current date is: current date is: 2022-02-14 13:10:03.353609
print("current date is:",cd)
New_date=cd+timedelta(weeks=4)         # new date is:new date is: 2022-03-14 13:10:03.353609
print("new date is:",New_date)
difference=New_date-cd
print(difference)                      # difference=28days