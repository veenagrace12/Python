# # while loop for finding odd number below 1000
# i=int(input("enter value of i:"))
# while(i<=1000):
#     if i%2!=0:
#         print(i,end=' ') 
#     i+=1
# # output enter value of i:749
# # 749 751 753 755 757 759 761 763 765 767 769 771 773 775 777 779 781 783 785 787 789 791 793 795 797 799 801 803 805 807 809 811 813 815 817 819 821 823 825 827 829 831 833 835 837 839 841 843 845 847 849 851 853 855 857 859 861 863 865 867 869 871 873 875 877 879 881 883 885 887 889 891 893 895 897 899 901 903 905 907 909 911 913 915 917 919 921 923 925 927 929 931 933 935 937 939 941 943 945 947 949 951 953 955 957 959 961 963 965 967 969 971 973 975 977 979 981 983 985 987 989 991 993 995 997 999 
# # for loop
# T= input()
# for i in T:  # it will continue the until the last num in i
#     print(T)
# # output
# '''for loop
# 2468975310
# 2468975310
# 2468975310
# 2468975310
# 2468975310
# 2468975310
# 2468975310
# 2468975310
# 2468975310
# 2468975310
# 2468975310
# '''
# # nested for loop for 1 to 100 tables
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end='_') # print tables
#     print()
# # output
# '''1_2_3_4_5_6_7_8_9_10_
# 2_4_6_8_10_12_14_16_18_20_
# 3_6_9_12_15_18_21_24_27_30_
# 4_8_12_16_20_24_28_32_36_40_
# 5_10_15_20_25_30_35_40_45_50_
# 6_12_18_24_30_36_42_48_54_60_
# 7_14_21_28_35_42_49_56_63_70_
# 8_16_24_32_40_48_56_64_72_80_
# 9_18_27_36_45_54_63_72_81_90_
# 10_20_30_40_50_60_70_80_90_100_
# '''

# #break statement
# for i in range(1,21):    #for loop
#     if i==11:             #checks whether i is equal to 11
#         break            #if condition is true break the loop
#     else:
#         print(i)
# # output
# '''1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# '''

# # CONTINUE
# name="veenagrace"
# for i in name:
#     if i=='g':     # checks whether i is equal to 
#         continue   # if condition is ture skip g and printing upto g 
#     else:
#         print("not equal")
#     print(i)    
# # output
# '''not equal
# v
# not equal
# e
# not equal
# e
# not equal
# n
# not equal
# a
# not equal
# r
# not equal
# a
# not equal
# c
# not equal
# e
# '''

# pass
a=int(input())
b=int(input())
if a>=b:      #if condition is ture it will pass the loop
    pass
else:
    ("a is less than b")
#output
'''56
24
'''