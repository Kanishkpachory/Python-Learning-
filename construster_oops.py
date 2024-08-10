class employee:
    language = "python"
    salary = 120000

    def __init__(self,name,salary,language) : #dunder method which is automatically called 
        print("i'm creating an object")
        self.name = name 
        self.salary = salary
        self.language = language

    def getinfo(self):
        print(f"my name is {harry.name} i am {self.language} developer and my salary is {self.salary}")

    def greet(self):
        print(f"good ")

    @staticmethod     # it is static method which donot take self attribute for defining object
    def greet():
        print(f"good morning")

harry = employee("harry" , 130000 , "javascript")
# harry.name = "harry"
print(harry.name ,harry.language , harry.salary)

# rohan = employee()