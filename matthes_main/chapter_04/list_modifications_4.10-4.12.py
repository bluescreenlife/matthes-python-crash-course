mypizzas = ["pepperoni", "sausage", "meat lovers", "hawaiian", "chicken bacon ranch", "toppers stix"]

for pizza in mypizzas[:3]:
    print(f"I like {pizza}.")
for pizza in mypizzas[3:]:
    print(f"I also like {pizza}.")

friendpizzas = mypizzas[:] # since lists are mutable, assigning the two and editing one will edit both, so use [:] to make a copy of a list

mypizzas.insert(len(mypizzas), "buffalina")
friendpizzas.insert(len(friendpizzas), "vegetarian")

for pizza in mypizzas:
    print(pizza)
for pizza in friendpizzas: 
    print(pizza)