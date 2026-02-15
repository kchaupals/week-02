# Atbilstības pārbaudītājs
# Šis skripts pārbauda un atgriež iespējas, vai lietotājs var:
    # Balsot (vecums >= 18) 
    # Īrēt auto (vecums >= 21 un ir vadītāja apliecība)
    # Saņemt senioru atlaidi (vecums >= 65 vai ir veterāns)
    # Saņemt studenta atlaidi (vecums starp 16 un 26, un ir students)

# Lietotāja vecuma ievade un pārveide par int
print("Labdien un laipni lūgti mūsu atbilstības pārbaudītājā!")
print("Lūdzu, ievadiet Jūsu vecumu:")
vecums_valid = False
while not vecums_valid:
    try:
        vecums = int(input("Ievadi Jūsu vecumu:"))
        if vecums < 0:
            print("Vecums nevar būt negatīvs. Lūdzu, ievadiet derīgu vecumu.")
        elif vecums != int(vecums):
            print("Lūdzu, ievadiet veselu skaitli vecumam.")
        else:
            vecums_valid = True
    except ValueError:
        print("Lūdzu, ievadiet derīgu skaitli vecumam.")
# Lietotaja autovadītāja apliecības statuss
print("Vai Jums ir vadītāja apliecība? (jā/nē)")
tiesibas_valid = False
while not tiesibas_valid:
    try:
        tiesibas = str(input("Ievadi 'jā' vai 'nē':"))
        if tiesibas.lower() == "ja" or tiesibas.lower() == "jā": # Pieņem gan ja, gan jā kā true vērtību
            tiesibas = True
            tiesibas_valid = True
        elif tiesibas.lower() == "nē" or tiesibas.lower() == "ne": 
            tiesibas = False
            tiesibas_valid = True
        else:
            print("Nederīga ievade. Lūdzu, ievadiet 'jā' vai 'nē'.")
    except ValueError:
        print("Lūdzu, ievadiet derīgu ievadi.")

# Lietotāja studenta statuss
print("Vai Jūs esat students? (jā/nē)")
students_valid = False
while not students_valid:
    try:
        students = str(input("Ievadi 'jā' vai 'nē':"))
        if students.lower() == "ja" or students.lower() == "jā": # Pieņem gan ja, gan jā kā true vērtību
            students = True
            students_valid = True
        elif students.lower() == "nē" or students.lower() == "ne": 
            students = False
            students_valid = True
        else:
            print("Nederīga ievade. Lūdzu, ievadiet 'jā' vai 'nē'.")
    except ValueError:
        print("Lūdzu, ievadiet derīgu ievadi.")

# Lietotaja veterāna statuss 
print("Vai Jūs esat veterāns? (jā/nē)")
veterans_valid = False
while not veterans_valid:
    try:
        veterans = str(input("Ievadi 'jā' vai 'nē':"))
        if veterans.lower() == "ja" or veterans.lower() == "jā":
            veterans = True
            veterans_valid = True
        elif veterans.lower() == "nē" or veterans.lower() == "ne": 
            veterans = False
            veterans_valid = True
        else:
            print("Nederīga ievade. Lūdzu, ievadiet 'jā' vai 'nē'.")
    except ValueError:
        print("Lūdzu, ievadiet derīgu ievadi.")

# Loģikas atgriešana 

print("--------------")
# Balsot ->

if vecums >= 18:
    print("Balsošana: Jā \u2713") 
else:
    print("Balsošana: Nē \u2717") 

# Īrēt auto ->

if vecums >= 21 and tiesibas:
    print("Auto īre: Jā \u2713")
else:
    print("Auto īre: Nē \u2717 (nav vadītāja apliecības)")

# Senioru atlaide ->  

if vecums >= 65 or veterans:
    print("Senioru atlaide: Jā \u2713")
else:
    print("Senioru atlaide: Nē \u2717")

# Studenta atlaide ->
if 16 <= vecums <= 26 and students:
    print("Studenta atlaide: Jā \u2713")
else:
    print("Studenta atlaide: Nē \u2717")
