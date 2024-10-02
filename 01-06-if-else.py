x = int(input("Bitte gibt eine Zahle ein: "))
if x > 5:
    print(f"{x} ist größer als 5")
else:
    print(f"{x} ist kleiner als 5")
    # Ausgabe: x ist größer als 5

note = int(input("Bitte gib deine Note ein: "))
if note >= 90:
    print("Sehr gut!")
elif note >= 75: 
    print("Gut!")
elif note >= 50:
    print("Befriedigend!")
else:
    print("Verbesserung nötig!")
# Ausgabe: Gut!