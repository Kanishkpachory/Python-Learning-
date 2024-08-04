mark = { "kanishk":100 , "rishi":200 , "papa": 300 , "mummy":400}
print(mark.items())
print(mark.keys())
print(mark.values())
mark.update({"kanishk":0 , "renuka":100})
print(mark)
print(mark.get("kanishk"))
print(mark["kanishk"])