# Importē nepieciešamas funkcijas no math un random moduļa
import math
from math import ceil,floor 
import random

# Divas pamata vērtību piešķiršanas
a = bool(False)
b = float(4.75)

# Konsole izvada katra mainīga tipu
print("Mainīgā a tips ir:", type(a))
print("Mainīgā b tips ir:", type(b))

# Vismaz 3 Python truthy / falsy piemēri

print(bool("")) # Falsy jo tukša virkne tiek uzskatīta par nepatiesu
print(bool('Sveika pasaule')) # Truthy jo virkne ar saturu tiek uzskatīta par patiesu
print(bool(" ")) #Truthy jo virkne ir ar simbolu, kas šajā gadījuma ir atstarpe 
print(bool(None)) # Falsy jo None - latviski tulkojot nekas, attiecīgi kā tukšums tiek uzskatīts par nepatiesu

# Vismaz 3 Python datu tipu pārveides ar robežgadījumiem, kas notiek, ja konversācija neizdodas
print(int("123")) # Pārveido str "123" par int 123
print(float("3.14")) # Pārveido str "3.14" par float 3.14
print(bool("")) # Pārveido tukšu str par bool False
# print(int("abc")) # Mēģina pārveidot str "abc" par int, bet tas neizdodas un izraisīs ValueError / Ši rinda ir ar komentāra zīmi, lai tālākas komandas tiktu kompilētas, jo tiek izvadīta kļūda
print("Hello world!".upper()) # Pārveido str "Hello world!" par "HELLO WORLD!"

# Piemēri, ko demonstrēt - jauktā izvēle

print(ceil(68.2)) # Pārveido float 68.2 par int 69, noapaļojot uz augšu
print(0.1 + 0.2 == 0.3) # False, jo izmantoti dažādi operandi, 0.2 nav vienāds ar 0.3. == operatoru izmanto salidzināšanai nevis aprēķināšanai, kā arī binari aprēķinot var būt nelielas novirzes
print(floor(random.random()*3)+1) # Ģenerē nejaušu skaitli no 1 līdz 3, funkcija randmo izvēlas skaitli no 0 līdz 1, reizinot ar 3 un noapaļojot uz leju ar floor, tad pieskaitot 1, lai izvēlētos no 1-3