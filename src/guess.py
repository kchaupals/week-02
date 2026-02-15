# Guess game with random number generation
import random
def guess_game():
    guessNumber = random.randint(1, 100)
    attempts = 0
    maxAttempts = 10
    print(f"★★★★ Sveicināti spēle 'Uzmini skaitli' ★★★★")
    print(f"★★★★ Es esmu izvēlējies skaitli no 1 līdz 100. Vai vari to uzminēt 10 mēģinājumos? ★★★★")
    print(f'★★★★ Lai izietu no spēles, nospiest taustiņu "q" ★★★★')
    while attempts < maxAttempts:
        try:
            userInput = input("ℹ Ievadi savu minējumu (Vai 'q' lai izietu):") # User input that accepts string and int, allowing to type q or Q to exit game or int to proceed to guess the number
            if userInput.lower() in ['q', 'Q']:
                print("★★★★ Paldies par spēli. Uzredzēšanos! ★★★★")
                exit()
            userGuess = int(userInput)
            if userGuess < 1 or userGuess > 100: # Data validation so there is no negative numbers or numbers above 100 passed, also this should not count in attempt
                print("⚠ Lūdzu, ievadīt skaitli no 1 līdz 100")
                continue

            attempts += 1
            attemptsLeft = maxAttempts - attempts
            if userGuess < guessNumber and attempts < 10:
                print(f"⚠ Par mazu! Mēģini vēlreiz. Tev ir atlikuši {attemptsLeft} mēģinājums(-i)!")
            elif userGuess > guessNumber and attempts < 10:
                print(f"⚠ Par lielu! Mēģini vēlreiz. Tev ir atlikuši {attemptsLeft} mēģinājums(-i)!")
            elif userGuess == guessNumber and attempts != maxAttempts:
                print(f"✔ Super, spēle beigusies! Tu uzminēji skaitli {guessNumber} pēc {attempts} mēģinājumiem!")
                break
            else:
                print(f"✖ Tev neizdevās uzminēt. Atbilde bija {guessNumber}")
                break
        except ValueError:
            print("⚠ Nederīga ievade. Lūdzu, ievadi skaitli no 1 līdz 100.")

# Logic for repeating the game if either user won or losed the previous one
    while True: 
        retry = input("ℹ Vai vēlies uzspēlēt vēlreiz? (Jā/Nē):").lower()
        if retry in ['jā','ja']:
            guess_game()
            return
        elif retry in ['nē', 'ne']:
            print("★★★★ Paldies par spēli, uzredzēšanos! ★★★★")
            exit()
        else:
            print("⚠ Lūdzu, ievadi atbilid (Jā/Nē)") 


guess_game()
     