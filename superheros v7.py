hero = {"THO":{"name": "Thomas",
           "power": "Has politial influence",
           "strength": 1},
         "SUD": {"name": "Thomas",
           "power": "Scares all the girls away",
           "strength": -1}}
for hero_id, hero_info in hero.items():
    print(f"\nHero ID: {hero_id}")
    for key in hero_info:
        print(f"{key}: {hero_info[key]}")