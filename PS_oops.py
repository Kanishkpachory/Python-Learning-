# class employee :
#     company = "Apple"

#     def __init__(self , name , salary , address):
#         self.name = name
#         self.salary = salary
#         self.address = address

# k = employee("kanishk" , 120000 , "chennai")
# print(k.name , k.salary , k.address)

# p = employee("parakram" , 150000 , "jaipur")

# print(f"hi I'm,{p.name} . My salary is {p.salary} and currently staying in {p.address}")



# class calculator :
#     def __init__(self ,n):
#         self.n = n

#     def square(self):
#         print(f"this is the square of {self.n} = {self.n*self.n}")
#     def cube(self):
#         print(f"this is the cube of {self.n} = {self.n*self.n*self.n}")
#     def squareroot(self):
#         print(f"this is the squareroot of {self.n} = {self.n*(1/2)}")


# a = calculator(4)
# a.square()
# a.cube()
# a.squareroot()


# class demo:
#     a=1

# o = demo()
# print(o.a)
# o.a = 0
# print(o.a)
# print(demo.a)



# class calculator :
#     def __init__(self ,n):
#         self.n = n
#     @staticmethod
#     def greet():
#         print("hello")

#     def square(self):
#         print(f"this is the square of {self.n} = {self.n*self.n}")
#     def cube(self):
#         print(f"this is the cube of {self.n} = {self.n*self.n*self.n}")
#     def squareroot(self):
#         print(f"this is the squareroot of {self.n} = {self.n*(1/2)}")


# a = calculator(4)
# a.greet()
# a.square()
# a.cube()
# a.squareroot()



# from random import randint
# class train :
#     def __init__(self , trainNo):
#         self.trainNo = trainNo
    
#     def book(self ,fro , to):
#         print(f"Ticket is booked in {self.trainNo} from {fro} to {to} .")

#     def getstatus(self):
#         print(f"Train no : {self.trainNo} is running on time . ")
    
#     def getfare(self , fro , to):
#         print(f"Fare for train {self.trainNo} from {fro} to {to} is {randint(500,5000)}") 

# t = train(11111)
# t.book("rampur", "jaipur") 
# t.getstatus()
# t.getfare("rampur","jaipur")