# #lambda example
# mul = lambda a,b : a*b
# print(mul(2,3))

# #join method example
# a = ["kanisk" , "pachory" , "parakram"]
# final = "::".join(a)
# print(final)

# #map example
# a = [ 1 , 2 , 3 , 4 , 5]
# sqr = lambda a : a*a
# sqrlist = map(sqr,a)
# print(list(sqrlist))

# #filter example
# a = [ 1 , 2 , 3 , 4 , 5]
# def even(n):
#     if(n%2 == 0):
#         return True
#     return False
# onlyeven =  filter(even , a)
# print(list(onlyeven))

# from functools import reduce
# a = [ 1 , 2 , 3 , 4 , 5]
# def sum(a ,b):
#     return a+b

# mul = lambda a,b : a*b

# print(reduce(sum,a))
# print(reduce(mul,a))