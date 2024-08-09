# # this is how file is read 
# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

# this is how you write in a file
# st = " hey kanishk how are you "
# f = open("myfile.txt", "w")
# f.write(st)
# f.close() 
# f = open("myfile.txt")
# data = f.read()
# print(data)
# f.close() 

# this is how you read line 
f = open("file.txt")
# # line = f.readlines()
# # print(line, type(line))
# # # f.close()

# line1 = f.readline()
# print(line1,type(line1))
# # f.close()
# line2 = f.readline()
# print(line2,type(line2))

# line = f.readline()
# while( line != ""):
#     print(line)
#     line = f.readline()

# this is how you append in a file

# st = " hey kanishk how are you "
# f = open("myfile.txt", "a")
# f.write(st)
# f.close() 

# with statment 

with open("file.txt") as f :
    print(f.read())