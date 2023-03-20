hero_0 = {"name": "Thomas",
               "power": "Has politial influence",
               "strength": 1}
if "name" in hero_0:
    print(f"the superheros name is {hero_0['name']}")
else:
    print("No name")
if "power" in hero_0:
    print(f"The superheros power is {hero_0['power']}")
else:
    print("No power")

if "Thomas" in hero_0['name']:
    print(f"That is the superhero's name")
else:
    print("Superhero's name is not Thomas")
print(hero_0)

hero_0["speed"] = 12
hero_0["strength"] = 6
hero_0["power"] = 10
print(hero_0)
popped_item = hero_0.pop("power")
print(popped_item)
for i in hero_0:
    print(f"{i} : {hero_0[i]}")