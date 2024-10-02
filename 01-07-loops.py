# Erklärung einer For-Schleife und While-Schleifen oder besser gesagt einem Loop

woerter = ["Apfel", "Banane", "Kirsche"]
for frucht in woerter:
    print(frucht)
    # Ausgabe:
    # Apfel
    # Banane
    # Kirsche

for i in range(3):
    print(i)
# Ausgabe:
# 0
# 1
# 2

zähler = 0
while zähler < 3:
    print(zähler)
    zähler += 1
# Ausgabe:
# 0
# 1
# 2

liste=["Kekse","Kuchen","Kirschen","Torte","Sahnebeutel","Kaffee",1,2,3]
for i in liste:
    print(i)
# Ausgabe:
# Kekse
# Kuchen
# Kirschen
# Torte
# Sahnebeutel
# Kaffee
# 1
# 2
# 3