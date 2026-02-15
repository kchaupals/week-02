# Guess game with random number generation
import random
def guess_game():
    guessNumber = random.randint(1, 100)
    attempts = 0
    maxAttempts = 10
    print("Sveicināti spēle 'Uzmini skaitli'")
    print("Es esmu izvēlējies skaitli no 1 līdz 100. Vai vari to uzminēt 10 mēģinājumos?")
    while attempts < maxAttempts:
        try:
            user_guess = int(input("Ievadi savu minējumu: "))
            attempts += 1
            attemptsLeft = maxAttempts - attempts
            if user_guess < guessNumber and attempts < 10:
                print(f"Par mazu! Mēģini vēlreiz. Tev ir atlikuši {attemptsLeft} mēģinājums(-i)!")
            elif user_guess > guessNumber and attempts < 10:
                print(f"Par lielu! Mēģini vēlreiz. Tev ir atlikuši {attemptsLeft} mēģinājums(-i)!")
            elif user_guess == guessNumber and attempts != maxAttempts:
                print(f"Super, spēle beigusies! Tu uzminēji skaitli {guessNumber} pēc {attempts} mēģinājumiem!")
                break
            else:
                print(f"Tev neizdevās uzminēt. Atbilde bija {guessNumber}")
                break
        except ValueError:
            print("Nederīga ievade. Lūdzu, ievadi skaitli no 1 līdz 100.")

# Logic for repeating the game if either user won or losed the previous one
    while True: 
        retry = input("Vai vēlies uzspēlēt vēlreiz? (Jā/Nē):").lower()
        if retry in ['jā','ja']:
            guess_game()
            return
        elif retry in ['nē', 'ne']:
            print("Paldies par spēli, uzredzēšanos!")
            exit()
        else:
            print("Lūdzu, ievadi atbilid (Jā/Nē)") 


guess_game()
     