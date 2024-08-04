s1 = {1 , 2 , 3}
s2 = { 3 , 4 , 5 ,6}

# print(len(s1))
# s1.remove(1)
# s1.add(7)
# print(s1)
# s1.pop()
# print(s1)
# s1.clear()
# print(s1)
# s = s1.union(s2)
print(s1.union(s2))
print(s1.intersection(s2))
s = s1 - s2
print(s)
s = s2 - s1
print(s)