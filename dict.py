#dictiony = a collections of keys and values {key:values} pairs
#ordered and changeable/mutable. No duplicates


capitals = {"USA":"washington DC",
            "India":"new Dehli",
            "russia": 'Moscow'}

#print(dir(capitals))
#print(help(capitals))

#print(capitals.get("India"))

#if capitals.get("India"):
#  print("That Capital Exists")
#lse:
 # print("that capital doesn't Exist")
#print(capitals.get())


#capitals.update({"Germany":"Berlin"})
#capitals.update({"USA":"Detroit"})
#capitals.pop("USA")

#capitals.popitem()
#capitals.clear()

#keys = capitals.keys()

#print(keys)

#for key in capitals.keys():
#  print(key)

#values = capitals.values()
#for value in capitals.values():
 # print(value)


items = capitals.items()
for key,value in capitals.items():
  print(f"{key}:{value}")