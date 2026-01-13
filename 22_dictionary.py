# dictionary = a collection of {key : value } pairs
# ordered and changeable . NO duplicates

capital = {"USA" : "Washington D.C.",
           "India" : "New Delhi",
           "China" : "Beijing",
           "Russia" : "Moscow"} 
print(dir(capital))
print(help(capital))
capital.get("USA")

if capital.get("Japan"):
    print("That capital exists")
else: 
    print("That capital doesn't exist")
    
capital.update({"Germany": "Berlin"})
capital.pop("China")
capital.popitem()
capital.clear()
keys = capital.keys() 

for key in capital.keys():
    print(key)

values =  capital.values()
for value in capital.values():
 print(values)

items = capital.items()
for key , value in capital.items():
    print(f"{key} : {value}")

print(capital)