# try:
#     with open("1.txt" ,"r") as f :
#         print(f.read())
# except Exception as e :
#     print(e)
# try :
#     with open("2.txt" ,"r") as f :
#         print(f.read())
# except Exception as e :
#     print(e)

# try :
#     with open("3.txt" ,"r") as f :
#         print(f.read())
# except Exception as e :
#     print(e)

# print(f" Thank You")


# l = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ,8]
# for i , item in enumerate(l):
#     if (i==2 or i == 4 or i == 6) :
#         print(f"The item number at index  {i} is {item}")

# n = int(input("enter a number :"))
# mul = [n*i for i in range(1,11)]
# print(mul)

# a = int(input("enter a number :"))
# b = int(input("enter a number :"))
# if (b ==0):
#     raise ZeroDivisionError (f"display infinite by handling {b} as dinomenator")
# else :
#     print(f"The division of {a}/{b} is {a/b}")

# try :
#     a = int(input("enter a number :"))
#     b = int(input("enter a number :"))
#     print(a/b)
# except ZeroDivisionError as z:
#     print("infinte")
# 

n = int(input("enter a number :"))

table = [n*i for i in range(1 , 11)]
with open("1.txt" ,"a") as f :
        f.write(str(table)+"\n")