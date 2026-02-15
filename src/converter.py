# Konversijas definēšana:
KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
DOL_TO_EUR = 0.84235020

# Lietotāja ievads, lai izvēlētos konversijas veidu
print("Izvēlies konversijas veidu:")
print("1) KM <-> MI 2) KG <-> LB 3) L <-> GAL 4) DOL <-> EUR")
choice = input("Ievadi izvēli (1-4): ")
# Pamatojoties uz izvēli, veic jautājumu par konversacijas virzienu
print("Izvēlies konversijas virzienu:")
if choice == "1":
    print("1) KM -> MI 2) MI -> KM")
    dir = input("Ievadi izvēli (1-2): ")
elif choice == "2":
    print("1) KG -> LB 2) LB -> KG")
    dir = input("Ievadi izvēli (1-2): ")
elif choice == "3":
    print("1) L -> GAL 2) GAL -> L")
    dir = input("Ievadi izvēli (1-2): ")
elif choice == "4":
    print("1) DOL -> EUR 2) EUR -> DOL")
    dir = input("Ievadi izvēli (1-2): ")
# Pamatojoties uz izvēli, veic jautājumu par vērtību, ko konvertēt
value = float(input("Ievadi vērtību: ")) 
# Veic konversiju un izvada rezultātu balstoties uz augstāk izvēlētajiem parametriem
if choice == "1":
    if dir == "1":
        result = value * KM_TO_MI
        print(f"{value} KM ir {result} MI")
    elif dir == "2":
        result = value / KM_TO_MI
        print(f"{value} MI ir {result} KM")
elif choice == "2":
    if dir == "1":
        result = value * KG_TO_LB
        print(f"{value} KG ir {result} LB")
    elif dir == "2":
        result = value / KG_TO_LB
        print(f"{value} LB ir {result} KG")
elif choice == "3":
    if dir == "1":
        result = value * L_TO_GAL
        print(f"{value} L ir {result} GAL")
    elif dir == "2":
        result = value / L_TO_GAL
        print(f"{value} GAL ir {result} L")
elif choice == "4":
    if dir == "1":
        result = value * DOL_TO_EUR
        print(f"{value} DOL ir {result} EUR")
    elif dir == "2":
        result = value / DOL_TO_EUR
        print(f"{value} EUR ir {result} DOL")


# If un elif attiecīgi iziet cauri vērtībam, ko lietotājs ievadījis un tālāk veic atbilstošas loģikas konversiju.
# Kā piemērs termināli ievadot pirmajā izvēlne 1 - choice tiek definēts kā 1 utt. 
# Choice - konversācijas veids, dir - konversācijas virziens, value - vērtība, ko lietotājs ievadījis un galā izvadītais rezultāts ir - result