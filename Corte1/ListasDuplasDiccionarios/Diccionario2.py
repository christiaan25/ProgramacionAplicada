# Obtener un valor con una clave
building_heights = {
    "Burj Khalifa": 828, 
    "Shanghai Tower": 632, 
    "Abraj Al Bait": 601, 
    "Ping An": 599, 
    "Lotte World Tower": 554.5, 
    "One World Trade": 541.3
}

print(building_heights["Burj Khalifa"])  # Imprime 828
print(building_heights["Ping An"])  # Imprime 599

zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}

print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

# Manejar claves inexistentes
key_to_check = "Landmark 81"
if key_to_check in building_heights:
    print(building_heights[key_to_check])
else:
    print("Clave no encontrada")

zodiac_elements["energy"] = "Not a Zodiac element"
if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])

# Obtener valores de forma segura
print(building_heights.get("Shanghai Tower"))  # Devuelve 632
print(building_heights.get("My House"))  # Devuelve None

user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

tc_id = user_ids.get("teraCoder", 1000)
print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

# Eliminar una clave
raffle = {
    223842: "Teddy Bear", 
    872921: "Concert Tickets", 
    320291: "Gift Basket", 
    412123: "Necklace", 
    298787: "Pasta Maker"
}

print(raffle.pop(320291, "No Prize"))  # Imprime "Gift Basket"
print(raffle)
print(raffle.pop(100000, "No Prize"))  # Imprime "No Prize"
print(raffle)
print(raffle.pop(872921, "No Prize"))  # Imprime "Concert Tickets"
print(raffle)

# Modificar valores
available_items = {
    "health potion": 10,
    "cake of the cure": 5,
    "green elixir": 20,
    "strength sandwich": 25,
    "stamina grains": 15,
    "power stew": 30
}

health_points = 20
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)

# Obtener todas las claves
test_scores = {
    "Grace": [80, 72, 90], 
    "Jeffrey": [88, 68, 81], 
    "Sylvia": [80, 82, 84], 
    "Pedro": [98, 96, 95], 
    "Martin": [78, 80, 78], 
    "Dina": [64, 60, 75]
}

print(list(test_scores.keys()))
for student in test_scores.keys():
    print(student)

# Obtener todos los valores
for score_list in test_scores.values():
    print(score_list)

num_exercises = {
    "functions": 10, 
    "syntax": 13, 
    "control flow": 15, 
    "loops": 22, 
    "lists": 19, 
    "classes": 18, 
    "dictionaries": 18
}

total_exercises = sum(num_exercises.values())
print(total_exercises)

# Obtener todos los ítems
biggest_brands = {
    "Apple": 184, 
    "Google": 141.7, 
    "Microsoft": 80, 
    "Coca-Cola": 69.7, 
    "Amazon": 64.8
}

for company, value in biggest_brands.items():
    print(f"{company} tiene un valor de {value} mil millones de dólares.")

pct_women_in_occupation = {
    "CEO": 28, 
    "Engineering Manager": 9, 
    "Pharmacist": 58, 
    "Physician": 40, 
    "Lawyer": 37, 
    "Aerospace Engineer": 9
}

for occupation, percentage in pct_women_in_occupation.items():
    print(f"Las mujeres representan el {percentage}% de los {occupation}s.")
