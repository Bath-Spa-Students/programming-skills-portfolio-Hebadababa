#make an empty list to store the pets in
pets=[]

#make individual pets,and store one in the list
pet={'animal':'dog','name':'sven','owner':'William','weight':'45','eats':'butch meat'}
pets.append(pet)
pet1={'animal':'parrot','name':'tofu','owner':'zain','weight':'14','eats':'cabbage'}
pets.append(pet1)
pet2={'animal':'cat','name':'simba','owner':'rasha','weight':'28','eats':'meat'}
pets.append(pet2)

#display information about each pet
for pet in pets:
    print("\nHere's what i know about"+pet['name'].title()+":")
for key,value in pet.items():
    print('\t'+key+':'+str(value))

