# f = open("poem.txt")
# c = f.read()
# if("twinkle" in c ):
#     print("the word is there in the given poem")
# else:
#     print("the word is not there in the given poem")



# f.close()
# import random
# def game():
#     print("you are playing the game :")
#     score = random.randint(1,100)
#     #fetch the hiscore
#     with open("hiscore.txt") as f:
#         hiscore = f.read()
#         if(hiscore !=""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0
#     print(f"your score :{score}")
#     if(score>hiscore):
#         with open("hiscore.txt","w") as f:
#             f.write(str(score))

#     #return score

# game()



# def generate(n):
#     table=""
#     for i in range(1,11):
#         table += f"{n} X {i} = {n*i}\n"

#     with open (f"tables/table_{n}.txt" , "w") as f:
#         f.write(table)
# for i in range(2,21) :
#     generate(i)

# def generate(n):
#     table =""
#     for i in range(1,11):
#         table += f"{n} X {i} = {n*i}\n"
#     with open(f"tables/table_{n}.txt", "w") as f:
#         f.write(table)

# for i in range(2,21):
#     generate(i)



# word = "donkey"
# with open("donkey.txt","r") as f :
#     content = f.read()

# contentnew = content.replace(word,"#####")

# with open("donkey.txt","w") as f:
#     f.write(contentnew)



# words = ["donkey" ,"bad" ,"ganda"]
# with open("donkey.txt","r") as f :
#     content = f.read()

# for word in words:
#     content = content.replace(word,"#####")
 
# with open("donkey.txt","w") as f:
#     f.write(content)




# with open("present.txt","r") as f :
#     content = f.read()
# if("python" in content):
#     print("yes im here")
# else:
#     print("oops you missed me ")


# with open("present.txt","r") as f :
#     content = f.readlines()

# lineno =1
# for line in content:
#     if("python" in line):
#          print(f"yes im here at {lineno}th line.")
#          break
#     lineno +=1
    
# else:
#     print("oops you missed me ")


# with open("poem.txt" ,"r") as f:
#     content = f.read()

# with open("poem_copy.txt" ,"w") as f:
#     f.write(content)

# with open("poem.txt","r") as f:
#     content1=f.read()

# with open("myfile.txt","r") as f:
#     content2 = f.read()

# if (content1 ==content2):
#     print("yes there content are same in files .")

# else:
#     print("no there content are not same in files . ")