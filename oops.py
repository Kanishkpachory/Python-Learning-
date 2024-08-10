class employee:
    language = "python"
    salary = 120000

    def getinfo(self):
        print(f"my name is {harry.name} i am {self.language} developer and my salary is {self.salary}")

    def greet(self):
        print(f"good ")

    @staticmethod     # it is static method which donot take self attribute for defining object
    def greet():
        print(f"good morning")


harry = employee()
harry.name = "harry"
print(harry.name ,harry.language , harry.salary)
harry.greet()
harry.getinfo()
#employee.getinfo(harry)    #this is how language interpritate the above 2 commands