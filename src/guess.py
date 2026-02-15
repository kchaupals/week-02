# Guess game with random number generation
import random

guessNumber = random.randint(1, 100)
attempts = 0
print("Sveicināti spēle 'Uzmini skaitli'")
print("Es esmu izvēlējies skaitli no 1 līdz 100. Vai vari to uzminēt?")
while True:
    try:
        user_guess = int(input("Ievadi savu minējumu: "))
        attempts += 1
        if user_guess < guessNumber:
            print("Par mazu! Mēģini vēlreiz.")
        elif user_guess > guessNumber:
            print("Par lielu! Mēģini vēlreiz.")
        else:
            print(f"Super, pēle beigusies! Tu uzminēji skaitli {guessNumber} pēc {attempts} mēģinājumiem!")
            print("Vai velētos spēlēt vēlreiz? (jā/nē)")
            break
    except ValueError:
        print("Nederīga ievade. Lūdzu, ievadi skaitli no 1 līdz 100.")