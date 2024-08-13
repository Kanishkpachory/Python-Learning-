# #walrus operator 
# if (n := len([1 , 2 , 3 , 4 , 5])) > 3 :
#     print(f"list is too long {n} elements , expected to be <=3")

# #type definitions 
# age : int = 25
# print(age)

# def sum(a: int , b : int) -> int:
#     return a+b

# print(sum(2 ,3))

#advance  type hints 
# from typing import List, Tuple
# numbers : list[int] = [1 , 2 , 3 , 4 , 5]
# person : Tuple[str,int] = ("kanishk" , 30)
# new_person = person + ("parakram" , 24)
# print(new_person)

#match case
# def http_status(status):
#     match status:
#         case 200:
#             return "ok"
#         case 404:
#             return "not found"
#         case _:
#             return "unkown status"
        
# print(http_status(200))


#merge dictinories
# dic1 = {"a" : 1 , "b" : 2}
# dic2 = {"b" : 3 , "c" : 4} 
# merge = dic1 | dic2
# print(merge)

# Exception handling in python
# try :
#     a = int(input("enter a number :"))
#     print(a)

# except Exception as e :
#     print(e)

# a = int(input("enter a nuber :"))
# b = int (input ("enter second number :"))
# # print({a/b})
# if ( b == 0):
#     raise ZeroDivisionError(f"hey our program is not able to divdee number {a} by zero")
# else:
#     print(f"value of the divison is {a/b}")
  


#enumerates

# l = [3 , 23 , 12 , 33]
# for index, item in enumerate(l):
#     print(f" the item number at index {index } is {item  }")

# # list comprehesion 
# my_list = [ 1 , 2 , 3 , 4 , 5]
# squarelist = [i*i for i in my_list]
# print(squarelist)