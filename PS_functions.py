# def great(a ,b , c):
#     if(a>b and a>c):
#         return a
#     elif(b>c and b>a):
#         return b
#     elif(c>a and c>b):
#         return c
    
# a = int(input("enter 1st number :"))
    
# b = int(input("enter 2nd number :"))
    
# c = int(input("enter 3rd number :"))
    
# print(great(a , b, c))

# def f_to_c(f):
#     return  5*(f-32)/9

# f = int(input("INPUT THE TEMERATURE :"))
# c = f_to_c(f)
# print(f"{round(c,2)} degree C")

# def find(n):
#     return (n*(n+1))/2

# n = int(input("enter a natural number :"))
# print(find(n))

# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n

# print(sum(5))

# def pattern(n):
#     if(n==0):
#         return
#     print("*"*n)
#     pattern(n-1)

# n = int(input("enter a number :"))
# print(pattern(n))

def inch(n):
    return n*2.54

n =  int(input("enter a value :"))

print(f"corresponding value in cms is {inch(n)}")