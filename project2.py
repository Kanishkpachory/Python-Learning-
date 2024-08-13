import random
n = random.randint(1,100)
a = -1
gusses = 0
while(a != n):
    gusses += 1
    a = int(input("gusse the number :"))
    if (a >n):
        print("number is higher .")
    else:
        print("number is lower .")

print(f"you have gussed the number {n} correctly in {gusses} attempts")